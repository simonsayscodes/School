a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_.ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
bob = str(input("Skriv:"))
bob = bob.upper()
bob = bob.split(" ")
i = int(bob[0])
coc = str(bob[1])
dod = []
ord = ""
for x in range(len(coc)):
    dod.append(coc[x])
for x in range(0, len(coc)):
    pos = a.find(dod[x])
    ord = ord + (a[pos + i])
   
txt = ord[::-1]
print(txt)