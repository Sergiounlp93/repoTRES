rawlist = ['im1 4,14', 'im2 13,15', 'im3 6,34', 'im4 410,134']

newlist=[]

for i in rawlist:
    name, space, strCoor = i.partition(" ")#con esto se obtienen la salida im " "  (4,14)
    x,_,y = strCoor.partition(",")
    newlist.append((int(x),int(y)))
newlist.sort()
print(newlist)