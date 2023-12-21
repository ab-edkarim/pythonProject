from connect import *

def readMenu():
  c.execute("SELECT * FROM menuItems")

  return c.fetchall()

def readFirstRecord():
  c.execute("SELECT * FROM menuItems LIMIT 1")

  return c.fetchall()

def readLastRecord():
  c.execute("SELECT * FROM menuItems ORDER BY id DESC LIMIT 1")

  return c.fetchall()

def addItem(itemName, itemPrice, itemType):
  c.execute("INSERT INTO menuItems(name, price, type) VALUES(?, ?, ?)", (itemName, itemPrice, itemType))
  conn.commit()

def updateItem(itemId, fieldName, fieldValue):
  fieldName = fieldName.lower()
  if (fieldName == 'name'):
    query = "UPDATE menuItems SET name = ? WHERE id = ?"
  elif (fieldName == 'price'):
    query = "UPDATE menuItems SET price = ? WHERE id = ?"
  elif (fieldName == 'type'):
    query = "UPDATE menuItems SET type = ? WHERE id = ?"
  else:
    raise Exception("Field name given does not match any in the database table")
  
  c.execute(query, (fieldValue, itemId))
  conn.commit()

def deleteItem(itemId):
  c.execute("DELETE FROM menuItems WHERE id=?", (itemId,))
  conn.commit()

if __name__ == "__main__":
  updateItem(3, "Price", 99)