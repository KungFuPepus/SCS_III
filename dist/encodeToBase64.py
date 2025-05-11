import base64
with open("WindowsUpdate.exe", "rb") as f:
    print(base64.b64encode(f.read()).decode("utf-8"))