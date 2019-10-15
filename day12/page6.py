class Cart:

    def __init__(self, products, customer):
        self._products = products
        self._customer = customer

    def __str__(self):
        return "this cart is owned by " + self._customer

    def __len__(self):
        return len(self._products)

    def count(self):
        return len(self._products)


cart = Cart(['iphone', 'ipad', 'imac', 'magic mouse'], 'customer 1')
print(cart)

# len() will try to find the method __len__ in the object
print('# products: ', len(cart))
print('# products: ', cart.count())
print(dir(cart))

# products = ['iphone', 'ipad', 'imac', 'magic mouse']
# print('count: ', len(products))
