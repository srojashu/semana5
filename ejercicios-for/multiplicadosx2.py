# Crea una función llamada multiplicar_elementos que reciba una lista de números como parámetro 
# y devuelva una nueva lista con los elementos de la lista original multiplicados por 2.

numeros = [3, 9, 1, 5, 12, 7]
resultado = [elemento * 2 for elemento in numeros]
print(f"Lista original: {numeros}")
print(f"Lista multiplicada por 2: {resultado}")
