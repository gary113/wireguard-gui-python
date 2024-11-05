from dotenv import load_dotenv as load_dotenv_
from datetime import datetime
from os import remove as remove_, getenv as getenv_
from pathlib import Path
from subprocess import Popen, getoutput as getoutput_, getstatusoutput as getstatusoutput_


load_dotenv_()
WIREGUARD_CONFIGS_FOLDER = '/etc/wireguard'
PROJECT_DIRECTORY = Path(__file__).parents[1]

DATETIME_FORMAT = getenv_('DATETIME_FORMAT', '%Y-%m-%d %H:%M:%S')
LOG_FILE = getenv_('LOG_FILE', '/var/log/wgp.log')
update_interval_value = int(getenv_('UPDATE_INTERVAL', 1))
UPDATE_INTERVAL = update_interval_value * \
    1000 if update_interval_value >= 1 else 1000



def get_interfaces():
    return getoutput_(f"ls {WIREGUARD_CONFIGS_FOLDER} | grep '.conf'").splitlines()


def get_config_file_content(interface: str):
    with open(f"{WIREGUARD_CONFIGS_FOLDER}/{interface}", mode='r') as config_file:
        content = config_file.read()
    interface_content = content[:content.find('[Peer]')].strip()
    peers_content = content[content.find('[Peer]'):].strip()
    return {'full_content': content, 'interface_content': interface_content, 'peers_content': peers_content}


def get_config_active_content(interface: str):
    content = getoutput_(f"wg show {get_interface_name(interface)}")

    interface_content = content[:content.find('peer:')].strip()
    peers_content = content[content.find('peer:'):].strip()
    return {'full_content': content, 'interface_content': interface_content, 'peers_content': peers_content}


def get_specific_config_interface(interface_config: str, config: str, active=False):
    content = interface_config.splitlines()
    if config == 'publickey':
        if active:
            return get_specific_config_interface(interface_config, 'public key', active)
        else:
            privatekey = get_specific_config_interface(
                interface_config, 'privatekey')
            if privatekey != '':
                return getoutput_(f"echo {privatekey} | wg pubkey")
    else:
        for line in content:
            if config in line.lower():
                return line[line.find(':' if active else '=') + 1:].strip()
    return ''


def get_interface_name(interface: str):
    return interface[:interface.find('.conf')]


def interface_active(interface: str):
    return getstatusoutput_(f"wg show {get_interface_name(interface)}")[0] == 0


def interface_exists(interface: str):
    return getstatusoutput_(f"ls {WIREGUARD_CONFIGS_FOLDER}/{interface}")[0] == 0


def turn_interface(interface: str):
    if interface_active(interface):
        down_interface(interface)
    else:
        up_interface(interface)


def down_interface(interface: str):
    append_log_line_without_timestamp(
        f"[##] TURNING OFF INTERFACE {get_interface_name(interface)} START")
    append_log_line_with_timestamp(getoutput_(
        f"unbuffer wg-quick down {get_interface_name(interface)} | ts '{DATETIME_FORMAT} ~'"))
    append_log_line_without_timestamp(
        f"[##] TURNING OFF INTERFACE {get_interface_name(interface)} END")


def up_interface(interface: str):
    append_log_line_without_timestamp(
        f"[##] TURNING ON INTERFACE {get_interface_name(interface)} START")
    append_log_line_with_timestamp(getoutput_(
        f"unbuffer wg-quick up {get_interface_name(interface)} | ts '{DATETIME_FORMAT} ~'"))
    append_log_line_without_timestamp(
        f"[##] TURNING ON INTERFACE {get_interface_name(interface)} END")

    return interface_active(interface)


def test_interface(interface: str):
    append_log_line_without_timestamp(
        f"[###] TESTING INTERFACE {get_interface_name(interface)} START")

    actived = interface_active(interface)

    if actived:
        down_interface(interface)

    if get_config_file_content(interface)['full_content'].strip() == '':
        valid_interface = False
    else:
        valid_interface = up_interface(interface)

    if not actived and valid_interface:
        down_interface(interface)

    append_log_line_without_timestamp(
        f"[###] TESTING INTERFACE {get_interface_name(interface)} END")

    return valid_interface


