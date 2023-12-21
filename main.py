import crud as db, helpers, formatters

def viewFoodItemsMenu():
  menuOptions = {
    0: "Return to main menu",
    1: "View all items",
    2: "View first item",
    3: "View last item"
  }
  menuTitle = "VIEWING FOOD MENU"
  headerData = ("Id", "Item", "Price", "Type")
  columnWidth = 30

  while True:
    choice = helpers.getMenuInput(menuOptions, menuTitle)

    match choice:
      case 0:
        return
      case 1:
        print(formatters.getTableFormatted(headerData, db.readMenu(), columnWidth))
      case 2:
        print(formatters.getTableFormatted(headerData, db.readFirstRecord(), columnWidth))
      case 3:
        print(formatters.getTableFormatted(headerData, db.readLastRecord(), columnWidth))
      case _:
        print("Something failed")

def addFoodItemMenu():
  menuOptions = {
    0: "Return to main menu",
    1: "Add an item"
  }
  menuTitle = "ADDING A FOOD ITEM"

  while True:
    choice = helpers.getMenuInput(menuOptions, menuTitle)

    match choice:
      case 0:
        return
      case 1:
        try:
          itemName = str(input("Enter item name: "))
          itemPrice = int(input("Enter the item price (in pence): "))
          itemType = str(input("Enter the item type: "))

          if itemPrice <= 0:
            raise Exception("Item price must be above 0")
          
          db.addItem(itemName, itemPrice, itemType)

        except Exception as e:
            print("\nInput is not in correct format, please try again")
            print(e)
      case _:
        print("Something failed")

def deleteFoodItemMenu():
  menuOptions = {
    0: "Return to main menu",
    1: "Delete an item"
  }
  menuTitle = "DELETING A FOOD ITEM"

  while True:
    choice = helpers.getMenuInput(menuOptions, menuTitle)

    match choice:
      case 0:
        return
      case 1:
        try:
          itemId = int(input("Enter id of item to delete: "))
          db.deleteItem(itemId)
        except Exception as e:
            print("\nInput is not in correct format, please try again")
            print(e)
      case _:
        print("Something failed")

def updateFoodItemMenu():
  menuOptions = {
    0: "Return to main menu",
    1: "Update an item"
  }
  itemFields = {
    1: "name",
    2: "price",
    3: "type"
  }
  menuTitle = "UPDATE A FOOD ITEM"
  subMenuTitle = "SELECTING AN ITEM FIELD"

  while True:
    choice = helpers.getMenuInput(menuOptions, menuTitle)

    match choice:
      case 0:
        return
      case 1:
        fieldChoice = helpers.getMenuInput(itemFields, subMenuTitle)
        try:
          itemId = int(input("Enter item ID: "))
          match fieldChoice:
            case 1:
              newValue = str(input("Enter new item name: "))
            case 2:
              newValue = int(input("Enter new item name: "))
              if newValue <= 0:
                raise Exception("Item price must be above 0")
            case 3:
              newValue = str(input("Enter new item name: "))
            case _:
              print("Something failed")

          db.updateItem(itemId, itemFields[fieldChoice], newValue)
        except Exception as e:
            print("\nInput is not in correct format, please try again")
            print(e)
      case _:
        print("Something failed")

def mainProgram():
  menuOptions = {
    0: "Exit",
    1: "View Items",
    2: "Add Items",
    3: "Update Items",
    4: "Delete Items"
  }
  menuTitle = "Main Menu - Abed's PFC"

  print("\nWelcome to Abed's PFC, what would you like to do today?")

  while True:
    choice = helpers.getMenuInput(menuOptions, menuTitle)

    match choice:
      case 0:
        return
      case 1:
        viewFoodItemsMenu()
      case 2:
        addFoodItemMenu()
      case 3:
        updateFoodItemMenu()
      case 4:
        deleteFoodItemMenu()
      case _:
        print("Something failed")

if __name__ == "__main__":
  mainProgram()
  exit()