#!/usr/bin/env python
# -*- coding: 850 -*-
# Listar, crear directorios y archivos del sistema
# @utor: Leonardo Marcos Santiago

import os
import shutil

# funciones
def crear_archivo():
    archivo = open('datos.txt','w')
    archivo.close()

def escribir_en_archivo():
    archivo = open('datos.txt','a')
    archivo.write('Hola')
    archivo.close()

# Variables
total_directorios = 1
directorio_origen = os.getcwd()

# Obtener la dirección absoluta en donde estamos ubicados
print("En este momento estas en %s" % os.getcwd())

# Listar todos los archivos
print("En el directorio donde estas ubicado hay %d archivos o carpetas" % len(os.listdir(os.getcwd())))
# Creamos un array con todos los archivos
listado = os.listdir(os.getcwd())
for elemento in listado:
	if os.path.isdir(elemento):
		print("--> %s es una carpeta" % elemento)
	elif os.path.isfile(elemento):
		print("--> %s es un archivo" % elemento)
	else:
		print("--> No se que es %s" % elemento)

#Crear directorios
if not os.path.exists("creado_desde_python"):
	os.mkdir("creado_desde_python")
if not os.path.exists("creado_desde_python1/odash9duas/dsaidas"):
	os.makedirs("creado_desde_python1/odash9duas/dsaidas")
if not os.path.exists("Lectura"):
	os.mkdir("Lectura",00444) # de solo lectura

# Cambiar al directorio creado_desde_python
os.chdir("creado_desde_python")
directorio_i = os.getcwd()
print("Estás en " + directorio_i)

#Crear directorios
contador_directorios = 0
for contador_i in range(1,total_directorios + 1):
	contador_directorios +=1
	if not os.path.exists("Hola" + str(contador_i)):
		print("Creando directorio " + os.getcwd())
		os.mkdir("Hola" + str(contador_i))
	os.chdir("Hola" + str(contador_i))
	for contador_j in range(1,total_directorios + 1):
		contador_directorios +=1
		if not os.path.exists("Hola" + str(contador_j)):
			print("Creando directorio " + os.getcwd())
			os.mkdir("Hola" + str(contador_j))
		os.chdir("Hola" + str(contador_j))
		for contador_k in range(1,total_directorios + 1):
			contador_directorios +=1
			if not os.path.exists("Hola" + str(contador_k)):
				print("Creando directorio " + os.getcwd())
				os.mkdir("Hola" + str(contador_k))
			os.chdir("Hola" + str(contador_k))
			for contador_l in range(1,total_directorios + 1):
				contador_directorios +=1
				if not os.path.exists("Hola" + str(contador_l)):
					print("Creando directorio " + os.getcwd())
					os.mkdir("Hola" + str(contador_l))
				os.chdir("Hola" + str(contador_l))
				for contador_m in range(1,total_directorios + 1):
					contador_directorios +=1
					if not os.path.exists("Hola" + str(contador_m)):
						print("Creando directorio " + os.getcwd())
						os.mkdir("Hola" + str(contador_m))
					os.chdir("Hola" + str(contador_m))
					crear_archivo()
					escribir_en_archivo()
					os.chdir("..") # Fin for contador_m
				os.chdir("..") # Fin for contador_l
			os.chdir("..") # Fin for contador_k
		os.chdir("..") # Fin for contador_j
	os.chdir("..") # Fin for contador_i
# Reporte
print("Total de directorios creados " + str(contador_directorios))

# Cambiar al directorio origen
os.chdir(directorio_origen)
print("En este momento estas en %s" % os.getcwd())

# Eliminando carpetas creadas
if os.path.exists("creado_desde_python"):
	# Eliminar directorios no vacíos
	shutil.rmtree("creado_desde_python") 
if os.path.exists("creado_desde_python1/odash9duas/dsaidas"):
	# Eliminar directorios recursivamente
	os.removedirs("creado_desde_python1/odash9duas/dsaidas")
if os.path.exists("Lectura"):
	# ELiminar una carpeta
	os.rmdir("Lectura") # de solo lectura
