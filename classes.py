# A class is like a blueprint for creating objects. An object has properties and methods(functions) 
# associated with it. Almost everything in Python is an object

# Create class
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Customer class 

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

# Init user object
gus = User('Gus Jimenez', 'Gus@gmail.com', 30)
janet = User('Janet Williams', 'janet@gmail.com', 27)


# Edit property
gus.age = 80 

janet.has_birthday()

# Call method 
print(janet.greeting())

# Init customer
john = Customer('John Doe', 'John@gmail.com', 40)

print(john.name)

john.set_balance(500)

print(john.greeting())