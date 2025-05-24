from Funciones import setters, utils
from Consultas import querys
from Comunicaciones import CNXNSQL
from Variables import variables

def putProductsInProductsTable (self):

    cursor = CNXNSQL.conexion.cursor()

    setters.update_idProd(self.ui.input_idprodNewItem.text())
    setters.update_nameProd(self.ui.input_nameNewItem.text())
    setters.update_price(self.ui.input_priceNewItem.text())
    setters.update_quantity(self.ui.input_quantityNewItem.text())

    flagExitsProduct = querys.getProductByID(cursor, variables.idProd)

    if flagExitsProduct == '' :

        querys.insertInfoProductTable(cursor, variables.idProd, variables.nameProd, variables.price, variables.quantity)
        CNXNSQL.conexion.commit()
        utils.cleanFieldsInsertItem(self)
    
    else:
        setters.update_nameProd(flagExitsProduct[0][1])
        querys.updateInfoProductTable(cursor, variables.quantity, variables.price, variables.idProd, variables.nameProd)
        CNXNSQL.conexion.commit()
        utils.cleanFieldsInsertItem(self)        
