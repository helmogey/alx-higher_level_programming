#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys
import json


def main():
    """Sends a POST request with a letter parameter and displays user information."""

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=data)

    if response.status_code == 200:
        try:
            data = json.loads(response.text)

            # Check if the parsed data is a dictionary and not empty
            if isinstance(data, dict) and data:
                # Extract and display user information
                user_id = data.get("id")
                user_name = data.get("name")
                print(f"[{user_id}] {user_name}")
            else:
                # JSON is empty
                print("No result")
        except json.JSONDecodeError:
            # Invalid JSON format
            print("Not a valid JSON")
    else:
        print(f"Error: Request failed with status code {response.status_code}")


if __name__ == "__main__":
    main()

