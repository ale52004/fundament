# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/196qk95wtXL8OYhTekFK1ckRAWP1NHmcE
"""

lista_trabajadores = []
lista_sueldos = []
nombre = ""
apellido = ""
sueldo_bruto = 0
sueldo_liquido = 0
cargo = ""
opc = 0

while True:
   (print)("""
  Menu de Trabajo
  1)Registrar trabajador
  2)listar a trabajadores
  3)imprimir planilla de sueldos
  4)salir""")
opc = int(print)("opcion")
if opc == 1:
    print("nombre: ")
    nombre = input()
    print("apellido: ")
    apellido = input()
    print("cargo: ")