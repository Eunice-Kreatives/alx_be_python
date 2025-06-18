class Book:
    def __init__(self, title:str, author:str, publication_year:int):
        self.title= title
        self.author= author
        self.publication_year= publication_year
        
    
    def __del__(self):
        print(f"Deleting {self.title}")
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.publication_year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.publication_year}."
    


