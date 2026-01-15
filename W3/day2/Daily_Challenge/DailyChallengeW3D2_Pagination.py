#Daily Challenge : Pagination
#Goal: Create a Pagination class that simulates a basic pagination system.

import math

class Pagination:
    """A simple pagination system for a list of items, page by page""" 

    def __init__(self, items=None, page_size=10):
        """Initialize pagination with items and page size."""
        self.items = items if items is not None else []
        self.page_size = page_size
        # current page index, starts at 0
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)  
        #math.ceil() Round up so the last page exists even if it's partial.
        
    def get_visible_items(self):
        """Returns the items visible on the current page."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]     # allows method chaining
                        #slicing [includes start : excludes end]


# Implement Navigation Methods

    def go_to_page(self, page_num):
        """Go to a specific page number (1-based)."""
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range")

        self.current_idx = page_num - 1  
        return self   
        #indice  → page
        # 0 →    page 1
        # 1 →    page 2
        # 2 →    page 3
        # 3 →    page 4
        # 4 →    page 5
        # 5 →    page 6
        # 6 →    page 7 (last)

    def first_page(self):
        """Go to the first page."""
        self.current_idx = 0
        return self

    def last_page(self):
        """Go to the last page."""
        self.current_idx = self.total_pages - 1  
        return self
        self.current_idx = self.total_pages - 1 
        #indice  → page
        # 0 →    page 1
        # 1 →    page 2
        # 2 →    page 3
        # 3 →    page 4
        # 4 →    page 5
        # 5 →    page 6
        # 6 →    page 7 (last)

    def next_page(self):
        """Go to the next page, if possible."""
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self     # allows method chaining

    def previous_page(self):
        """Go to the previous page, if possible."""
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

#Bonus: should return a string displaying the items on the current page, each on a new line.
    def __str__(self):
        """Return a string displaying the items on the current page, each on a new line"""
        return "\n".join(self.get_visible_items())

#Testing the code

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))
# a
# b
# c
# d

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

#p.go_to_page(0)    # ValueError

p.go_to_page(7)
print(p)
# y
# z

#p.go_to_page(8)   # ValueError

#p.go_to_page(10)   # ValueError

# Bonus: upgrade your code by changing the return statement in a way that will allow you to concatenate methods like this:
# p.nextPage().nextPage().nextPage().getVisibleItems()

# Bonus: method chaining
p.first_page()
print(p.next_page().next_page().next_page().get_visible_items())  # ['m', 'n', 'o', 'p']
    
# __str__ representation
print("\nCurrent page items:\n")
print(p)  
# Current page items:

# m
# n
# o
# p