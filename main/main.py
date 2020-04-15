__author__ = "Karthik Surya"

from flask import Flask, jsonify, request
from service.mac_service import MacService
from conf import url, header

app = Flask(__name__)


@app.route('/')
def main():
    return 'Python Test Sample'


@app.route("/mac_address/<mac_address>")
def fetch_mac_details(mac_address):
    if not mac_address:
        return jsonify({"success": False, "error": "Please enter mac address"})
    mac_service = MacService(url, header)
    response = mac_service.get_company_name(mac_address)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
