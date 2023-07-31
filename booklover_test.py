import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        
        # create booklover instance, adding book
        blov = BookLover("Freddy T", "fred@gmail.com", "fantasy")
        blov.add_book("myfavbook", 5)
        
        # test
        message = "book not added"
        self.assertTrue("myfavbook" in list(blov.book_list['book_name']), message)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        # create booklover instance, adding book
        blov = BookLover("Freddy T", "fred@gmail.com", "fantasy")
        blov.add_book("myfavbook", 5)
        blov.add_book("myfavbook", 3)
        
         # test
        expected = 1
        self.assertEqual(len(blov.book_list), expected)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        # create booklover instance, adding book
        blov = BookLover("Freddy T", "fred@gmail.com", "fantasy")
        blov.add_book("myfavbook", 5)
        blov.has_read("myfavbook")
        
        # test
        message = "book not in list"
        self.assertTrue(blov.has_read("myfavbook"), message)

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        blov = BookLover("Freddy T", "fred@gmail.com", "fantasy")
        blov.add_book("myfavbook", 5)
        
        # test
        message = "book is in list"
        self.assertFalse(blov.has_read("hunger games"), message)


    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        blov = BookLover("Freddy T", "fred@gmail.com", "fantasy")
        blov.add_book("myfavbook", 5)
        blov.add_book("book1", 2)
        blov.add_book("book45", 4)
        
         # test
        expected = 3
        self.assertEqual(blov.num_books_read(), expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        blov = BookLover("Freddy T", "fred@gmail.com", "fantasy")
        blov.add_book("myfavbook", 5)
        blov.add_book("book1", 2)
        blov.add_book("book45", 4)
        
        # test
        testval = all(blov.fav_books().book_rating > 3)
        message = "ratings are not over 3"
        self.assertTrue(testval, message)
        
if __name__ == '__main__':
    unittest.main(verbosity=3)