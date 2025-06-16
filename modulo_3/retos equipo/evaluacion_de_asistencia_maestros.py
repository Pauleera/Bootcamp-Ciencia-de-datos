import math
def evaluar_asistencia(asistencias):

    print("Asistencias:", asistencias)

    porcentaje_asistencia = (sum(asistencias) / len(asistencias)) * 100
    redondear_asistencia = math.ceil(porcentaje_asistencia)
    print(f"Porcentaje de asistencia: {redondear_asistencia:.2f}%")

    if porcentaje_asistencia >= 90:
        print("Cumple: ✅ Sí.")
    else:
        print("Cumple: ❌ No.")

asistencias = [1 , 1, 0 , 1, 1]
evaluar_asistencia(asistencias)
