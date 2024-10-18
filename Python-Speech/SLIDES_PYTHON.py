# SLIDE: VARIABLES ##################################################

# Function demonstrating the use of local variables
def show_local_variable():
    s = "DevOps course."  # Local variable
    print("Local variable inside function:", s)

# Global variable
s = "Python Data"
print("\n-- SLIDE: VARIABLES --")
show_local_variable()
print("Global variable outside function:", s)


# SLIDE: DATA TYPES #################################################

print("\n-- SLIDE: DATA TYPES --")

# Tuple Example
tuple1 = (("cicd", "Jenkins"), ("security", "fortify"))
print("\nTuple:", tuple1)

# List Example
list_data = [9, 2.9, [-3, 5], ["jenkins", "Jira"]]
print("\nList:", list_data)

# Different ways to store alphabets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_letters = str(letters)
list_letters = list(letters)
tuple_letters = tuple(letters)
set_letters = set(letters)

print("\nString:", string_letters)
print("\nList:", list_letters)
print("\nTuple:", tuple_letters)
print("\nSet:", set_letters)

# Dictionary Example
dict1 = {"name": "Devops", "batch": 1.0, "canVote": True, "name": "test"}
print("\nDictionary:", dict1)
print("\nAccess Dictionary Value by key 'name':", dict1["name"])


# SLIDE: NUMBERS/OPERATORS #################################################

print("\n-- SLIDE: NUMBERS/OPERATORS --")

x = 13
if x >= 13:
    print("\nCondition met: x >= 13")
else:
    print("\nCondition not met")

# Boolean operations
print("\nBoolean values:")
print("Zero:", bool(0))
print("Integer:", bool(23))
print("Float:", bool(3.142))
print("Complex:", bool(5 + 2j))


# OPERATIONS ON STRINGS ##################################################

print("\n-- SLIDE: OPERATIONS ON STRINGS --")

Tool = "SONAR"
print(f"\nLength of Tool '{Tool}':", len(Tool))
print(f"Code analysis tool is {Tool}. It’s part of DevOps.")

IAAS = "TERRAFORM"
print("\nFirst 5 characters of IAAS:", IAAS[:5])
print("Characters from 5th position onwards:", IAAS[5:])
print("Slicing in between (2-6):", IAAS[2:6])

# Loop through string
print("\nCharacters in 'AMAZON WEB SERVICES':")
Name = "AMAZON WEB SERVICES"
for char in Name:
    print(char, end=" ")
print()


# SLIDE: LIST OPERATIONS #################################################

print("\n-- SLIDE: LIST OPERATIONS --")

ToolsData = ["Maven", "Ansible", "Jenkins", "Sonar"]
if "Maven" in ToolsData:
    print("\nMaven is present in ToolsData.")
else:
    print("\nMaven is absent in ToolsData.")

ToolsData.append("Fortify")
print("\nAfter appending Fortify:", ToolsData)

del ToolsData[3]  # Deleting the 4th item
print("\nAfter deleting 4th item:", ToolsData)

# Sorting list
ToolsData.sort()
print("\nSorted ToolsData:", ToolsData)


# SLIDE: CONDITIONAL STATEMENTS #################################################

print("\n-- SLIDE: CONDITIONAL STATEMENTS --")

applePrice = 180
budget = 200
if applePrice <= budget:
    print("\nAlexa, add 1kg Apples to the cart.")

VERSION = 18
if VERSION < 0:
    print("\nVersion is negative.")
elif 0 < VERSION <= 10:
    print("\nVersion is between 1-10")
elif 10 < VERSION <= 20:
    print("\nVersion is between 11-20")
else:
    print("\nVersion is greater than 20")


# SLIDE: LOOPS ###########################################################

print("\n-- SLIDE: LOOPS --")

# For loop to iterate over string
name = 'SINGAM'
print("\nIterating over string 'SINGAM':")
for letter in name:
    print(letter, end=" ")
print()

# Iterating over a tuple
tools = ("Maven", "Jenkins", "Sonar", "Jira")
print("\nIterating over a tuple:")
for tool in tools:
    print(tool)

# While loop
count = 5
print("\nWhile loop counting down:")
while count > 0:
    print(count, end=" ")
    count -= 1
print()

# Nested loops
i = 1
print("\nMultiplication table using nested loops:")
while i <= 3:
    for k in range(1, 4):
        print(f"{i} * {k} = {i * k}")
    i += 1
    print()


# SLIDE: FUNCTIONS #########################################################

print("\n-- SLIDE: FUNCTIONS --")

def toolname(security, analysis):
    print(f"\nTools: {security}, {analysis}")

toolname("Fortify", "Sonar")

# Function with default arguments
def greeting(fname, mtame="Jenkins", boardname="Jira"):
    print(f"\nHello, {fname}, {mtame}, {boardname}")

greeting("Sonar")

# Function with keyword arguments
def name_tools(firsttool, secondtool, thirdtool):
    print(f"\nHello, {firsttool}, {secondtool}, {thirdtool}")

name_tools(thirdtool="Ansible", firsttool="Terraform", secondtool="JMeter")

# Function with variable-length arguments
def name_varargs(*tools):
    print(f"\nHello, {tools[0]}, {tools[1]}, {tools[2]}")

name_varargs("Ansible", "Terraform", "JMeter")


# SLIDE: RECURSION ##########################################################

print("\n-- SLIDE: RECURSION --")

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Example use of factorial function
num = 7
print(f"\nFactorial of {num}: {factorial(num)}")


# SLIDE: OOPS ###############################################################

print("\n-- SLIDE: OOPS --")

# Class Example
class Tools:
    def __init__(self, name="Jenkins", version=20):
        self.name = name
        self.version = version

    def tools_description(self):
        print(f"{self.name}, Version: {self.version}")

tool = Tools()
tool.tools_description()


# Class with Inheritance
class A:
    def __init__(self, something):
        print("\nA init called")
        self.something = something

class B(A):
    def __init__(self, something):
        print("\nB init called")
        A.__init__(self, something)

obj = B("Something")


# SLIDE: JSON OPERATIONS ##################################################

print("\n-- SLIDE: JSON OPERATIONS --")

import json

# JSON string to Python list
json_string = '["Maven", "Jira", "Kubernetes", "Docker"]'
tools_list = json.loads(json_string)
print("\nPython List:", tools_list)

# Python list to JSON string
python_list = ['Maven', 'Jira', 'Kubernetes', 'Docker']
json_object = json.dumps(python_list)
print("\nJSON String:", json_object)


# SLIDE: EXCEPTION HANDLING ################################################

print("\n-- SLIDE: EXCEPTION HANDLING --")

try:
    num = int(input("\nEnter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")
