#!/bin/bash

# Verifica si se está ejecutando como root
if [[ $UID -ne 0 ]]; then
  echo "Este script debe ejecutarse como root."
  exit 1
fi

# Actualiza el repositorio de paquetes
sudo apt update

# Instala las dependencias usando pip
sudo pip install Flask tabulate

# Ejecuta el programa
sudo python efm3_app.py