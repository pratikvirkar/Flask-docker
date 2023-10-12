

class Product:
    def __init__(self,pid,pnm,pqty,pven,pric):
        self.prod_id = pid
        self.prod_name = pnm
        self.prod_qty = pqty
        self.prod_ven = pven
        self.prod_price = pric

    def __str__(self):
        return f'''{self.__dict__}'''

        def __repr__(self):
            return str(self)
