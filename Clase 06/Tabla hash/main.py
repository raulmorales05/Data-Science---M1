from os import system
from lista_hash import ListaHash

TablaHash = []
for i in range(5):
    TablaHash.append(ListaHash())

#Crear un elemento para ejecutat la funcion Hash
h = ListaHash()

while True:
    system("clear")
    for i in range(5):
        "ListaHash[" + str(i) + "] = " , TablaHash[i].recorrer()
        print("")

    codigo = int(input("\n\n Digite el codigo: "))
    nombre = input("Digite el nombre: ")

    clave = h.funcionHash(codigo)
    TablaHash[clave].insertar(codigo, nombre)
    




    continuar = input("\n Desea continuar? (s/n): ")
    if continuar == "n" or continuar == "N": break

print("\n El programa ha finalizado.")