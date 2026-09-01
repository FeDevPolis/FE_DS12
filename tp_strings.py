espacio = "=" * 100
'''
Ejercicio I.1. Ficha de inscripción
La secretaría de la institución necesita registrar a cada persona que se inscribe y conocer el largo
exacto del nombre completo, porque el sistema de credenciales admite un máximo de 30
caracteres.
CONSIGNA
a) Solicitar el nombre y el apellido por separado.
b) Armar el nombre completo en una sola variable, con un espacio en el medio.
c) Mostrar el nombre completo y la cantidad de caracteres que ocupa.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «Ana» «Gomez»
Nombre completo: Ana Gomez
Cantidad de caracteres: 9
'''
name = input("Ingrese su nombre: ")
surname = input("Ingrese su apellido: ")
full_name = name + " " + surname
print(f"Nombre completo: {full_name}")
print(f"Cantidad de caracteres: {len(full_name)}")

print(espacio)
'''
Ejercicio I.2. Normalización de nombres
Los datos de los socios de un club fueron cargados por distintas personas y llegan con
mayúsculas y espacios irregulares. Antes de emitir los carnets hay que unificarlos.
CONSIGNA
a) Solicitar un nombre completo tal como está cargado en el sistema.
b) Quitar los espacios sobrantes de los extremos.
c) Mostrar el nombre en tres formatos: todo en mayúscula, todo en minúscula y con la
primera letra de cada palabra en mayúscula.

EJEMPLO DE EJECUCIÓN
Datos ingresados: « mARIA jOSE fERNANDEZ »
Mayúsculas: MARIA JOSE FERNANDEZ
Minúsculas: maria jose fernandez
Formato carnet: Maria Jose Fernandez
'''
full_name = input("Ingrese su nombre completo: ")
full_name = full_name.strip()  
print(f"Mayúsculas: {full_name.upper()}")
print(f"Minúsculas: {full_name.lower()}")
print(f"Formato carnet: {full_name.title()}")

print(espacio)
'''
Ejercicio I.3. Cartel de góndola
Un comercio imprime carteles de oferta. Todos llevan el nombre del producto encerrado entre
dos líneas de igual longitud.
CONSIGNA
a) Solicitar el nombre del producto.
b) Construir una línea formada por treinta signos igual.
c) Mostrar la línea, el nombre del producto en mayúsculas y la línea nuevamente.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «yerba mate»
==============================
YERBA MATE
==============================
'''
product_name = input("Ingrese el nombre del producto: ")
line = "=" * 30
print(line)
print(product_name.upper())
print(line)

print(espacio)
'''
Ejercicio I.4. Lectura de un documento de identidad
Un sistema de control de acceso muestra sólo algunos dígitos del documento por razones de
privacidad.
CONSIGNA
a) Solicitar un número de documento de ocho dígitos.
b) Mostrar el primer dígito, el último dígito y los tres dígitos centrales (posiciones 2, 3 y 4).
c) Antes de escribir el programa, completar el diagrama de posiciones.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «40123456»
Primer dígito: 4
Último dígito: 6
Dígitos centrales: 123
DIAGRAMA

Escribir en la fila superior cada dígito del documento 40123456 y en la fila inferior su índice. Marcar
con un corchete el tramo que devuelve documento[2:5].
=========================
Carácter 4 0 1 2 3 4 5 6
Índice   0 1 2 3 4 5 6 7
=========================
'''
document = input("Ingrese su número de documento de ocho dígitos: ")
print(f"Primer dígito: {document[0]}")
print(f"Último dígito: {document[7]}")
print(f"Dígitos centrales: {document[2:5]}")

print(espacio)
'''
Ejercicio I.5. Fecha en formato compacto
Un sistema de expedientes guarda las fechas como una sola cadena de ocho dígitos, con el
formato AAAAMMDD. La mesa de entradas necesita verlas en el formato habitual.
CONSIGNA
a) Solicitar la fecha en formato compacto.
b) Separar el año, el mes y el día usando cortes.
c) Mostrar la fecha en el formato DD/MM/AAAA.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «20260415»
Fecha: 15/04/2026
'''
date = input("Ingrese la fecha en formato compacto (AAAAMMDD): ")
year = date[0:4]
month = date[4:6]
day = date[6:8]
print(f"Fecha: {day}/{month}/{year}")

