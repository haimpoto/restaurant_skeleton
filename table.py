class Table:

    total_tables: int = 0

    def __init__(self, number: int, seats: int = 4):
        self.__number = number
        self.__seats = seats
        self.__is_occupied = False
        Table.total_tables += 1
    
    @property
    def number(self) -> int:
        return self.__number

    @property
    def seats(self) -> int:
        return self.__seats

    @property
    def is_occupied(self) -> bool:
        return  self.__is_occupied
    
    def occupy(self) -> bool:
        if self.__is_occupied:
            return False
        self.__is_occupied = True
        return True

    def free(self):
       self.__is_occupied = False

    def __str__(self) -> str:
        if self.__is_occupied:
            return f"Table {self.__number} ({self.__seats} seats) - Occupied"
        return f"Table {self.__number} ({self.__seats} seats) - Free"