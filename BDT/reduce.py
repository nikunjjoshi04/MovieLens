disc = dict()

map = open("E:\\Document\\SEM-IV\\matirieals\\BDT\\word_count\\map.txt","r")
red = open("E:\\Document\\SEM-IV\\matirieals\\BDT\\word_count\\red.txt","w")

prevkey = None
count = 0
dict = dict()
lst = []
set = set()
for i in map:
    key,val = i.split("\t")
    val = val.split("\n")
    lst.append(key)
    set.add(key)
for i in set:
    dict[i] = lst.count(i)
    red.write("%s\t%s\n"%(i,lst.count(i)))
    print(lst.count(i))

print(lst)
print(set)
print(dict)
