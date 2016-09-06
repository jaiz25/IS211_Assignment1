#!/usr/bin/env/python
#-*- coding: utf-8 -*-
"""Assignment 1 part 2."""


class Book(object):
    """A book class.

    Args:
        author(str): Name of the author
        title(str): Name of the book
    """
    author = ''
    title = ''

    def __init__(self, author, title):
        """__init__ function."""
        self.author = author
        self.title = title

    def display(self):
        """Function that will display the author and
        title of the book.
        """
        name = '\"{1}, written by {0}.\"'
        output = name.format(self.title, self.author)
        return output


BOOK1 = Book('Of Mice and Men', 'John Steinbeck')
BOOK2 = Book('To Kill a Mockingbird', 'Harper Lee')

print BOOK1.display()
print BOOK2.display()
