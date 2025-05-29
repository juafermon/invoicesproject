from src.database import CNXNSQL, querys
from src.core import setters, variables, utils
from src.services import ValidationsCreateInv, ValidationsUpdateStock

cursor = CNXNSQL.conexion.cursor()

#Insert info in products table from update stock function

def insertProductsInProductsTable (self):

    setters.update_idProd(self.ui.input_idprodNewItem.text())
    setters.update_nameProd(self.ui.input_nameNewItem.text())
    setters.update_price(self.ui.input_priceNewItem.text())
    setters.update_quantity(self.ui.input_quantityNewItem.text())
    
    #Validation field Id product is empty
    if not variables.idProd:

        ValidationsCreateInv.productCamp(self, variables.idProd)

    else:
        #Get product info it is exits
        flagExitsProduct = querys.getProductByID(cursor, variables.idProd)

        #If the product does not exits, insert the new product in the BD
        if not flagExitsProduct:
    
            if variables.quantity == '' or variables.price =='' or variables.nameProd == '':
                
                ValidationsUpdateStock.emptyFieldsNewProduct(self, variables.nameProd)
            
            else:
                
                querys.insertInfoProductTable(cursor, variables.idProd, variables.nameProd, variables.price, variables.quantity)
                CNXNSQL.conexion.commit()
                utils.cleanFieldsInsertItem(self)
            
        #Validate if quantity, price and name product fields are empty
        elif variables.quantity == '' and variables.price =='' and variables.nameProd == '':
        
            ValidationsUpdateStock.emptyFields(self, variables.nameProd)
        
        #Update the product with price and name product fields empty
        elif variables.price =='' and variables.nameProd == '':
        
            setters.update_price(int(flagExitsProduct[0][2]))
            setters.update_nameProd(flagExitsProduct[0][1])
            querys.updateInfoProductTable(cursor, int(variables.quantity) + int(flagExitsProduct[0][3]), variables.price, variables.idProd, variables.nameProd)
            CNXNSQL.conexion.commit()
            utils.cleanFieldsInsertItem(self)

        #Update the product with quantity and name product fields empty
        elif variables.quantity == '' and variables.nameProd == '':
        
            setters.update_quantity(int(flagExitsProduct[0][3]))
            setters.update_nameProd(flagExitsProduct[0][1])
            querys.updateInfoProductTable(cursor, variables.quantity, variables.price, variables.idProd, variables.nameProd)
            CNXNSQL.conexion.commit()
            utils.cleanFieldsInsertItem(self)
        
        #Update the product with quantity and price product fields empty
        elif variables.quantity == '' and variables.price =='':
        
            setters.update_quantity(int(flagExitsProduct[0][3]))
            setters.update_price(flagExitsProduct[0][2])
            querys.updateInfoProductTable(cursor, variables.quantity, variables.price, variables.idProd, variables.nameProd)
            CNXNSQL.conexion.commit()
            utils.cleanFieldsInsertItem(self)
        
        #Update the product with price field empty
        elif variables.price == '':
        
            setters.update_price(flagExitsProduct[0][2])
            querys.updateInfoProductTable(cursor, int(variables.quantity) + int(flagExitsProduct[0][3]), variables.price, variables.idProd, variables.nameProd)
            CNXNSQL.conexion.commit()
            utils.cleanFieldsInsertItem(self)

        #Update the product with product name field empty 
        elif variables.nameProd == '':
        
            setters.update_nameProd(flagExitsProduct[0][1])
            querys.updateInfoProductTable(cursor, int(variables.quantity) + int(flagExitsProduct[0][3]), variables.price, variables.idProd, variables.nameProd)
            CNXNSQL.conexion.commit()
            utils.cleanFieldsInsertItem(self)            

        #Update the product with quantity field empty 
        elif variables.quantity == '':
        
            setters.update_quantity(flagExitsProduct[0][3])
            querys.updateInfoProductTable(cursor, variables.quantity, variables.price, variables.idProd, variables.nameProd)
            CNXNSQL.conexion.commit()
            utils.cleanFieldsInsertItem(self)            
