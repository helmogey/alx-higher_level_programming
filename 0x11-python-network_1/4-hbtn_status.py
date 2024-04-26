#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""

import requests
def main():
    """Fetches the status of https://alx-intranet.hbtn.io/status
    and displays the response body."""

    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

if __name__ == "__main__":
    main()
