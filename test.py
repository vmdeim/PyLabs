s = "abcdefghijklmnop"
while s != "":
    print(s)
    s = s[1:-1]

for i in range(1, 10):
     for j in range(1, 10):
         print(" %2i" % (i*j), end = '')
     print()
