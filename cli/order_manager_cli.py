# cli/order_manager_cli.py - ניהול הזמנות (לא ממומש - עליכם להשלים!)

import os
import sys

from table import Table

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from restaurant import Restaurant
from order import Order
from menu_item import MenuItem, Appetizer, MainCourse


class OrderManagerCLI:
    """
    ניהול הזמנות - פתיחה, עריכה, וסגירת חשבון.
    
    מחלקה זו אחראית על כל הפעולות הקשורות להזמנות:
    - פתיחת הזמנה חדשה לשולחן
    - הצגת הזמנות פעילות
    - עריכת הזמנה (הוספה/הסרה של פריטים)
    - סגירת חשבון
    
    שדות:
        _restaurant (Restaurant): אובייקט המסעדה
    """
    
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
        """
        לולאת הוספת פריטים להזמנה.
        
        דרישות:
        - לולאה שרצה עד שהמשתמש מקליד 'done' או מחרוזת ריקה
        - בכל איטרציה:
            - להציג את כל התפריט (לפי קטגוריות)
            - לבקש "Item name (or 'done' to finish): "
            - אם 'done' או ריק -> break
            - לחפש את הפריט בתפריט
            - אם לא נמצא -> "*** Item 'X' not found ***", continue
            - לבקש "Quantity: " (ברירת מחדל: 1)
            - לבקש "Notes (optional): "
            - אם זו מנה ראשונה (Appetizer):
                - להציג "Available breads: ..."
                - לשאול "Add bread? (leave empty to skip): "
            - אם זו מנה עיקרית (MainCourse):
                - להציג "Available sides: ..."
                - לשאול "Choose side (leave empty to skip): "
            - להוסיף להזמנה (order.add_item)
            - להציג "*** Added: X x ItemName ***"
        
        Args:
            order: ההזמנה להוספה אליה
        """
        pass
    
    def _remove_item_from_order(self, order: Order):
        """
        הסרת פריט מההזמנה.
        
        דרישות:
        - אם ההזמנה ריקה, להציג "*** Order is empty ***" ולחזור
        - להציג רשימת הפריטים "Items in order:"
        - לבקש "Item name to remove: "
        - לחפש את הפריט בתפריט
        - לקרוא ל-order.remove_item
        - להציג "*** Item 'X' removed ***" או "*** Item 'X' not found in order ***"
        
        Args:
            order: ההזמנה להסרה ממנה
        """
        pass
    
    def _print_bill(self, order: Order):
        """
        הדפסת חשבון נוכחי.
        
        דרישות:
        - לנקות מסך
        - להציג את החשבון (order.get_bill)
        - לחכות ל-"Press Enter to go back..."
        
        Args:
            order: ההזמנה להדפסת החשבון שלה
        """
        pass
    
    def _close_order(self):
        """
        סגירת חשבון והזמנה.
        
        דרישות:
        - להציג רשימת הזמנות פעילות
        - אם אין, להציג "*** No active orders ***" ולחזור
        - לבקש "Table number to close: "
        - לחפש הזמנה פעילה לשולחן
        - אם לא נמצאה, להציג "*** No active order for table X ***" ולחזור
        - להציג את החשבון (get_bill)
        - לבקש "Tip percent (default X%): "
        - לבקש אישור "Close order? (y/n): "
        - אם אושר:
            - לסגור את ההזמנה (restaurant.close_order)
            - להציג "*** Order closed. Total: ₪XX.XX ***"
        - אם לא, להציג "*** Closing cancelled ***"
        - לטפל בשגיאות
        """
        pass
