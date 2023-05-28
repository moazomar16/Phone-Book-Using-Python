import sys,os
import re

def addContact(phone_book,index):
  if index == -1:
    print('\n*************************************\n')
    print('Please Select PhoneBook First')
    print('\n*************************************\n')
    #pat = re.compile(r"[0-9]")
    #if re.fullmatch(pat, choice):
  else:
    person = []
    namePat = re.compile(r'[a-zA-Z]+(\s[a-zA-Z]+)?')
    numberPat = re.compile(r'(012|011|010)\d{8}')
    mailPat = re.compile(r'([\w_.])+@([\w]+\.)[\w]{2,4}')
    genderPat = re.compile(r'(?:m|M|male|Male|f|F|female|Female|FEMALE|MALE)')
    
    name = input('Please Enter The Name: ')
    while not re.fullmatch(namePat, name):
      print('Please Enter a Valid Name')
      name = input('Please Enter The Name: ')
      
    
    number = input('Please Enter The Number: ')
    while not re.fullmatch(numberPat, number):
      print('Please Enter a Valid Number')
      number = input('Please Enter The Number: ')
      
      
    mail = input('Please Enter The Mail: ')
    while not re.fullmatch(mailPat, mail):
      print('Please Enter a Valid Mail')
      mail = input('Please Enter The Mail: ')
      
      
    gender = input('Please Enter The Gender: ')
    while not re.fullmatch(genderPat, gender):
      print('Please Enter a Valid Gender')
      gender = input('Please Enter The Gender: ')
      
    
    person.append(number)
    person.append(mail)
    person.append(gender)
    phone_book[index][name] = person
  
  
def showContacts(phone_book,index):
  if index == -1:
    print('\n*************************************\n')
    print('Please Select PhoneBook First')
    print('\n*************************************\n')
    
  else:
    print('\n*************************************\n')
    print('The contacts:')
    print('\n*************************************\n')
    for name in phone_book[index]:
      print('Name: '+name)
      print('Number: '+phone_book[index][name][0])
      print('Mail: '+phone_book[index][name][1])
      print('Gender: '+phone_book[index][name][2]+'\n')

def searchContact(phone_book,index):
  if index == -1:
    print('\n*************************************\n')
    print('Please Select PhoneBook First')
    print('\n*************************************\n')
  else:
    namePat = re.compile(r'[a-zA-Z]+(\s[a-zA-Z]+)?')
    name = input('Enter name you want to search for: ')
    while not re.fullmatch(namePat, name):
      print('Please Enter a Valid Name')
      name = input('Enter name you want to search for: ')
    if name in phone_book[index]:
      print('\n*************************************\n')
      print('The contact you are searching for:')
      print('Name: '+name)
      print('Number: '+phone_book[index][name][0])
      print('Mail: '+phone_book[index][name][1])
      print('Gender: '+phone_book[index][name][2])
      print('\n*************************************\n')
    else:
      print('\n*************************************\n')
      print('Contact not found')
      print('\n*************************************\n')
  
def modifyContact(phone_book,index):
  if index == -1:
    print('\n*************************************\n')
    print('Please Select PhoneBook First')
    print('\n*************************************\n')
  else:
    namePat = re.compile(r'[a-zA-Z]+(\s[a-zA-Z]+)?')
    name = input('Enter name you want to Modify: ')
    while not re.fullmatch(namePat, name):
      print('Please Enter a Valid Name')
      name = input('Enter name you want to Modify: ')
    if name in phone_book[index]:
        print('\n*************************************\n')
        print("1. Edit Name")
        print("2. Edit Number")
        print("3. Edit Mail")
        print("4. Edit Gender")
        pat = re.compile(r"[1-9]")
        choice = int(input('Enter your choice'))
        while not re.fullmatch(pat, choice):
          print('Please Enter a Valid choice')
          choice = int(input('Enter your choice'))
        if choice == 1:
          newName = input('Enter The New Name: ')
          phone_book[index][newName] = phone_book[index][name]
          del phone_book[index][name]
          print('\n*************************************\n')
          print('Modified Successfully')
          print('\n*************************************\n')
        elif choice == 2:
          newNumber = input('Enter The New Number: ')
          phone_book[index][name][0] = newNumber
          print('\n*************************************\n')
          print('Modified Successfully')
          print('\n*************************************\n')
        elif choice == 3:
          newMail = input('Enter The New Mail: ')
          phone_book[index][name][1] = newMail
          print('\n*************************************\n')
          print('Modified Successfully')
          print('\n*************************************\n')
        elif choice == 4:
          newGender = input('Enter The New Gender: ')
          phone_book[index][name][2] = newGender
          print('\n*************************************\n')
          print('Modified Successfully')
          print('\n*************************************\n')
    else:
      print('\n*************************************\n')
      print('Contact not found')
      print('\n*************************************\n')

