def promedio_notas(diccionario):
    accum = 0
    for nota in diccionario.values():
        accum += nota
    promedio = accum / len(diccionario)
    print(f"El promedio de notas de los alumnos es: {promedio:.2f}")


def alumno_con_mejor_nota(diccionario):
    highestGrade = 0
    for nombre, nota in diccionario.items():
        if nota > highestGrade:
            highestGrade = nota
            alumno = nombre
    print(f"El alumno {alumno} tiene nota {highestGrade} y es la mayor nota.")
    
            
        
        
    

stop = False
diccionario = {}
while True:
    if stop == "0":
        break
    nombre = str(input("Ingrese el nombre del alumno: "))    
    nota = float(input(f"Ingrese la nota de {nombre}"))
    
    stop = str(input("Para dejar de ingresar datos ingrese cero, de lo contrario ingrese cualquier tecla: "))
    diccionario[nombre]=nota

promedio_notas(diccionario)
alumno_con_mejor_nota(diccionario)