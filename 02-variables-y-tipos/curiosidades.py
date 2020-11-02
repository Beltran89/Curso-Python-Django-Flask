#para poder mostrar las comillas en un string

texto=" 'mi curso ' " #una forma seria con las comillas simples (o a la inversa ' " mi curso" ')
texto2= "en lenguaje \" Python \" " # o con la contrabarra

textoUnido= texto + "\n" +  texto2 # salto de linea

print(textoUnido)


textoUnido= texto + "\t" +  texto2 # tabulacion

print(textoUnido)

textoUnido= texto + "\r" +  texto2 # borrar lo anterior

print(textoUnido)