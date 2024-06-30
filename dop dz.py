class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"{item_name} добавлен в ассортимент {self.name} по цене {price}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} удален из ассортимента {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена {item_name} в ассортименте {self.name} обновлена")
        else:
            print(f"{item_name} нет в ассортименте {self.name}")


store1 = Store("Пятерочка", "ул. Ленина, 5")
store2 = Store("Магнит", "ул. Мира, 10")
store3 = Store("Лента", "ул. Весенняя, 51")

store1.add_item("молоко", 2.5)
store1.add_item("хлеб", 1.5)
store1.add_item("масло", 3.5)

store1.get_price("молоко")
store1.get_price("масло")

store1.remove_item("молоко")
store1.remove_item("масло")

store1.get_price("хлеб")
store1.get_price("масло")

store1.update_price("хлеб", 2.0)
store1.update_price("масло", 1.6)

print(store1.get_price("хлеб"))
print(store1.get_price("масло"))

