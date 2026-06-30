from datetime import datetime
from os import remove

from menu_item import MenuItem
from order_item import OrderItem
from table import Table


class Order:

    __order_counter: int = 0
    DEFAULT_TIP_PERCENT: float = 10.0
    
    def __init__(self, table: Table):
        Order.__order_counter += 1
        self.__order_id = Order.__order_counter
        self.__table = table
        self.__items = []
        self.__created_at = datetime.now()
        self.__is_closed = False
    
    @property
    def order_id(self) -> int:
        return self.__order_id
    
    @property
    def table(self) -> Table:
        return self.__table

    @property
    def items(self) -> list:
        return self.__items.copy()
    
    @property
    def is_closed(self) -> bool:
        return self.__is_closed

    @property
    def created_at(self) -> datetime:
        return self.__created_at
    
    def add_item(self, menu_item: MenuItem, quantity: int = 1, notes: str = "") -> OrderItem:
        if self.is_closed:
            raise Exception("Cannot add items to closed order")
        order_item = None
        for i in range(len(self.__items)):
            if menu_item.name == self.__items[i].menu_item.name and menu_item.description == self.__items[i].menu_item.description:
                self.__items[i].quantity += quantity
                order_item = self.__items[i]
                break
        if order_item is None:
            order_item = OrderItem(menu_item, quantity, notes)
            self.__items.append(order_item)
        return order_item

    def remove_item(self, menu_item: MenuItem) -> bool:
        if self.is_closed:
            raise Exception("Cannot remove items from closed order")
        for i in range(len(self.__items)):
            if self.__items[i].menu_item == menu_item:
                self.__items.pop(i)
                return True
        return False

    def get_subtotal(self) -> float:
        subtotal = 0.0
        for order_item in self.__items:
            subtotal += order_item.subtotal
        return subtotal
    
    def get_total(self, tip_percent: float = None) -> float:
        if tip_percent is None:
            tip_percent = Order.DEFAULT_TIP_PERCENT
        return self.get_subtotal() + (self.get_subtotal() * tip_percent / 100)
    
    def get_bill(self, tip_percent: float = None) -> str:
        if tip_percent is None:
            tip_percent = Order.DEFAULT_TIP_PERCENT
        account = f"""========================================
        Bill - Order {self.__order_id}
        Table: {self.__table}
        Time: {self.__created_at}
        ========================================
        {self.__items}
        ----------------------------------------
        Subtotal: ${self.get_subtotal():.2f}
        Tip (X%): ${tip_percent:.2f}
        ========================================
        Total: ${self.get_total():.2f}
        ========================================"""
        return account

    def close(self):
        self.__is_closed = True
        self.table.free()
    
    @classmethod
    def get_total_orders(cls) -> int:
        return cls.__order_counter
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def __str__(self) -> str:
        if self.is_closed:
            return f"Order {self.order_id} (Table {self.table}) - {len(self)} items - Closed"
        return f"Order {self.order_id} (Table {self.table}) - {len(self)} items - Open"
