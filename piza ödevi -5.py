class Pizza:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class Menu:
    def __init__(self):
        self.pizzas = [
            Pizza("Klasik", "Domates sosu, mozzarella peyniri ve zeytin", 20),
            Pizza("Margarita", "Domates sosu, mozzarella peyniri ve fesleğen", 22),
            Pizza("TürkPizza", "Domates sosu, sucuk, kaşar peyniri, biber ve domates", 25),
            Pizza("Sade Pizza", "Domates sosu ve mozzarella peyniri", 18)
        ]
        self.sauces = [
            Pizza("Zeytin", "Zeytin", 2),
            Pizza("Mantarlar", "Mantarlar", 3),
            Pizza("Keçi Peyniri", "Keçi peyniri", 5),
            Pizza("Et", "Et", 4),
            Pizza("Soğan", "Soğan", 2),
            Pizza("Mısır", "Mısır", 2)
        ]

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        # Burada kredi kartı işlemi gerçekleştirilebilir
        print("Ödeme işlemi tamamlandı.")

class Order:
    def __init__(self, menu):
        self.menu = menu
        self.pizza = None
        self.sauce = None
        self.total_price = 0

    def choose_pizza(self, index):
        self.pizza = self.menu.pizzas[index-1]
        self.total_price += self.pizza.price

    def choose_sauce(self, index):
        self.sauce = self.menu.sau
        # hocam yapabildiğim buydu eksik ve yanlışlar için şimdiden özürdilerim
