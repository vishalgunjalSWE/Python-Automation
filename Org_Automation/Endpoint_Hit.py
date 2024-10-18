import json
import requests
from socket import timeout
import logging

def hit_endpoint(url):
    list2 = []
    if url != "null":
        try:
            data = requests.get(url, timeout=10)
            # Check if the status code is 200 (OK)
            if data.status_code == 200:
                try:
                    dump = data.json()
                    print(f"Total Count: {dump.get('count')}")
                    for link in dump.get("entries", []):
                        print(link['Link'])
                        try:
                            data2 = requests.get(link['Link'], timeout=10)
                            if data2.status_code == 200:
                                list2.append(link['Link'])
                                print(list2)
                            else:
                                print(f"Link {link['Link']} returned status code {data2.status_code}")
                        except requests.exceptions.Timeout:
                            logging.error(f"Timeout error when accessing {link['Link']}")
                except requests.exceptions.JSONDecodeError:
                    print("Error: The response is not in valid JSON format.")
                    print("Response Text:", data.text)  # Print the raw response
            elif data.status_code == 404:
                print("Error: The resource was not found (404).")
            else:
                print(f"Error: Received status code {data.status_code}")
                print(f"Response Text: {data.text}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
    else:
        print("Error loading the URL")

hit_endpoint("https://api.publicapis.org/entries")
