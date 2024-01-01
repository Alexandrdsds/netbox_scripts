#!/usr/bin/env python3
import pynetbox

nb = pynetbox.api(
        'https://netbox.dpsu.gov.ua',
    token='8a2f84287748453d629ed55b74f32c314b0e2d48'
)
listserial = [
              '6J70VW2','5J70VW2','3J70VW2','4J70VW2','3NVF5Y1','DSFWG62','DSFSS62','DR8YF82','979MRH2','97BHRH2','8LNG8X2','9LNG8X2','JQ5L973','DMDW2T2','DMDT2T2','BFCT8X3','CFCT8X3','DFCT8X3',
              '8FCT8X3','9FCT8X3','7FCT8X3','GJXPYQ2','GJYJYQ2','GJWNYQ2','GJXQYQ2','FKFGXP2','GJWKYQ2','GJVPYQ2','GJXMYQ2','GJXJYQ2','8RXTV33','461VV33','9RXTV33','261VV33','661VV33','7SXY1L2','3818Y42',
              '4SKYTS1','DR8F9X3','BQF984900002','CZ275201P2','CZ275201P3','CZ275201NY','CZ275201NZ','CZ275201P0','CZ275201P1','BNVF5Y1','979QRH2','GJRJYQ2', 'CZ275201P3']
def show_devices():
    roles = [7,12]
    devices = list(nb.dcim.devices.filter())
    for device in devices:
        
    #nb.dcim.devices.update([
    #print(device.name, device.id, device.serial)
    #{'id': 172, 'name': 'esxi-245.dpsu.dpsugov.loc'},
    #{'id': 80, 'name': 'esxi-113.dpsu.dpsugov.loc'},
    #{'id': 79, 'name': 'esxi-114.dpsu.dpsugov.loc'},
    #{'id': 82, 'name': 'esxi-111.dpsu.dpsugov.loc'}
    #{'id': 81, 'name': 'esxi-112.dpsu.dpsugov.loc'},
    #])
        print(device.name, device.id, device.serial, device.site, device.location, device.rack, device.position, device.url, device.device_type)
    #print(type(device.position))
    print(len(devices))

def show_device_types():
    devices = list(nb.dcim.device_types.filter())
    for device in devices:
        print(device.manufacturer, device, device.id, device.is_full_depth)

def create_racks():
    counts = ['RD1','RD2','RD3','RD4','RD5','RD6']
    for count in counts:
        data = [
    
            {
            'site': 1,
            'locations': 'DC1.2',
            'name': count,
            'status': 'active',
            'role': 3
            },
    
            ]
        new_racks = nb.dcim.racks.create(data)
        print(new_racks)
    
def create_module_bays():
   
    devices_info = [
        {
        'device': 173, 
        'name': 'NIC.Embedded',
        'position': 1,  
        },
        {
        'device': 173, 
        'name': 'NIC.Mezzanine',
        'position': 2,  
        },
        {
        'device': 173, 
        'name': 'NIC.Slot.3',
        'position': 3,  
        },
        {
        'device': 173, 
        'name': 'FC-Network Card',
        'position': 4,  
        },
        {
        'device': 173, 
        'name': 'Storage Controller',
        'position': 5,  
        },
        {
        'device': 171, 
        'name': 'NIC.Embedded',
        'position': 1,  
        },
        {
        'device': 171, 
        'name': 'NIC.Mezzanine',
        'position': 2,  
        },
        {
        'device': 171, 
        'name': 'NIC.Slot.3',
        'position': 3,  
        },
        {
        'device': 171, 
        'name': 'FC-Network Card',
        'position': 4,  
        },
        {
        'device': 171, 
        'name': 'Storage Controller',
        'position': 5,  
        },
        {
        'device': 169, 
        'name': 'NIC.Embedded',
        'position': 1,  
        },
        {
        'device': 169, 
        'name': 'NIC.Mezzanine',
        'position': 2,  
        },
        {
        'device': 169, 
        'name': 'NIC.Slot.3',
        'position': 3,  
        },
        {
        'device': 169, 
        'name': 'FC-Network Card',
        'position': 4,  
        },
        {
        'device': 169, 
        'name': 'Storage Controller',
        'position': 5,  
        },
        {
        'device': 168, 
        'name': 'NIC.Embedded',
        'position': 1,  
        },
        {
        'device': 168, 
        'name': 'NIC.Slot.2',
        'position': 2,  
        },
        {
        'device': 168, 
        'name': 'FC-Network Card',
        'position': 3,  
        },
        {
        'device': 168, 
        'name': 'Storage Controller',
        'position': 4,  
        },
        {
        'device': 167, 
        'name': 'NIC.Embedded',
        'position': 1,  
        },
        {
        'device': 167, 
        'name': 'NIC.Slot.2',
        'position': 2,  
        },
        {
        'device': 167, 
        'name': 'FC-Network Card',
        'position': 3,  
        },
        {
        'device': 167, 
        'name': 'Storage Controller',
        'position': 4,  
        },
    
        ]
    for device_info in devices_info:
        data = {
            'device': device_info['device'],
            'name': device_info['name'],
            'position': device_info['position']
        }
        new_module = nb.dcim.module_bays.create(data)
        print(new_module)
   
