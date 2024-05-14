Integrantes (Nombre / Paralelo):
·Diego Alonso Ramirez Rojas / Paralelo 200
·Ignacio Gómez González / Paralelo 201

Uso correcto del programa:
·Para poder ejecutar el programa se necesita de un archivo 'operaciones.txt' localizado en la misma carpeta que la del archivo, este
debe contener las operaciones a realizar, el formato es el siguiente: El archivo puede contener una cantidad indeterminada de filas,
en las que hay 2 números decimales separados por un ”;” en cada línea.

Supuestos utilizados:
·Se aume que para la parte "decimal" o "fraccionaria" del número, al realizar los cálculos, se iteraba una cantidad limitada de veces,
en este programa se itera la cantidad de dígitos después del punto o coma, más una itineración extra. Es por esto que puede haber una 
pequeña diferencia de precisión con lo que podría llegar a ser el resultado "real" o "exacto".
·Después de calcular la suma en punto flotante, se transforma a decimal nuevamente y el resultado de la suma en decimal se redondea al
tercer decimal del número.

Especificación de los algoritmos y desarrollo realizado:
·Conversión de número decimal a número binario: Se utilizan métodos de división sucesiva para convertir la parte entera y de multiplicación sucesiva
para convertir la parte fraccionaria a su representación binaria. La función entero_a_bin divide el número decimal entre 2 para obtener la parte 
entera binaria y la función parte_fraccionaria_a_bin multiplica la parte fraccionaria por 2 para obtener la parte fraccionaria.
·Conversión de número binario a número decimal: Mediante la función bin_a_entero se convierte desde el número binario a decimal.
·Conversión de número decimal a punto flotante: Mediante la función decimal_a_punto_flotante, se calcula el signo, el exponente y la mantissa correspondiente
para poder realizar la representación del número decimal a punto flotante, dentro de esta función se llama a las funciones mencionadas anteriormente.
·Suma de números en punto flotante y en binario: Mediante la función suma_float y la función suma_binaria se realizan las sumas correspondientes entre 2 números,
igualando exponentes, luego se realiza la suma bit a bit, considerando el acarreo de bits "carry".
·Conversión de punto flotante a número decimal: Mediante la función punto_flotante_a_decimal, se convierte un número punto flotante en precisión simple a decimal,
considerando signo, exponente y mantissa.
·Main: Coordina todo el programa entre si, se lee el archivo de entrada, se almacenan en variables los cálculos necesarios para luego generar la salida esperada en el archivo
de salida y en la consola.
