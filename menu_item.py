# menu_item.py - מחלקת פריט תפריט ותתי-מחלקות


class MenuItem:


    def __init__(self, name: str, price: float, description: str = ""):
        self.__name = name
        self.price = price
        self.__description = description
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def price(self) -> float:
        return self.__price
    
    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Price cannot be negative")
        self.__price = value
    
    @property
    def description(self) -> str:
        return self.__description
    
    @description.setter
    def description(self, value: str):
        self.__description = value

    def get_category(self) -> str:
        return "General"

    @staticmethod
    def format_price(price: float) -> str:
        return f"${price:.2f}"

    def __str__(self) -> str:
        return f"{self.name} - {MenuItem.format_price(self.price)}"
    
    def __repr__(self) -> str:
       return f"MenuItem(name={self.name}, price={self.price}, description={self.description})"

    def __eq__(self, other) -> bool:
        if isinstance(other, MenuItem):
            return self.name == other.name
        return False



class Appetizer(MenuItem):
    __bread_inventory: dict = {}
    BREAD_PRICE: float = 5.0
    
    def __init__(self, name: str, price: float, description: str = ""):
        super().__init__(name, price, description)
        self.__selected_bread = None
    
    @property
    def selected_bread(self) -> str:
        return self.__selected_bread
    
    def add_bread(self, bread_type: str) -> bool:
        if self.selected_bread is not None:
            return False
        if bread_type not in Appetizer.__bread_inventory:
            return False
        if Appetizer.__bread_inventory[bread_type] < 1:
            return False
        self.__selected_bread = bread_type
        Appetizer.__bread_inventory[bread_type] -= 1
        return True
    
    def remove_bread(self):
        if self.selected_bread is not None:
            Appetizer.__bread_inventory[self.selected_bread] += 1
            self.__selected_bread = None

    def get_total_price(self) -> float:
        if self.selected_bread is not None:
            return self.price + Appetizer.BREAD_PRICE
        return self.price
    
    def get_category(self) -> str:
        return "Appetizers"
    
    @classmethod
    def get_available_breads(cls) -> list:
        bread_list = []
        for bread in cls.__bread_inventory:
            if cls.__bread_inventory[bread] > 0:
                bread_list.append(bread)
        return bread_list
    
    @classmethod
    def add_bread_to_inventory(cls, bread_type: str, quantity: int):
        if bread_type in cls.__bread_inventory:
            cls.__bread_inventory[bread_type] += quantity
        else:
            cls.__bread_inventory[bread_type] = quantity
    
    @classmethod
    def remove_bread_from_inventory(cls, bread_type: str, quantity: int) -> bool:
        if quantity < cls.__bread_inventory[bread_type]:
            cls.__bread_inventory[bread_type] -= quantity
            return True
        return False

    @classmethod
    def get_bread_quantity(cls, bread_type: str) -> int:
        if bread_type in cls.__bread_inventory:
            return cls.__bread_inventory[bread_type]
        return 0
    
    @classmethod
    def get_bread_inventory(cls) -> dict:
        return cls.__bread_inventory.copy()

    def __str__(self) -> str:
        if self.__selected_bread is None:
            return f"{self.name} - {self.format_price(self.price)}"
        return f"{self.name} - {self.format_price(self.price)} + bread {self.format_price(Appetizer.BREAD_PRICE)}"


class MainCourse(MenuItem):
    __side_options: list = []
    
    def __init__(self, name: str, price: float, description: str = ""):
        super().__init__(name, price, description)
        self.__selected_side = None
    
    @property
    def selected_side(self) -> str:
       return self.__selected_side

    def select_side(self, side: str) -> bool:
        if side not in MainCourse.__side_options:
            return False
        self.__selected_side = side
        return True
    
    def get_category(self) -> str:
         return "Main Courses"
    
    @classmethod
    def get_side_options(cls) -> list:
        return cls.__side_options.copy()

    @classmethod
    def add_side_option(cls, side: str):
        if side not in cls.__side_options:
            cls.__side_options.append(side)
    
    @classmethod
    def remove_side_option(cls, side: str):
        if side not in cls.__side_options:
            cls.__side_options.remove(side)

    def __str__(self) -> str:
        if self.__selected_side is None:
            return f"{self.name} - {self.format_price(self.price)}"
        return f"{self.name} - {self.format_price(self.price)} (with {self.__selected_side})"



class Dessert(MenuItem):
    def __init__(self, name: str, price: float, description: str = "", is_sugar_free: bool = False):
        super().__init__(name, price, description)
        self.__is_sugar_free = is_sugar_free
    
    @property
    def is_sugar_free(self) -> bool:
        return self.__is_sugar_free
    
    def get_category(self) -> str:
        return "Desserts"

    def __str__(self) -> str:
        if not self.is_sugar_free:
            return f"{self.name} - {self.format_price(self.price)}"
        return f"{self.name} - {self.format_price(self.price)} - (sugar free)"


class Beverage(MenuItem):

    SIZES = ["S", "M", "L"]

    def __init__(self, name: str, price: float, description: str = "", size: str = "M", is_cold: bool = True):
        super().__init__(name, price, description)
        self.size = size
        self.__is_cold = is_cold
    
    @property
    def size(self) -> str:
        return self.__size
    
    @size.setter
    def size(self, value: str):
        if value not in Beverage.SIZES:
            raise ValueError("Size must be one of: ['S', 'M', 'L']")
        self.__size = value
    
    @property
    def is_cold(self) -> bool:
        return self.__is_cold
    
    def get_category(self) -> str:
         return "Beverages"

    @staticmethod
    def get_size_multiplier(size: str) -> float | None:
        if size == "S":
            return 0.8
        if size == "M":
            return 1.0
        if size == "L":
            return 1.3
        return None

    def get_total_price(self) -> float:
        return self.price * self.get_size_multiplier(self.size)
    
    def __str__(self) -> str:
        if self.is_cold:
            return f"{self.name} ({self.size} cold) - {self.format_price(self.price)}"
        return f"{self.name} ({self.size} hot) - {self.format_price(self.price)}"
