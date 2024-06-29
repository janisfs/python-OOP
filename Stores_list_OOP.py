class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Пустой словарь для хранения товаров и их цен

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент"""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента, если он существует"""
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        """Возвращает цену товара по его названию, если товар отсутствует, возвращает None"""
        return self.items.get(item_name, None)

    def update_item_price(self, item_name, new_price):
        """Обновляет цену товара, если он существует в ассортименте"""
        if item_name in self.items:
            self.items[item_name] = new_price

    def __str__(self):
        """Возвращает строковое представление магазина"""
        items_str = ', '.join(f"'{k}': {v}" for k, v in self.items.items())
        return f"Store: {self.name}, address: {self.address}, items: {items_str}"

# Пример использования класса
store = Store("My Grocery Store", "123 Red square St")
store.add_item("apples", 0.5)
store.add_item("bananas", 0.75)
store.add_item("oranges", 0.25)
store.add_item("milk", 2.0)
store.add_item("bread", 1.5)
print(store)

store.update_item_price("apples", 0.55)
store.update_item_price("bread", 1.6)
print(store.get_item_price("apples"))
print(store.get_item_price("bread"))

store.remove_item("bananas")
print(store)
