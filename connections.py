#!/usr/bin/env python3
from netmiko import ConnectHandler
from pprint import pprint
import re
import textfsm
import pynetbox
import netmiko
nb = pynetbox.api(
        'https://netbox.dpsu.gov.ua',
    token='8a2f84287748453d629ed55b74f32c314b0e2d48'
)

def create_more_interfaces():
    devices = nb.dcim.devices.filter(device_type_id=5)
    interfaces = [{"name": f"eth1/{i}", "type": "10gbase-t"} for i in range(1, 33)]
    for device in devices:
        #print(device)
        for interface in interfaces:
            data = [
                    {
                        'device': device.id,
                        'name': interface['name'],
                        'type': interface['type'],
                        #'enabled': interface_info['enabled']
                    },
                ]

            try:
                new_interface = nb.dcim.interfaces.create(data)
                print(new_interface)
            except pynetbox.core.query.RequestError as e:
                if 'Interface with this Device and Name already exists' in str(e):
                    print(f"Інтерфейс з іменем {interface['name']} вже існує.")
                    continue
                else:
                    print(f"Помилка при створенні інтерфейсу: {str(e)}")
                    
def delete_interfaces():
    interfaces_to_delete = nb.dcim.interfaces.filter(name='eth1/1', type="10gbase-t")
    print(len(interfaces_to_delete))
    for interface in interfaces_to_delete:
        try:
            interface.delete()
            print(f"Інтерфейс {interface.name} видалений успішно.")
        except pynetbox.core.query.RequestError as e:
            print(f"Помилка при видаленні інтерфейсу {interface.name}: {str(e)}")

def create_connections():
    cisco_router = {
    'device_type': 'cisco_ios',
    'host': '10.201.100.3',
    'username': 'hrynkov',
    'password': 'BgYbQU71',
    'secret': '7753191',
    'port': 22,
    }
    ssh = ConnectHandler(**cisco_router)
    result = ssh.send_command('show interface brief')
    #result = ssh.send_command('show interface')
    with open("interface.txt", 'w') as f:
        f.write(result)
    filename = 'interface.txt'
    
    # with open(filename) as f:
    #     for line in f:
    #         if line.startswith("  Description:"):
    #             description = line.split()[-1]
    #         elif line.startswith("  Hardware:"):
    #             mac_address = line.split()[4]
    #             print(f"{} {}")
    
    with open(filename) as f:
       for line in f:
            colums = line.split()
            #print(colums)
            if len(colums) > 0 and ('/' in colums[0] or re.search(r'Po\d', colums[0])):
                interface_name = colums[0]
                interface_mode = 'tagged' if colums[3].lower() == 'trunk' else colums[3].lower()
                interface_status = colums[4]
                interface_speed = colums[6]
                
                
            device = nb.dcim.devices.get(name='DC1_RD5_Nexus-1')  # Замініть ідентифікатор на свій

            # Створення інтерфейсу в NetBox
            if 'Po' in interface_name:
                interface_type = 'lag'
            elif '10G' in interface_speed:
                interface_type = '10gbase-t'

            # Опреділити статус в залежності від статусу
            enabled = True if interface_status.lower() == 'up' else False
            data = {
                'device': device.id,
                'name': interface_name,
                'mode': interface_mode,
                'status': interface_status,
                'type': interface_type,
                'enabled': enabled,
            }

            try:
                new_interface = nb.dcim.interfaces.create(data)
                print(f"Інтерфейс {interface_name} створено в NetBox.")
            except pynetbox.core.query.RequestError as e:
                if 'Interface with this Device and Name already exists' in str(e):
                    print(f"Інтерфейс з іменем {interface_name} вже існує в NetBox.")
                else:
                    print(f"Помилка при створенні інтерфейсу {interface_name} в NetBox: {str(e)}")
                
    
create_connections()
    
    
