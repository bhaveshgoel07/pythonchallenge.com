
string = "\n".join([line.rstrip() for line in open('equality.txt')])
ans = ""
for i in range(4,len(string)-4):
    if string[i].islower() and string[i-1].isupper() and string[i-2].isupper() and string[i-3].isupper() and string[i+1].isupper() and string[i+2].isupper() and string[i+3].isupper() and string[i].islower() and string[i-4].islower() and string[i+4].islower():
        ans = ans + string[i]

print(ans)