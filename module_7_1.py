class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'




class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        f = open(self.__file_name, "r")
        a = f.read()
        f.close()
        return a

    def add(self, *products):
        f = open(self.__file_name, "a")
        for i in products:
            if i.name not in self.get_products():
                f.write(f'{str(i)}\n')
            else:
                print(f'Продукт {i.name} уже есть в магазине' )
        f.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())