def hola():
 g = int(input("ingrese su fecha de nacimiento DDMMAA:"))

 dia = g // 1000000
 mes = (g // 10000) % 100
 año = g % 10000


 print("su fecha de nacimiento es:", dia,"/", mes,"/", año)
hola()
