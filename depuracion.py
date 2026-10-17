import logging

# Configuración básica para guardar los logs en un archivo
logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calcular_precio_con_descuento(precio_base, descuento_porc):
    factor_descuento = descuento_porc / 100


    precio_final = precio_base * (1 + factor_descuento)
    logging.info(f"Precio final: {precio_final}")
    return precio_final

precio_producto = 100
descuento = 20
print(f"El precio final es: {calcular_precio_con_descuento(precio_producto, descuento)}")