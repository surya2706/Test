__author__ = "Karthik Surya"

import sys
from flask import Flask, jsonify, request
from api_helper import ApiHelper
from conf import url, header

app = Flask(__name__)


@app.route("/mac_address/<mac_address>")
def hello(mac_address):
    api_helper = ApiHelper(url, header)
    response = api_helper.get_mac_addr_details(mac_address)

    if not response:
        return jsonify({'success': False, 'error': 'Please check the mac address'})

    company_name = response.get('vendorDetails').get('companyName')
    return jsonify({'companyName': company_name, 'success': True})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
