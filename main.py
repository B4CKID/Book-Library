import json
library = [

]

def list():
  with open('library.txt', 'r') as f:
    d = read(f)
    print(d)

def read():
  print("It seems you have finished a book, congrats!")
  read = input('What Book Did You Finish Reading?: ')
  pass

def delete():
  print("It seems you are trying to delete a book from your library!")
  delete = input('What Book do you want deleted?: ')
  pass

def quit():
  print('The program will end now!')

def copy():
  with open("library.txt", 'w') as f:
    json.dump(library,f, indent=4)


def add():
  print("It seems you would like to add a book to your library, how exciting!")
  add = input("Please Enter The Book's Name: ")  
  add1 = input("Please Enter The Author's Name: ")
  add2 = input("Have You Finished Reading This Book?: T or F")

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
  while book:
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



book_menu()


