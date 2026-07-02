from typing import Any

from menu import Menu
from table import Table
from order import Order
from menu_item import MenuItem



class Restaurant:
    def __init__(self, name: str):
        self.__name = name
        self.__menu = Menu()
        self.__tables = []
        self.__active_orders = []
        self.__closed_orders = []
        self.__total_revenue = 0.0
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def menu(self) -> Menu:
        return self.__menu

    def add_table(self, table: Table):
        self.__tables.append(table)

    def get_table(self, number: int) -> Table | None:
        for table in self.__tables:
            if table.number == number:
                return table
        return None
    
    def get_all_tables(self) -> list:
        return self.__tables.copy()

    def get_free_tables(self) -> list:
        lst = []
        for table in self.__tables:
            if not table.is_occupied:
                lst.append(table)
        return lst
    
    def get_occupied_tables(self) -> list:
        lst = []
        for table in self.__tables:
            if table.is_occupied:
                lst.append(table)
        return lst

    def open_order(self, table_number: int) -> Order:
        the_table = None
        for tabel in self.__tables:
            if tabel.number == table_number:
                the_table = tabel
        if the_table is None:
            raise ValueError(f"Table {table_number} does not exist")
        if not the_table.occupy():
            raise ValueError(f"Table {table_number} is already occupied")
        # self.__active_orders.append(Order(the_table))
        return Order(the_table)
    
    def get_active_orders(self) -> list:
        return self.__active_orders.copy()
    
    def get_order_by_table(self, table_number: int) -> Order | None:
        for order in self.__active_orders:
            if order.table.number == table_number:
                return order
        return None
    
    def close_order(self, order: Order, tip_percent: float = None) -> float:
        if order not in self.__active_orders:
            raise ValueError("Order not found in active orders")
        total_count = order.get_total(tip_percent)
        order.close()
        self.__closed_orders.append(order)
        self.__active_orders.remove(order)
        self.__total_revenue += total_count
        return total_count
    
    def get_total_revenue(self) -> float:
        return self.__total_revenue
    
    def get_orders_count(self) -> int:
        return len(self.__closed_orders)
    
    def get_average_order_value(self) -> float:
        if not self.get_orders_count():
            return 0.0
        return self.get_total_revenue() / self.get_orders_count()
    
    def get_most_popular_item(self) -> tuple:
        dictionary = {}
        for order in self.__closed_orders:
            for order_item in order.items:
                if order_item.menu_item.name not in dictionary:
                    dictionary[order_item.menu_item.name] = 0
        for order in self.__closed_orders:
            for order_item in order.items:
                dictionary[order_item.menu_item.name] += order_item.quantity
        if not dictionary:
            return None, 0
        num_max_menu_item = 0
        name_max_menu_item = ""
        for menu_item in dictionary:
            if num_max_menu_item < dictionary[menu_item]:
                name_max_menu_item = menu_item
                num_max_menu_item = dictionary[menu_item]
        return name_max_menu_item, num_max_menu_item

    
    def get_revenue_by_category(self) -> dict:
        dictionary = {}
        for
        """
        מחזיר הכנסות מחולקות לפי קטגוריה.
        
        Returns:
            מילון {category: amount}
        """
        raise NotImplementedError("Implement this method")
    
     # --- Magic Methods ---
    
    def __str__(self) -> str:
        """
        ייצוג מחרוזת.
        
        Returns:
            "Restaurant 'name' - X tables, Y menu items"
        """
        raise NotImplementedError("Implement this method")
