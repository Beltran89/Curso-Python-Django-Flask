"""
Ejercicio 2 
    -Mostrar los numero pares del 1 al 120

"""

contador = 1

while contador <= 120:  
    
    if contador%2 == 0:
        print(contador)
        
    contador+=1

"""
    Forma del curso 
        #No declaramos contador
        for contador in range(1,120):
            
            if contador%2 == 0:
                print(contador)
                
            contador+=1
            
"""