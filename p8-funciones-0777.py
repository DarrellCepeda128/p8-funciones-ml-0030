# ==============================================================================
# Cepeda Darrell
# NC = 0030
# Alumno: Hombre
# Ejemplos asignados: 1 al 6
# ==============================================================================

# ------------------------------------------------------------------------------
# EJEMPLO 1: Función básica sin parámetros
# ------------------------------------------------------------------------------
print("=== EJEMPLO 1: Función básica sin parámetros ===")
def saludar():
    print("¡Hola! Bienvenido a la práctica de funciones en Python.")

# Llamada a la función
saludar()


# ------------------------------------------------------------------------------
# EJEMPLO 2: Función con parámetros de entrada
# ------------------------------------------------------------------------------
print("\n=== EJEMPLO 2: Función con parámetros ===")
def saludar_usuario(nombre):
    print(f"Hola, {nombre}. ¡Mucho gusto en conocerte!")

# Llamada a la función enviando un argumento
saludar_usuario("Usuario 0030")


# ------------------------------------------------------------------------------
# EJEMPLO 3: Función que retorna un valor (return)
# ------------------------------------------------------------------------------
print("\n=== EJEMPLO 3: Función que retorna un valor ===")
def sumar(a, b):
    return a + b

# Guardamos el valor devuelto en una variable
resultado = sumar(15, 25)
print(f"El resultado de la suma es: {resultado}")


# ------------------------------------------------------------------------------
# EJEMPLO 4: Función con parámetros por defecto
# ------------------------------------------------------------------------------
print("\n=== EJEMPLO 4: Función con parámetros por defecto ===")
def presentar_persona(nombre, rol="Estudiante"):
    print(f"Nombre: {nombre} | Rol: {rol}")

# Si no pasamos el segundo argumento, usa "Estudiante" por defecto
presentar_persona("Carlos")                   
# Si pasamos el argumento, reemplaza el valor por defecto
presentar_persona("Ana", "Desarrolladora Machine Learning")


# ------------------------------------------------------------------------------
# EJEMPLO 5: Función con argumentos arbitrarios (*args)
# ------------------------------------------------------------------------------
print("\n=== EJEMPLO 5: Función con argumentos arbitrarios (*args) ===")
def calcular_promedio(*notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Podemos enviar la cantidad de argumentos numéricos que queramos
promedio = calcular_promedio(85, 90, 78, 92, 88)
print(f"El promedio de las notas enviadas es: {promedio:.2f}")


# ------------------------------------------------------------------------------
# EJEMPLO 6: Función con argumentos clave-valor (**kwargs)
# ------------------------------------------------------------------------------
print("\n=== EJEMPLO 6: Función con argumentos de palabra clave (**kwargs) ===")
def mostrar_informacion_alumno(**datos):
    print("Ficha de Datos:")
    for clave, valor in datos.items():
        print(f"  - {clave.capitalize()}: {valor}")

# Enviamos argumentos con clave = valor
mostrar_informacion_alumno(
    control="0030",
    grupo="Gpo3H_IA_0777",
    materia="Machine Learning",
    estado="Activo"
)

print("Programa ejecutado por Cepeda Darrell")