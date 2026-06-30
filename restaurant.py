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
        if not the_table:
            raise ValueError(f"Table {table_number} does not exist")
        if the_table.is_occupied:
            raise ValueError(f"Table {table_number} is already occupied")
        the_table.__is_occupied = True
        return Order(the_table)
    
    def get_active_orders(self) -> list:
        return self.__active_orders.copy()
    
    def get_order_by_table(self, table_number: int) -> Order | None:
        for order in self.__active_orders:
            if order.table == table_number:
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
        list_of_tested = []
        max_num = 0
        max_item = ""

        current_num = 0
        current_item = ""
        flag = False
        while not flag:
            flag = True
            for order in self.__closed_orders:
                for item in order.items:
                    if item not in list_of_tested and current_item == "":
                        current_item = item
                        current_num += current_item.quantity
                        flag = False
            current_item = 0

        """
        מחזיר את הפריט שהוזמן הכי הרבה.
        
        דרישות:
        - לעבור על כל ההזמנות הסגורות
        - לספור כמה פעמים כל פריט הוזמן
        - להחזיר את הפריט עם הספירה הגבוהה ביותר
        
        Returns:
            (item_name, count) או (None, 0) אם אין נתונים
        """
        raise NotImplementedError("Implement this method")
    
    def get_revenue_by_category(self) -> dict:
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
