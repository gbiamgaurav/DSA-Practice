
# Delete a file

import os 
os.remove("file.txt")

# Check if file exists

if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("file not found")