class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        items_str = ', '.join(f"'{k}': {v}" for k, v in self.items.items())
        return f"Store: {self.name}, address: {self.address}, items: {items_str}"

# Создаем список магазинов
stores = []

# Создаем первый магазин и добавляем товары
store1 = Store("My Grocery Store", "123 Main St")
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store1.add_item("oranges", 0.25)
stores.append(store1)

# Создаем второй магазин и добавляем товары
store2 = Store("Tech Store", "456 Tech Blvd")
store2.add_item("laptop", 999.99)
store2.add_item("mouse", 25.99)
store2.add_item("keyboard", 49.99)
stores.append(store2)

# Создаем третий магазин и добавляем товары
store3 = Store("Book Store", "789 Book Ave")
store3.add_item("novel", 12.99)
store3.add_item("notebook", 2.49)
store3.add_item("pen", 1.99)
stores.append(store3)

# Выводим информацию о всех магазинах
for store in stores:
    print(store)
