from menu_item import MenuItem, Appetizer, Beverage


class OrderItem:
    
    def __init__(self, menu_item: MenuItem, quantity: int = 1, notes: str = ""):
        self.__menu_item = menu_item
        self.quantity = quantity
        self.__notes = notes

    @property
    def menu_item(self) -> MenuItem:
        return self.__menu_item
    
    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value: int):
        if value < 1:
            raise ValueError("Quantity must be at least 1")
        self.__quantity = value
    
    @property
    def notes(self) -> str:
        return self.__notes

    @notes.setter
    def notes(self, value: str):
        self.__notes = value

    @property
    def subtotal(self) -> float:
        if isinstance(self.__menu_item, Appetizer):
            return Appetizer.get_total_price(self.__menu_item) * self.__quantity
        if isinstance(self.__menu_item, Beverage):
            return Beverage.get_total_price(self.__menu_item) * self.__quantity
        return self.__menu_item.price * self.__quantity
    
    def __str__(self) -> str:
        return f"{self.__menu_item} * {self.__quantity} = ${self.subtotal}"
