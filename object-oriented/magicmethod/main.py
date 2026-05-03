# Magic method adalah dunder method atau double underscore __init__, __str__, __len__,
# Yang dimana di setiap method itu digunakan untuk mereprensentasikan hal yang berbeda 
# __init__ yang menggunakan base self 

class Test:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} and the author {self.author} with number of page {self.num_pages}"

    def __eq__(self, value):
        return self.title == value.title and self.author == value.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __mul__(self, other):
        return f"Num of pages {self.num_pages * other.num_pages}"
    
    def __contains__(self, item):
        return item in {self.title} or item in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Input the right key not {key}"

test1 = Test("Tioa", "Disanaaaaaa", 30)
test2 = Test("Asyu", "Disanaaaaaa", 10)
test3 = Test("Welo", "Anjir", 30)

print(test1 == test2)
print(test2 < test3)
print(test1 > test2)
print(test1 * test2)
print("Tioa" in test1)

print(test1)

print(test1)