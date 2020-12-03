print("Puedo calcular el perimetro y el area de un circulo")
radio = input("Introduce el radio del circulo: ")
perimetro = 2*3.14*int(radio)
area = 3.41*(int(radio)*int(radio))
mensajePerimetro = "El perimetro es {}"
mensajeArea = "El area circulo es {}"
print(mensajePerimetro.format(perimetro))
print(mensajeArea.format(area))
