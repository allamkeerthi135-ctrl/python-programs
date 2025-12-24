class Customer:
    def __init__(self, name, pnumber, address):
        self.name = name
        self.pnumber = pnumber
        self.address = address
    def order(self):
        print("Ordering food")
    def cancel_order(self):
        print("I am cancelling the order")
    def payment(self):
        print("I am paying the amount")
class GoldCustomer(Customer):
    def __init__(self, name, pnumber, address, gold_id):
        super().__init__(name, pnumber, address)
        self.gold_id = gold_id
    def free_delivery(self):
        print("I am ordering with no delivery cost")
C = Customer("Keerthi", 45673, "Badvel")
G = GoldCustomer("Ganga", 456, "Kadapa", 1)
C.order()
C.payment()
G.order()
G.free_delivery()
G.payment()

