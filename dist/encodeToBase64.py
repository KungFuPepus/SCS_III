import base64

# Read the executable file
with open("FriendlyMalware.exe", "rb") as f:
    encoded_data = base64.b64encode(f.read()).decode("utf-8")

# Write the Base64 string to a text file
with open("encoded_payload.txt", "w") as f:
    f.write(encoded_data)