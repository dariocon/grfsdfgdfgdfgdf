'''
Created on Sep 27, 2022

@author: estudiante
'''
temperatura = int(input("¿Cuál es la temperatura: "))

if temperatura <0:
    print ("Encendemos la chimenea")

elif temperatura >=0 and temperatura <17:
    print("ENcendemos el calefacción")
    
elif temperatura >=17 and temperatura <=27:
    print("Encendemos el ventilador")
    
else: 
    print("La temperatura es demasiado alta. Encendemos el aire acondicionado")

    
