# tests.py - Tests for your implementation
# Run this file to check your implementation
# python tests.py

import sys
from idlelib.stackviewer import FrameTreeItem

# Colors for output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

passed = 0
failed = 0


def test(name, condition):
    """Helper function for tests"""
    global passed, failed
    if condition:
        print(f"{GREEN}PASS:{RESET} {name}")
        passed += 1
    else:
        print(f"{RED}FAIL:{RESET} {name}")
        failed += 1


def test_exception(name, exception_type, func):
    """Test that a function raises an exception"""
    global passed, failed
    try:
        func()
        print(f"{RED}FAIL:{RESET} {name} (no exception raised)")
        failed += 1
    except exception_type:
        print(f"{GREEN}PASS:{RESET} {name}")
        passed += 1
    except Exception as e:
        print(f"{RED}FAIL:{RESET} {name} (wrong exception: {type(e).__name__})")
        failed += 1


print("=" * 60)
print("  Restaurant Management System Tests")
print("=" * 60)
print()

# ==========================================
# MenuItem Tests
# ==========================================
print(f"{YELLOW}--- MenuItem Tests ---{RESET}")

try:
    from menu_item import MenuItem, Appetizer, MainCourse, Dessert, Beverage
    
    # Basic item creation
    item = MenuItem("Test", 50, "Description")
    test("MenuItem.__init__ - creation", item.name == "Test" and item.price == 50)
    test("MenuItem.description", item.description == "Description")
    test("MenuItem.get_category", item.get_category() == "General")
    test("MenuItem.format_price", MenuItem.format_price(32.5) == "$32.50")
    test("MenuItem.__str__", "Test" in str(item) and "50" in str(item))
    test("MenuItem.__eq__", MenuItem("a", 10, "") == MenuItem("a", 20, "x"))
    
    # Price validation
    test_exception("MenuItem.price negative", ValueError, lambda: MenuItem("x", -5, ""))
    
    # Price setter
    item.price = 60
    test("MenuItem.price setter", item.price == 60)

except Exception as e:
    print(f"{RED}Error in MenuItem tests: {e}{RESET}")

print()

# ==========================================
# Appetizer Tests
# ==========================================
print(f"{YELLOW}--- Appetizer Tests ---{RESET}")

try:
    # Reset bread inventory
    Appetizer._bread_inventory = {}
    
    Appetizer.add_bread_to_inventory("Pita", 10)
    test("Appetizer.add_bread_to_inventory", Appetizer.get_bread_quantity("Pita") == 10)
    
    Appetizer.add_bread_to_inventory("Pita", 5)
    test("Appetizer add to existing", Appetizer.get_bread_quantity("Pita") == 15)
    
    test("Appetizer.get_available_breads", "Pita" in Appetizer.get_available_breads())
    
    app = Appetizer("Hummus", 30, "")
    test("Appetizer.get_category", app.get_category() == "Appetizers")
    test("Appetizer.selected_bread initial", app.selected_bread is None)
    
    result = app.add_bread("Pita")
    test("Appetizer.add_bread success", result == True and app.selected_bread == "Pita")
    test("Appetizer inventory decreased", Appetizer.get_bread_quantity("Pita") == 14)
    test("Appetizer.get_total_price with bread", app.get_total_price() == 35)
    
    app.remove_bread()
    test("Appetizer.remove_bread", app.selected_bread is None)
    test("Appetizer inventory increased", Appetizer.get_bread_quantity("Pita") == 15)
    
    test("Appetizer.add_bread non-existent", app.add_bread("Baguette") == False)

except Exception as e:
    print(f"{RED}Error in Appetizer tests: {e}{RESET}")

print()

# ==========================================
# MainCourse Tests
# ==========================================
print(f"{YELLOW}--- MainCourse Tests ---{RESET}")

try:
    MainCourse._side_options = []
    
    MainCourse.add_side_option("Rice")
    MainCourse.add_side_option("Fries")
    test("MainCourse.add_side_option", "Rice" in MainCourse.get_side_options())
    
    mc = MainCourse("Schnitzel", 60, "")
    test("MainCourse.get_category", mc.get_category() == "Main Courses")
    
    result = mc.select_side("Rice")
    test("MainCourse.select_side success", result == True and mc.selected_side == "Rice")
    test("MainCourse.select_side non-existent", mc.select_side("Pasta") == False)

