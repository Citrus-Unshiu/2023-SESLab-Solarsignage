import sys
import requests

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
    cnts = ['battery', 'energyGeneration', 'energyConsumption']

    for cnt in cnts:
        if cnt == 'battery':
            data = {
                'm2m:cnt': {  # Modify resource type
                    'cnd': cnt,
                    'rn': cnt,
                    'level': None,
                    'current': None,
                    'voltage': None,
                    'power': None,
                    'maxvolt': None,
                    'minvolt': None,
                    'temp': None,
                    'charging': None,
                    'discharging': None
                }
            }
        elif cnt == 'energyGeneration':
            data = {
                'm2m:cnt': {  # Modify resource type
                    'cnd': cnt,
                    'rn': cnt,
                    'power': None,
                    'current': None,
                    'voltage': None,
                    'daily': None,
                    'monthly': None,
                    'annual': None,
                    'total': None,
                    'maxvolt': None,
                    'minvolt': None
                }
            }
        elif cnt == 'energyConsumption':
            data = {
                'm2m:cnt': {  # Modify resource type
                    'cnd': cnt,
                    'rn': cnt,
                    'power': None,
                    'current': None,
                    'voltage': None,
                    'daily': None,
                    'monthly': None,
                    'annual': None,
                    'total': None
                }
            }

        create_cnt('Modbus_IPE', cnt, data)  # Modify function call

# ³ª¸ÓÁö ºÎºÐÀº µ¿ÀÏÇÏ°Ô À¯ÁöµË´Ï´Ù.

if __name__ == "__main__":
    create_ae('modbus-ipe', 'Modbus_IPE')
    create_ipe_cnt()

    create_ae('solar-ae', 'Solar_AE')
    create_solar_cnt()

    input('\n[*] If you want create subscriptions, press any keys (It requires \'solar wrapper\' is running.)')
    create_subs()