def deleteContact(phone_book,index):
  if index == -1:
    print('\n*************************************\n')
    print('Please Select PhoneBook First')
    print('\n*************************************\n')
  else:
    namePat = re.compile(r'[a-zA-Z]+(\s[a-zA-Z]+)?')
    name = input('Enter name you want to delete: ')
    while not re.fullmatch(namePat, name):
      print('Please Enter a Valid Name')
      name = input('Enter name you want to delete: ')
    if name in phone_book[index]:
      del phone_book[index][name]
      print('\n*************************************\n')
      print('Contact Deleted Successfully')
      print('\n*************************************\n')
    else:
      print('\n*************************************\n')
      print('Contact not found')
      print('\n*************************************\n')

def deletePhoneBook(phone_book,index):
  if index == -1:
    print('\n*************************************\n')
    print('Please Select PhoneBook First')
    print('\n*************************************\n')
  else:
    del phone_book[index]
    print('\n*************************************\n')
    print('PhoneBook Deleted Successfully')
    print('\n*************************************\n')

def Create_phonebook():
  # We are collecting the initial number of contacts the user wants to have in the
  # phonebook already. User may also enter 0 if he doesn't wish to enter any.
  phone_book = []
  index = -1
  while (True):
    choice = menu()
    pat = re.compile(r"[1-9]")
    if re.fullmatch(pat, choice):
      choice = int(choice)
      #1. Create phone book
      if choice == 1:
        contact = {}
        phone_book.append(contact)
        
      #2. Select phone book
      elif choice == 2:
        indexPat = re.compile(r"[0-9]+")
        index = input('Please The PhoneBook Number: ')
        while not re.fullmatch(indexPat, index):
          print('Please Enter a number')
          index = input('Please The PhoneBook Number: ')
        index = int(index)
        index = index-1
        if index > len(phone_book)+1:
          print('\n*************************************\n')
          print('PhoneBook Number Not Found')
          print('\n*************************************\n')
        
      #3. Add contacts
      elif choice==3:
        addContact(phone_book,index)
        
      #4. Modify contact
      elif choice == 4:
        modifyContact(phone_book,index)
        
      #5. Show contacts
      elif choice == 5:
        showContacts(phone_book,index)
        
      #6. Search contacts
      elif choice == 6:
        searchContact(phone_book,index)
        
      #7. Delete contacts
      elif choice == 7:
        deleteContact(phone_book,index)
        
      #8. Delete Phonebook
      elif choice == 8:
        deletePhoneBook(phone_book,index)
        index = -1
        
      #9. Exit phonebook
      elif choice == 9:
        exit()
        
    else:
      print('\n*************************************\n')
      print("Not Valid Choice")
      print('\n*************************************\n')

def menu():
  # We created this simple menu function for
  # code reusability & also for an interactive console
  # Menu func will only execute when called
  os.system('cls')
  print("1. Create phone book")
  print("2. Select phone book")
  print("3. Add contacts")
  print("4. Modify contact")
  print("5. Show contacts")
  print("6. Search contacts")
  print("7. Delete contacts")
  print("8. Delete Phonebook")
  print("9. Exit phonebook")

  # Out of the provided 6 choices, user needs to enter any 1 choice among the 6
  # We return the entered choice to the calling function wiz main in our case
  choice = input("Please enter your choice: ")
   
  return choice
def main():
  Create_phonebook()
  

if __name__ == '__main__':
  main() 