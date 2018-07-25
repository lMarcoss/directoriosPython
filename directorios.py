#!/usr/bin/env python
# -*- coding: 850 -*-
# Listar, crear directorios y archivos del sistema
# @utor: Leonardo Marcos Santiago

import os
import shutil

# Obtener la dirección absoluta en donde estamos ubicados
print("En este momento estas en %s" % os.getcwd())

# Listar todos los archivos
print("En el directorio donde estas ubicado hay %d archivos o carpetas" % len(os.listdir(os.getcwd())))
# Creamos un array con todos los archivos
listado = os.listdir(os.getcwd())
for elemento in listado:
	if(os.path.isfile(elemento) and elemento.endswith(".gz"))
		print("--> %s es un archivo" % elemento)
		os.remove(elemento)