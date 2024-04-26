#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,
and finally displays the body of the response."""
import requests
import sys

def main(url, email):
    """Sends a POST request to a URL with an email
     parameter and displays the response body."""

    data = {"email": email}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        # Display the response body
        print(dict(response.headers).get("X-Request-Id"))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
