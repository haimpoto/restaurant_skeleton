from typing import Any

from menu_item import MenuItem, Appetizer, MainCourse, Dessert, Beverage


class Menu:

    def __init__(self):
        self.__items = []
    
    @property
    def items(self) -> list:
        return self.__items.copy()

    
    def add_item(self, item: MenuItem) -> bool:
        for i in range(len(self.__items)):
            if item.name == self.__items[i].name:
                return False
        self.__items.append(item)
        return True
    
    def remove_item(self, name: str) -> bool:
        for i in range(len(self.__items)):
            if name == self.__items[i].name:
                self.__items.pop(i)
                return True
        return False
    
    def find_item(self, name: str) -> MenuItem | None:
        for i in range(len(self.items)):
            if name == self.items[i].name:
                return self.__items[i]
        return None
    
    def update_price(self, name: str, new_price: float) -> bool:
        for i in range(len(self.items)):
            if name == self.items[i].name:
                self.items[i].price = new_price
                return True
        return False
    
    def get_by_category(self, category: str) -> list:
        lst = []
        for i in range(len(self.items)):
            if self.items[i].get_category() == category:
                lst.append(self.items[i])
        return lst
    
    def get_all_categories(self) -> list:
        set_of_cat = set()
        for i in range(len(self.items)):
            set_of_cat.add(self.items[i].get_category())
        return list(set_of_cat)
    
    def get_items_in_price_range(self, min_price: float, max_price: float) -> list:
        lst = []
        for i in range(len(self.items)):
            if min_price <= self.items[i].price <= max_price:
                lst.append(self.items[i])
        return lst
    
    @classmethod
    def from_file(cls, filename: str) -> 'Menu':
        """
        יצירת תפריט מקובץ טקסט.
        
        פורמט הקובץ (כל שורה):
            type,name,price,description
        
        סוגים: "Appetizer", "MainCourse", "Dessert", "Beverage"
        
        דרישות:
        - לדלג על שורות ריקות או שמתחילות ב-#
        - ליצור את הפריט המתאים לפי הסוג
        - להוסיף לתפריט
        - אם הקובץ לא נמצא, להדפיס "File {filename} not found" ולהחזיר תפריט ריק
        
        Returns:
            אובייקט Menu חדש
        """
        pass
    
    def __len__(self) -> int:
        return len(self.items)
    
    def __contains__(self, name: str) -> bool:
        for i in range(len(self.items)):
            if name == self.items[i].name:
                return True
        return False
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, name: str) -> MenuItem:
        for i in range(len(self.items)):
            if name == self.items[i].name:
                return self.items[i]
        raise KeyError(f"Item '{name}' not found in menu")