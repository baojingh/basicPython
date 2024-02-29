#!/usr/bin/env python

# -*- coding: UTF-8 -*-


'''
@File          : http-client.py
@Author        : baojing.he
@Date          : 2/29/2024 10:18 AM
@Description   : 
'''

import json
import requests

with open("/var/run/edgedevice/certsips.json", 'r') as certsip:
    data = json.load(certsip)
    DEVICE_IP = data["edge-ips"]
    API_PATH = "/device/edge/b.service/api/v1"

BASE_URL = "https://" + DEVICE_IP + API_PATH
HEADERS = {
    'accept': '*/*',
    'Content-Type': 'application/json'
}

def get_device_id():
    try:
        response = requests.request("GET", BASE_URL,
                                    # headers=HEADERS, verify="/root/cacert.crt").json()
                                    headers = HEADERS, verify =False).json()
        print(response)
    except Exception as result:
        print(result)

if __name__ == '__main__':
    get_device_id()