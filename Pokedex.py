import requests
import json
import os

# URL base oficial de la PokeAPI
URL_BASE = "https://pokeapi.co/api/v2/pokemon/"
NOMBRE_ARCHIVO = "pokedex.json"

# Códigos de color ANSI para personalizar la interfaz en tu terminal
VERDE = "\033[32m"
AZUL_TURQUESA = "\033[36m"
AMARILLO_BRILLANTE = "\033[93m"
ROJO = "\033[31m"
RESET = "\033[0m"


def guardar_en_json(datos_pokemon):
    """
    Sección 2: Carga el archivo json existente, le añade el nuevo Pokémon
    y guarda la información actualizada en el disco duro (Evita sobrescritura vacía).
    """
    pokedex_local = []
    
    # 1. Si el archivo ya existe en tu computadora, cargamos los Pokémon guardados antes
    if os.path.exists(NOMBRE_ARCHIVO):
        try:
            with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
                pokedex_local = json.load(archivo)
        except json.JSONDecodeError:
            # Si el archivo está vacío o corrupto, iniciamos la lista limpia
            pokedex_local = []

    # 2. Estructuramos únicamente los datos limpios solicitados por la rúbrica
    nuevo_registro = {
        "nombre": datos_pokemon.get("name", "Desconocido").capitalize(),
        "peso": datos_pokemon.get("weight", 0) / 10,
        "altura": datos_pokemon.get("height", 0) / 10,
        "enlace_imagen": datos_pokemon["sprites"]["front_default"]
    }
    
    # Evitar duplicados: Si el Pokémon ya estaba guardado, lo eliminamos antes de actualizarlo
    pokedex_local = [p for p in pokedex_local if p["nombre"] != nuevo_registro["nombre"]]
    
    # Añadimos el nuevo Pokémon a la lista existente
    pokedex_local.append(nuevo_registro)
    
    # 3. Guardamos la lista actualizada de forma física en la computadora
    try:
        with open(NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(pokedex_local, archivo, indent=4, ensure_ascii=False)
        print(f"{VERDE}¡Éxito! Datos de {nuevo_registro['nombre']} guardados permanentemente en '{NOMBRE_ARCHIVO}'.{RESET}\n")
    except Exception as e:
        print(f"{ROJO}Error al intentar escribir en el archivo json: {e}{RESET}\n")


def buscar_pokemon(nombre_o_numero):
    """Sección 1: Realiza la petición HTTP a la PokeAPI y valida los status codes."""
    busqueda = str(nombre_o_numero).strip().lower()
    
    print(f"\n{AZUL_TURQUESA}Conectando con la base de datos de PokeAPI...{RESET}")
    
    try:
        url_completa = f"{URL_BASE}{busqueda}"
        respuesta = requests.get(url_completa, timeout=10)
        
        # Validación de status codes de la rúbrica (Atrapa el error si no existe)
        if respuesta.status_code == 404:
            print(f"\n{ROJO}Error 404: El Pokémon '{nombre_o_numero}' no existe en el registro.{RESET}\n")
            return None
        elif respuesta.status_code != 200:
            print(f"\n{ROJO}Error {respuesta.status_code}: Problema con el servidor externo.{RESET}\n")
            return None
            
        datos = respuesta.json()
        
        # Despliegue de datos en pantalla (Requisito de rúbrica)
        nombre = datos.get("name", "Desconocido").capitalize()
        peso = datos.get("weight", 0) / 10
        altura = datos.get("height", 0) / 10
        url_imagen = datos["sprites"]["front_default"]
        
        print(f"\n{AZUL_TURQUESA}---  Pokédex: Datos Encontrados ---{RESET}")
        print(f"{AMARILLO_BRILLANTE}Nombre:{RESET} {nombre}")
        print(f"{AMARILLO_BRILLANTE}Peso:{RESET} {peso} kg")
        print(f"{AMARILLO_BRILLANTE}Altura:{RESET} {altura} m")
        print(f"{AMARILLO_BRILLANTE}Enlace de Imagen:{RESET} {url_imagen}")
        print(f"{AZUL_TURQUESA}---------------------------------------{RESET}\n")
        
        # Ejecutamos de forma automática el guardado físico de datos
        guardar_en_json(datos)
        return datos
        
    except requests.exceptions.RequestException as e:
        print(f"\n{ROJO}Error de red: Verifica tu conexión. Detalle: {e}{RESET}\n")
        return None


# --- PROGRAMA PRINCIPAL INTEGRADO SOBRE TU BASE ---
if __name__ == "__main__":
    while True:
        print(f"{AZUL_TURQUESA}========================================={RESET}")
        print(f"{AZUL_TURQUESA}          POKÉDEX VIRTUAL MULTI-API       {RESET}")
        print(f"{AZUL_TURQUESA}========================================={RESET}")
        print("1. Buscar un Pokémon (Por Nombre o Número)")
        print("S. Salir de la Pokédex")
        print(f"{VERDE}Selecciona una opción del menú:{RESET} ", end="")
        
        opcion = input().strip().upper()
        
        if opcion == "1":
            print(f"{VERDE}Ingresa el nombre o el número del Pokémon:{RESET} ", end="")
            entrada = input().strip()
            
            if entrada:
                # Invoca directamente tu función base que ya funciona bien
                buscar_pokemon(entrada)
            else:
                print(f"\n{ROJO}Error: El campo de búsqueda no puede estar vacío.{RESET}\n")
                
        elif opcion == "S":
            print(f"\n{AMARILLO_BRILLANTE}¡Pokédex cerrada con éxito! Tu archivo quedó guardado.{RESET}\n")
            break
        else:
            print(f"\n{ROJO}Opción inválida. Por favor, selecciona 1 o S.{RESET}\n")
