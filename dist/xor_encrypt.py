# encrypt.py
key = 0x42
with open("FriendlyMalware.exe", "rb") as f:
    data = f.read()
encrypted = bytes([b ^ key for b in data])
with open("encrypted.bin", "wb") as f:
    f.write(encrypted)