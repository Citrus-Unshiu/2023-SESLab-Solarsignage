import sys
import requests
import json

modbus_addr = '<modbus_address>'
wrapper_addr = '<solar_wrapper_address>'

host = '<tinyIoT_server_address>'
port = '8080'

headers = {
    'X-M2M-Origin': '<om2m-id>:<om2m-passwd>',
    'Content-Type': '',
    'Cache-Control': 'no-cache',
}

def create_ae(api, rn):
    # create Modbus IPE AE
    headers['Content-Type'] = 'application/json;ty=2'
    data = {
        'm2m:ae': {
            'api': api,
            'rn': rn,
            'lbl': [],
            'rr': True
        }
    }
    res = requests.post(f'http://{host}:{port}/~/in-cse', json=data, headers=headers)
    print('[CREATE AE]', res.status_code)

    if res.status_code != 201:
        sys.exit('AE creation is failed.')

def create_cnt(ae_name, cnt_name, data):  # Modify function name and parameters
    headers['Content-Type'] = 'application/json;ty=3'
    res = requests.post(f'http://{host}:{port}/~/in-cse/in-name/{ae_name}', json=data, headers=headers)
    print(f'[CREATE {cnt_name} CONTAINER]', res.status_code)

    if res.status_code != 201:
        sys.exit(f'{cnt_name} container creation is failed.')

def create_sub(ae_name, cnt_name, rn, nu):
    headers['Content-Type'] = 'application/json;ty=23'
    data = {
        'm2m:sub': {
            'rn': rn,
            'nu': [nu],
            'nct': 2
        }
    }
    res = requests.post(f'http://{host}:{port}/~/in-cse/in-name/{ae_name}/{cnt_name}', json=data, headers=headers)
    print(f'[CREATE {cnt_name} SUBSCRIPTION]', res.status_code)

    if res.status_code != 201:
        sys.exit(f'{cnt_name} subscription creation is failed.')

def create_ipe_cnt():  # Modify function name
    IPE_NAME = "Modbus_IPE"
    cnts = ['battery', 'energyGeneration', 'energyConsumption']
    battery_subrn = ["cnd", "rn", "level", "current", "voltage", "power", "maxvolt", "minvolt", "temp", "charging", "discharging"]
    energyGeneration_subrn = ["cnd", "rn", "power", "current", "voltage", "daily", "monthly", "annual", "total", "maxvolt", "minvolt"]
    energyConsumption_subrn = ["cnd", "rn", "power", "current", "voltage", "daily", "monthly", "annual", "total"]
    
    
    for cnt in cnts:    
        data = {
            "m2m:cnt" : {
                "rn" : cnt
            }
        }
        if cnt == "battery":            
            create_cnt(IPE_NAME, cnt, data)
            for subrn in battery_subrn:
                data = {
                    "m2m:cnt" : {
                        "rn" : subrn
                    }
                }       
                create_cnt(IPE_NAME + f"/{subrn}", subrn, data)
        if cnt == "energyGeneration":
            create_cnt(IPE_NAME, cnt, data)
            for subrn in energyGeneration_subrn:
                data = {
                    "m2m:cnt" : {
                        "rn" : subrn
                    }
                }       
                create_cnt(IPE_NAME + f"/{subrn}", subrn, data)
        if cnt == "energyConsumption":
            create_cnt(IPE_NAME, cnt, data)
            for subrn in energyConsumption_subrn:
                data = {
                    "m2m:cnt" : {
                        "rn" : subrn
                    }
                }       
                create_cnt(IPE_NAME + f"/{subrn}", subrn, data)


if __name__ == "__main__":
    create_ae('modbus-ipe', 'Modbus_IPE')
    create_ipe_cnt()

    create_ae('solar-ae', 'Solar_AE')
    create_solar_cnt()

    input('\n[*] If you want create subscriptions, press any keys (It requires \'solar wrapper\' is running.)')
    create_sub()
