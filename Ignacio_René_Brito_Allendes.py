juegos = {
'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
}

inventario = {
'G001': [9990, 7],
'G002': [19990, 0],
'G003': [42990, 3],
'G004': [14990, 5],
'G005': [17990, 9],
'G006': [39990, 2],
}
def validar_codigo_nuevo(codigo, stock_plataforma):
    cod = codigo.strip().upper()
    if not cod or cod in stock_plataforma: return False
    return True

def validar_precios(p_min, p_max):
    return p_min < p_max

def leer_opcion():
    try:
        op = int(input("Ingrese opción: "))
        if 1 <= op <= 6: return op
        print("Debe seleccionar una opción válida")
    except ValueError:
        print("ERROR. SOLO DEBE INGRESAR NUMEROS")
    return 0

def buscar_codigo(codigo, stock_plataforma):
    return codigo.strip().upper() in stock_plataforma

def reporte_precios(genero, stock_plataforma, dict_inv):
    gen = genero.strip().upper()
    total = 0
    for cod, datos in stock_plataforma.items():
        if datos[1].upper() == gen:
            total += dict_inv[cod][1]
    print(f"\nTotal stock para el género '{genero}': {total}")
    print("--- JUEGOS (ALFABÉTICO) ---")
    for cod, datos in sorted(stock_plataforma.items(), key=lambda x: x[1][0]):
        print(f"{datos[0]}--{cod}")

def buscar_por_clasificación(p_min, p_max, stock_plataforma, dict_inv):
    if not validar_precios(p_min, p_max):
        return print("Error: El precio mínimo debe ser menor al máximo.")
    print("\n--Juegos por clasificación--")
    encontrado = False
    for cod, datos_inv in dict_inv.items():
        if p_min <= datos_inv[0] <= p_max:
            print(f"[{cod}] {stock_plataforma[cod][0]} | Precio: ${datos_inv[0]} | stock: {datos_inv[1]}")
            encontrado = True
    if not encontrado: print("No hay juegos clasificados con ese precio.")

def agregar_pelicula(stock_plataforma, dict_inv):
    cod = input("Ingrese nuevo código (ej: P105): ").strip().upper()
    if not validar_codigo_nuevo(cod, stock_plataforma):
        return print("Error: Código vacío o ya existente.")
    try:
        titulo = input("Título: ").strip()
        genero = input("Género: ").strip()
        plataforma = int(input("cambio (min): "))
        clasif = input("Clasificación: ").strip()
        multijugador = input("¿Es Multijugador? (S/N): ").strip().upper() == "S"
        editor = input("EDITAR: ").strip()
        precio = int(input("Precio Base: "))
        stock = int(input("stock disponibles: "))
        
        stock_plataforma[cod] = [titulo, genero, clasif, multijugador, editor,plataforma ]
        dict_inv[cod] = [precio, stock]
        print(f"¡Juego {titulo} agregado exitosamente!")
    except ValueError:
        print("ERROR. SOLO DEBE INGRESAR NUMEROS EN CAMPOS NUMÉRICOS.")

def actu_precio(stock_plataforma, dict_inv):
    cod = input("Código de juego a aactualizar: ").strip().upper()
    if buscar_codigo(cod, stock_plataforma):  
        try:
            nuevo_p = int(input(f"Nuevo precio para {stock_plataforma[cod][0]}: "))
            if nuevo_p > 0:
                dict_inv[cod][0] = nuevo_p
                print("Precio modificado exitosamente.")
            else: print("El precio debe ser mayor a 0.")
        except ValueError: print("ERROR. SOLO DEBE INGRESAR NUMEROS")
    else: print("Error: El código del juego no existe.")

def eliminar_juego(stock_plataforma, dict_inv):
    cod = input("Código del juego a eliminar: ").strip().upper()
    if buscar_codigo(cod, stock_plataforma):
        stock_plataforma.pop(cod)
        dict_inv.pop(cod)
        print(f"juego{cod} eliminado de ambos registros.")
    else: print("Error: El código del juego no existe.")

# --- 4. FLUJO PRINCIPAL ---
def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=======================================")
        
        opcion = leer_opcion()
        if opcion == 1:
            reporte_precios(input("Ingrese género: "), juegos, inventario)
        elif opcion == 2:
            try:
                p_min = int(input("Precio mínimo: "))
                p_max = int(input("Precio máximo: "))
                buscar_por_clasificación(p_min, p_max, juegos, inventario)
            except ValueError: print("ERROR. SOLO DEBE INGRESAR NUMEROS")
        elif opcion == 3:
            agregar_pelicula(juegos, inventario)
        elif opcion == 4:
            actu_precio(juegos, inventario)
        elif opcion == 5:
            eliminar_juego(juegos, inventario)
        elif opcion == 6:
            print("Programa finalizado limpiamente.")
            break

if __name__ == "__main__":
    main()
