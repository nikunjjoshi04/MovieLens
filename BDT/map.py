import sys
import string

file = open("E:\\Document\\SEM-IV\\matirieals\\BDT\\word_count\\nik.txt","r")
file2 = open("E:\\Document\\SEM-IV\\matirieals\\BDT\\word_count\\map.txt","w")
lst = []
for line in file:
    word = line.split(" ")
    for i in word:
        lst.append(i.split("\n"))
for j in lst:
    file2.write("%s\t%s\n"%(j[0],1))
    print("%s\t%s\n"%(j[0],1))
print(lst[1][0])
file2.close()
