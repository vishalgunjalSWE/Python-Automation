import json
import requests

person_ISS = []
person_Tiangong = []

def space_data(url):
    # Fetch the data from the URL
    data = requests.get(url)
    
    # Convert response to JSON format
    dump = data.json()
    
    # Iterate through each person in the response
    for person in dump["people"]:
        print(f"{person['name']} is on {person['craft']}")
        
        # Categorize based on the spacecraft
        if person["craft"] == "ISS":
            person_ISS.append(person["name"])
        else:
            person_Tiangong.append(person["name"])
    
    # Print the total number of people aboard each spacecraft
    print("Total number of persons in ISS: " + str(len(person_ISS)))
    print("Total number of persons in Tiangong: " + str(len(person_Tiangong)))

# Call the function with the API URL
space_data("http://api.open-notify.org/astros.json")