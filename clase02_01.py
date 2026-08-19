#18/8/2026 clase 2
'''
Escriban expresiones que permita calcular:
El costo de comprar 5 productos que cuestan $1200 cada uno.
El promedio de las notas 7, 8 y 9.Cuántos segundos hay en 3 horas.
El precio final de un producto de $1500 al que se le agregan $300.
La cantidad de días que representan 240 horas
subir un archivo con la captura de pantalla
'''

costoPorProducto = 1200
cantidadProductos = 5
totalCosto = costoPorProducto * cantidadProductos
print("El costo total de comprar", cantidadProductos, "productos es:", totalCosto)  

notas = [7, 8, 9]
promedioNotas = sum(notas) / len(notas)
print("El promedio de las notas es:", promedioNotas)

horas = 3
segundosEnUnaHora = 3600    
totalSegundos = horas * segundosEnUnaHora
print("El total de segundos en", horas, "horas es:", totalSegundos)

precioBase = 1500
impuesto = 300
precioFinal = precioBase + impuesto
print("El precio final del producto es:", precioFinal)

horasTotales = 240
dias = horasTotales / 24
print("La cantidad de días que representan", horasTotales, "horas es:", dias)

