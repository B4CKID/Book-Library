import database
import json
library = [

]

def list():
  with open('library.txt', 'r') as file:
    d = json.load(file)
    library.append(d)
    print(library)
  book_menu()
  
def read():
  print("It seems you have finished a book, congrats!")
  read = input('What Book Did You Finish Reading?: ')
  library.append({
        'Name': add,
        'Author': add1,
        'Read': add2
    })
  print('You have added a new book to your library!')
  

def delete():
  print("It seems you are trying to delete a book from your library!")
  delete = input('What Book do you want deleted?: ')
  with open('library.txt', 'r') as d:
    for lines in d:
      if lines == delete:
        d.remove(lines)
              
  book_menu()

def quit():
  print('The program will end now!')
  

def copy():
  with open("library.txt", 'a') as f:
    json.dump(library,f, indent=4)
  

def add():
  print("It seems you would like to add a book to your library, how exciting!")
  add = input("Please Enter The Book's Name: ")  
  add1 = input("Please Enter The Author's Name: ")
  add2 = False

  library.append({
        'Name': add,
        'Author': add1,
        'Read': add2 
    })
  print('You have added a new book to your library!')
  copy()
  book_menu()



def book_menu():
  book = input("Please Choose an Option: A(Add A Book to Library) - R(Mark A Book As Now Read) - D(Delete A Book From Library) Q(Quit APP) ")
  while book != 'q':
    if book == 'a':
      add()

    elif book == 'a':
      read()

    elif book  == 'd':
      delete()

    elif book == 'l':
      list()
      
    elif book == 'q':
      quit()
    else:
      print("This is not a valid command")
      book_menu()

book_menu()
copy()