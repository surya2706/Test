__author__ = "Karthik Surya"

import sys
from api_helper import ApiHelper
from conf import url, header


def main(mac_address):
    print("Entered mac address is {}".format(mac_address))
    api_helper = ApiHelper(url, header)
    response = api_helper.get_mac_addr_details(mac_address)
    if not response:
        print('Sorry, there is an Error. Check the mac address.')
        return
    company_name = response.get('vendorDetails').get('companyName')
    print('Company name for mac address {} is : {}'.format(
        mac_address, company_name))


if __name__ == "__main__":
    print("Executing python cisco-test")
    main(sys.argv[1])
