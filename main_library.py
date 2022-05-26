class Book:
    def __init__(self, title, author, description, pub_date, isbn,
                 copies_available, checked_out_by):
        self.title = title
        self.author = author
        self.description = description
        self.pub_date = pub_date
        self.isbn = isbn
        self.copies_available = copies_available
        self.checked_out_by = checked_out_by

    def checkout(self, name):
      self.checked_out_by.append(name)
      self.copies_available -= 1

    def check_in(self, name):
      self.checked_out_by.remove(name)
      self.copies_available += 1

    def add_copies(self, number):
      # Add comment
      self.copies_available += number
      # self.copies_available = self.copies_available + number

    def remove_copies(self, number):
      self.copies_available -= number
      
dreadnought = Book(
    title="Dreadnought (Nemesis Book 1)",
    author="April Daniels",
    description=
    "Danny Tozer has a problem: she just inherited the powers of Dreadnought, the world's greatest superhero. Until Dreadnought fell out of the sky and died right in front of her, Danny was trying to keep people from finding out she's transgender. But before he expired, Dreadnought passed his mantle to her, and those secondhand superpowers transformed Danny's body into what she's always thought it should be. Now there's no hiding that she's a girl.",
    isbn="9781682300688",
    pub_date="2016",
    copies_available=3,
    checked_out_by=[])

print(dreadnought.title)
print(dreadnought.copies_available)
dreadnought.checkout("Ghameerah")
dreadnought.checkout("Tara")

print(dreadnought.checked_out_by)
print(dreadnought.copies_available)

dreadnought.check_in("Ghameerah")

print(dreadnought.checked_out_by)
print(dreadnought.copies_available)

dreadnought.add_copies(10)
print(dreadnought.copies_available)

dreadnought.remove_copies(5)
print(dreadnought.copies_available)

mindfulness = Book(
  title="The Power of Now",
  author="Eckhart Tolle",
  description="The Power of Now: A Guide to Spiritual Enlightenment",
  isbn="9781682300688",
  pub_date="1997",
  copies_available=8,
  checked_out_by=["Ajh", "Parker"])