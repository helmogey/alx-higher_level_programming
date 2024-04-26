#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
 the value of the variable X-Request-Id in the response header"""

import requests
import sys


def main(url):
    """Fetches a URL, extracts the X-Request-Id
     header value, and displays it."""

    response = requests.get(url)
    if response.status_code == 200:
        # Extract X-Request-Id header value
        request_id = response.headers.get("X-Request-Id")
        print(request_id.headers.get("X-Request-Id"))


if __name__ == "__main__":
    main(sys.argv[1])
