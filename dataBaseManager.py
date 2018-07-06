"""
Author: Michael Tekin, michael.tekin@uky.edu, CS115-009
Assignment: Program 4 (Simple Database)
Purpose: simple database manager
Preconditions: no parameters, user gives a menu choice
Postconditions: N/A
Date completed: 9th Dec, 2015
"""

#Bonus complete, starting on line 234

def main():
  """
  Purpose: get a menu choice from the user and use that choice to determine
  which function to run or to close the program
  Preconditions: no parameters, user gives a menu choice
  Postconditions: the appropriate function is called (or the program is closed)
  """
  
  databaselist = []

  #Display the main menu and get the users menu choice
  choice = get_menu_choice()
  
  #While the choice isn't to close the program
  while choice != 9:
    #If the choice is to load
    if choice == 1:
      databaselist = load()
    #Else if the choice is to save
    elif choice == 2:
      save(databaselist)
    #Else if the choice is to query
    elif choice == 3:
      query(databaselist)
    #Else if the choice is to display the database
    elif choice == 4:
      #Print submenu title and number of records here because display_db is
      #called by other functions
      print('Database Report')
      display_db(databaselist, False)
      print('{} records'.format(len(databaselist)))
    #Else if the choice is to sort
    elif choice == 5:
      sort_db(databaselist)
    #Else if the choice is to enter a new item
    elif choice == 6:
      get_new_entry(databaselist)
    #Else if the choice is to remove item
    elif choice == 7:
      #Check to see if the database list is empty to keep the user from getting
      #stuck in an input validation loop
      if len(databaselist) > 0:
        remove_data(databaselist)
      else:
        print('Empty database; no records to remove')
    #Otherwise
    else:   
      if len(databaselist) > 0:
        change_status(databaselist)
      else:
        print('Empty database; no records to change')
      
    input('\nPress Enter\n')
    
    choice = get_menu_choice()


def load():
  """
  Purpose: turn a sequence of records into a list of records
  Preconditions: no parameters, user gives a filename
  Postconditions: returns the database
  """

  print('Loading a database file\n')
  print('Filename will have a .db extension added, do not enter it')
  filename = input('Enter a filename: ') + '.db'
  
  valid_name = False
  while not valid_name:
    #Try opening the file  
    try:
      file = open(filename, 'r')
      valid_name = True
    #If the file won't open ask for another one
    except IOError:
      print('Error, file would not open')
      filename = input('Enter a filename: ') + '.db'
    
  #Read the data from the file, creating a database list
  databaselist = []  
  for line in file.readlines():
    line = line.strip().split(',')
    databaselist.append(line)
  file.close()
  print('Database loaded')
  
  return databaselist


def save(databaselist):
  """
  Purpose: write a list of records to a database file
  Preconditions: the database list
  Postconditions: N/A
  """

  print('Saving a database file\n')
  print('Filename will have a .db extension added, do not enter it')
  filename = input('Enter a filename: ') + '.db'
  
  #if the file already exists, open the file for writing only after verifying
  #the user wishes to overwrite the file
  try:
    #Check if the file exists
    fileobj = open(filename, 'r')
    fileobj.close()
    
    #If the file exists check if the user wants to overwrite
    if verifyYN('{} already exists. Overwrite {}? '.format(filename,
                                                           filename)) == 'y':
      fileobj = open(filename, 'w')
      for record in range(len(databaselist)):
        #Writes each record in the database list to the file on its own line as
        #a set of fields seperated by commas (no brackets or quotes)        
        print(','.join(databaselist[record]), file=fileobj)
      print('\nFile saved')
    else:
      print('\nFile not saved')
  #If the file does not already exist, create the file and save the database
  except IOError:
    fileobj = open(filename, 'w')
    for record in range(len(databaselist)):      
      print(','.join(databaselist[record]), file=fileobj)
    print('\nFile saved')


