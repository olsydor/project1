import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://tssgowkofctcyh:4b746964b408a6ae79254f334ab1ec2058fab01def7c52d99edc98f0d78636dc@ec2-54-217-235-166.eu-west-1.compute.amazonaws.com:5432/d92uo0gvk9etef")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn,title,author,year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"Added books isbn {isbn} Title {title} author {author} year {year}.")
    db.commit()

if __name__ == "__main__":
    main()
