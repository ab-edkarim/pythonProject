from connect import *

c.execute("""INSERT INTO menuItems(name, price, type) VALUES
          ("Lamb Donner", 699, "Kebab"),
          ("Chicken Donner", 599, "Kebab"),
          ("Chicken & Chips", 199, "Chicken"),
          ("Chicken Burger Meal", 499, "Burger")
          """)

conn.commit()
