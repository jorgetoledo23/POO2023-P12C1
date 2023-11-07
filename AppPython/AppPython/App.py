import os
from Model.Categoria import Categoria
from BDConnect import DAO

while True:
    os.system("cls")
    print("{1} - Insertar Categoria")
    print("{2} - Listar Categorias")
    print("{5} - Actualizar una Categoria")
    print("{6} - Eliminar una Categoria")
    print("{7} - Filtrar Categorias")

    #TASKS
    print("{3} - Insertar nuevo Producto")
    print("{4} - Listar Productos")


    print("{0} - Salir")
    op = input("Selecciona una Opcion: ")

    dao = DAO()
    if(op == "1"):
        nombre = input("Nombre de la Categoria: ")
        category = Categoria(0, nombre)
        dao.InsertarCategoria(category)
        input("Categoria Insertada")

    if(op == "2"):
        for cat in dao.LeerCategorias():
            print(cat.getNombreCategoria())
        input("Categorias Listadas... Presiona ENTER para continar")

    if(op == "5"):
        cod = input("Ingresa Codigo de la Categoria: ")
        newName = input("Ingresa el Nuevo Nombre de la Categoria: ")
        cat = Categoria(cod, newName)
        dao.ActualizarCategoria(cat)
        input("Categoria Actualizada! Presiona ENTER para Continuar...")

    if(op == "6"):
        cod = input("Ingresa Codigo de la Categoria: ")
        respuesta = input(f"¿Estas Seguro de Eliminar la Categoria {cod}? (S/N): ")
        if(respuesta.upper() == "S"):   
            dao.EliminarCategoria(cod)
            input("Categoria Eliminada! Presiona ENTER para Continuar...")

    if(op == "7"):
        filtro = input("Ingrese el Filtro: ")
        print("Resultados: ")
        for cat in dao.FiltrarCategorias(filtro):
            print(cat.getNombreCategoria())
        input()