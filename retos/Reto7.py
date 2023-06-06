def diccnionario_frase(frase):
    frase_y_longitud = dict()
    frase_split = frase.split()

    for i in frase_split:
        (frase_y_longitud)[i] = len(i)

    return frase_y_longitud

frase_input = input("Ingresa la frase> ")

print(diccnionario_frase(frase_input))

