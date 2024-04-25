def calcular_capital():
    # Pedir al usuario la cantidad a invertir, el interés anual y el número de años
    cantidad = float(input("Ingrese la cantidad a invertir: "))
    interes_anual = float(input("Ingrese el interés anual (%): "))
    años = int(input("Ingrese el número de años: "))

    # Convertir el interés anual a porcentaje
    interes_anual /= 100

    # Calcular el capital obtenido por cada año
    for año in range(1, años + 1):
        capital = cantidad * (1 + interes_anual) ** año
        print(f"Año {año}: Capital obtenido = {capital:.2f}")

calcular_capital()