def change_status(databaselist):
  """
  Purpose: change the location and IN/OUT status of a database record
  Preconditions: the database list
  Postconditions: N/A
  """

  print("Change an item's status")
  
  #Displays all the records in the database with record numbers
  display_db(databaselist, True)
  
  #Get the user to choose a record accounting for the fact that the user sees 
  #record numbers starting at 1
  record_choice = int(input('Which record? ')) - 1
  while not 0 <= record_choice <= len(databaselist) - 1:
    print('Invalid choice')
    record_choice = int(input('Which record? ')) - 1
  
  #Create a copy of the record so that the actual record is only changed after
  #verifying the user wants to make the change
  record_copy = databaselist[record_choice][:]
  
  if record_copy[2].lower() == 'in':
    record_copy[2] = 'OUT'
  else:
    record_copy[2] = 'IN'
  
  #Ask the user for the new location and replace the commas with spaces
  record_copy[3] = input('New location? ').replace(',', ' ')
  
  #Display the copy with the changes
  displayRecord(record_copy, 25)
  
  #If the user confirms they want to change the status
  if verifyYN('Do you want to make the change? ') == 'y':
    #Replace the original record with the copy
    databaselist[record_choice] = record_copy  
    print('Status and location changed')
  else:
    print('Status and location not changed')


def remove_data(databaselist):
  """
  Purpose: remove a record from a database
  Preconditions: the database list
  Postconditions: N/A
  """

  print('Remove a record')
  
  #Display all the records in the database with record numbers
  display_db(databaselist, True)
  
  #Get the user to choose a record
  record_choice = int(input('Which record? ')) - 1
  while not 0 <= record_choice <= len(databaselist) - 1:
    print('Invalid choice')
    record_choice = int(input('Which record? ')) - 1
  
  print()
  #Display the chosen record
  displayRecord(databaselist[record_choice], 25)
  
  #If the user confirms they want to remove the record
  if verifyYN('\nDo you want to delete this record? ') == 'y':
    #Remove that record from the database list
    del databaselist[record_choice]
    print('\nRecord removed')
  else:
    print('\nRecord not removed')


def query(databaselist):
  """
  Purpose: find and report the records containing a given field value
  Preconditions: the database list, inputs from the user are a field choice and
  a value choice. The value search is case sensitive
  Postconditions: N/A
  """

  print('Querying the Database\n')
  print('Which field to query?')
  
  #Display the valid fields following their respective field numbers and get a
  #choice from the user
  fieldchoice = get_field_choice()
  valuechoice = input('\nWhat value to look for? ')
  
  print()
  #Search the database list for the value in the given field
  matches = 0
  for i in range(len(databaselist)):
    #If a match is found then
    #BONUS# Use if in instead of if ==, in order to search for substrings
    if valuechoice in databaselist[i][fieldchoice]:
      #Report that record
      displayRecord(databaselist[i], 25)
      matches += 1
  
  #Report the number of matching record, if any
  print('\n{} records found'.format(matches))


def sort_db(databaselist):
  """
  Purpose: sort records in a database using values from a given field
  Preconditions: the database list
  Postconditions: N/A
  """

  print('Sorting the Database')
  
  #Display the valid fields and their respective field numbers
  #Ask the user which field to sort by
  fieldchoice = get_field_choice()
  order = input('Ascending(A) or Descending(D)? ')
  
  #If the user confirms they want to sort the database then
  if verifyYN('Are you sure you want to sort the database? ') == 'y':
    #Sort the database
    for pos in range(len(databaselist) - 1):
      sliced = databaselist[pos:]
      minloc = find_min(sliced, fieldchoice) + pos
      (databaselist[pos], databaselist[minloc]) = (databaselist[minloc],
                                                   databaselist[pos])
    #Adjust for the given direction (Ascending or Descending)
    if order.lower() == 'd':
      reverse(databaselist)
    print('Database sorted')
  else:
    print('Database not sorted')
    

def get_new_entry(databaselist):
  """
  Purpose: add a record to a database
  Preconditions: the database list
  Postconditions: N/A
  """

  print('Create new record\n')
  
  newrecord = []
  newrecord.append(input('Item name? '))
  newrecord.append(input('Date bought (YYYY/MM/DD) ? '))
  status = input('Status (IN/OUT)? ')
  while status.lower() != 'in' and status.lower() != 'out':
    print('Invalid response')
    status = input('Status (IN/OUT)? ')
  newrecord.append(status)
  newrecord.append(input('Location? '))
  
  for field in range(len(newrecord)):
    newrecord[field] = newrecord[field].replace(',', ' ')
    
  #Use the users given values to display a record
  displayRecord(newrecord, 25)
  
  #If the user confirms they want to add the record
  if verifyYN('\nDo you want to add this record (y/n)? ') == 'y':
    #Add the record to the end of the database list
    databaselist.append(newrecord)
    print('\nRecord added')
  else:
    print('\nRecord not added')


