def eje9():
    g = int(input("ingrese su fecha"))
    
    print("su fecha es", g//1000000,"/",g//10000-(g//1000000*100),"/", g%10000)

eje9()