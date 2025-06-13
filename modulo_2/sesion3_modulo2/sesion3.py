print( "- Revisar alumno Aprobado o Desaprobado - \n")

nombre_estudiante = input("Ingrese el nombre del estudiante: ")
calificacion = -1
while calificacion>100 or calificacion<0:
    calificacion = float(input("Ingrese calificación del estudiante (0 - 100): "))

if calificacion >= 60: 
    print(f" ⭐️ Estudiante {nombre_estudiante} ha aprobado. ")
else:
    print(f"❌ Estudiante {nombre_estudiante} ha desaprobado. ")


lista_alumnos = []

print("\n-- Registro de estudiantes y calificaciones -- \n")

while True:
    print("\n-- Nuevo registro de estudiante -- \n")
    
    alumno = {}
    alumno["nota1"] = -1
    alumno["nota2"] = -1
    alumno["nota3"] = -1

    alumno["nombre_alumno"] = input("\n 💬 Si desea salir del programa escriba \"salir\" \n Escriba el nombre de un estudiante \n")
    if alumno["nombre_alumno"].lower() == 'salir':
        break
    
    try:
        while alumno["nota1"]>100 or alumno["nota1"]<0:
            alumno["nota1"] = float(input("Ingrese la calificación de Matemáticas (0-100): "))
        while alumno["nota2"]>100 or alumno["nota2"]<0:
            alumno["nota2"] = float(input("Ingrese la calificación de Programacióm (0-100): "))
        while alumno["nota3"]>100 or alumno["nota3"]<0:
            alumno["nota3"] = float(input("Ingrese la calificación de Historia (0-100): "))
    except ValueError:
        print(" ⚠️ Debes ingresar números para las clasificaciones - Este alumno no se ha registrado.")
        continue

    alumno["promedio"] = (alumno["nota1"] + alumno["nota2"] + alumno["nota3"]) / 3

    print("Evaluando promedio: ")


    if alumno["promedio"] >= 90:
        print(" 🥳 Excelente")
        alumno["comentario"] = "Excelente"
    elif alumno["promedio"] <= 89 and alumno["promedio"]>=75:
        print(" 🤩 Bueno")
        alumno["comentario"] = "Bueno"
    elif alumno["promedio"] < 75:
        print(" 🙂 Necesita mejorar")
        alumno["comentario"] = "Necesita mejorar"
    
    alumno["comentario"] = "Excelente - ¡Puntuación Perfecta!" if alumno["promedio"] == 100 else alumno["comentario"]
    
    lista_alumnos.append(alumno)


print("\n-- Revisar todos los alumnos nombre y comentarios -- \n")

for alumno in lista_alumnos:
    print(f"Estudiante: {alumno['nombre_alumno']} - Comentario: {alumno['comentario']}")
