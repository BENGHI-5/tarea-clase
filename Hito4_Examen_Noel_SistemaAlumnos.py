# Inicialización de variables globales (Estadísticas globales)
total_alumnos = 0
aprobados = 0
rep_nota = 0
rep_asistencia = 0
continuar = "si"

print("--- SISTEMA DE EVALUACIÓN DE ALUMNOS ---")

# Bucle principal controlado por el usuario
while continuar.lower() == "si":
    print("\n--- Registro de Alumno ---")
    
    # Entrada de datos individuales
    nombre = input("Ingrese el nombre del alumno: ")
    clases_total = int(input("Ingrese la cantidad total de clases de la materia: "))
    clases_asist = int(input("Ingrese las clases asistidas por el alumno: "))
    nota = float(input("Ingrese la nota final del alumno (0-100): "))
    
    # Cálculos individuales
    porcentaje_asist = (clases_asist / clases_total) * 100
    total_alumnos = total_alumnos + 1
    
    # Estructura lógica de decisión (Evaluación de condiciones)
    if nota >= 51 and porcentaje_asist >= 80:
        condicion = "Aprobado"
        aprobados = aprobados + 1
    else:
        if porcentaje_asist >= 80:
            condicion = "Reprobado por nota"
            rep_nota = rep_nota + 1
        else:
            condicion = "Reprobado por asistencia"
            rep_asistencia = rep_asistencia + 1
            
    # Mostrar resultado individual inmediato
    print(f"\nResultado de {nombre}:")
    print(f"Asistencia: {porcentaje_asist:.2f}%")
    print(f"Condición: {condicion}")
    
    # Control para continuar o cerrar el bucle
    continuar = input("\n¿Desea registrar otro alumno? (si/no): ")

# Bloque final: Estadísticas y Reporte Global (Se ejecuta al salir del bucle)
print("\n========================================")
print("       REPORTE ESTADÍSTICO FINAL       ")
print("========================================")
print(f"Total de alumnos evaluados: {total_alumnos}")

if total_alumnos > 0:
    # Cálculo del porcentaje de aprobación general
    porcentaje_aprobados = (aprobados / total_alumnos) * 100
    
    print(f"Alumnos aprobados: {aprobados}")
    print(f"Reprobados por nota académica: {rep_nota}")
    print(f"Reprobados por faltas/asistencia: {rep_asistencia}")
    print(f"Rendimiento general: {porcentaje_aprobados:.2f}% de aprobación")
else:
    print("No se registraron alumnos en el sistema.")

print("========================================")
