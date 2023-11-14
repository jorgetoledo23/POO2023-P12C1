


class Producto:
    def __init__(self, cod:int, nombre:str, desc:str, valor:str, stock:str, cod_cat:int):
        self.__Cod_Producto = cod
        self.__Nombre = nombre
        self.__Descripcion = desc
        self.__Valor = valor
        self.__Stock = stock
        self.__Cod_Categoria = cod_cat

    def getCodProducto(self)->int:
        return self.__Cod_Producto
    
    def getNombre(self)->str:
        return self.__Nombre
    
    def setNombre(self, nuevonombre:str):
        self.__Nombre = nuevonombre
    
    def getDescripcion(self)->str:
        return self.__Descripcion
    
    def getValor(self)->int:
        return self.__Valor
    
    def getStock(self)->int:
        return self.__Stock
    
    def getCodCategoria(self)->int:
        return self.__Cod_Categoria