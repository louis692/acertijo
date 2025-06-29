# 29/06/2025

# Juego del acertijo 

Este programa se trata de adivinar el número, implementa un juego interactivo basado en el acertijo del candado donde el usuario debe adivinar una combinación de 3 dígitos basándose en pistas.

# Las pistas son:

1. Fila 1 (3-2-1): Dos números son correctos y no están bien puestos
2. Fila 2 (5-6-2): Ninguno es correcto
3. Fila 3 (8-3-0): Dos son correctos, pero solo uno está bien puesto
4. Fila 4 (1-8-5): Dos son correctos, pero no están bien puestos

# combinacion correcta (8,  1,  3)

# Instrucciones del juego
1. Tu objetivo es encontrar la combinación correcta de 3 dígitos.
2. Ingresa 3 dígitos ejemplo: 123
3. Después de cada intento, recibirás pistas que indiquen si los números son correctos, pertenecen a la combinación o son incorrectos
4. Usa las pistas para deducir la combinación.
   
# Como funciona el juego
Este juego empieza con un pequeño menu interactivo que contiene las opciones, al inicar y observar las pistas le pedira que introduzca tres digitos individualmente
los cuales de la misma manera  se realizara la respectiva validacion de entrada que consta de verficar si el numero ingresado es un digito entre 0 y 9 tambien se
valida que la entrada no sea letras ni simbolos de lo contrario mostrara un error y pedira que ingrese nuevamente el digito, despues de ingresar cada numero
tambien recibira una retroalimentacion que pueden ser 3 condiciones:
1. El numero es correcto
2. El numero pertenece a la combinacion
3. El numero es incorrecto

Basandose en esta retroalimentacion el juego determina si la combinacion ingresada es correcta o incorrecta y mostrara un mensaje segun sea el caso.

La condicion de victoria es ingresar la combinacion de numeros en el orden correcto 

