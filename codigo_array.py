def invertir_array(array):

    return array[::-1]  


def main():
   
    n = int(input("Ingrese la cantidad de arreglos: "))

    elementos = []

    
    for i in range(n):
        valor = input(f"Ingrese el valor del elemento {i + 1}: ")
        elementos.append(valor)

   
    print("\nArray original:", elementos)

    
    invertido = invertir_array(elementos)

    
    print("Array invertido:", invertido)


if __name__ == "__main__":
    main()

