#mapping c->e, g->i, k->m

#chr() and ord() to be used

string = input()

str_list = string.split(" ")
correct_str_list = []
for i in str_list:
    word = ""
    for j in i:
        j = ord(j)
        if j>=97 and j<=122:
            
            j = j+2
            if j > 122:
                j = j -26
        word = word + chr(j)
    correct_str_list.append(word)

print(" ".join(correct_str_list))