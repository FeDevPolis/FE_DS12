#18/8/2026 clase 2 actividad 4
'''
Tenés la variable frase = "Python es genial para aprender".
Escribí código que: 
1) muestre su longitud con len(), 
2) extraiga solo la palabra "genial" usando slicing, 
3) reemplace "genial" por "divertido", y
4)muestre el resultado final.
'''

frase = "Python es genial para aprender"   
print("La longitud de la frase es:", len(frase))
print(frase[:10] + frase[17:])  # Extrae la palabra "genial" usando slicing
fraseModificada = frase.replace("genial", "divertido")
print("La frase modificada es:", fraseModificada)
