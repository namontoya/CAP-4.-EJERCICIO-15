#Capitulo 4. Ejercicio resuelto 15

PESOA = float(input('Ingrese el peso de la esfera A: '))
PESOB = float(input('Ingrese el peso de la esfera B: '))
PESOC = float(input('Ingrese el peso de la esfera C: '))
PESOD = float(input('Ingrese el peso de la esfera D: '))

if PESOA == PESOB and PESOA == PESOC:
  if PESOD > PESOA:
    print('LA ESFERA D ES LA DIFERENTE Y ES DE MAYOR PESO')
  else:
    print('LA ESFERA D ES LA DIFERENTE Y ES DE MENOR PESO')
elif PESOA == PESOB and PESOA == PESOD:
  if PESOC > PESOA:
    print('LA ESFERA C ES LA DIFERENTE Y ES DE MAYOR PESO')
  else:
    print('LA ESFERA C ES LA DIFERENTE Y ES DE MENOR PESO')
elif PESOA == PESOC and PESOA == PESOD:
  if PESOB > PESOD:
    print('LA ESFERA B ES LA DIFERENTE Y ES DE MAYOR PESO')
  else:
    print('LA ESFERA B ES LA DIFERENTE Y ES DE MENOR PESO')
else:
  if PESOA > PESOB:
    print('LA ESFERA A ES LA DIFERENTE Y ES DE MAYOR PESO')
  else:
    print('LA ESFERA A ES LA DIFERENTE Y ES DE MENOR PESO')

