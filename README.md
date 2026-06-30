# Restaurant Management System - Final Project

## Project Description

In this project you will implement a restaurant management system in Python, using Object-Oriented Programming (OOP) principles.

## What You Get

- **Code Skeleton** - All classes defined with method signatures and documentation
- **Working CLI** - Except for Order Management
- **Test File** - To verify your implementation

## What You Need to Implement

### Part A: Model Classes
All files contain only skeletons - you need to implement the body of each method:

| File | Classes |
|------|---------|
| `menu_item.py` | MenuItem, Appetizer, MainCourse, Dessert, Beverage |
| `table.py` | Table |
| `order_item.py` | OrderItem |
| `order.py` | Order |
| `menu.py` | Menu |
| `restaurant.py` | Restaurant |

### Part B: Order Management CLI
The file `cli/order_manager_cli.py` contains only a skeleton - you need to implement it.

## How to Work

### Step 1: Read the Documentation
Each method contains a docstring explaining exactly what to do.

### Step 2: Implement One Method at a Time
Start with simple classes (Table, MenuItem) and progress to complex ones.

### Step 3: Test Yourself
Run the tests after implementing a few methods:

```bash
python tests.py
```

### Step 4: Try Running
```bash
python main.py
```

## Tips

1. **Read Existing Code** - The implemented CLI shows how to use the classes

2. **Start Simple** - Recommended order:
   - MenuItem (base)
   - Table
   - Appetizer, MainCourse, Dessert, Beverage
   - OrderItem
   - Menu
   - Order
   - Restaurant
   - OrderManagerCLI

3. **Mind Inheritance** - Appetizer, MainCourse, etc. inherit from MenuItem

4. **Mind Class Variables** - `_bread_inventory`, `_order_counter`, etc. are shared across all instances

5. **Test Often** - Don't wait until the end

## OOP Requirements

Make sure you use:

- [x] Inheritance
- [x] Composition
- [x] Private fields
- [x] Properties (getter/setter)
- [x] Magic methods (__str__, __len__, __eq__, __contains__, __iter__, __getitem__)
- [x] Class variables
- [x] Class methods (@classmethod)
- [x] Static methods (@staticmethod)

## Good Luck!
