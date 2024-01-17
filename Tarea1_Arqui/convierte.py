"""
Función leer_archivo
Lee el archivo "operaciones.txt", guardando la información en una lista "info".
Se retorna una lista "info" con los números que contiene cada línea.
"""
def leer_archivo():
    file = open("operaciones.txt", "r")
    info = []
    for linea in file:
        info.append(linea)
    file.close()
    return info


"""
Función entero_a_bin
Recibe un numero decimal, se trabaja la parte entera para poder transformalo a binario,
almacenando el numero binario en una lista "bin".
Se retorna la lista "bin" que contiene el numero binario.
"""
def entero_a_bin(numero):
    numero = int(numero)
    bin = []
    while numero > 0:
        bin.append(numero % 2)
        numero = numero // 2
    bin.reverse()
    return bin

"""
Función bin_a_entero
Recibe un numero en binario, luego lo transforma a decimal entero "entero".
Retorna el numero decimal entero "entero".
"""
def bin_a_entero(num):
    entero = 0
    pos = len(num) - 1
    for bit in num:
        entero = entero + int(bit)*(2**pos)
        pos -= 1
    return entero


"""
Funcion parte_fraccionaria_a_bin
Trabaja con la parte "fraccionaria" o "decimal" del número que es ingresado en el archivo
de texto y luego se convierte esta parte "fraccionaria" o "decimal" a binario en forma de lista:"bin_fraccionaria".
Se retorna la lista "bin_fraccionaria".
"""
def parte_fraccionaria_a_bin(fraccionaria_str):
    tamanio = len(fraccionaria_str)
    fraccionaria = float(fraccionaria_str)
    bin_fraccionaria = []
    i = 0
    while (fraccionaria != 1.0) and (fraccionaria != 0.0) and (i < (tamanio - 1)):
        fraccionaria = fraccionaria * 2
        bin_fraccionaria.append((int(fraccionaria)))
        fraccionaria = fraccionaria - int(fraccionaria)
        i += 1
    return bin_fraccionaria

"""
Funcion suma_binaria
Suma 2 números en binario del mismo tamaño bit a bit en una variable de tipo string "suma_binaria".
Se retorna "suma_binaria" que contiene la suma entre ambos números binarios.
"""
def suma_binaria(num1, num2):
    carry = 0
    suma_binaria = ''

    for i in range(len(num1)-1, -1, -1):
        bit1 = int(num1[i])
        bit2 = int(num2[i])
        suma_bits = bit1 + bit2 + carry
        suma_binaria = str(suma_bits % 2) + suma_binaria
        carry = suma_bits // 2

    return suma_binaria

"""
Funcion decimal_a_punto_flotante
Transforma cualquier numero decimal a punto flotante de precision simple (IEEE754), calculando signo,
exponente, mantissa y luego uniendo todo respectivamente en un string "punto_flotante".
Se retorna el string "punto_flotante" y el string "signo".
"""
def decimal_a_punto_flotante(numero_str):
    numero = float(numero_str)
    #Se verifica si el número es positivo o negativo, irá un 0 o un 1 respectivamente dependiendo del caso.
    if numero >= 0:
        signo = '0'
    else:
        signo = '1'
    #Se separa el número entre su parte entera (parte_entera) y parte fraccionaria (parte_fraccionaria).
    numero = abs(numero)
    parte_entera = int(numero)
    numero_separado = numero_str.split('.')
    parte_fraccionaria = "0" + "." + numero_separado[1]
    #Se hace uso de las funciones entero_a_bin(numero) y parte_fraccionaria_a_bin(fraccionaria_str) para obtener ambas partes en binario.
    entero_bin = entero_a_bin(parte_entera)
    parte_fraccionaria_bin = parte_fraccionaria_a_bin(parte_fraccionaria)
    #Se anida todo el número en un string (numero_completo_str).
    numero_completo_str = numero_como_string(entero_bin) + "." + numero_como_string(parte_fraccionaria_bin)
    contador = 0
    #Se calcula el exponente
    exponente = len(entero_bin) - 1
    lista_nument = numero_completo_str.split('.')
    #Se expresa el numero como notación científica (notacion_cientifica).
    notacion_cientifica = lista_nument[0] + lista_nument[1]
    notacion_cientifica = notacion_cientifica[0] + "." + notacion_cientifica[1 : ]
    i_rellenar_0 = 25 - len(notacion_cientifica)
    exp_segado = exponente + 127
    exponente_bin = numero_como_string(entero_a_bin(exp_segado))
    #Se calcula el número como punto flotante (punto_flotante).
    punto_flotante = signo + exponente_bin + notacion_cientifica[2 : ]
    #Se rellena con ceros hasta llegar al tamaño deseado, en este caso de 23.
    while contador < i_rellenar_0:
        punto_flotante += "0"
        contador += 1
    return punto_flotante, signo


