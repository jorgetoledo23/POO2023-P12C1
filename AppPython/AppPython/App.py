import os
from Model.Categoria import Categoria
from Model.Producto import Producto
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

    if(op == "3"):
        os.system("cls")
        for cat in dao.LeerCategorias():
            print(f"{cat.getCodCategoria()} | {cat.getNombreCategoria()}")
        cat = input("Selecciona la Categoria a la cual pertenece el Producto: ")
        os.system("cls")
        n = input("Ingresa Nombre del Producto: ")
        d = input("Ingresa la Descripcion detalla del Producto: ")
        v = input("Ingresa el Valor Unitario del Producto: ")
        s = input("Ingresa el Stock disponible del Producto: ")
        p = Producto(0, n, d, v, s, cat)
        dao.InsertarProducto(p)
        input("Producto Insertado! Presiona ENTER para continuar...")

    if(op == "4"):
        for prod in dao.LeerProductos():
            print(f"{prod.getCodProducto()} | {prod.getNombre()} | {prod.getDescripcion()} | {prod.getValor()} | {prod.getStock()} | {prod.getCodCategoria()}")
        input("Productos Listados... Presiona ENTER para continar")


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