def edit_interface(interface: str, new_name: str, old_config: str, new_config: str):
    append_log_line_without_timestamp(
        f"[####] EDITING INTERFACE {get_interface_name(interface)} START")

    actived = interface_active(interface)

    if old_config != new_config:
        write_wireguard_config(interface, new_config)
        valid_interface = test_interface(interface)
    else:
        valid_interface = True

    if valid_interface:
        new_name = new_name[:15]
        if new_name.strip() != '' and new_name != get_interface_name(interface):
            if actived:
                down_interface(interface)
            Popen(
                f"cp {WIREGUARD_CONFIGS_FOLDER}/{interface} {WIREGUARD_CONFIGS_FOLDER}/{new_name}.conf".split(' '))
            if actived:
                up_interface(f"{new_name}.conf")
            append_log_line_without_timestamp(
                f"[###] COPYED INTERFACE {get_interface_name(interface)} => {new_name}")
            delete_interface(interface)
    else:
        write_wireguard_config(interface, old_config)

    append_log_line_without_timestamp(
        f"[####] EDITING INTERFACE {get_interface_name(interface)} END")

    return valid_interface


def delete_interface(interface: str):
    if interface_active(interface):
        down_interface(interface)

    remove_(f"{WIREGUARD_CONFIGS_FOLDER}/{interface}")

    append_log_line_without_timestamp(
        f"[##] DELETED INTERFACE {get_interface_name(interface)}")


def export_interfaces(directory: str):
    return getstatusoutput_(f"cd {WIREGUARD_CONFIGS_FOLDER} && zip -R {directory}/wireguard_interfaces.zip . '*.conf'")[0] == 0


def import_interfaces(zip_file: str):
    zip_name = zip_file.split("/")[-1]

    append_log_line_without_timestamp(f"[##] IMPORTING ZIP {zip_name} START")
    import_process = getstatusoutput_(f"unzip -jo {zip_file} -d {WIREGUARD_CONFIGS_FOLDER} '*.conf'")
    append_log_line_without_timestamp(import_process[1])
    append_log_line_without_timestamp(f"[##] IMPORTING ZIP {zip_name} END")
 
    return import_process[0] == 0

def add_interface(interface: str):
    interface_name = interface.split("/")[-1]

    append_log_line_without_timestamp(f"[##] ADDING INTERFACE {interface_name} START")
    add_process = getstatusoutput_(f"cp {interface} {WIREGUARD_CONFIGS_FOLDER}")
    append_log_line_without_timestamp(add_process[1])
    append_log_line_without_timestamp(f"[##] ADDING INTERFACE {interface_name} END")

    return add_process[0] == 0


def new_interface(interface_name: str, interface_config: str):
    interface_name = interface_name[:15]
    append_log_line_without_timestamp(
        f"[####] CREATING INTERFACE {interface_name} START")

    write_wireguard_config(f"{interface_name}.conf", interface_config)

    valid_interface = test_interface(f"{interface_name}.conf")

    if not valid_interface:
        delete_interface(f"{interface_name}.conf")

    append_log_line_without_timestamp(
        f"[####] CREATING INTERFACE {interface_name} END")

    return valid_interface


def write_wireguard_config(interface: str, config: str):
    with open(f"{WIREGUARD_CONFIGS_FOLDER}/{interface}", 'w') as interface_file:
        interface_file.write(config)


def get_log_file_lines(start_datetime: datetime):
    with open(LOG_FILE, 'r') as log_file:
        log_file_lines = log_file.readlines()

    return [log_file_line for log_file_line in log_file_lines if compare_datetimes(log_file_line, start_datetime)]


def get_log_line_datetime(log_line: str):
    return datetime.strptime(f"{log_line[:log_line.find('~')].strip()}", DATETIME_FORMAT)


def compare_datetimes(log_line: str, start_datetime:datetime):
    try:
        return datetime.strptime(f"{log_line[:log_line.find('~')].strip()}", DATETIME_FORMAT) > start_datetime
    except:
        return False


def append_log_line_without_timestamp(log_message: str):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(
            f"{datetime.now().strftime(DATETIME_FORMAT)} ~ {log_message}\n")


def append_log_line_with_timestamp(log_message: str):
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"{log_message}\n")
