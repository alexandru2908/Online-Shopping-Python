import cart

class Store:
    def __init__(self, stock):
        self.stock = stock
        self.customer_carts = dict() 

    def login(self, customer_id):
        self.customer_carts[customer_id] = cart.Cart()

    def add_to_cart(self, customer_id, product_name):
        if customer_id in self.customer_carts:
            for product in self.stock.list_stock:
                if product.name == product_name:
                    self.customer_carts[customer_id].add(product)
                    self.stock.remove(product_name)
                    break
    
    def remove_from_cart(self, customer_id, product_name):
        if customer_id not in self.customer_carts:
            return
        for product in self.customer_carts[customer_id].list_cart:
            if product_name == product.name:
                self.customer_carts[customer_id].remove(product_name)
                self.stock.add(product)
                break

    def view_cart(self, customer_id):
        return [(product.name, product.price) for product in self.customer_carts[customer_id].view()]

    def checkout(self, customer_id):
        total_price = self.customer_carts[customer_id].cart_checkout()
        self.customer_carts[customer_id] = cart.Cart()
        return total_price


