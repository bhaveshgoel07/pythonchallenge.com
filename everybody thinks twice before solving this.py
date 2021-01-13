#mapping c->e, g->i, k->m

#chr() and ord() to be used

string = input()
a = "abcdefghijklmnopqrstuvwxyz"
b = "cdefghijklmnopqrstuvwxyzab"
mytable = string.maketrans(a,b)

print(string.translate(mytable))