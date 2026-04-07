"""
STANDARD LIBRARIES IN PYTHON - os, sys, and json Modules (Automation and System Interaction)
Common applications:
    -Automation Scripts
    -Backend Systems
    -Data Processing
"""
# 1. os Module (Operating System Interaction)
"""
USES:
    -Working with files and folders 
    -Automation Scripts
    -Getting system paths 
"""
    # a. Get current working directory
import os
print(os.getcwd())

    # b. List files from folder
import os
print(os.listdir())

"""
    # c. Create a new folder
import os
os.mkdir("newfolder")
"""

    # d. Check if file exists
import os
print(os.path.exists("data.txt"))


# 2. sys Module (System-Level Operations)
"""
USES:
    -Accessing Python runtime info
    -Command-line arguments
    -System configuration
"""
    # a. check Python version
import sys
print(sys.version)

    # b. command line arguments
import sys
print(sys.argv)


# 3. json Module (Data Exchange Format)
"""
USES:
    -APIs Web applications Configuration files
EXAMPLE:
    JSON { "name": "Samwel", "age": "18"}
"""
    # a. Convert Python to JSON
import json
data = {"name": "Samwel", "age": 18}
json_data = json.dumps(data)
print(json_data)

    # b. Convert JSON to Python
import json
json_string = '{"name": "Samwel", "age": 18}'
data = json.loads(json_string)
print(data)

    # c. Save JSON to file
import json
data = {"name": "Samwel", "age": 18}
with open("data.json", "w") as file:
    json.dump(data, file)

    # d. Read JSON from file
import json
with open("data.json", "r") as file:
    data = json.load(file)
print(data)

#Real Example
import json
with open("config.json") as f:
    config = json.load(f)
print(config["database"])
