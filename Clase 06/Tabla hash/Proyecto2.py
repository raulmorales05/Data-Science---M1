

class Nodo:
    def __init__(self, datoN):
        self.dato = datoN
        self.siguiente = None

    def verDato(self):
        return self.dato
    
    def traerSiguiente(self):
        return self.siguiente
    
    def entrarDato(self, datoNuuevo):
        self.dato= datoNuuevo
    
    def colocarSiguiente(self, sigNuevo):
        self.siguiente= sigNuevo
        
    




class Lista:
    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None
        
    def agregar(self, dato):
        temp = Nodo(dato)
        temp.colocarSiguiente(self.cabeza)
        self.cabeza = temp

    def cantidad(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador +=1
            actual= actual.traerSiguiente()
        return contador
    
    def verLista(self):
        actual = self.cabeza
        cadena= ""
        while actual != None:
            cadena+="->"+"["+ ste(actual.verDato())+"]"
            actual= actual.traerSiguiente()
        print(cadena)
    
    def buscar(self,dato):
        actual = self.cabeza
        while actual != None:
            if(dato == actual.verDato()):
                return True
            else:
                actual= actual.traerSiguiente()
        return False
    
    def borrar(self,dato):
        actual = self.cabeza
        previo = None
        encontrado= False
        while not encontrado:
            if(actual != None):
                if(actual.verDato()==dato):
                    encontrado = True
                else:
                    previo = actual
                    actual= actual.traerSiguiente()
                
            else:
                break

        if(actual != None):
            if(previo== None):
                self.cabeza= actual.traerSiguiente()
            
            else:
                previo.colocarSiguiente(actual.traerSiguiente())



list = Lista()
list.agregar(1)

print(list.cantidad())
print(list.verLista())
print(list.buscar(1))