def update_module_bays():
    nb.dcim.module_bays.update([
    {'device': 82, 'id': 57,' manufacturer': 'Qlogic', 'module_type': 7},
    #{'id': 54, 'module_type': ''}
    #{'id': 80, 'name': 'esxi-113.dpsu.dpsugov.loc'},
    #{'id': 79, 'name': 'esxi-114.dpsu.dpsugov.loc'},
    #{'id': 82, 'name': 'esxi-111.dpsu.dpsugov.loc'},
    #{'id': 81, 'name': 'esxi-112.dpsu.dpsugov.loc'},
    ])
    
def show_module_bays():
    rack = nb.dcim.racks.get(site='2010', name="RD6",  location_id=2, role='server')
    servers_in_rack = nb.dcim.devices.filter(rack.id, role='server',device_type_id='56')
    for server in servers_in_rack:
        modules = list(nb.dcim.module_bays.filter(site='2010',rack='RD6',role='server',device_id=server.id))
    for module in modules:
        print(module.name, module.id, module)
       
def show_module_types():
    types = list(nb.dcim.module_types.filter())
    for mod_type in types:
        print(mod_type, mod_type.id, mod_type.manufacturer, mod_type.part_number)
        
def check_and_create_module_types():
    
    manufacturers = list(nb.dcim.manufacturers.filter(name='Qlogic'))
    for manufacture in manufacturers:
            module_type_data_to_check = {
            'manufacturer_id': manufacture.id,
            'model': 'FC16 2P QLE2692 Adapter',
            'part_number': '03C27H'
            }
    existing_module_type = nb.dcim.module_types.get(**module_type_data_to_check)
    if existing_module_type:
        print(f"Модуль типу {existing_module_type} вже існує: {existing_module_type}\n" 
              f"ID: {existing_module_type.id}\n"
              f"Виробник: {existing_module_type.manufacturer}")
    else:
        data = [
        {
        'manufacturer': module_type_data_to_check['manufacturer_id'],
        'model': module_type_data_to_check['model'],
        'part_number': module_type_data_to_check['part_number']
        },]
        new_module = nb.dcim.module_types.create(data)
        print(f"Модуль {new_module} успішно створений")
        
def show_and_crearte_manufacturers():
    manufacturer = {'name': 'SAMSUNG'.title()}
    existing_manufacture_type = nb.dcim.manufacturers.get(**manufacturer)
    if existing_manufacture_type:
        print(f"Виробник {existing_manufacture_type} вже існує. Його ID: {existing_manufacture_type.id}")
    else:
        data = [
        {
        'name': manufacturer['name'],
        'slug': manufacturer['name'].lower()
        },]
        new_manufacturer = nb.dcim.manufacturers.create(data)
        print(f"Виробник {new_manufacturer} успішно доданий")

def create_interfaces():
    id_devices = [82]
    interface_data = [
        #{'number': 2, 'type': '25gbase-kr', 'module_name': 'NIC.Slot.5', 'mac_address': 'BC:97:E1:26:9F:F0', 'enabled': 'false'},
        #{'number': 3, 'type': '25gbase-kr', 'module_name': 'NIC.Slot.5', 'mac_address': 'BC:97:E1:26:9F:F1', 'enabled': 'false'},
        #{'number': 0, 'type': '25gbase-x-sfp28', 'module_name': 'NIC.Integrated.1-1', 'mac_address': 'BC:97:E1:69:CB:80','enabled': 'true'},
        #{'number': 1, 'type': '25gbase-x-sfp28', 'module_name': 'NIC.Integrated.1-1', 'mac_address': 'BC:97:E1:69:CB:81','enabled': 'true'},
        {'number': 6, 'type': '16gfc-sfpp', 'module_name': 'FC.Slot.4-1', 'wwn': '20:00:F4:C7:AA:09:61:36','enabled': 'true'},
        {'number': 7, 'type': '16gfc-sfpp', 'module_name': 'FC.Slot.4-1', 'wwn': '20:00:F4:C7:AA:09:61:37','enabled': 'true'},
        

       
     
    
    ]

    module_mapping = {
        #'NIC.Slot.5': 450,
        #'NIC.Slot.5': 450,
        #'NIC.Integrated.1-1': 448,
        #'NIC.Integrated.1-1': 448,
        'FC.Slot.4-1': 451,
        'FC.Slot.4-1': 451
        
           
        
        # Додайте інші зв'язки
    }

    servers_in_rack = list(nb.dcim.devices.filter(id=id_devices))
    for server in servers_in_rack:
        for interface_info in interface_data:
            number = interface_info['number']
            interface_name = f'vmnic{number}'
        
            data = [
                {
                    'device': server.id,
                    'name': interface_name,
                    'type': interface_info['type'],
                    'module': module_mapping.get(interface_info['module_name']),
                    #'mac_address': interface_info['mac_address'],
                    'wwn': interface_info['wwn'],
                    'enabled': interface_info['enabled']
                },
            ]

            try:
                new_interface = nb.dcim.interfaces.create(data)
                print(new_interface)
            except pynetbox.core.query.RequestError as e:
                if 'Interface with this Device and Name already exists' in str(e):
                    print(f"Інтерфейс з іменем {interface_name} вже існує.")
                    continue
                else:
                    print(f"Помилка при створенні інтерфейсу: {str(e)}")
                    
                    
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
        
        
            
