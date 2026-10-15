import asyncio
import time

async def pedir_cafe():
    print("Pidiendo un café...")

    await asyncio.sleep(3)

    print("¡Café listo!")

    return "Café"

async def main():

    inicio = time.time()

    await asyncio.gather(
        pedir_cafe(),
        pedir_cafe(),
        pedir_cafe()
    )

    fin = time.time()

    print(f"Tiempo total = {fin - inicio:.2f}")

asyncio.run(main())