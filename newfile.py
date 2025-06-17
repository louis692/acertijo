print()
print(" PISTAS DISPONIBLES:")
print("-" * 60)
print("Fila 1 (3-2-1): Uno es correcto y está bien puesto")
print("Fila 2 (5-6-2): Ninguno es correcto")
print("Fila 3 (8-3-0): Dos son correctos pero no están bien puestos")
print("Fila 4 (1-8-5): Dos son correctos pero no están bien puestos")
print("-" * 60 + "\n")
print()




while True:
    try:
        numero_1 = int(input("Por favor, ingresa el primer número (0-9): "))
        if 0 <= numero_1 <= 9:    
            print("Has ingresado el número válido:", numero_1)
            if numero_1 == 8:
                print("El primer número es correcto.")
            elif numero_1 == 1:
                print("El número pertenece a la combinación.")
            elif numero_1 == 3:    
                print("El número pertenece a la combinación.")
            else:
                 print("Número incorrecto.")
            break  
        else:
            print("Error: El número debe estar entre 0 y 9. Inténtalo de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingresa un número entero.")


while True:
    try:
        numero_2 = int(input("Por favor, ingresa el segundo número (0-9): "))
        if 0 <= numero_2 <= 9:
            print("Has ingresado el número válido:", numero_2)
            if numero_2 == 1:
                print("El segundo número es correcto.")
            elif numero_2 == 8:   
                print("El número pertenece a la combinación.") 
            elif numero_2 == 3:
                print("El número pertenece a la combinación.")
            else:
                 print("Número incorrecto.")
            break  
        else:
            print("Error: El número debe estar entre 0 y 9. Inténtalo de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingresa un número entero.")

while True:
    try:
        numero_3 = int(input("Por favor, ingresa el tercer número (0-9): "))
        if 0 <= numero_3 <= 9:
            print("Has ingresado el número válido:", numero_3)
            if numero_3 == 3:
                print("El tercer número es correcto.")
            elif numero_3 == 8:
                print("El número pertenece a la combinación.")
            elif numero_3 == 1:
                print("El número pertenece a la combinación.")  
            else:
                 print("Número incorrecto.")         
            break  
        else:
            print("Error: El número debe estar entre 0 y 9. Inténtalo de nuevo.")
    except ValueError:
        print("Error: Entrada no válida. Por favor, ingresa un número entero.")

# Condición de victoria
if numero_1 == 8 and numero_2 == 1 and numero_3 == 3:
    print("\n¡FELICIDADES! Has ingresado la combinación correcta (8-1-3). ¡HAS GANADO!")
else:
    print("\nLa combinación ingresada no es la correcta. Sigue intentándolo.")