def show_modules():
    #modules = {'name': ''}
    #existing_modules_type = nb.dcim.modules.get(**modules)
    #if existing_manufacture_type:
    #    print(f"Модуль {existing_modules_type} вже існує. Його ID: {existing_modules_type.id}")
    #else:
    devices = [82]
    modules = list(nb.dcim.modules.filter(site='2010', rack='RD3', device_id=devices))
    for module in modules:
        print(module)
    

def create_modules():
        names = ['Linecard (slot 2)']
        id_devices = [110]
        module_type_mapping = {
            'Linecard (slot 2)': 114, #show_module_types
        }
        modules = list(nb.dcim.module_bays.filter(site='2010',device_id=id_devices,name=names))
        for module in modules:
            print(module)
            id_module = module.id
            id_device = module.device.id
            
            module_name = module.name
            manufacturer = module_name.split()[0]  # Отримайте перше слово, яке є виробником
            module_type = module_type_mapping.get(module_name, None)
            
            data = [
            {
            'device': id_device,
            'manufacturer': manufacturer, 
            'module_type': module_type,
            'module_bay': id_module,
            'serial': 'CAT2240L59R',
            'description': '1'
            },
            
            ]
            try:
                new_module = nb.dcim.modules.create(data)
                print(f"Модуль {new_module} успішно доданий")
            except pynetbox.core.query.RequestError as e:
                if 'Module bay already exists' in str(e):
                    print(f"Модуль {module.name} з ідентифікатором {id_module} вже існує.")
                    continue
                else:
                    print(f"Помилка при додаванні модуля: {str(e)}")
        
def show_manufacturer():
    manufacturers = list(nb.dcim.manufacturers.filter())
    for manufacture in manufacturers:
        print(manufacture.name, manufacture.id)
        
def delete_module_bays():
    rack = nb.dcim.racks.get(site='2010',name='RD3', role='server')
    servers_in_rack = nb.dcim.devices.filter(rack_id=rack.id, role='server',device_type_id='32')
    for server in servers_in_rack:
        modules = list(nb.dcim.module_bays.filter(site='2010',rack='RD3',role='server',device_id=server.id, name='RDMA Ethernet Controller 2'))
        for module in modules:
            module.delete()
        #module_bay_names_to_delete = ['RDMA Ethernet Controller 1', 'RDMA Ethernet Controller 2']
        #module_bays_to_delete = nb.dcim.module_bays.filter(device=server.id, name__in=module_bay_names_to_delete)
        #for module_bay in module_bays_to_delete:
        #    deleted_module_bay = module_bays.delete()
        #    if deleted_module_bay:
        #        print(f"Модульний слот {module_bay.name} на сервері {server.name} було видалено.")
        #    else:
        #        print(f"Помилка під час видалення модульного слоту {module_bay.name} на сервері {server.name}.")

def show_device_role():
    roles = list(nb.dcim.device_roles.filter())
    for role in roles:
        print(role, role.id)

def show_interfaces():
    interfaces = list(nb.dcim.interfaces.filter())
    for interface in interfaces:
        print(interface.module, interface.device, interface.rack)

def delete_devices():
    device_id_to_delete = [175,174,173,171,169,168,167]  # ID девайса, який потрібно видалити
    for dev_id in device_id_to_delete:
        device_to_delete = nb.dcim.devices.get(id=dev_id)
        if device_to_delete:
            try:
                deleted_device = device_to_delete.delete()
                if deleted_device:
                    print(f"Девайс з ID {device_id_to_delete} успішно видалений.")
                else:
                    print(f"Помилка під час видалення девайса з ID {device_id_to_delete}.")
            except pynetbox.core.query.RequestError as e:
                print(f"Помилка при видаленні девайса: {str(e)}")
        else:
            print(f"Девайс з ID {device_id_to_delete} не знайдений.")

