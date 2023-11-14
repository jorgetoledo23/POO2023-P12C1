#pip install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode
from Model.Categoria import Categoria
from Model.Producto import Producto
from typing import List

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user="root",
                password="root",
                host="localhost",
                database="test"
            )
            #print("Conexion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos NO existe")
            else:
                print(err)

    def InsertarCategoria(self, cat:Categoria):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO tbl_categorias (nombre) VALUES (%s);")
        data = (cat.getNombreCategoria(),)
        cursor.execute(query, data)
        self.cnx.commit()

    def InsertarProducto(self, prod:Producto):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO tbl_productos (nombre, descripcion, valor_unitario, stock, cod_categoria) VALUES (%s, %s, %s, %s, %s);")
        data = (prod.getNombre(), prod.getDescripcion(), prod.getValor(), prod.getStock(), prod.getCodCategoria())
        cursor.execute(query, data)
        self.cnx.commit()

    def ActualizarCategoria(self, cat:Categoria):
        cursor = self.cnx.cursor()
        query = ("UPDATE tbl_categorias SET nombre = %s WHERE cod_categoria = %s;")
        data = (cat.getNombreCategoria(), cat.getCodCategoria())
        cursor.execute(query, data)
        self.cnx.commit()

    def EliminarCategoria(self, cod:int):
        cursor = self.cnx.cursor()
        query = ("DELETE FROM tbl_categorias WHERE cod_categoria = %s;")
        data = (int(cod),)
        cursor.execute(query, data)
        self.cnx.commit()

    def LeerCategorias(self) -> List[Categoria]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM tbl_categorias")
        cursor.execute(query)
        categorias:List[Categoria] = []
        for (cod_categoria, nombre) in cursor:
            cat = Categoria(cod_categoria, nombre)
            categorias.append(cat)
        return categorias
    
    def LeerProductos(self) -> List[Producto]:
        cursor = self.cnx.cursor()
        query = ("""select p.cod_producto, p.nombre, p.descripcion, 
                p.valor_unitario, p.stock, c.nombre, p.cod_categoria
                from tbl_productos p
                inner join tbl_categorias c 
                on p.cod_categoria = c.cod_categoria""")
        cursor.execute(query)
        productos:List[Producto] = []
        for (cod_producto, nombre, descripcion, valor_unitario, stock, cod_categoria) in cursor:
            prod = Producto(cod_producto, nombre, descripcion, valor_unitario, stock, cod_categoria)
            productos.append(prod)
        return productos
    
    def FiltrarCategorias(self, filtro:str) -> List[Categoria]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM tbl_categorias WHERE nombre LIKE CONCAT('%', %s, '%')")
        data = (filtro,)
        cursor.execute(query, data)
        categorias:List[Categoria] = []
        for (cod_categoria, nombre) in cursor:
            cat = Categoria(cod_categoria, nombre)
            categorias.append(cat)
        return categorias
    
    def FiltrarProductos(self, filtro:int) -> List[Categoria]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM tbl_productos WHERE valor_unitario < %s")
        data = (int(filtro),)
        cursor.execute(query, data)
        categorias:List[Categoria] = []
        for (cod_categoria, nombre) in cursor:
            cat = Categoria(cod_categoria, nombre)
            categorias.append(cat)
        return categorias

    