def eje1():
    auto = int(input("ingrese una cantidad:"))
    valores = [0]*auto
    salario = 0

    for n in range(0, auto):
        valores[n] = int(input("Ingrese el valor:"))
        salario += valores[n]*0.05 + 200

    print("el valor de cada auto es:", salario+5500)

    eje1()
