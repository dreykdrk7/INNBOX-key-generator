def tiene_4_consecutivos(s):
    """Verifica si la cadena 's' tiene 4 dígitos iguales consecutivos."""
    for i in range(len(s) - 3):
        if s[i] == s[i+1] == s[i+2] == s[i+3]:
            return True
    return False

def generar_diccionario(longitud, ruta_destino):
    """Genera un diccionario de contraseñas según los criterios especificados y devuelve el número de claves generadas."""
    contador_claves = 0  # Inicializa el contador de claves
    with open(ruta_destino, "w") as file:
        for i in range(10**longitud):
            numero = str(i).zfill(longitud)
            if not tiene_4_consecutivos(numero):
                password = "INNBOX" + numero
                file.write(password + "\n")
                contador_claves += 1  # Incrementa el contador por cada clave añadida
    return contador_claves

if __name__ == "__main__":
    longitud = int(input("Número de caracteres después de INNBOX: "))
    ruta_destino = input("Ruta de destino y nombre del archivo del diccionario: ")
    
    total_claves = generar_diccionario(longitud, ruta_destino)
    print(f"Diccionario generado en {ruta_destino}. Total de claves generadas: {total_claves}")
