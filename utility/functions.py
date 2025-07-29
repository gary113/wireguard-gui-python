from os import remove
from pathlib import Path
from subprocess import PIPE, Popen, getoutput, getstatusoutput, run

from wgconfig import WGConfig

WIREGUARD_CONFIGS_FOLDER = "/etc/wireguard"
PROJECT_DIRECTORY = Path(__file__).parents[1]
UPDATE_INTERVAL = 1000


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


def get_interface_name(interface: str) -> str:
    return interface[: interface.find(".conf")]


def is_actived_interface(interface: str) -> bool:
    return getstatusoutput(f"wg show {get_interface_name(interface)}")[0] == 0


def is_systemd_actived_interface(interface: str) -> bool:
    return (
        getstatusoutput(
            f"systemctl is-active wg-quick@{get_interface_name(interface)}.service"
        )[0]
        == 0
    )


def is_systemd_enabled_interface(interface: str) -> bool:
    return (
        getstatusoutput(
            f"systemctl is-enabled wg-quick@{get_interface_name(interface)}.service"
        )[0]
        == 0
    )


def count_active_interfaces():
    interfaces = get_interfaces()
    active_count = 0
    for interface in interfaces:
        if is_actived_interface(interface):
            active_count += 1
    return active_count


def interface_exists(interface: str) -> bool:
    return getstatusoutput(f"ls '{WIREGUARD_CONFIGS_FOLDER}/{interface}'")[0] == 0


def turn_interface(interface: str):
    if is_actived_interface(interface):
        stop_interface(interface)
    else:
        start_interface(interface)


def stop_interface(interface: str):
    if is_systemd_actived_interface(interface):
        run(
            f"systemctl stop wg-quick@{get_interface_name(interface)}.service",
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )

        if is_systemd_enabled_interface(interface):
            Popen(
                f"systemctl disable wg-quick@{get_interface_name(interface)}.service",
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
            )
    else:
        Popen(
            f"wg-quick down {get_interface_name(interface)}",
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )


def start_interface(interface: str) -> bool:
    run(
        f"systemctl start wg-quick@{get_interface_name(interface)}.service",
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
    )

    is_actived = is_actived_interface(interface)

    if is_actived:
        Popen(
            f"systemctl enable wg-quick@{get_interface_name(interface)}.service",
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )

    return is_actived


def restart_interface(interface: str) -> bool:
    if is_systemd_actived_interface(interface):
        run(
            f"systemctl restart wg-quick@{get_interface_name(interface)}.service",
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )

        is_actived = is_actived_interface(interface)
    else:
        Popen(
            f"wg-quick down {get_interface_name(interface)}",
            shell=True,
            stdout=PIPE,
            stderr=PIPE,
        )

        is_actived = start_interface(interface)

    return is_actived


def is_valid_interface(interface: str):
    wc = WGConfig(f"{WIREGUARD_CONFIGS_FOLDER}/{interface}")
    wc.read_file()

    if not wc.get_interface():
        valid_interface = False
    else:
        valid_interface = True

    return valid_interface


def edit_interface(interface: str, new_name: str, old_config: str, new_config: str):
    is_actived = is_actived_interface(interface)
    edited_config = old_config != new_config

    if edited_config:
        write_wireguard_config(interface, new_config)
        valid_interface = is_valid_interface(interface)
    else:
        valid_interface = True

    if valid_interface:
        new_name = new_name.strip()[:15]

        if new_name != "" and new_name != get_interface_name(interface):
            copy_process = run(
                f"cp {WIREGUARD_CONFIGS_FOLDER}/{interface} {WIREGUARD_CONFIGS_FOLDER}/{new_name}.conf",
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
            )

            if copy_process.returncode != 0:
                return False

            delete_interface(interface)

            if is_actived:
                start_interface(f"{new_name}.conf")
        elif is_actived and edited_config:
            restart_interface(interface)
    else:
        write_wireguard_config(interface, old_config)

    return valid_interface


def delete_interface(interface: str):
    if is_actived_interface(interface):
        stop_interface(interface)

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

    valid_interface = is_valid_interface(f"{interface_name}.conf")

    if not valid_interface:
        delete_interface(f"{interface_name}.conf")

    return valid_interface


def write_wireguard_config(interface: str, config: str):
    with open(f"{WIREGUARD_CONFIGS_FOLDER}/{interface}", "w") as interface_file:
        interface_file.write(config)