except Exception as e:
    print(f"{RED}Error in MainCourse tests: {e}{RESET}")

print()

# ==========================================
# Dessert Tests
# ==========================================
print(f"{YELLOW}--- Dessert Tests ---{RESET}")

try:
    d1 = Dessert("Cake", 40, "", is_sugar_free=False)
    d2 = Dessert("Fruit", 30, "", is_sugar_free=True)
    
    test("Dessert.get_category", d1.get_category() == "Desserts")
    test("Dessert.is_sugar_free False", d1.is_sugar_free == False)
    test("Dessert.is_sugar_free True", d2.is_sugar_free == True)
    test("Dessert.__str__ sugar-free", "sugar free" in str(d2))

except Exception as e:
    print(f"{RED}Error in Dessert tests: {e}{RESET}")

print()

# ==========================================
# Beverage Tests
# ==========================================
print(f"{YELLOW}--- Beverage Tests ---{RESET}")

try:
    b = Beverage("Cola", 10, "", "M", True)
    
    test("Beverage.get_category", b.get_category() == "Beverages")
    test("Beverage.size", b.size == "M")
    test("Beverage.is_cold", b.is_cold == True)
    test("Beverage.get_size_multiplier S", Beverage.get_size_multiplier("S") == 0.8)
    test("Beverage.get_size_multiplier L", Beverage.get_size_multiplier("L") == 1.3)
    test("Beverage.get_total_price M", b.get_total_price() == 10)
    
    b.size = "L"
    test("Beverage.get_total_price L", b.get_total_price() == 13)
    
    test_exception("Beverage.size invalid", ValueError, lambda: setattr(b, 'size', 'XL'))

except Exception as e:
    print(f"{RED}Error in Beverage tests: {e}{RESET}")

print()

# ==========================================
# Table Tests
# ==========================================
print(f"{YELLOW}--- Table Tests ---{RESET}")

try:
    from table import Table
    
    Table.total_tables = 0
    
    t = Table(1, 4)
    test("Table.__init__", t.number == 1 and t.seats == 4)
    test("Table.is_occupied initial", t.is_occupied == False)
    test("Table.total_tables", Table.total_tables == 1)
    
    result = t.occupy()
    test("Table.occupy success", result == True and t.is_occupied == True)
    test("Table.occupy already occupied", t.occupy() == False)
    
    t.free()
    test("Table.free", t.is_occupied == False)

except Exception as e:
    print(f"{RED}Error in Table tests: {e}{RESET}")

print()

# ==========================================
# OrderItem Tests
# ==========================================
print(f"{YELLOW}--- OrderItem Tests ---{RESET}")

try:
    from order_item import OrderItem
    
    item = MenuItem("Test", 25, "")
    oi = OrderItem(item, 2, "Note")
    
    test("OrderItem.__init__", oi.quantity == 2 and oi.notes == "Note")
    test("OrderItem.menu_item", oi.menu_item == item)
    test("OrderItem.subtotal", oi.subtotal == 50)
    
    oi.quantity = 3
    test("OrderItem.quantity setter", oi.quantity == 3 and oi.subtotal == 75)
    
    test_exception("OrderItem.quantity < 1", ValueError, lambda: setattr(oi, 'quantity', 0))

except Exception as e:
    print(f"{RED}Error in OrderItem tests: {e}{RESET}")

print()

# ==========================================
# Order Tests
# ==========================================
print(f"{YELLOW}--- Order Tests ---{RESET}")

