# cli/order_manager_cli.py - ניהול הזמנות (לא ממומש - עליכם להשלים!)

import os
import sys
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
        """
        אתחול מנהל ההזמנות.
        
        Args:
            restaurant: אובייקט המסעדה
        """
        pass
    
    def run(self):
        """
        לולאת תת-התפריט הראשית.
        
        דרישות:
        - להציג תפריט (קריאה ל-_display_menu)
        - לקבל בחירה מהמשתמש
        - לטפל בבחירה:
            "0" -> יציאה מהלולאה (break)
            "1" -> פתיחת הזמנה (_open_new_order)
            "2" -> הצגת הזמנות פעילות (_show_active_orders)
            "3" -> עריכת הזמנה (_manage_order)
            "4" -> סגירת חשבון (_close_order)
            אחרת -> הודעת שגיאה
        - הלולאה רצה עד שהמשתמש בוחר 0
        
        הדפסות צפויות (באנגלית):
        - "Choose option: " לקלט
        - "*** Invalid choice ***" לבחירה לא חוקית
        - "Press Enter to continue..."
        """
        pass
    
    def _display_menu(self):
        """
        הצגת תפריט ניהול הזמנות.
        
        דרישות:
        - לנקות מסך
        - להציג:
            ===== Order Management =====
            1. Open New Order
            2. Show Active Orders
            3. Edit Existing Order
            4. Close Order (Bill)
            0. Back to Main Menu
        """
        pass
    
    def _open_new_order(self):
        """
        פתיחת הזמנה חדשה לשולחן.
        
        דרישות:
        - להציג "Open New Order" ככותרת
        - להציג רשימת שולחנות פנויים
        - אם אין שולחנות פנויים, להציג "*** No free tables ***" ולחזור
        - לבקש "Table number: "
        - לפתוח הזמנה (דרך self._restaurant.open_order)
        - להציג "*** Order #X opened for table Y ***"
        - לשאול "Add items now? (y/n): "
        - אם כן, לקרוא ל-_add_items_loop
        - לטפל בשגיאות (ValueError) ולהציג "*** Error: ... ***"
        """
        pass
    
    def _show_active_orders(self):
        """
        הצגת כל ההזמנות הפעילות.
        
        דרישות:
        - לנקות מסך
        - להציג כותרת "Active Orders"
        - אם אין הזמנות, להציג "No active orders"
        - אחרת, לעבור על כל ההזמנות ולהציג:
            - פרטי ההזמנה (str של Order)
            - "Current total: ₪XX.XX"
        - לחכות ל-"Press Enter to go back..."
        """
        pass
    
    def _manage_order(self):
        """
        עריכת הזמנה קיימת.
        
        דרישות:
        - להציג רשימת הזמנות פעילות
        - אם אין, להציג "*** No active orders ***" ולחזור
        - לבקש "Table number to edit: "
        - לחפש הזמנה פעילה לשולחן (get_order_by_table)
        - אם לא נמצאה, להציג "*** No active order for table X ***"
        - אם נמצאה, לקרוא ל-_edit_order_menu
        """
        pass
    
    def _edit_order_menu(self, order: Order):
        """
        תפריט עריכת הזמנה ספציפית.
        
        דרישות:
        - לולאה שמציגה:
            ===== Edit Order #X (Table Y) =====
            1. Show Order Items
            2. Add Item
            3. Remove Item
            4. Show Current Bill
            0. Back
        - לטפל בכל בחירה:
            "1" -> _show_order_items
            "2" -> _add_item_to_order
            "3" -> _remove_item_from_order
            "4" -> _print_bill
            "0" -> יציאה
        
        Args:
            order: ההזמנה לעריכה
        """
        pass
    
    def _show_order_items(self, order: Order):
        """
        הצגת פריטים בהזמנה.
        
        דרישות:
        - להציג כותרת "Items in Order #X:"
        - אם ריקה, להציג "(Order is empty)"
        - אחרת, להציג כל פריט (str של OrderItem)
        - לחכות ל-"Press Enter to go back..."
        
        Args:
            order: ההזמנה להצגה
        """
        pass
    
    def _add_item_to_order(self, order: Order):
        """
        הוספת פריט להזמנה (wrapper ל-_add_items_loop).
        
        Args:
            order: ההזמנה להוספה אליה
        """
        pass
    
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