def display_db(databaselist, flag):
  """
  Purpose: display all the records in a database
  Preconditions: the database list, the flag for show numbers
  Postconditions: N/A
  """
  
  #No submenu title in function because it's called in other functions
  #Submenu title in main function
  print()
  
  #Put record labels into a list so that they can be displayed with
  #displayRecord function, ensuring correct alignment
  header = ['Name', 'Date Purchased', 'Status', 'Location']
  #Leave enough space before name for record number column
  print('   ', end='')
  displayRecord(header, 25)
  
  #Display each record in the database list on its own line, in a column under
  #the appropriate header  
  for i in range(len(databaselist)):
    #If the flag is set to True then
    if flag:
      #Add record numbers
      nums = str(i+1) + '. '
    #Otherwise
    else:
      #Add empty column where record numbers would be
      nums = '   '
    print(nums, end='')
    displayRecord(databaselist[i], 25)
                                  
  #Report the number of records in the database list in the main function
  #instead of here because this function is used by other functions
  print()
  

#Utility Functions


def get_menu_choice():
  """
  Purpose: take the user to the main menu and allow them to choose what they
  would like to do next
  Preconditions: no parameters, user gives a menu choice
  Postconditions: returns choice as a single character string
  """

  print('Main Menu\n')
  print('1. Load database\n'
        '2. Save (close) database\n'
        '3. Query (search)\n'
        '4. Display database\n'
        '5. Sort\n'
        '6. Enter new item\n'
        '7. Remove item\n'
        '8. Change status and location of item\n'
        '9. Exit\n')
  
  #Get an item choice from the user
  #Try typecasting to integer so that an invalid choice such as '10' isn't
  #accepted because it's between '1' and '9'
  try:
    choice = int(input('Choose item from menu: '))
    while not (1 <= choice <= 9):
      print('Invalid choice')
      choice = int(input('Choose item from menu: '))
  except ValueError:
    print('Invalid choice')
    choice = int(input('Choose item from menu: '))    
  print()
  return choice


def get_field_choice():
  """
  Purpose: get a valid record field choice from the user
  Preconditions: no parameters, user gives a field choice
  Postconditions: returns choice as a single character string
  """

  #Get a valid field choice from the user
  print('1. Name\n2. Date\n3. Status\n4. Location')
  user_choice = int(input('Choose a field (1-4): '))
  while user_choice not in [1,2,3,4]:
    print('Invalid choice')
    user_choice = int(input('Choose a field (1-4): '))
  #Return the users choice accounting for the fact that the user sees field
  #choices starting at 1 rather than 0
  return user_choice - 1


def find_min(databaselist, field):
  """
  Purpose: get the smallest value in the database list for a given field
  Preconditions: the database list, the field choice
  Postconditions: returns the smallest value in the database list for the field
  chosen
  """
  
  small = 0
  for i in range(len(databaselist)):
    if databaselist[i][field] < databaselist[small][field]:
      small = i

  #Return the position of the smallest value in the database list for the chosen
  #field
  return small


def verifyYN(prompt):
  """
  Purpose: verify a users choice with a yes or no question
  Preconditions: a prompt that is a string
  Postconditions: returns choice as a single character string, 'Y' or 'N'
  """

  #Display the prompt and get a 'y' or 'n' from the user
  user_choice = input(prompt).lower()
  while user_choice != 'y' and user_choice != 'n':
    print('Invalid response')
    user_choice = input(prompt)

  return user_choice


def displayRecord(record, col):
  """
  Purpose: display a record using a given number of columns
  Preconditions: record to be displayed, column width to use
  Postconditions: N/A
  """
  
  #Display the record using the given number of columns
  for i in range(len(record)):
    field = record[i] + (' ' * col)
    print(field[:col], end='')
  
  print() 


main()