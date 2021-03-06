# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 16:42:34 2018

@author: yocoy
"""
import sqlite3

class BaseDeDatos():

    @staticmethod
    #Pasa de lenguaje Python reciviendo un arreglo de los Clases que debe tener la base de datos, a comandos en Lenguaje SQL para crear
    #LAS TABLAS PARA CADA CLASE
    def transformarArgumentos(argumentos):
        
        cadena = ""
        for a in range(len(argumentos)-1): 
            cadena += str(argumentos[a]) + ' VARCHAR(100) NOT NULL, '
        cadena += str(argumentos[len(argumentos)-1]) + ' NOT NULL'
        return cadena

    #Crea LA BASE DE DATOS Y LAS TABLAS POR CADA CLASE  en SQL
    def __init__(self, nombreBase, argumentos):
        
        self.nombreBase = nombreBase               
        self.argumentos = argumentos

        # Parte del comando en "Lenguaje" SQL que creara la Base de Datos en SQL
        sqlTerm = self.transformarArgumentos(self.argumentos)
        
        conexion = sqlite3.connect(self.nombreBase+".sqlite3")
        consulta = conexion.cursor()

        #comando texto en "Lenguaje SQL"
        sql = """
        CREATE TABLE IF NOT EXISTS %s(
        no INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        %s)""" %(self.nombreBase, sqlTerm)

        #Ejecuta comando SQL
        consulta.execute(sql)
        consulta.close()
        conexion.commit()
        conexion.close()
    
    @classmethod    
    def agregarDatos(cls, base, datos, argumentos):
        conexion = sqlite3.connect(base+'.sqlite3')
        consulta = conexion.cursor()

        #Genera un comando de texto en Leguaje SQL para insertat un dato en cada Tabla-Clase
        #para la misma primaryKey
        col = ""
        for args in range(len(argumentos)-1):
            col += argumentos[args]+ ', '
        col += argumentos[len(argumentos)-1]

        sql = """
        INSERT INTO %s(%s)
        VALUES(%s)
        """%(base, col, '?,'*(len(argumentos)-1) + '?')   
        consulta.execute(sql, datos)

        firebse.put(argumentos, datos)


        consulta.close()
        conexion.commit()
        conexion.close()
    
    def mostrarDatos(base):
        conexion = sqlite3.connect(base+'.sqlite3')
        consulta = conexion.cursor()
        
        sql = "SELECT * FROM %s" %base
        consulta.execute(sql)        
        listas = consulta.fetchall()
        for lista in listas:
            for dato in lista:
                print(dato, end=' ')
            print('')
            
        consulta.close()
        conexion.commit()
        conexion.close()

    #RERESA TODA LA BASE DE DATOS, OSEA TODAS LAS TABLAS
    def obtenerDatosTotales(base):
        conexion = sqlite3.connect(base+'.sqlite3')
        consulta = conexion.cursor()
        
        sql = "SELECT * FROM %s" %base
        consulta.execute(sql)
        listas = consulta.fetchall()
        consulta.close()
        conexion.commit()
        conexion.close()
        return listas


    def comprobarDato(base, argumento, dato):
        conexion = sqlite3.connect(base+'.sqlite3')
        consulta = conexion.cursor()
        #Comando en "Lenguaje SQL" para ver si para obtener de la tabla correspondiente al arguemto todas las
        # primaryKeys de donde ya se encuentre el Dato
        sql = "SELECT * FROM %s WHERE %s = '%s' " %(base, argumento, dato)
        consulta.execute(sql)
        #Se obtiene una lista de todas los elementos de la tabla "Argumento" que tengan un valor ="Dato"----------------------------------------------
        lista = consulta.fetchone()
        for dato in lista:
          print('', end = '')
        consulta.close()
        conexion.commit()
        conexion.close()

    def buscarDato(base, argumento, dato):
        conexion = sqlite3.connect(base+'.sqlite3')
        consulta = conexion.cursor()
        sql = "SELECT * FROM %s WHERE %s = '%s' " %(base, argumento, dato)
        consulta.execute(sql)
        lista = consulta.fetchone()
        for dato in lista:
            print(dato, end=' ')
        print('')
        consulta.close()
        conexion.commit()
        conexion.close()
    
    @staticmethod
    def borrarDatos(base, argumento, dato):
        
        conexion = sqlite3.connect(base+'.sqlite3')
        consulta = conexion.cursor()
        
        sql = "DELETE FROM %s WHERE %s = '%s'" %(base, argumento, dato) 
        
        consulta.execute(sql)
        consulta.close()
        conexion.commit()
        conexion.close()
    
    def editarDatos(base, argumento, datoIdentificacion, argumentoCambiado, nuevoDato):
        
        conexion = sqlite3.connect(base+'.sqlite3')
        consulta = conexion.cursor()
        
        sql = "UPDATE %s set %s = '%s' WHERE %s = '%s'"%(base, argumentoCambiado, nuevoDato, argumento, datoIdentificacion)
        
        consulta.execute(sql)
        consulta.close()
        conexion.commit()
        conexion.close()