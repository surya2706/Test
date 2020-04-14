__author__ = "Karthik Surya"

import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode


class ApiHelper:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_mac_addr_details(self, mac_addr):
        """
        A function which takes mac_addr as the parametr and returns the JSON response.
        If there is an exception on the response status code is other than 200, it returns None.
        """
        full_url = '{}{}'.format(self.url, urlencode({'search': mac_addr}))
        req = Request(full_url, headers=self.headers)
        try:
            with urlopen(req) as response:
                if response.status != 200:
                    return
                for line in response:
                    response_in_dict = json.loads(line)
                    return response_in_dict
        except:
            return
