s = "one two three four five"
l = ["one", "five"]
for word in l:
    s = s.replace(word, "%s")
s = s % (l[1], l[0])
print (s)