print(espacio)
'''
Ejercicio I.6. Correo institucional
El área de sistemas genera las direcciones de correo del personal siguiendo siempre la misma
regla: nombre punto apellido, todo en minúscula, seguido del dominio de la institución.
CONSIGNA
a) Solicitar el nombre y el apellido.
b) Construir la dirección de correo respetando la regla.
c) Mostrar la dirección obtenida.

EJEMPLO DE EJECUCIÓN
Datos ingresados: «Lucía» «Ramírez»
Correo asignado: lucía.ramírez@instituto.edu.ar
'''
name = input("Ingrese su nombre: ").strip()
surname = input("Ingrese su apellido: ").strip()
clean_name = name.lower().replace(" ", "")
clean_surname = surname.lower().replace(" ", "")
email = f"{clean_name}.{clean_surname}@instituto.edu.ar"
print(f"Correo asignado: {email}")

print(espacio)
'''
Ejercicio I.7. Depuración de un teléfono
Los teléfonos de una base de contactos fueron cargados con espacios, guiones y paréntesis. El
sistema de envío de mensajes sólo acepta dígitos.
CONSIGNA
a) Solicitar un teléfono tal como figura en la base.
b) Eliminar los espacios, los guiones y los paréntesis.
c) Mostrar el teléfono depurado y la cantidad de dígitos que quedaron.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «(011) 4567-8900»
Teléfono depurado: 01145678900
Cantidad de dígitos: 11
'''
phone = input("Ingrese el número de teléfono: ")
phone = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
print(f"Teléfono depurado: {phone}")
print(f"Cantidad de dígitos: {len(phone)}")

print(espacio)
'''
Ejercicio I.8. Análisis de un reclamo
El área de atención al cliente necesita saber con qué frecuencia aparece una palabra clave en el
texto de un reclamo y en qué posición aparece por primera vez.
CONSIGNA
a) Solicitar el texto del reclamo.
b) Solicitar la palabra que se desea buscar.
c) Mostrar cuántas veces aparece y la posición de la primera aparición.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «el envio no llego y el envio estaba pago» «envio»
Apariciones: 2
Primera aparición en la posición: 3
'''
complaint_text = input("Ingrese el texto del reclamo: ")
keyword = input("Ingrese la palabra clave a buscar: ")
occurrences = complaint_text.count(keyword)
first_occurrence = complaint_text.find(keyword)

print(f"Apariciones: {occurrences}")
print(f"Primera aparición en la posición: {first_occurrence}")

print(espacio)
'''
Ejercicio I.9. Comprobante de venta
Un comercio emite un comprobante simple. Los importes deben mostrarse siempre con dos
decimales y con separador de miles.
CONSIGNA
a) Solicitar el nombre del producto, el precio unitario y la cantidad.
b) Convertir el precio y la cantidad a número.
c) Mostrar una línea de comprobante usando f-strings, con el total calculado, dos decimales y
separador de miles.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «Monitor 24 pulgadas» «185400.5» «3»
Producto: Monitor 24 pulgadas
Precio unitario: $ 185,400.50
Cantidad: 3
TOTAL: $ 556,201.50
'''
product = input("Ingrese el nombre del producto: ")
price = float(input("Ingrese el precio unitario: "))
quantity = int(input("Ingrese la cantidad: "))

total = price * quantity

print(f"Producto: {product}")
print(f"Precio unitario: $ {price:,.2f}")
print(f"Cantidad: {quantity}")
print(f"TOTAL: $ {total:,.2f}")

print(espacio)
'''
Ejercicio I.10. Lista de asistentes
El registro de asistencia de una jornada se exporta como una única cadena con los apellidos
separados por comas. La coordinación necesita presentarla de otra forma.
CONSIGNA
a) Solicitar la cadena exportada.
b) Separarla en una lista usando la coma como separador.
c) Mostrar la cantidad de asistentes y la lista unida con el separador ' | '.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «Gomez,Ramirez,Suarez,Peralta»
Cantidad de asistentes: 4
Listado: Gomez | Ramirez | Suarez | Peralta
'''
attendees = input("Ingrese la cadena de asistentes: ")
attendees_list = attendees.split(",")
print(f"Cantidad de asistentes: {len(attendees_list)}")
print(f"Listado: { ' | '.join(attendees_list) }")

