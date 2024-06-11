

def calculate():
    residue = pay - articulo
    count = 0
    bu5k = 0
    bu10k = 0
    bu20k = 0
    bu50k = 0
    bu100k = 0
    bu2k = 0
    co1k = 0
    co50 = 0
    co10 = 0
    co20 = 0
    while True:
        if count + 100000 <= residue:
            count += 100000
            bu100k += 1
        elif count + 50000 <= residue:
            count += 50000
            bu50k += 1
        elif count + 20000 <= residue:
            count += 20000
            bu20k += 1
        elif count + 10000 <= residue:
            count += 10000
            bu10k += 1
        elif count + 5000 <= residue:
            count += 5000
            bu5k += 1
        elif count + 2000 <= residue:
            count += 2000
            bu2k += 1
        elif count + 1000 <= residue:
            count += 1000
            co1k += 1
        elif count + 500 <= residue:
            count += 500
            co50 += 1
        elif count + 200 <= residue:
            count += 200
            co20 += 1
        elif count + 100 <= residue:
            count += 100
            co10 += 1

        if count == residue:
            break
    lista1 = [bu100k, bu50k, bu20k, bu10k, bu5k, bu2k, co1k, co50, co20, co10]
    name = ["Billete de 10000", "Billete de 50000", "Billete de 20000", "Billete de 10000",
            "Billete de 5000", "Billete de 2000", "Moneda de 1000", "Moneda de 500",
            "Moneda de 200", "Moneda de 100"]
    print(f"Residue: {residue}")
    for i in range(len(lista1)):
        if lista1[i] > 0:
            print(name[i])
            print(lista1[i])


if __name__ == '__main__':
    articulo = int(input("Digit the value of the article: "))
    while True:
        pay = int(input("Digit the value to pay: "))
        if pay < articulo:
            print("ERROR: The pay is minus than article")
        else:
            break
    calculate()
