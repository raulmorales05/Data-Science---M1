import random as r

class juego(object):
    def random(lista):
        random = []
        for i in lista:
                i = lista[r.randint(0,20)]
                random.append(i)
        return random
    def init(self):
        self.list = list(range(0,21))
    def pop(self):
        return self.list.pop()
    def size(self):
        return len(self.list)
    def lista(self):
        print(self.list)
    def jugar(self):
        lista = self.random(self.list)
        nro = int(input("Escriba un numero:"))
        if (nro > 20):
            nro = 20
        else:
            nro = nro
        print("Lista original:",lista)
        ultimos = []
        while(nro >0):
            # a = lista.pop()
            # ultimos.append(a)
            ultimos.append(lista.pop())
            nro -= 1
        print("Lista actual", lista)
        sumar = sum(ultimos)
        print("La suma es:", str(sumar))
        if(sumar > 50):
            return "Perdiste jaja"
        else:
            print("Ganaste")
        Nota = len(lista) - 10
        return f"Nota:{Nota}"


a = juego()
a.jugar()