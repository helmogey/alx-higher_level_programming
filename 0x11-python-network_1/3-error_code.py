#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

import urllib.request
import urllib.error
import sys
def main(url):
    """Fetches a URL, handles potential errors, and displays the
    response body (decoded in UTF-8)."""

    try:
        with urllib.request.urlopen(url) as response:
            # Read the response body
            response_body = response.read().decode("utf-8")
            print(response_body)  # Display response body on success
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.code}")

if __name__ == "__main__":
    main(sys.argv[1])
