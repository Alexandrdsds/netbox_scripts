#!/usr/bin/env python3
from pprint import pprint
import pynetbox
import requests
nb = pynetbox.api(
        'https://netbox.dpsu.gov.ua',
    token='8a2f84287748453d629ed55b74f32c314b0e2d48'
)
def create_devices():
    #Here modifies
    devices_info = [
    {'device_type': 'Nexus N9K-C93180YC-FXl', 
     'device_role': 'aci leaf',
     'site': '2030',
     'location': 'DC2',
     'rack': 'FD1', 
     'position': 22.0, 
     'face': 'front', 
     'status': 'active',
     'serial': ''
    },
     {'device_type': 'Nexus N9K-C93180YC-FXl', 
     'device_role': 'aci leaf',
     'site': '2030',
     'location': 'DC2',
     'rack': 'FD1', 
     'position': 20.0, 
     'face': 'front', 
     'status': 'active',
     'serial': ''
    },
    {'device_type': 'FortiAnalyzer 300G', 
     'device_role': 'Firewall Manager Center',
     'site': '2030',
     'location': 'DC2',
     'rack': 'RD5', 
     'position': 37.0, 
     'face': 'front', 
     'status': 'active',
     'serial': ''
    },
    {'device_type': 'Fortinet FortiGate 100F', 
     'device_role': 'Firewall',
     'site': '2030',
     'location': 'DC2',
     'rack': 'RD5', 
     'position': 36.0, 
     'face': 'front', 
     'status': 'active',
     'serial': ''
    },
    {'device_type': 'FortiManager 400G', 
     'device_role': 'Firewall Manager Center',
     'site': '2030',
     'location': 'DC2',
     'rack': 'RD5', 
     'position': 15.0, 
     'face': 'front', 
     'status': 'active',
     'serial': ''
    },
    {'device_type': 'Catalyst 9300 24S', 
     'device_role': 'aci leaf',
     'site': '2030',
     'location': 'DC2',
     'rack': 'RD1', 
     'position': 32.0, 
     'face': 'front', 
     'status': 'active',
     'serial': ''
    },
    {'device_type': 'PowerEdge R650', 
     'device_role': 'server',
     'site': '2030',
     'location': 'DC2',
     'rack': 'RD1', 
     'position': 7.0, 
     'face': 'front', 
     'status': 'active',
     'serial': '79FH7T3'
    },
    {'device_type': 'PowerEdge R650', 
     'device_role': 'server',
     'site': '2030',
     'location': 'DC2',
     'rack': 'RD1', 
     'position': 27.0, 
     'face': 'front', 
     'status': 'active',
     'serial': '6R457T3'
    },
    {'device_type': 'PowerEdge R650', 
     'device_role': 'server',
     'site': '2030',
     'location': 'DC2',
     'rack': 'RD1', 
     'position': 27.0, 
     'face': 'front', 
     'status': 'active',
     'serial': '6R457T3'
    },
    
    ]
    for device_info in devices_info:
        device_type = nb.dcim.device_types.get(slug=device_info['device_type'].replace(' ','-').lower().translate({ord(i): None for i in '+'}))
        device_role = nb.dcim.device_roles.get(slug=device_info['device_role'].replace(' ','-').lower())
        site = nb.dcim.sites.get(slug=device_info['site'])
        location = nb.dcim.locations.get(name=device_info['location'].upper())
        position = device_info['position']
        face = device_info['face']
        status = device_info['status']
        serial_number = device_info['serial']
        rack = nb.dcim.racks.get(name=device_info['rack'].upper(),site_id=site.id,location_id=location.id)
        existing_device = nb.dcim.devices.get(rack_id=rack.id, position=position)
        data = {
            'device_type': device_type.id,
            'role': device_role.id,
            'site': site.id,
            'location': location.id,
            'rack': rack.id,
            'serial': serial_number,
            'position': position,
            'face': face,
            'status': status,
        }
        if existing_device != None:
            # Unrack існуючий пристрій
            try:
                data_for_unracked = [{'id': existing_device.id, 'position': ''}]
                print(f"Пристрій з id {existing_device.id} unracked в {site} {rack.name}.")
                nb.dcim.devices.update(data_for_unracked)
            except pynetbox.core.query.RequestError as e:
                print(f"Помилка при unracking пристрою {existing_device.id} в NetBox: {str(e)}")
            try:
                new_device = nb.dcim.devices.create(data)
                print(f"Пристрій {new_device} створено в NetBox.")
            except pynetbox.core.query.RequestError as e:
                print(f"Помилка при створенні пристрою {new_device} в NetBox: {str(e)}")
        else:
                # Створюємо новий пристрій
            try:
                new_device = nb.dcim.devices.create(data)
                print(f"Пристрій {new_device} створено в NetBox.")
            except pynetbox.core.query.RequestError as e:
                if 'already occupied' in str(e):
                    print(f'Зайнятий unit {position} в {site} {rack.name}. {device_type} {serial_number} НЕ СТВОРЕНО')
                else:
                    print(f"Помилка при створенні пристрою {new_device} в NetBox: {str(e)}")
#create_devices()
devices = nb.dcim.devices.get(rack_id=41)
height = int(devices.device_type['model'].split('U')[0])
#pprint(dict(devices.device_type['model']))
