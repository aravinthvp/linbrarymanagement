
class Library:
    
    def __init__(self,listofbooks):
        
        self.availablebooks = listofbooks

    def displayavailablebooks(self):
        
        print()
        print("Available Books:")
        for book in self.availablebooks:
            print(book)
            
    def lendbook(self,requestedbook):
        if requestedbook in self.availablebooks:
            print("you have now barrowed the book")
            self.availablebooks.remove(requestedbook)
        else:
            print("sorry book is not available")
    def addbook(self, returnbook):
        self.availablebooks.append(returnbook)
        print("you have returned the book .thank u!")
        
class Customer:
    
    def requestbook(self):
        print("Enter the name of a book you would like to barroow")
        self.book =input()
        return self.book
    def returnbook(self):
        print("Enter the book name")
        self.book =input()
        return self.book
    
    
library = Library(['Ramaayanam','Thirukkural','Mahabaratham','Ponniyin selvan','silappathikaaram'])
customer = Customer()
while True:
    print("Enter  1 to display the available books")
    print("Enter  2 to request for a book")
    print("Enter 3 to retunr the book")
    print("Enter 4 to exit")
    usechoice = int(input())
    if usechoice is 1:
        library.displayavailablebooks()
    elif usechoice is 2:
        requestedbook =customer.requestbook()
        library.lendbook(requestedbook)
    elif usechoice is 3:
        returnbook = customer.returnbook()
        library.addbook(returnbook)
    elif usechoice is 4:
        quit()
