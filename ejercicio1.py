from datetime import date, timedelta

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None or mes is None or año is None:
            hoy = date.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.año = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = anio
        self.fecha = date(self.año, self.mes, self.dia)

    def calcular_dif_fecha(self, otra_fecha):
        if not isinstance(otra_fecha, Fecha):
            raise TypeError("El argumento debe ser una instancia de la clase Fecha")
        return abs((self.fecha - otra_fecha.fecha).days)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"

    def __add__(self, days):
        if not isinstance(days, int):
            raise TypeError("El argumento debe ser un número entero")
        nueva_fecha = self.fecha + timedelta(days=days)
        return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)

    def __eq__(self, otra_fecha):
        if not isinstance(otra_fecha, Fecha):
            raise TypeError("El argumento debe ser una instancia de la clase Fecha")
        return self.fecha == otra_fecha.fecha





#Ejercicio 2
from datetime import date, datetime

class Alumno:
    def _init_(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

    def cambiar_datos(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.datos:
                self.datos[key] = value
    def antiguedad(self):
        fecha_ingreso = self.datos["FechaIngreso"]
        if isinstance(fecha_ingreso, str):
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d").date()
        hoy = date.today()
        return (hoy - fecha_ingreso).days // 365

    def _str_(self):
        return f"Alumno({self.datos})"

    def _eq_(self, otro):
        if isinstance(otro, Alumno):
            return self.datos["DNI"] == otro.datos["DNI"]
        return False






#ejercicio 3
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





#Ejercicio 4
class Alumno:
    def _init_(self, nombre, fecha_ingreso):
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso  # Suponiendo que fecha_ingreso es una cadena en formato 'YYYY-MM-DD'

class Nodo:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None

class ListaDoblementeEnlazada:
    def _init_(self):
        self.head = None
        self.tail = None

    def append(self, data):
        nuevo_nodo = Nodo(data)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            nuevo_nodo.prev = self.tail
            self.tail = nuevo_nodo

    def display(self):
        current = self.head
        while current:
            print(f"Nombre: {current.data.nombre}, Fecha de Ingreso: {current.data.fecha_ingreso}")
            current = current.next

    def sort_by_fecha_ingreso(self):
        if self.head is None:
            return

        current = self.head.next
        while current:
            key = current
            mover = current.prev

            while mover and mover.data.fecha_ingreso > key.data.fecha_ingreso:
                mover = mover.prev

            next_node = current.next
            if key.prev:
                key.prev.next = key.next
            if key.next:
                key.next.prev = key.prev

            if mover is None:
                key.next = self.head
                self.head.prev = key
                key.prev = None
                self.head = key
            else:
                key.next = mover.next
                if mover.next:
                    mover.next.prev = key
                key.prev = mover
                mover.next = key

            current = next_node






#Ejercicio 5
import os
import random
from datetime import date

class Alumno:
    def _init_(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def _str_(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Promedio: {self.promedio}"

def guardar_lista_alumnos(ruta_archivo, lista_alumnos):
    with open(ruta_archivo, 'w') as f:
        for alumno in lista_alumnos:
            f.write(f"{alumno.nombre},{alumno.edad},{alumno.promedio}\n")

def crear_directorio_y_guardar_lista(lista_alumnos):
    
    nombre_directorio = "lista_alumnos_dir"
    os.makedirs(nombre_directorio, exist_ok=True)
    
    
    ruta_archivo = os.path.join(nombre_directorio, "lista_alumnos.txt")
    guardar_lista_alumnos(ruta_archivo, lista_alumnos)
    
    return nombre_directorio

def mover_directorio_a_nueva_ruta(nombre_directorio, nueva_ruta):
    
    nuevo_directorio = os.path.join(nueva_ruta, nombre_directorio)
    os.rename(nombre_directorio, nuevo_directorio)
    return nuevo_directorio

def borrar_archivo_y_directorio(nombre_directorio):
    
    ruta_archivo = os.path.join(nombre_directorio, "lista_alumnos.txt")
    os.remove(ruta_archivo)
    
    
    os.rmdir(nombre_directorio)


def generar_lista_alumnos(n):
    nombres = ["Juan", "María", "Pedro", "Ana", "Luisa"]
    lista_alumnos = []
    for _ in range(n):
        nombre = random.choice(nombres)
        edad = random.randint(18, 25)
        promedio = round(random.uniform(6, 10), 2)
        alumno = Alumno(nombre, edad, promedio)
        lista_alumnos.append(alumno)
    return lista_alumnos