try:
    from order import Order
    
    Order._order_counter = 0
    Table.total_tables = 0
    
    t = Table(1, 4)
    o = Order(t)
    
    test("Order.__init__", o.order_id == 1 and o.table == t)
    test("Order.is_closed initial", o.is_closed == False)
    test("Order.__len__ empty", len(o) == 0)
    test("Order.get_total_orders", Order.get_total_orders() == 1)
    
    item1 = MenuItem("Item1", 30, "")
    item2 = MenuItem("Item2", 20, "")
    
    o.add_item(item1, 2)
    test("Order.add_item", len(o) == 1)
    test("Order.get_subtotal", o.get_subtotal() == 60)
    
    o.add_item(item2, 1)
    test("Order.get_subtotal two items", o.get_subtotal() == 80)
    
    total = o.get_total(10)
    test("Order.get_total with tip", total == 88)
    
    o.remove_item(item1)
    test("Order.remove_item", len(o) == 1 and o.get_subtotal() == 20)
    
    t.occupy()
    o.close()
    test("Order.close", o.is_closed == True and t.is_occupied == False)
    
    test_exception("Order.add_item to closed", Exception, lambda: o.add_item(item1, 1))

except Exception as e:
    print(f"{RED}Error in Order tests: {e}{RESET}")

print()

# ==========================================
# Menu Tests
# ==========================================
print(f"{YELLOW}--- Menu Tests ---{RESET}")

try:
    from menu import Menu
    
    m = Menu()
    test("Menu.__init__", len(m) == 0)
    
    item1 = MenuItem("Item1", 30, "")
    item2 = MenuItem("Item2", 20, "")
    
    test("Menu.add_item success", m.add_item(item1) == True)
    test("Menu.add_item duplicate", m.add_item(MenuItem("Item1", 50, "")) == False)
    test("Menu.__len__", len(m) == 1)
    test("Menu.__contains__", "Item1" in m)
    
    m.add_item(item2)
    test("Menu.find_item exists", m.find_item("Item1") == item1)
    test("Menu.find_item not exists", m.find_item("None") is None)
    test("Menu.__getitem__", m["Item1"] == item1)
    
    m.update_price("Item1", 40)
    test("Menu.update_price", m["Item1"].price == 40)
    
    test("Menu.remove_item", m.remove_item("Item1") == True and len(m) == 1)
    
    # Test __iter__
    m.add_item(MenuItem("A", 10, ""))
    count = sum(1 for _ in m)
    test("Menu.__iter__", count == 2)

except Exception as e:
    print(f"{RED}Error in Menu tests: {e}{RESET}")

print()

# ==========================================
# Restaurant Tests
# ==========================================
print(f"{YELLOW}--- Restaurant Tests ---{RESET}")

try:
    from restaurant import Restaurant
    
    Table.total_tables = 0
    Order._order_counter = 0
    
    r = Restaurant("Test")
    test("Restaurant.__init__", r.name == "Test")
    
    t1 = Table(1, 4)
    t2 = Table(2, 6)
    r.add_table(t1)
    r.add_table(t2)
    
    test("Restaurant.get_all_tables", len(r.get_all_tables()) == 2)
    test("Restaurant.get_free_tables", len(r.get_free_tables()) == 2)
    test("Restaurant.get_table", r.get_table(1) == t1)
    
    order = r.open_order(1)
    test("Restaurant.open_order", order is not None)
    test("Restaurant table occupied", len(r.get_free_tables()) == 1)
    test("Restaurant.get_order_by_table", r.get_order_by_table(1) == order)
    
    test_exception("Restaurant.open_order occupied", ValueError, lambda: r.open_order(1))
    test_exception("Restaurant.open_order not exist", ValueError, lambda: r.open_order(99))
    
    item = MenuItem("Item", 100, "")
    r.menu.add_item(item)
    order.add_item(item, 1)
    
    total = r.close_order(order, 10)
    test("Restaurant.close_order", total == 110)
    test("Restaurant.get_total_revenue", r.get_total_revenue() == 110)
    test("Restaurant.get_orders_count", r.get_orders_count() == 1)

except Exception as e:
    print(f"{RED}Error in Restaurant tests: {e}{RESET}")

print()

# ==========================================
# Summary
# ==========================================
print("=" * 60)
total = passed + failed
print(f"  Summary: {passed}/{total} tests passed")
if failed == 0:
    print(f"  {GREEN}Excellent! All tests passed!{RESET}")
else:
    print(f"  {RED}{failed} tests failed - keep working!{RESET}")
print("=" * 60)

sys.exit(0 if failed == 0 else 1)
