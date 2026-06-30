# cli/table_manager_cli.py - ניהול שולחנות (ממומש)

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from restaurant import Restaurant


class TableManagerCLI:
    """ניהול שולחנות - הצגת מצב, פתיחה וסגירה"""
    
    def __init__(self, restaurant: Restaurant):
        self._restaurant = restaurant
    
    def run(self):
        """לולאת תת-התפריט"""
        while True:
            self._display_menu()
            choice = input("Choose option: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._show_all_tables()
            elif choice == "2":
                self._show_free_tables()
            elif choice == "3":
                self._show_occupied_tables()
            else:
                print("\n*** Invalid choice ***\n")
                input("Press Enter to continue...")
    
    def _display_menu(self):
        """הצגת אפשרויות ניהול"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("  Table Management")
        print("=" * 50)
        print()
        print("1. Show All Tables")
        print("2. Show Free Tables")
        print("3. Show Occupied Tables")
        print()
        print("0. Back to Main Menu")
        print()
    
    def _show_all_tables(self):
        """הצגת כל השולחנות"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("  All Tables")
        print("=" * 50)
        print()
        
        tables = self._restaurant.get_all_tables()
        if not tables:
            print("No tables in restaurant")
        else:
            for table in tables:
                print(f"  {table}")
        
        print()
        input("Press Enter to go back...")
    
    def _show_free_tables(self):
        """הצגת שולחנות פנויים"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("  Free Tables")
        print("=" * 50)
        print()
        
        tables = self._restaurant.get_free_tables()
        if not tables:
            print("No free tables")
        else:
            for table in tables:
                print(f"  {table}")
        
        print()
        input("Press Enter to go back...")
    
    def _show_occupied_tables(self):
        """הצגת שולחנות תפוסים"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("  Occupied Tables")
        print("=" * 50)
        print()
        
        tables = self._restaurant.get_occupied_tables()
        if not tables:
            print("No occupied tables")
        else:
            for table in tables:
                order = self._restaurant.get_order_by_table(table.number)
                print(f"  {table}")
                if order:
                    print(f"      -> Order #{order.order_id} - {len(order)} items")
        
        print()
        input("Press Enter to go back...")
