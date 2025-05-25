from src.core import variables, utils, setters
from src.database import CNXNSQL, querys

#Se define la variable con el cursor para ejecutar las consultas
cursor = CNXNSQL.conexion.cursor() 

def searchProductById(self):
    
    #Se limpia la tabla para poder ingresar los productos
    utils.cleanStockTable(self)
    setters.update_search_id(self.ui.input_searchStock.text())
    print(variables.searchId,  "Prueba", self.ui.input_searchStock.text())
    # Se guarda el resultado de la consulta en la variable result
    result = querys.getProductByID(cursor, variables.searchId)
    print(result)
    # Se imprimen los resultados en la tabla
    utils.stockTable(self, result)

def getListProduct(self):
    #Se limpia la tabla para poder ingresar los productos
    utils.cleanStockTable(self)
    # Se guarda el resultado de la consulta en la variable result
    results = querys.getAllProducts(cursor)
    # Se imprimen los resultados en la tabla
    utils.stockTable(self, results)
