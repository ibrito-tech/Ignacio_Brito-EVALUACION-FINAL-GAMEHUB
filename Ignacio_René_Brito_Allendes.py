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

