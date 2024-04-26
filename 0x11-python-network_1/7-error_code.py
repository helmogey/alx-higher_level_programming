#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response."""
import requests
import sys

def main(url):
    """Fetches a URL, checks the status code,
     and displays the response body (or error message)."""

    response = requests.get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))

if __name__ == "__main__":
    main(sys.argv[1])
