#!/usr/bin/python3
"""  script that fetches https://alx-intranet.hbtn.io/status. """

import urllib.request

def main():
    """Fetches the status of https://alx-intranet.hbtn.io/status and displays the response body."""

    url = "https://alx-intranet.hbtn.io/status"

    # Use a with statement to manage the connection and response
    with urllib.request.urlopen(url) as response:
        # Read the response body
        data = response.read().decode("utf-8")

    # Split lines and add a tab before '-' characters
    formatted_data = ["\t" + line.strip() for line in data.splitlines() if line.startswith("-")]

    # Print the formatted response body
    print("\n".join(formatted_data))

if __name__ == "__main__":
    main()