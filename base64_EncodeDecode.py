# This is to test the Encode and Decode functions of base64 module
# Which be used to encode the data to put into .pro6 files

import base64

data = bytes(input("Enter the data to be encoded: "), 'utf-8') 

b64_data = str(base64.b64encode(data))[2:-1]

print(b64_data)
print(base64.b64decode(b64_data))
