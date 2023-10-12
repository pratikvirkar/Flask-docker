from config.app_config import *
from models.product import Product

prodList = []
@app.route('/product/save',methods=['POST'])
def product_save():
    formdata = request.form                 #post method --
    pid = formdata.get('product_id')        # one one field--> read
    pnm = formdata.get('product_name')
    price = formdata.get('product_price')
    qty = formdata.get('product_qty')
    ven = formdata.get('product_ven')
    type1 = formdata.get('type1')
    type3 = formdata.get('type3')
    type2 = formdata.getlist('type2')   # []
    type4 = formdata.getlist('type4')
    print('TYPE1 : ',type1)
    print('TYPE2 : ', type2)
    print('TYPE3 : ', type3)
    print('TYPE4 : ', type4)
    prod =Product(pid,pnm,qty,ven,price)        # product create
    prod.type1 = type1
    prod.type2 = type2
    prod.type3 = type3
    prod.type4 = type4
    prodList.append(prod)                       # adding that product inside list..
    return render_template('home.html',product_list = prodList)


