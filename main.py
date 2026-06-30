# main.py - Entry point

from restaurant import Restaurant
from table import Table
from menu_item import Appetizer, MainCourse, Dessert, Beverage
from cli.restaurant_cli import RestaurantCLI


def initialize_restaurant() -> Restaurant:
    """Create restaurant with initial data"""
    
    # Create restaurant
    restaurant = Restaurant("Bella Italia")
    
    # === Setup bread inventory ===
    Appetizer.add_bread_to_inventory("White Bread", 20)
    Appetizer.add_bread_to_inventory("Pita", 15)
    Appetizer.add_bread_to_inventory("Focaccia", 10)
    Appetizer.add_bread_to_inventory("Baguette", 8)
    
    # === Setup side options ===
    MainCourse.add_side_option("Rice")
    MainCourse.add_side_option("Fries")
    MainCourse.add_side_option("Mashed Potatoes")
    MainCourse.add_side_option("Green Salad")
    MainCourse.add_side_option("Steamed Vegetables")
    
    # === Add menu items ===
    
    # Appetizers
    restaurant.menu.add_item(Appetizer("Hummus", 12, "Homemade hummus with olive oil"))
    restaurant.menu.add_item(Appetizer("Caesar Salad", 14, "Fresh romaine lettuce"))
    restaurant.menu.add_item(Appetizer("Soup of the Day", 10, "Ask your server"))
    
    # Main Courses
    restaurant.menu.add_item(MainCourse("Grilled Chicken", 24, "Herb marinated chicken breast"))
    restaurant.menu.add_item(MainCourse("Beef Steak", 38, "300g ribeye steak"))
    restaurant.menu.add_item(MainCourse("Fish & Chips", 22, "Beer battered cod"))
    restaurant.menu.add_item(MainCourse("Pasta Bolognese", 18, "Classic meat sauce"))
    
    # Desserts
    restaurant.menu.add_item(Dessert("Chocolate Cake", 12, "Belgian chocolate"))
    restaurant.menu.add_item(Dessert("Fruit Salad", 9, "Seasonal fruits", is_sugar_free=True))
    restaurant.menu.add_item(Dessert("Ice Cream", 8, "3 scoops"))
    
    # Beverages
    restaurant.menu.add_item(Beverage("Cola", 4, "Soft drink", "M", True))
    restaurant.menu.add_item(Beverage("Orange Juice", 5, "Fresh squeezed", "M", True))
    restaurant.menu.add_item(Beverage("Coffee", 4, "Espresso", "S", False))
    restaurant.menu.add_item(Beverage("Beer", 7, "Draft beer", "M", True))
    
    # === Add tables ===
    for i in range(1, 5):
        restaurant.add_table(Table(i, seats=4))
    for i in range(5, 8):
        restaurant.add_table(Table(i, seats=6))
    
    return restaurant


def main():
    """Main function"""
    restaurant = initialize_restaurant()
    cli = RestaurantCLI(restaurant)
    cli.run()


if __name__ == "__main__":
    main()
