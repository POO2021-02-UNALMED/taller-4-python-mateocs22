
from classroom.asignatura import Asignatura

class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista= None):
        if(lista is None and self.listadoAlumnos is None):
            self.listadoAlumnos = [alumno]
        elif(lista is None):
            self.listadoAlumnos.append(alumno)   
        elif(lista is not None and self.listadoAlumnos is None):
            self.listadoAlumnos =  lista + [alumno]
        else:
            self.listadoAlumnos =  self.listadoAlumnos + lista + [alumno]
    
    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo
        return cadena

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

if __name__ == "__main__":
    a= Asignatura("Mates")
    print(a)

