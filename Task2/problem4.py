catalogue = {
    "Book1": {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "year": 1997
    },
    "Book2": {
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J.K. Rowling",
        "year": 1998
    },
    "Book3": {
        "title": "Harry Potter and the Prisoner of Azkaban",
        "author": "J.K. Rowling",
        "year": 1999
    },
    "Book4": {
        "title": "Harry Potter and the Goblet of Fire",
        "author": "J.K. Rowling",
        "year": 2000
    },
    "Book5": {
        "title": "Harry Potter and the Order of the Phoenix",
        "author": "J.K. Rowling",
        "year": 2003
    },
    "Book6": {
        "title": "Harry Potter and the Half-Blood Prince",
        "author": "J.K. Rowling",
        "year": 2005
    },
    "Book7": {
        "title": "Harry Potter and the Deathly Hallows",
        "author": "J.K. Rowling",
        "year": 2007
    }
}

for book, details in catalogue.items():
    print(f"{book}:")
    print(f"Title : {details["title"]}")
    print(f"Author : {details["author"]}")
    print(f"Year : {details["year"]}")
    print("--------------------------------")

