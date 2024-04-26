#!/usr/bin/python3
"""  script that fetches https://alx-intranet.hbtn.io/status. """

import urllib.request

def main():
    """Fetches the status of https://alx-intranet.hbtn.io/status
    and displays the response body."""

    url = "https://alx-intranet.hbtn.io/status"

    # Use a with statement to manage the connection and response
    with urllib.request.urlopen(url) as res:
        data = res.read()

    # Split lines and add a tab before '-' characters
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode('utf-8')))

if __name__ == "__main__":
    main()