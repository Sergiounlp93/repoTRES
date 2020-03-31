import random
preguntas = [
  ['Buenos Aires limita con Santiago del Estero', 'no'],
  ['Jujuy limita con Bolivia', 'si'],
  ['San Juan limita con Misiones','no']
]

puntaje,contador=0,0

while(preguntas):
  pregunta = random.choice( preguntas ) #random.choice(iterable) retorna un elemento al azar de la lista
  print(pregunta[0])
  respuesta=input("responda: ")
  if( pregunta[1].lower() == respuesta.lower() ):
    puntaje = puntaje + 1
  else:
    print("incorrecto\n\r")
  preguntas.remove(pregunta)#elimino una pregunta para no volverla a repetir (parametro [elemento de la lista])

print("Respuestas correctas: "+str(puntaje))