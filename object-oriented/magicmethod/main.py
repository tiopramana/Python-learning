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
    
    def __len__(self):
        return f"The length of pages{self.num_pages}"

test1 = Test("Tio", "Bali", 20)

print(test1)