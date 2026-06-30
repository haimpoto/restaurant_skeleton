# cli/menu_manager_cli.py - ניהול תפריט (ממומש)

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from restaurant import Restaurant
from menu_item import MenuItem, Appetizer, MainCourse, Dessert, Beverage


class MenuManagerCLI:
    """ניהול התפריט - הוספה, הסרה, עדכון, וניהול מלאי לחמים"""
    
    def __init__(self, restaurant: Restaurant):
        self._menu = restaurant.menu
    
    def run(self):
        """לולאת תת-התפריט"""
        while True:
            self._display_menu()
            choice = input("Choose option: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                self._show_full_menu()
            elif choice == "2":
                self._show_by_category()
            elif choice == "3":
                self._search_item()
            elif choice == "4":
                self._add_item()
            elif choice == "5":
                self._remove_item()
            elif choice == "6":
                self._update_price()
            elif choice == "7":
                self._manage_bread_inventory()
            else:
                print("\n*** Invalid choice ***\n")
                input("Press Enter to continue...")
    
    def _display_menu(self):
        """הצגת אפשרויות ניהול"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("  Menu Management")
        print("=" * 50)
        print()
        print("1. Show Full Menu")
        print("2. Show by Category")
        print("3. Search Item")
        print("4. Add New Item")
        print("5. Remove Item")
        print("6. Update Price")
        print("7. Manage Bread Inventory")
        print()
        print("0. Back to Main Menu")
        print()
    
    def _show_full_menu(self):
        """הצגת כל פריטי התפריט"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("  Full Menu")
        print("=" * 50)
        print()
        
        if len(self._menu) == 0:
            print("Menu is empty")
        else:
            categories = self._menu.get_all_categories()
            for category in sorted(categories):
                print(f"\n--- {category} ---")
                for item in self._menu.get_by_category(category):
                    print(f"  {item}")
        
        print()
        input("Press Enter to go back...")
    
    def _show_by_category(self):
        """הצגת פריטים לפי קטגוריה"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Choose category:")
        print("1. Appetizers")
        print("2. Main Courses")
        print("3. Desserts")
        print("4. Beverages")
        print()
        
        choice = input("Choice: ").strip()
        
        categories = {
            "1": "Appetizers",
            "2": "Main Courses",
            "3": "Desserts",
            "4": "Beverages"
        }
        
        if choice in categories:
            category = categories[choice]
            items = self._menu.get_by_category(category)
            
            print(f"\n--- {category} ---")
            if not items:
                print("No items in this category")
            else:
                for item in items:
                    print(f"  {item}")
        else:
            print("\n*** Invalid choice ***")
        
        print()
        input("Press Enter to go back...")
    
    def _search_item(self):
        """חיפוש פריט"""
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("Enter item name to search: ").strip()
        
        item = self._menu.find_item(name)
        if item:
            print(f"\nFound: {item}")
            print(f"Category: {item.get_category()}")
            print(f"Description: {item.description}")
        else:
            print("\n*** Item not found ***")
        
        print()
        input("Press Enter to go back...")
    
    def _add_item(self):
        """הוספת פריט חדש"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Add New Item")
        print("-" * 30)
        print()
        print("Choose item type:")
        print("1. Appetizer")
        print("2. Main Course")
        print("3. Dessert")
        print("4. Beverage")
        print()
        
        item_type = input("Choice: ").strip()
        
        name = input("Item name: ").strip()
        if not name:
            print("\n*** Name cannot be empty ***")
            input("Press Enter to go back...")
            return
        
        try:
            price = float(input("Price: ").strip())
        except ValueError:
            print("\n*** Invalid price ***")
            input("Press Enter to go back...")
            return
        
        description = input("Description (optional): ").strip()
        
        try:
            if item_type == "1":
                item = Appetizer(name, price, description)
            elif item_type == "2":
                item = MainCourse(name, price, description)
            elif item_type == "3":
                is_sugar_free = input("Sugar free? (y/n): ").strip().lower() == 'y'
                item = Dessert(name, price, description, is_sugar_free)
            elif item_type == "4":
                print("Size (S/M/L): ", end="")
                size = input().strip().upper()
                if size not in ["S", "M", "L"]:
                    size = "M"
                is_cold = input("Cold? (y/n): ").strip().lower() == 'y'
                item = Beverage(name, price, description, size, is_cold)
            else:
                print("\n*** Invalid type ***")
                input("Press Enter to go back...")
                return
            
            if self._menu.add_item(item):
                print(f"\n*** Item '{name}' added successfully! ***")
            else:
                print(f"\n*** Item '{name}' already exists ***")
        
        except ValueError as e:
            print(f"\n*** Error: {e} ***")
        
        input("Press Enter to go back...")
    
    def _remove_item(self):
        """הסרת פריט"""
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("Enter item name to remove: ").strip()
        
        if self._menu.remove_item(name):
            print(f"\n*** Item '{name}' removed successfully! ***")
        else:
            print(f"\n*** Item '{name}' not found ***")
        
        input("Press Enter to go back...")
    
    def _update_price(self):
        """עדכון מחיר פריט"""
        os.system('cls' if os.name == 'nt' else 'clear')
        name = input("Enter item name to update: ").strip()
        
        item = self._menu.find_item(name)
        if not item:
            print(f"\n*** Item '{name}' not found ***")
            input("Press Enter to go back...")
            return
        
        print(f"Current price: {MenuItem.format_price(item.price)}")
        
        try:
            new_price = float(input("New price: ").strip())
            if self._menu.update_price(name, new_price):
                print(f"\n*** Price updated to {MenuItem.format_price(new_price)} ***")
        except ValueError:
            print("\n*** Invalid price ***")
        
        input("Press Enter to go back...")
    
    def _manage_bread_inventory(self):
        """ניהול מלאי לחמים"""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 50)
            print("  Bread Inventory Management")
            print("=" * 50)
            print()
            
            print("Current inventory:")
            inventory = Appetizer.get_bread_inventory()
            if not inventory:
                print("  (No bread in inventory)")
            else:
                for bread, qty in inventory.items():
                    print(f"  {bread}: {qty} units")
            
            print()
            print("1. Add bread to inventory")
            print("2. Remove bread from inventory")
            print()
            print("0. Back")
            print()
            
            choice = input("Choice: ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                bread_type = input("Bread type: ").strip()
                try:
                    quantity = int(input("Quantity: ").strip())
                    Appetizer.add_bread_to_inventory(bread_type, quantity)
                    print(f"\n*** Added {quantity} units of {bread_type} ***")
                except ValueError:
                    print("\n*** Invalid quantity ***")
                input("Press Enter to continue...")
            
            elif choice == "2":
                bread_type = input("Bread type: ").strip()
                try:
                    quantity = int(input("Quantity to remove: ").strip())
                    if Appetizer.remove_bread_from_inventory(bread_type, quantity):
                        print(f"\n*** Removed {quantity} units of {bread_type} ***")
                    else:
                        print("\n*** Not enough in inventory ***")
                except ValueError:
                    print("\n*** Invalid quantity ***")
                input("Press Enter to continue...")
