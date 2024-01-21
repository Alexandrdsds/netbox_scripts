import pynetbox
from netmiko import ConnectHandler
from pprint import pprint
import re
import netmiko
import json
import os

nb = pynetbox.api(
        'https://netbox.dpsu.gov.ua',
    token='8a2f84287748453d629ed55b74f32c314b0e2d48'
)

def connect_to_host():
    with open('test') as f:
        switches = f.read().splitlines()
        
    connections = {}
    for switch in switches:
        try:
            cisco_router = {
                'device_type': 'cisco_ios',
                'host': switch,
                'username': 'nadubov',
                'password': 'Wanga15',
                'secret': 'Qq123456',
                'port': 22,
            }
            print(f"---------------Connect to {switch}------------------------------------")
            ssh = ConnectHandler(**cisco_router)
            ssh.enable()
            connections[switch] = ssh # додає елементи до словника connections з ключем IP та значенням сесії цього IP
        except Exception as e:
            print(f"Unable to connect to the Device {switch}. Error: {e}")
    return connections

connections = connect_to_host()

def devices_hostname():
    hostnames = []
    for ssh in connections.values():
        show_hostname = ssh.send_command("show run | include hostname")
        pattern = r'hostname\s+(\S+)'
        matches = re.finditer(pattern,show_hostname)
        for match in matches:
            hostnames.append({'hostname': match.group(1)})
    return hostnames

def find_devices_sn():
    sn_info = []
    for ip , ssh in connections.items():
        show_inventory = ssh.send_command("show inventory",use_textfsm=True)
        device_sn = show_inventory[0] if show_inventory else None #виводить значення тільки SN пристрою
        sn = device_sn.get('sn')
        model = device_sn.get('descr')
        sn_info.append({'ip': ip, 'serial': sn, 'device_type': model})
    return sn_info

serials = find_devices_sn()

hostnames = devices_hostname()

def chek_devices_in_netbox():
    for device_serial in serials:
        result = nb.dcim.devices.get(serial = device_serial['serial'])
        if not result:
            create_devices_in_nb()
        else:
            print(result.id)
            
def create_devices_in_nb():
    print("f")
    
