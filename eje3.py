rawlist = ['Auto', '123', 'Viaje', '50', '120']

newlist=[]

for i in rawlist:
  if(i.isdecimal()):
    newlist.append(int(i))
newlist.sort()
print(newlist)