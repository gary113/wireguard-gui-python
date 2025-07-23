from os import getenv
from os import remove
from pathlib import Path
from subprocess import Popen
from subprocess import getoutput
from subprocess import getstatusoutput

from dotenv import load_dotenv

load_dotenv()

WIREGUARD_CONFIGS_FOLDER = "/etc/wireguard"
PROJECT_DIRECTORY = Path(__file__).parents[1]
update_interval_value = int(getenv("UPDATE_INTERVAL", 1))
UPDATE_INTERVAL = update_interval_value * 1000 if update_interval_value >= 1 else 1000


def get_interfaces():
    return getoutput(f"ls {WIREGUARD_CONFIGS_FOLDER} | grep '.conf'").splitlines()


def get_config_file_content(interface: str):
    with open(f"{WIREGUARD_CONFIGS_FOLDER}/{interface}", mode="r") as config_file:
        content = config_file.read()
    interface_content = content[: content.find("[Peer]")].strip()
    peers_content = content[content.find("[Peer]") :].strip()
    return {
        "full_content": content,
        "interface_content": interface_content,
        "peers_content": peers_content,
    }


def get_config_active_content(interface: str):
    content = getoutput(f"wg show {get_interface_name(interface)}")

    interface_content = content[: content.find("peer:")].strip()
    peers_content = content[content.find("peer:") :].strip()
    return {
        "full_content": content,
        "interface_content": interface_content,
        "peers_content": peers_content,
    }


def get_specific_config_interface(interface_config: str, config: str, active=False):
    content = interface_config.splitlines()
    if config == "publickey":
        if active:
            return get_specific_config_interface(interface_config, "public key", active)
        else:
            privatekey = get_specific_config_interface(interface_config, "privatekey")
            if privatekey != "":
                return getoutput(f"echo {privatekey} | wg pubkey")
    else:
        for line in content:
            if config in line.lower():
                return line[line.find(":" if active else "=") + 1 :].strip()
    return ""


def get_interface_name(interface: str):
    return interface[: interface.find(".conf")]


def actived_interface(interface: str):
    return getstatusoutput(f"wg show {get_interface_name(interface)}")[0] == 0


def interface_exists(interface: str):
    return getstatusoutput(f"ls '{WIREGUARD_CONFIGS_FOLDER}/{interface}'")[0] == 0


def turn_interface(interface: str):
    if actived_interface(interface):
        down_interface(interface)
    else:
        up_interface(interface)


def down_interface(interface: str):
    Popen(
        f"systemctl stop wg-quick@{get_interface_name(interface)}.service",
        shell=True,
    )


def up_interface(interface: str):
    Popen(
        f"systemctl start wg-quick@{get_interface_name(interface)}.service",
        shell=True,
    )

    return actived_interface(interface)


def test_interface(interface: str):
    if get_config_file_content(interface)["full_content"].strip() == "":
        valid_interface = False
    else:
        valid_interface = up_interface(interface)

    return valid_interface


def edit_interface(interface: str, new_name: str, old_config: str, new_config: str):
    actived = actived_interface(interface)

    if old_config != new_config:
        write_wireguard_config(interface, new_config)
        valid_interface = test_interface(interface)
    else:
        valid_interface = True

    if valid_interface:
        new_name = new_name[:15]
        if new_name.strip() != "" and new_name != get_interface_name(interface):
            if actived:
                down_interface(interface)
            Popen(
                f"cp {WIREGUARD_CONFIGS_FOLDER}/{interface} {WIREGUARD_CONFIGS_FOLDER}/{new_name}.conf".split(
                    " "
                )
            )
            if actived:
                up_interface(f"{new_name}.conf")

            delete_interface(interface)
    else:
        write_wireguard_config(interface, old_config)

    return valid_interface


def delete_interface(interface: str):
    if actived_interface(interface):
        down_interface(interface)

    remove(f"{WIREGUARD_CONFIGS_FOLDER}/{interface}")


def export_interfaces(directory: str):
    export_process = getstatusoutput(
        f"cd '{WIREGUARD_CONFIGS_FOLDER}' && zip -R '{directory}/wireguard_interfaces.zip' . '*.conf'"
    )

    return export_process[0] == 0


def import_interfaces(zip_file: str):
    import_process = getstatusoutput(
        f"unzip -jo '{zip_file}' -d '{WIREGUARD_CONFIGS_FOLDER}' '*.conf'"
    )

    return import_process[0] == 0


def add_interface(interface: str):
    add_process = getstatusoutput(f"cp '{interface}' '{WIREGUARD_CONFIGS_FOLDER}'")

    return add_process[0] == 0


def new_interface(interface_name: str, interface_config: str):
    interface_name = interface_name[:15]

    write_wireguard_config(f"{interface_name}.conf", interface_config)

    valid_interface = test_interface(f"{interface_name}.conf")

    if not valid_interface:
        delete_interface(f"{interface_name}.conf")

    return valid_interface


def write_wireguard_config(interface: str, config: str):
    with open(f"{WIREGUARD_CONFIGS_FOLDER}/{interface}", "w") as interface_file:
        interface_file.write(config)
