__author__ = "Karthik Surya"

from urllib.parse import urlencode
from api_helper import ApiHelper


class MacService:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_company_name(self, mac_address):
        """
        Fetches the details of the Mac Address
        :param mac_address:
        :return: Response from the network
        """
        full_url = '{}{}'.format(self.url, urlencode({'search': mac_address}))
        response = ApiHelper.get(full_url, self.headers)
        if not response:
            return {'success': False, 'error': 'Please check the mac address'}

        company_name = response.get('vendorDetails').get('companyName')
        return {'companyName': company_name, 'success': True}

