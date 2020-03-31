rawlist = ['im1 4,14', 'im2 13,15', 'im3 6,34', 'im4 410,134']

lower=[]
greater=[]

print("Ingrese un numero")
number=int(input())

for i in rawlist:
    name, space, tupla = i.partition(" ")#con esto se obtienen la salida im " "  (4,14)
    x= int(tupla.split(",")[0])#
    if(x > number):
      greater.extend([name,tupla])
    else:
      lower.extend([name,tupla])
print(greater)
print(lower)