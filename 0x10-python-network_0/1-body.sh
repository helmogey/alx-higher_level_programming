#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL
url="$1"
curl -s -w "%{http_code}" "$url"
