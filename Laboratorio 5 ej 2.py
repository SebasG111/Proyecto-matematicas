# Laboratorio 5-------


def a():
    pass



if __name__=='__main__':
    frase = input("Digite una frase: ")
    vocales = ["a","e","i","o","u"]
    #-contar mayusculas-#
    mayusculas = 0
    vocales1 = 0
    for i in range(len(frase)):
        frase2 = frase[i].upper()
        print(frase[i])
        print(frase2)
        if frase[i].isupper():
            mayusculas += 1
    
    for vocal in frase:
        if vocal.lower() in vocales:
            vocales1 += 1
        
    
    frase1 = []
    verificar = ""
    palabras = 0
    contador = 0
    for i in frase:
        if i == " ":
            if contador <= 3:
              palabras += 1
            contador = 0
        else:
            contador += 1
            
            
    print(f""" 
Numero de vocales: {vocales1}
Numero de mayusculas: {mayusculas}
Palabras con menos de 3 letras: {palabras}

Frase nueva: {frase}

""")




        
    