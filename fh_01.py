f = open("abc.txt",'w+')
f.write("He is gentle man")
for lines in f:
    print(lines)

f.close()
