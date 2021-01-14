

string = "".join(line.rstrip() for line in open('ocr.txt'))

occurences = {}
for c in string:
    occurences[c] = occurences.get(c,0)+1

avgoc = len(string)//len(occurences)
print("".join([c for c in occurences.keys() if occurences[c]<avgoc]))
#answer is equality