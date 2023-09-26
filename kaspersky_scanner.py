#!/usr/bin/env python

import requests
import json 
import pandas

kaspersky_headers = {
    'x-api-key': 'API-KEY'
}

def scan_domain():
    domain = input("Enter domain: ")
    kaspersky_domain = f'https://opentip.kaspersky.com/api/v1/search/domain?request={domain}'
    response = requests.request(method='GET', url=kaspersky_domain, headers=kaspersky_headers)
    decodedResponse = json.loads(response.text)
    return decodedResponse
    
def scan_hash():
    hash_value = input("Enter hash value: ")
    kaspersky_hash = f'https://opentip.kaspersky.com/api/v1/search/hash?request={hash_value}'
    response = requests.request(method='GET', url=kaspersky_hash, headers=kaspersky_headers)
    decodedResponse = json.loads(response.text)
    return decodedResponse
    
def scan_ip():
    ip = input("Enter IP address: ")
    kaspersky_ip = f'https://opentip.kaspersky.com/api/v1/search/ip?request={ip}'
    response = requests.request(method='GET', url=kaspersky_ip, headers=kaspersky_headers)
    decodedResponse = json.loads(response.text)
    return decodedResponse
    
def scan_url():
    url = input("Enter url: ")
    kaspersky_url = f'https://opentip.kaspersky.com/api/v1/search/url?request={str(url)}'
    response = requests.request(method='GET', url=kaspersky_url, headers=kaspersky_headers)
    decodedResponse = json.loads(response.text)
    return decodedResponse

def dashboard():
    print("\n[+] Kaspersky Scanner")
    print("\n[+] Available options")
    print("\n[1] Scan Domain")
    print("\n[2] Scan Hash")
    print("\n[3] Scan IP")
    print("\n[4] Scan Url")

    option = input("\nEnter option to scan: ")
    
    if option == '1':
        result = scan_domain()
        print(result)
    elif option == '2':
        result = scan_hash()
        print(result)
    elif option == '3':
        result = scan_ip()
        print(result)
    elif option == '4':
        result = scan_url()
        print(result)
    else:
        print("Invalid choice")

while True:
    dashboard()