"""
Funcion suma_float
Suma 2 numeros en punto flotante de precision simple.
Se retorna el resultado de la suma.
"""
def suma_float(num1,num2):
    #Los números serán de igual signo debido a las condiciones impuestas en el main().

    #Se extraen los exponetes y mantisas de ambos numeros
    exp1 = num1[1:9]
    exp2 = num2[1:9]
    frac1 = '1' + num1[9:31]
    frac2 = '1' + num2[9:31]
    
    #Se compara los exponentes para saber cual es mayor y por cuanto
    exp1_int = bin_a_entero(exp1) - 127
    exp2_int = bin_a_entero(exp2) - 127
    shift = exp1_int - exp2_int

    #Si el 1er exponete es mayor, se agregan '0's a la izquierda del 2do numero
    #  y la misma cantidad de '0's a la dercha del 1do numero
    # Luego se suman usando suma_binaria
    if shift > 0:
        frac2 = '0'*abs(shift) + frac2
        frac1 = frac1 + '0'*abs(shift)
        sum = suma_binaria(frac1,frac2)[:23]
        exp_mayor = exp1

    #Se entra a este if cuando el exp del 2do numero es mayor al del 1ero
    # Luego se repinte los pasos del primer if para igualar exponentes        
    elif shift < 0:
        frac1 = '0'*abs(shift) + frac1
        frac2 = frac2 + '0'*abs(shift)
        sum = suma_binaria(frac1,frac2)[:23]
        exp_mayor = exp2

    #Este caso ocurre cuando ambos numeros tienen el mismo exponente
    else:
        sum = suma_binaria(frac1,frac2)[:23]
        exp_mayor = exp1

    #Normaliza el resultado de la suma
    sum_normal = sum[1 : ]

    #Se arma el resultado final parte por parte y se retorna
    resultado = num1[0] + exp_mayor + sum_normal + '0'
    return resultado 

"""
Funcion punto_flotante_a_decimal
Recibe un número en punto flotante de precision simple y lo transforma a decimal.
Se retorna el número en forma decimal "resultado".
"""
def punto_flotante_a_decimal(bin):
    #Se Obtiene el signo, el exponente y la mantisa del número en formato binario
    signo = int(bin[0])
    exp = int(bin[1:9], 2) - 127
    mantisa = 1 + sum(int(bin[i]) * 2**-(i-8) for i in range(9, 32))
    
    #Se calcula el valor decimal del número
    resultado = (-1)**signo * mantisa * 2**exp
    return resultado
    
"""
Funcion numero_como_string
Recibe un numero binario como lista y lo transforma a string "numero_str".
Se retorna el número como string "numero_str".
"""
def numero_como_string(numero_lista):
    numero_str = ""
    for numero in numero_lista:
        numero_str += str(numero)
    return numero_str

"""
Funcion main
Esta función es la que enlaza todo el programa entre sí, acá se realiza toda
la escritura y almacenamiento de las variables que se requieren para poder generar
el output deseado. 
No retorna nada.
"""
def main():
    #Lee el archivo de operaciones y crea el archivo de resultados
    arch_out = open("resultados.txt", "w")
    info = leer_archivo()

    #Contadores que seran utiles mas adelante
    lineas_procesadas = 0
    sumas_hechas = 0

    #Ciclo para leer la informacion del archivo de entrada
    for linea in info:
        #Se obtienen los numeros a sumar
        numeros = linea.split(";")
        num1 = numeros[0]
        num2 = numeros[1]

        #Se transforman a punto flotante de precision simple
        num1_pf, signonum1 = decimal_a_punto_flotante(num1)
        num2_pf, signonum2 = decimal_a_punto_flotante(num2)

        #Se suman si es que ambos numeros tienen el mismo signo
        #Y se va escribiendo en el archivo de salida los resultados pedidos
        if signonum1 != signonum2:
            num1_str = numero_como_string(num1_pf)
            num2_str = numero_como_string(num2_pf)
            arch_out.write(str(num1) + "/" + num1_str + ";" + str(num2) + "/" + num2_str + '\n')
        else:
            suma_pf = suma_float(num1_pf, num2_pf)
            suma_decimal = punto_flotante_a_decimal(suma_pf)
            suma_decimal = round(suma_decimal, 3)
            arch_out.write(str(suma_decimal) + "/" + suma_pf + '\n')
            sumas_hechas += 1
        lineas_procesadas += 1
    #Se cierra el archivo y se obtienen las sumas no procesasdas
    arch_out.close() 
    no_procesado = lineas_procesadas - sumas_hechas

    #Se imprime por consola las lineas procesadas, las sumas hechas y las sumas no hechas
    print(f"Se procesaron {lineas_procesadas} lineas")
    print(f"Fue posible hacer {sumas_hechas} sumas")
    print(f"No se pudo procesar {no_procesado} sumas")


#Llamado a main
main()