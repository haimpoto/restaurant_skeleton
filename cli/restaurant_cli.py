# cli/restaurant_cli.py - הממשק הראשי (ממומש)

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from restaurant import Restaurant
from menu_item import MenuItem
from cli.menu_manager_cli import MenuManagerCLI
from cli.table_manager_cli import TableManagerCLI
from cli.order_manager_cli import OrderManagerCLI


class RestaurantCLI:
    """המחלקה הראשית - מנהלת את הלולאה הראשית והתפריט הראשי"""
    
    def __init__(self, restaurant: Restaurant):
        self._restaurant = restaurant
        self._menu_manager = MenuManagerCLI(restaurant)
        self._table_manager = TableManagerCLI(restaurant)
        self._order_manager = OrderManagerCLI(restaurant)
        self._running = True
    
    def run(self):
        """הלולאה הראשית"""
        while self._running:
            self._display_main_menu()
            choice = self.get_user_input("Choose option: ")
            self._handle_choice(choice)
    
    def _display_main_menu(self):
        """הצגת התפריט הראשי"""
        self.clear_screen()
        print("=" * 50)
        print(f"  Welcome to {self._restaurant.name} Restaurant")
        print("=" * 50)
        print()
        print("1. Menu Management")
        print("2. Table Management")
        print("3. Order Management")
        print("4. Statistics")
        print()
        print("0. Exit")
        print()
    
    def _handle_choice(self, choice: str):
        """טיפול בבחירת המשתמש"""
        if choice == "1":
            self._menu_manager.run()
        elif choice == "2":
            self._table_manager.run()
        elif choice == "3":
            self._order_manager.run()
        elif choice == "4":
            self._show_statistics()
        elif choice == "0":
            self._exit()
        else:
            self.display_message("Invalid choice, try again")
            self.get_user_input("Press Enter to continue...")
    
    def _show_statistics(self):
        """הצגת סטטיסטיקות (בונוס)"""
        self.clear_screen()
        print("=" * 50)
        print("  Restaurant Statistics")
        print("=" * 50)
        print()
        
        print(f"Total Revenue: {MenuItem.format_price(self._restaurant.get_total_revenue())}")
        print(f"Closed Orders: {self._restaurant.get_orders_count()}")
        
        avg = self._restaurant.get_average_order_value()
        print(f"Average Order Value: {MenuItem.format_price(avg)}")
        
        popular_name, popular_count = self._restaurant.get_most_popular_item()
        if popular_name:
            print(f"Most Popular Item: {popular_name} ({popular_count} orders)")
        
        print()
        print("Revenue by Category:")
        revenue_by_cat = self._restaurant.get_revenue_by_category()
        for category, amount in revenue_by_cat.items():
            print(f"  {category}: {MenuItem.format_price(amount)}")
        
        print()
        self.get_user_input("Press Enter to go back...")
    
    def _exit(self):
        """יציאה מהתוכנית"""
        self.clear_screen()
        print("Thank you for visiting! Goodbye!")
        self._running = False
    
    @staticmethod
    def get_user_input(prompt: str) -> str:
        """קבלת קלט מהמשתמש"""
        return input(prompt).strip()
    
    @staticmethod
    def display_message(msg: str):
        """הצגת הודעה למשתמש"""
        print(f"\n*** {msg} ***\n")
    
    @staticmethod
    def clear_screen():
        """ניקוי המסך"""
        os.system('cls' if os.name == 'nt' else 'clear')
