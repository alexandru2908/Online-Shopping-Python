class Cart:
    def __init__(self):
        self.list_cart = []

    def add(self, new_product):
        self.list_cart.append(new_product)
      


    def remove(self, product_name):
        for product in self.list_cart:
            if product.name == product_name:
                
                self.list_cart.remove(product)
      


    def view(self):
        return self.list_cart

    def cart_checkout(self):
        s=0
        for product in self.list_cart:
            s+=product.price
        self.list_cart=[]
        return s

    