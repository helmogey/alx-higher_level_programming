#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response
(decoded in utf-8)"""

import urllib.request
import urllib.parse
import sys

def main(url, email):
    """Sends a POST request to a URL with an email parameter and displays the response body."""

    data = {"email": email}
    data_encoded = urllib.parse.urlencode(data).encode("utf-8")
    with urllib.request.urlopen(url, data=data_encoded) as response:
        print(response.read().decode("utf-8"))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

