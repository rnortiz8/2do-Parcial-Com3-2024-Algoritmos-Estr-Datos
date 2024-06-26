import random

class Alumno:
    def _init_(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def _str_(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Promedio: {self.promedio}"

class Nodo:
    def _init_(self, alumno=None):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class ListaIterador:
    def _init_(self, cabeza):
        self.actual = cabeza

    def _iter_(self):
        return self

    def _next_(self):
        if self.actual is None:
            raise StopIteration
        else:
            nodo = self.actual
            self.actual = self.actual.siguiente
            return nodo.alumno

class ListaDoblementeEnlazada:
    def _init_(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self, alumno):
        actual = self.cabeza
        encontrado = False
        while actual is not None and not encontrado:
            if actual.alumno == alumno:
                encontrado = True
            else:
                actual = actual.siguiente

        if actual is None:
            raise ValueError("El alumno no está en la lista")
        elif actual == self.cabeza:
            self.cabeza = actual.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
        elif actual == self.cola:
            self.cola = actual.anterior
            self.cola.siguiente = None
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

    def _iter_(self):
        return ListaIterador(self.cabeza)

    def lista_ejemplo(self, n):
        nombres = ["Juan", "María", "Pedro", "Ana", "Luisa"]
        lista = ListaDoblementeEnlazada()
        for _ in range(n):
            nombre = random.choice(nombres)
            edad = random.randint(18, 25)
            promedio = round(random.uniform(6, 10), 2)
            alumno = Alumno(nombre, edad, promedio)
            lista.insertar_al_final(alumno)
        return lista




    
    
