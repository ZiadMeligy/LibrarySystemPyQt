import json

class Book:

    def __init__(self, title=None, author=None, isbn=None, cost=None, section= None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.section = section
       
        try:
            self.cost = int(cost)
        except:
            raise ValueError("Cost must be an integer, Please try again!")

    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getCost(self):
        return self.cost
    
    def getISBN(self):
        return self.isbn
    
    def getInfo(self):
        return f'This book is {self.title} made by {self.author}'

    def getSection(self):
        return self.section    






class Section:
    def __init__(self,title):
        self.title = title
        self.books= []

    def getTitle(self):
        return self.title

    def addBook(self,book):
        if isinstance(book,Book):
            self.books.append(book)


    def searchBookByTitle(self, title):
        searchedBooks = []
        for book in self.books:
            if book.title == title:
                searchedBooks.append(book)
        if not searchedBooks:  
            return None
        return searchedBooks
        
    def searchBookByAuthor(self, Author):
        searchedBooks=[]
        for book in self.books:
            if book.author == Author:
                searchedBooks.append(book)
            else:
                continue
        if len(searchedBooks) == 0:
            
            return
        else:
            return searchedBooks
        
    def deleteBook(self, title):
        self.books = [book for book in self.books if book.title != title]

    def ShowBooks(self):
        print(f'Books in {self.title} category/section')
        for index, book in enumerate(self.books,1):
            print(f'#{index} {book.title}')


class Library:
    def __init__(self):
        self.title = None
        self.sections = []
        self.booklist=[]
        self.profit = 0
        self.itemsSold = 0
    
    def setName(self,title):
        self.title = title

    def addSection(self,section):
        if isinstance(section,Section):
            self.sections.append(section)
            for book in section.books:
                self.booklist.append(book)

    def searchBookByTitle(self, title):
        searchedBooks=[]
        for book in self.booklist:
            if book.title == title:
                searchedBooks.append(book)
                print("Inserting: ",book.title)
        return searchedBooks


    def searchBookByAuthor(self, Author):
        searchedBooks=[]
        for book in self.booklist:
            if book.author == Author:
                searchedBooks.append(book)
                print("Inserting: ",book.author)
        return searchedBooks
        
    def sellBook(self,title):
        bookDeleted = None
        bookSection= None
        DeleteSectionBool= True
        for book in self.booklist:
            if book.title == title:
                self.profit += book.cost
                bookDeleted = book
                bookSection = book.section
        if bookDeleted != None:
            self.booklist.remove(bookDeleted)
            self.itemsSold = self.itemsSold + 1
            for book in self.booklist:
                if book.section == bookSection:
                    DeleteSectionBool= False
            if DeleteSectionBool:
                self.deleteSection(bookSection)

            print(f"Item Sold. current Profit: {self.profit}, items sold: {self.itemsSold} ")
    
    def getTotalProfit(self):
        return self.profit
    
    def deleteSection(self, section):
        self.sections = [sectionLib for sectionLib in self.sections if sectionLib.title != section.title]
    
    def ExportLibData(self, pathFile="exported_books.json"):
        exportedData={}
        for book in self.booklist:
            book_data={
                "author":book.author,
                "cost":book.cost,
                "section":book.section.title
            }
           
            exportedData[book.title] = book_data
        with open(pathFile, 'w') as json_file:
            json.dump(exportedData, json_file, indent=4)

    def lOAD_DATA(self, pathFile="books.json"):

        with open(pathFile, 'r') as json_file:
            data = json.load(json_file)

        for data, item in data.items():
            book_author = item["author"] 
            book_title = data         
            book_cost = item["cost"]   
            section_title = item["section"]
            print(f"Creating book: {book_title} by {book_author}")

            book = Book(book_title, book_author, None, book_cost)
            section = None

            # lets check if section already exists if not we make a new one C:

            for libSection in self.sections:
                if section_title == libSection.title:
                    section = libSection
                    break
            
            if section is None:
                section = Section(section_title) 
                self.addSection(section)   

            section.addBook(book)
            book.section = section
            self.booklist.append(book)





def main():


    #Lets test it out C:

    newLib = Library()
    newLib.setName("Alexandria Library")
    print(newLib.title)
    





        
    
if __name__ == "__main__":
    main()


