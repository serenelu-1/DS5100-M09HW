import pandas as pd
class BookLover():
    ''' This is a booklover object. '''

    def __init__(self, name, email, fav_genre, num_books = 0, 
                 book_list= pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.num_books = num_books
        self.book_list = book_list
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

    def add_book(self, book_name, rating):
        if book_name not in list(self.book_list['book_name']):
            new_book = pd.DataFrame({
                            'book_name': [book_name], 
                            'book_rating': [rating]
                        })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1

    def has_read(self, book_name):
        if book_name in list(self.book_list['book_name']):
            return True
        else:
            return False
    
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
    
    

    
if __name__ == '__main__':
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.add_book("hello", 2)
    test_object.book_list
    test_object.has_read("War of the Worlds")
    test_object.num_books_read()
    test_object.fav_books()