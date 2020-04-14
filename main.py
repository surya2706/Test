__author__ = "Karthik Surya"

import json
from urllib.request import Request, urlopen
from conf import url, header

print("Executing python cisco-test")

mac_address = input("Enter the mac address: ")
full_url = '{}{}'.format(url, mac_address)
company_name = None

req = Request(full_url, headers=header)
with urlopen(req) as response:
    for line in response:
        line_in_dict = json.loads(line)
        company_name = line_in_dict.get("vendorDetails").get('companyName')

print('Company name: {}'.format(company_name))