print(espacio)
'''
Ejercicio I.11. Encabezado de informe
Los informes internos llevan un encabezado de ancho fijo de cuarenta caracteres, con el título
centrado y el código de área alineado a la derecha.
CONSIGNA
a) Solicitar el título del informe y el código del área.
b) Mostrar el título centrado en cuarenta caracteres, usando puntos como relleno.
c) Mostrar el código del área alineado a la derecha en cuarenta caracteres.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «Informe mensual» «AREA-014»
............Informe mensual.............
AREA-014
'''
title = input("Ingrese el título del informe: ")
area_code = input("Ingrese el código del área: ")

print(f"{title:.^40}")
print(f"{area_code: >40}")

print(espacio)
'''
Ejercicio I.12. Cartel de señalización
Los carteles de evacuación se imprimen con las letras separadas por un espacio para mejorar la
lectura a distancia.
CONSIGNA
a) Solicitar la palabra del cartel.
b) Convertirla a mayúsculas.
c) Mostrarla con un espacio entre cada letra.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «salida»
S A L I D A
'''
sign = input("Ingrese la palabra del cartel: ")
print(" ".join(sign.upper()))

print(espacio)
'''
Ejercicio I.13. Validación de un expediente
Los expedientes de la institución respetan un formato fijo: comienzan con EXP- y terminan con el
año en cuatro dígitos.
CONSIGNA
a) Solicitar el número de expediente.
b) Mostrar si comienza con EXP-.
c) Mostrar si termina con -2026.
d) Mostrar si contiene la letra A.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «EXP-A1450-2026»
Comienza con EXP-: True
Termina con -2026: True
Contiene la letra A: True
'''

expedient_number = input("Ingrese el número de expediente: ")
print(f"Comienza con EXP-: {expedient_number.startswith('EXP-')}")
print(f"Termina con -2026: {expedient_number.endswith('-2026')}")
print(f"Contiene la letra A: {'A' in expedient_number}")

print(espacio)
'''
Ejercicio I.14. Las cadenas no se modifican
Un operador informa que el sistema 'no guarda los cambios' al corregir un nombre mal cargado.
El objetivo del ejercicio es entender por qué.
CONSIGNA
a) Solicitar un nombre que contenga un error de tipeo.
b) Aplicar replace() para corregirlo, sin asignar el resultado a ninguna variable.
c) Mostrar el nombre original: se comprueba que no cambió.
d) Aplicar replace() nuevamente, ahora asignando el resultado a una segunda variable, y
mostrar ambas.
e) Completar el diagrama de memoria.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «Jhon Smith»
Después del primer replace: Jhon Smith
Original : Jhon Smith
Corregido: John Smith
DIAGRAMA
Dibujar dos recuadros que representen la memoria, uno por cada variable, indicando con una flecha a
qué texto apunta cada una después de ejecutar el programa completo.

'''
name = input("Ingrese un nombre con error de tipeo: ")
name_error = input("Ingrese donde se produce el error: ")
name_corrected = input("Ingrese la corrección del error: ")
name.replace(name_error, name_corrected)
print(f"Después del primer replace: {name}")
name_updated = name.replace(name_error, name_corrected)
print(f"Original: {name}")
print(f"Corregido: {name_updated}")

print(espacio)
'''
Ejercicio I.15. Renglón de reporte
Al cierre de cada jornada, el sistema de pedidos imprime un renglón por operación con todos los
datos alineados.
CONSIGNA
a) Solicitar el código del pedido, el nombre del cliente y el importe.
b) Mostrar un renglón con el código en mayúsculas, el nombre del cliente con formato de
título ocupando veinte caracteres, y el importe con dos decimales alineado a la derecha en
doce caracteres.
EJEMPLO DE EJECUCIÓN
Datos ingresados: «p-2026-001» «maria elena paz» «48750.4»
P-2026-001Maria Elena Paz 48,750.40
'''
pedido = input("Ingrese el código del pedido: ")
cliente = input("Ingrese el nombre del cliente: ")
importe = float(input("Ingrese el importe: "))

print(f"{pedido.upper():<20} {cliente.title():<20} {importe:>12.2f}")

print(espacio)
