import crud as db

def getHorizontalTableLine(numberOfColumns, colWidth):
  formattedString = " ";

  for i in range(colWidth * numberOfColumns + numberOfColumns - 1):
    formattedString += "-"
  formattedString += "\n"
  return formattedString

# Truncates a column value to a max string length appended with "..." and returns it
def truncateColumnValue(columnValue, maxStringLength):
  if maxStringLength <= 3:
    raise Exception("Max string length must be greater than 3 to account for elipses")
  columnValue = str(columnValue)
  if (len(columnValue) > maxStringLength):
    columnValue = columnValue[0:(maxStringLength-3)]+"..."
  return columnValue

# Truncates all row values in a rowData tuple to a max string length appended with "..."
# Returns the row as a tuple containing the truncated values
def truncateRowValues(rowData, maxStringLength):
  returnList = []

  for i in range(len(rowData)):
    returnList.append(truncateColumnValue(rowData[i], maxStringLength))

  return tuple(returnList)

# Takes a tuple containing the field names of the table, and a max string length and column width to format it to
# Returns a string formatted to look like a table heading
def getFormattedTableHeader(headerRowData, maxStringLength, colWidth):
  truncatedRowData = truncateRowValues(headerRowData, maxStringLength)

  formattedString = ""
  formattedString += getHorizontalTableLine(len(truncatedRowData), colWidth)

  for i in range(len(truncatedRowData)):
    formattedString += "|{:^{max}}".format(truncatedRowData[i], max=colWidth)
  formattedString += "|\n"

  formattedString += getHorizontalTableLine(len(truncatedRowData), colWidth)

  return formattedString

# Takes a tuple containing row values of the table, and a max string length and column width to format it to
# Returns a string formatted to look like a table row
def getFormattedTableRow(rowData, maxStringLength, colWidth):
  truncatedRowData = truncateRowValues(rowData, maxStringLength)

  formattedString = ""

  for i in range(len(truncatedRowData)):
    formattedString += "|{:^{max}}".format(truncatedRowData[i], max=colWidth)
  formattedString += "|"

  return formattedString

# Takes header data tuple, a row data list of tuples and a column width
# Returns the data as a string containing the formatted table
def getTableFormatted(headerData, rowDataList, columnWidth):
  if (len(headerData) != len(rowDataList[0])):
    raise Exception("Header data size must match row data size")
  maxStringLength = columnWidth - 4

  formattedString = getFormattedTableHeader(headerData, maxStringLength, columnWidth)
  
  for i in range(len(rowDataList)):
    formattedString += getFormattedTableRow(rowDataList[i], maxStringLength, columnWidth)
    formattedString += "\n"
  formattedString += getHorizontalTableLine(len(headerData), columnWidth)

  return formattedString

if __name__ == "__main__":
  print(getTableFormatted(("Film ID", "Title", "Year", "Rating", "Duration", "Genre"), db.readAll(), 15))