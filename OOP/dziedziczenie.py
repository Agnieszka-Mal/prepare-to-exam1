class Cart:
    def __init__(self):
        self.products = []

    def add(self, price: float, product: str):
        return self.products.append((price, product))

    def summary(self):
        return self.products

class Discount20PercentCart(Cart):
    def __init__(self):
        super().__init__()


    def summary(self, object):
        return [(i[0] * 0.8, i[1]) for i in object.summary()]


class Above3ProductsCheapestFreeCart(Cart):

    def summary(self, object):
        list_products = sorted(object.summary())
        x = len(list_products)
        if x > 3:
            list_products[0] = list(list_products[0])
            list_products[0][0] = 0
            list_products[0] = tuple(list_products[0])
            return list_products
        else:
            return list_products





u = Cart()
u.add(20, 'masło')
u.add(10, "sok")
u.add(4, 'guma')
u.add(16, 'fajki')
print(u.summary())
k = Discount20PercentCart()
print(k.summary(u))
g = Above3ProductsCheapestFreeCart()
print(g.summary(u))