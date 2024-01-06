from netmiko import ConnectHandler
from pprint import pprint
import re
import textfsm
import pynetbox
import netmiko

def create_connections(switches,commands,descriptions):
    try:
        for switch in switches:
            cisco_router = {
                'device_type': 'cisco_ios',
                'host': switch,
                'username': 'nadubov',
                'password': 'Wanga15',
                'secret': 'Qq123456',
                'port': 22,
                }
            ssh = ConnectHandler(**cisco_router)
            for description, command in zip(descriptions, commands): 
                ssh.enable()  
                result = ssh.send_command(command)
                with open(f"C:\\Users\\grink\\test_script\\{description}_{switch}.txt", 'w') as f:
                    f.write(result.rstrip())
    except:
        print(f"Unable to connect to the Device {switch}")
        
switches = ['10.51.130.10',
            '10.51.130.12',
            '10.51.130.13',
            '10.51.130.19',
            '10.51.130.23',
            '10.51.130.24',
            '10.51.130.25',
            '10.51.130.26',
            '10.51.130.31',
            '10.51.130.5',
            '10.51.130.6',
            '10.51.130.7',
            '10.51.130.9'
            ]
descriptions = ['cdp_neighbors','interfaces','inventory']
commands = ['show cdp neighbors','show ip interface brief','show inventory']
create_connections(switches,commands,descriptions)
