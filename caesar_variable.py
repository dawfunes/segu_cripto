
alfabeto = [chr(i) for i in range(97, 123)]

palabra = input("Ingrese la palabra a descifrar: ")

for i in range(26):
    for j in range(26):
        resultado = []
        for idx, char in enumerate(palabra):
            if char in alfabeto:
                if idx % 2 == 0:
                    resultado += alfabeto[(alfabeto.index(char) + i) % 26]
                else:
                    resultado += alfabeto[(alfabeto.index(char) + j) % 26]
            else:
                resultado += char
        print(f"i={i}, j={j}: {''.join(resultado)}")