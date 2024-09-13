diccionario = {}
def buscar_palabra(palabraD):
    for palabra in diccionario.keys():
        if palabra==palabraD:
            print(f"La definición de {palabra} es: {diccionario[palabra]}")
            return
    print(f"{palabra} no está en el diccionario")    
        
stop = False
diccionario = {}
while True:
    if stop == "0":
        break
    palabra = str(input("Ingrese una palabra: "))    
    definicion = str(input(f"Ingrese la definición de {palabra}: "))
    
    diccionario[palabra]=definicion
    stop = str(input("Para dejar de ingresar datos ingrese cero, de lo contrario ingrese cualquier tecla: "))

for palabra, definicion in diccionario.items():
    print(f"{palabra}: {definicion}")
    
buscar = str(input("Ingrese la palabra que quiere buscar: "))
buscar_palabra(buscar)