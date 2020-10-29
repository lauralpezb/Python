# -*- coding: utf-8 -*-

"""
Para este proyecto, realizarás un sistema para una escuela. 
Este sistema permite registrar nuevos alumnos, profesores y cursos.
Un alumno es asignado a un curso y un curso puede tener asociado más de un profesor. 
Los profesores tienen un horario que indica cuando están en cada curso.
El horario asociará un curso y un profesor para un día de la semana 
(Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo), una hora desde y una hora hasta.
El sistema permitirá consultar los alumnos que pertenecen a un curso, el horario de cada profesor y el horario del curso.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

#Crear tablas
class Alumnos(Base):
    __tablename__ = 'alumnos'

    idAlumno = Column(Integer, Sequence('alumnos_id_seq'), primary_key = True)
    nombreCompleto =  Column(String)
    idCurso = Column(Integer, ForeignKey('cursos.idCurso'))

    horarioc = relationship("Cursos", back_populates="curso")

    def __repr__(self):
        return "{} {}".format(self.nombreCompleto, self.idCurso)

class Profesores(Base):
    __tablename__ = 'profesores'
    idProfesor = Column(Integer, Sequence('alumnos_id_seq'), primary_key = True)
    nombreCompleto =  Column(String)

    profesor = relationship("Horarios", order_by = "Horarios.idHorario",  back_populates = "horariop")

    def __repr__(self):
        return "{}".format(self.nombreCompleto)

class Cursos(Base):
    __tablename__ = 'cursos'

    idCurso = Column(Integer, Sequence('alumnos_id_seq'), primary_key = True)
    nombreCurso = Column(String)

    curso = relationship("Alumnos", order_by = "Alumnos.idAlumno",  back_populates = "horarioc")
    curso1 = relationship("Horarios", order_by = "Horarios.idHorario",  back_populates = "cursos")

    def __repr__(self):
        return "{}".format(self.nombreCurso)
    
class Horarios(Base):
    __tablename__ = 'horarios'

    idHorario = Column(Integer, Sequence('alumnos_id_seq'), primary_key = True)
    idCurso = Column(Integer, ForeignKey('cursos.idCurso'))
    idProfesor = Column(Integer, ForeignKey('profesores.idProfesor'))
    idDia = Column(Integer, ForeignKey('semanas.idDia'))
    horaDesde = Column(String)
    horaHasta = Column(String)

    cursos = relationship("Cursos", back_populates="curso1")
    horariop = relationship("Profesores", back_populates="profesor")
    dia = relationship("Semanas", back_populates="semana")

    def __repr__(self):
        return "{} {} {} {} {}".format(self.idCurso, self.idProfesor, self.idDia, self.horaDesde, self.horaHasta)
    

class Semanas(Base):
    __tablename__ = 'semanas'
    idDia = Column(Integer, Sequence('alumnos_id_seq'), primary_key = True)
    dia = Column(String)

    semana = relationship("Horarios", order_by = "Horarios.idHorario",  back_populates = "dia")

    def __repr__(self):
        return "{}".format(self.dia)

engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

#Crear sesion

Session = sessionmaker(bind=engine)

session = Session()

#Ingresar datos
alumno1 = Alumnos(nombreCompleto = 'Harold Ramirez', idCurso = 1)
alumno2 = Alumnos(nombreCompleto = 'Maria Hernandez', idCurso = 1)
alumno3 = Alumnos(nombreCompleto = 'Maria Montoya', idCurso = 2)

alumno1.horarioc = Cursos(nombreCurso='Calculo')

horarios1 = Horarios(idCurso=1, idProfesor=1, idDia=1, horaDesde='8 AM', horaHasta='10 AM')
horarios2 = Horarios(idCurso=1, idProfesor=2, idDia=1, horaDesde='10 AM', horaHasta='12 AM')

horarios1.dia = Semanas(dia ='Lunes')

profesor1 = Profesores(nombreCompleto='Oscar Mejia')
profesor2 = Profesores(nombreCompleto='Mario Cano')

#Guardar dato en la tabla
session.add(alumno1)
session.add(alumno2)
session.add(alumno3)
session.add(profesor1)
session.add(profesor2)
session.add(horarios1)
session.add(horarios2)
session.commit()

#Consultas
print('Query 1: Alumnos que pertenecen al curso 1')
for name in session.query(Alumnos.nombreCompleto).filter_by(idCurso=1):
    print(name)

print('Query 2: Horario del profesor 2')
for hora in session.query(Horarios.horaDesde, Horarios.horaHasta).filter_by(idProfesor=2):
    print(hora)

print('Query 3: Horario del Curso 1')
for hora in session.query(Horarios.horaDesde, Horarios.horaHasta).filter_by(idCurso=1):
    print(hora)

