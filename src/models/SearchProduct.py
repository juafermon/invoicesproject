from src.core import variables, utils, setters
from src.database import CNXNSQL, querys
from src.services import ValidationsSearchProduct, ValidationsCreateInv

#Se define la variable con el cursor para ejecutar las consultas
cursor = CNXNSQL.conexion.cursor() 

def searchProductById(self):
        
    setters.update_search_id(self.ui.input_searchStock.text())
    if variables.searchId == '':
        ValidationsCreateInv.productCamp(self)
    else:
        # Se guarda el resultado de la consulta en la variable result 
        results = querys.getProductByID(cursor, variables.searchId)

        if not results:
            ValidationsSearchProduct.searchIdField(self, variables.searchId)
        else:    
            #Se limpia la tabla para poder ingresar los productos
            utils.cleanStockTable(self)
            # Se imprimen los resultados en la tabla
            utils.stockTable(self, results)

def getListProduct(self):
    #Se limpia la tabla para poder ingresar los productos
    utils.cleanStockTable(self)
    # Se guarda el resultado de la consulta en la variable result
    results = querys.getAllProducts(cursor)
    # Se imprimen los resultados en la tabla
    utils.stockTable(self, results)
