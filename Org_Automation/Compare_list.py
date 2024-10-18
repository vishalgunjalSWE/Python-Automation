list = ["V1_abcd", "V2_cejn", "V300_dnmewx", "V300_cenjc", "V301_ceiknce"]

list2 = []
list3 = []

def file_read():
    if len(list) > 0:  # Check if the list is not empty
        for i in list:
            k = i.split("_")  # Split the string at the underscore
            list2.append(k[0])  # Append the first part (e.g., V1, V2)
    else:
        print("list is empty")

# Call the file_read function to populate list2
file_read()

# Check for duplicates in list2
for i in range(len(list2)):
    for j in range(i + 1, len(list2)):
        if list2[i] == list2[j]:
            print(f"SAME: {list2[i]} at index {i} and {j}")