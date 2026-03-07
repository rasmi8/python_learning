
class book: 
    def __init__(self,title, author, pages): 
        self.title = title 
        self.author = author 
        self.pages = pages 
    def book_info(self): 
        print(self.title, self.author, self.pages) 
b1 = book('atomic habits','rashmita',100) 
b1.book_info() 