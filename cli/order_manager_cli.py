import os
import sys

from table import Table

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from restaurant import Restaurant
from order import Order
from menu_item import MenuItem, Appetizer, MainCourse


class OrderManagerCLI:
    def __init__(self, restaurant: Restaurant):
        self.__restaurant = restaurant
    
    def run(self):
        while True:
            self._display_menu()
            user_choose = input("Choose option: ")
            if user_choose == "0":
                break
            elif user_choose == "1":
                self._open_new_order()
            elif user_choose == "2":
                self._show_active_orders()
            elif user_choose == "3":
                self._manage_order()
            elif user_choose == "4":
                self._close_order()
            else:
                print("*** Invalid choice ***")

    def _display_menu(self):
        os.system("cls" if os.name == "nt" else "clear")
        print( """
            ===== Order Management =====
            1. Open New Order
            2. Show Active Orders
            3. Edit Existing Order
            4. Close Order (Bill)
            0. Back to Main Menu
        """)

    def _open_new_order(self):
        print("----Open New Order----")
        tables = self.__restaurant.get_free_tables()
        if not tables:
            print("*** No free tables ***")
            return
        print("---tables---")
        for table in tables:
            print(table.number)
        user_choose = input("Choose table: ")
        if not user_choose.isdigit():
            raise ValueError("*** Error: you need choose number ***")
        user_choose = int(user_choose)
        if user_choose not in tables:
            raise ValueError("*** Error: invalid table ***")
        the_order = self.__restaurant.open_order(user_choose)
        print("===", the_order, "===")
        user_choose = input("Add items now? (y/n): ")
        if user_choose == "y" or user_choose == "Y" or user_choose == "ט":
            self._add_items_loop(the_order)
    
    def _show_active_orders(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Active Orders ---")
        active_orders = self.__restaurant.get_active_orders()
        if not active_orders:
            print("*** No active orders ***")
        else:
            for i, order in enumerate(active_orders):
                print(i, ".", order, f"Current total: ${order.get_subtotal():.2f}")
        input("Press Enter to go back...")
    
    def _manage_order(self):
        print("--- manage_order ---")
        active_orders = self.__restaurant.get_active_orders()
        if not active_orders:
            print(" *** No active orders ***")
            return
        for order in active_orders:
            print(order)
        user_choose = input("Table number to edit: ")
        if not user_choose.isdigit():
            raise ValueError("*** Error: you need choose number ***")
        user_choose = int(user_choose)
        order = self.__restaurant.get_order_by_table(user_choose)
        if not order:
            print(f"*** Error No active order for table {user_choose} ***")
        else:
            self._edit_order_menu(order)
    
    def _edit_order_menu(self, order: Order):
        while True:
            print(f""" ===== Edit Order #{order.order_id} (Table {order.table.number}) =====
            1. Show Order Items
            2. Add Item
            3. Remove Item
            4. Show Current Bill
            0. Back""")
            user_choose = input("choose option: ")
            if user_choose == "1":
                self._show_order_items(order)
            elif user_choose == "2":
                self._add_item_to_order(order)
            elif user_choose == "3":
                self._remove_item_from_order(order)
            elif user_choose == "4":
                self._print_bill(order)
            elif user_choose == "0":
                return
            else:
                print("*** Invalid choice ***")

    def _show_order_items(self, order: Order):
        print(f"---Items in Order #{order.order_id}:---")
        if not order.items:
            print("(Order is empty)")
        else:
            for order_item in order.items:
                print(order_item)
        input("Press Enter to go back...")

    def _add_item_to_order(self, order: Order):
        self._add_items_loop(order)

    def _add_items_loop(self, order: Order):
        categories = self.__restaurant.menu.get_all_categories()
        while True:
            print("==== Menu ====\n")
            for cat in sorted(categories):
                print(f"---{cat}---\n")
                for item in self.__restaurant.menu.get_by_category(cat):
                    print("\t", item)
            user_item = input("Item name (or 'done' to finish): ")
            if not user_item or user_item == "done":
                break
            user_item = self.__restaurant.menu.find_item(user_item)
            if user_item is None:
                print(f"*** Item {user_item} not found ***")
                continue
            user_quantity = input("Enter quantity (enter to 1): ")
            if not user_quantity.isdigit() and user_quantity:
                raise ValueError("*** Error: you need choose number ***")
            user_quantity = int(user_quantity)
            user_notes = input("Enter notes (optional): ")
            if user_item.get_category() == "Appetizers":
                print("Available breads:", end="")
                for bread in Appetizer.get_available_breads():
                    print(", ", bread, end="")
                user_bread = input("Add bread? (leave empty to skip): ")
                if not user_item.add_bread(user_bread):
                    print("breads no added")
            elif user_item.get_category == "Main Courses":
                print("Available sides: ", end="")
                for side in MainCourse.get_side_options():
                    print(", ", side)
                user_side = "Choose side (leave empty to skip): "
                if not user_item.select_side(user_side):
                    print("sides no added")
            order.add_item(user_item, user_quantity, user_notes)
            print(f"*** Added: {user_item.name} * {user_quantity if user_quantity else 1} {user_notes} ***")
    
    def _remove_item_from_order(self, order: Order):
        if not order.items:
            print("*** Order is empty ***")
            return
        print("Items in order: ")
        for item in order.items:
            print("\t", item)
        user_item = input("Item name to remove: ")
        user_item = self.__restaurant.menu.find_item(user_item)
        if not user_item:
            print(f"*** Item {user_item} not found in order ***")
        order.remove_item(user_item)
        print(f"*** Item {user_item} removed ***")
    
    def _print_bill(self, order: Order):
        os.system("cls" if os.name == "nt" else "clear")
        print(order.get_bill())
        input("Press Enter to go back...")
    
    def _close_order(self):
        if not self.__restaurant.get_active_orders():
            print("*** No active orders ***")
            return
        print("--- orders ---")
        for order in self.__restaurant.get_active_orders():
            print(order)
        user_choose = input("Table number to close: ")
        for order in self.__restaurant.get_active_orders():
            if order.table.number == int(user_choose):
                user_choose = order
        if not isinstance(user_choose, Order):
            print(f"*** No active order for table {user_choose} ***")
            return
        print(user_choose.get_bill())
        user_tip = input("Tip percent (default 10%): ")
        if user_tip.isdigit():
            user_tip = float(user_tip)
        print(user_choose.get_bill(user_tip))
        user_close = input("Close order? (y/n): ")
        if user_close == "y" or user_close == "yes":
            total = self.__restaurant.close_order(user_choose, user_tip)
            print(f"*** Order closed. Total: ₪{total} ***")
            return
        print("*** Closing cancelled ***")