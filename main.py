import json
import os
from file_manager import write_data, read_data
from data_filter_enum import DataFilterEnum as data_field

# REGISTRAR DATOS COMPRA
# date format dd/MM/yyyy

#Carga los registros antiguos
def load_registers():
    data_read = read_data()
    if (data_read == ''):
        return []
    json_deserialized = json.loads(data_read)
    return json_deserialized

#Obtiene los registros guardados y añade el nuevo
def register_buy_data(deal_name, cost, date, desc):
    registers = load_registers()
    data = create_data(deal_name, cost, date, desc)
    print(data)
    registers.append(data)
    data_json = json.dumps(registers)
    write_data(data_json)
    return ''

#Crea el objeto de registro de compra
def create_data(deal_name, cost, date, desc):
    return {
        data_field.DEAL.name: deal_name,
        data_field.DATE.name: date,
        data_field.COST.name: cost,
        data_field.DESC.name: desc
    }

def create_filter(field_to_filter):
    if (type(field_to_filter) is data_field):
        filter_value = field_to_filter.name
        print('-- Creating data structure with filter: ' + filter_value)
        registers = load_registers()
        new_register_map = {} 
        for purchase_data in registers:
            key = purchase_data[filter_value]
            purchase_data.pop(filter_value, None)
            data_for_this_filter = new_register_map.get(key)  
            #si el valor es None, aun no hay valor para esa clave y hay que crearlo
            if (data_for_this_filter is None):
                data_for_this_filter = []    
            data_for_this_filter.append(purchase_data)
            new_register_map[key] = data_for_this_filter
        return new_register_map
    else:
        print("There is no filter")



register_buy_data('Mercadona', 25, '04/09/2020', 'Compra en mercadona')
#read_data()
#load_registers()
print(create_filter(data_field.DATE))
