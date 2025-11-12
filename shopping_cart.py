class Product:
    def __init__(self, item_name, price, deal_price, rating):
        self.item_name = item_name 
        self.price = price
        self.deal_price = deal_price 
        self.rating = rating 
        self.you_saved = price - deal_price
        
    def display_product_details(self):
        print("Product Name :{}".format(self.item_name))
        print("Price :{}".format(self.price))
        print("Deal Price :{}".format(self.deal_price))
        print("Rating :{}".format(self.rating))
        print("You Save :{}".format(self.you_saved))
        
    def get_deal_price(self):
        return self.deal_price
        
class ElectronicItem(Product):
    def set_warrenty(self, warrenty_in_months):
        self.warrenty_in_months = warrenty_in_months
        
    def get_warrenty(self):
        return self.warrenty_in_months 
        
    def display_product_details(self):
        super().display_product_details()
        print("Warrenty In Months :{}".format(self.warrenty_in_months))
        
        
class GroceryItem(Product):
    def set_expiry_date(self, expiry_date):
        self.expiry_date = expiry_date 
        
    def get_expiry_date(self):
        return self.expiry_date
        
    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date :{}".format(self.expiry_date))
        
class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_speed 
        
    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))
        
    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity :{}".format(quantity))
            print(" ")
            
    def get_total_bill(self):
        total_bill = 0 
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price 
        print("Total Bill :{}".format(total_bill))
        return total_bill
    
E = ElectronicItem("Samsung Fold F4", 48500, 47999, 5.0)
E.set_warrenty(24)
G = GroceryItem("Chana Dal", 5200, 5000, 4.8)
G.set_expiry_date("22-12-2023")


my_order = Order("Prime", "Hyderabad")
my_order.add_item(E, 1)
my_order.add_item(G, 2)
my_order.display_order_details()
my_order.get_total_bill()