def check_and_create_device_types():
    
    manufacturers = list(nb.dcim.manufacturers.filter(name='Cisco'))
    for manufacture in manufacturers:
            device_type_data_to_check = {
            'manufacturer_id': manufacture.id,
            'model': "FortiManager 400G",
            }
    existing_device_type = nb.dcim.device_types.get(**device_type_data_to_check)
    if existing_device_type:
        print(f"Device типу {existing_device_type} вже існує\n" 
              f"ID: {existing_device_type.id}\n"
              f"Виробник: {existing_device_type.manufacturer}")
    else:
        data = [
        {
        'manufacturer': device_type_data_to_check['manufacturer_id'],
        'model': device_type_data_to_check['model'],
        'slug': device_type_data_to_check['model'].replace(' ', '-').translate({ord(i): None for i in '+'}).lower(),
        'is_full_depth': False,
        'u_height': 1
        },]
        new_device = nb.dcim.device_types.create(data)
        print(f"Device {new_device} успішно створений")

def update_device():
    id = [287,288,405,406,407,408,409]
    for i in id:
        nb.dcim.devices.update([
        {'id': 287, 'name': 'esxi-191.dpsu.dpsugov.loc'},
        ])

def create_items():
    #list_name = ['DIMM.Socket.B1','DIMM.Socket.B5','DIMM.Socket.B3','DIMM.Socket.B2','DIMM.Socket.A4','DIMM.Socket.A2','DIMM.Socket.A3','DIMM.Socket.B6','DIMM.Socket.B4','DIMM.Socket.A1','DIMM.Socket.A5','DIMM.Socket.A6']
    #list_serial = ['2694E2D8','2694D0B2','2694D045','2694DAF9','2694DAC5','2694DA64','2694E024','2694D06F','2694DACB','2694E2AA','2694E095','2694DA9E']
    #for name, serial in zip(list_name, list_serial):
        items_data = [
            ############################DISK##########################
            #{'device': 82,
            # 'name': 'PCIe SSD in Slot 20 in Bay 1', 
            # 'label': 'PCIe',
            # 'role': 'SSD',
            # 'serial_number': 'PHKE001400YL375AGN',
            # 'description': 'Size 349.32 GB', 
            # 'manufacturer': 'Intel'
            # },
            #############################RAM################################
            #{'device': 82,
            # 'name': name, 
            # 'label': 'DDR4',
            # 'role': 'RAM',
            # 'part_id': '36ASF4G72PZ-2G9J3', 
            # 'serial_number': serial,
            # 'description': 'Size 32 GB, SPEED 2933 MHZ', 
            # 'manufacturer': 'Micron'
            # },
            ##########################CPU###################################
            {'device': 82,
             'name': 'Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz', 
             'role': 'CPU',
             'description': 'Total Cores 20| MAX SPEED 4000 MHZ | CURRENT SPEED 2500 MHZ ', 
             'manufacturer': 'Intel'
             },
                     
    
        ]
        for item_info in items_data:
            servers_in_rack = list(nb.dcim.devices.filter(id=item_info['device']))
            for server in servers_in_rack:
                    items_roles = list(nb.dcim.inventory_item_roles.filter(name=item_info['role']))
                    for role in items_roles:
                        manufacturers = nb.dcim.manufacturers.filter(name=item_info['manufacturer'].title())
                        for manufacture in manufacturers:
                            inventory_item_data =  {
                                'device': server.id,
                                'name': item_info['name'],
                                'label': item_info['label'],
                                'role': role.id,
                                'serial': item_info['serial_number'],
                                'part_id': item_info['part_id'],
                                'description': item_info['description'],
                                'manufacturer': manufacture.id
                                }
                            existing_device_type = list(nb.dcim.inventory_items.filter(inventory_item_data['serial']))
                            if existing_device_type:
                                print(f"Device {inventory_item_data['name']} вже існує\n" 
                                f"Serial: {inventory_item_data['serial']}\n")
                                continue
                            else:
                                new_inventory_item = nb.dcim.inventory_items.create(**inventory_item_data)
                                print(f'{new_inventory_item} успішно створено')
                

#create_items()
#show_devices()
#create_modules()
#update_modules()
#update_module_bays()
#create_module_bays()
#show_module_bays()
#show_modules()
#show_module_types()
#create_module_types()
#show_manufacturer()
#print("###############################################################")
#check_and_create_module_types()
#show_and_crearte_manufacturers()
#delete_module_bays()
#create_interfaces()
#show_device_types()
#print("###############################################################")
#delete_devices()
#create_racks()
#show_device_role()
check_and_create_device_types()
#show_interfaces()
#create_more_interfaces()
#delete_interfaces()
