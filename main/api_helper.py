__author__ = "Karthik Surya"

import json
from urllib.request import Request, urlopen


class ApiHelper:

    @classmethod
    def get(cls, url, headers):
        """
        Helper function which fetches the resource using GET request
        :param url: Url to query in the network
        :param headers: Header to be passed to the network url
        :return: Response
        """
        req = Request(url, headers=headers)
        try:
            with urlopen(req) as response:
                if response.status != 200:
                    return
                for line in response:
                    response_in_dict = json.loads(line)
                    return response_in_dict
        except:
            return
