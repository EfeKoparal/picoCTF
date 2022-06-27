

for i in range(0,len(flag)):
    print(chr(ord(flag[i])>>8), end="")
    print(chr(int(bin(ord(flag[i]))[9:], 2)),end="")
