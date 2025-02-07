# class stringUpper:
#     def __init__(self):
#         self.q = ""
#     def string(self):
#         self.q = input()
#     def printsrt(self):
#         print(self.q.upper())

# a = stringUpper()
# a.string()
# a.printsrt()


# class Shape:
#     def __init__(self):
#         self.name = "shape"
        
#     def area(self):
#         return 0
        
# class Square(Shape): 
#     def __init__(self, l):
#         super().__init__()
#         self.l = l
#         self.name = "square"
        
#     def area(self):
#         return self.l ** 2

# shape = Shape()
# l = int(input("Enter the length of the square: "))
# square = Square(l)
# print(square.area())


# class Shape:
#     def __init__(self):
#         self.name = "shape"
#     def area(self):
#         return 0
# class Square(Shape):  
#     def __init__(self, l, w): 
#         super().__init__()
#         self.l = l
#         self.w = w
#         self.name = "square"
#     def area(self):
#         return self.l * self.w 
# shape = Shape()
# l = int(input("Enter the length of the square: "))
# w = int(input("Enter the width of the square: "))
# square = Square(l, w)
# print(square.area())



# import math
# class Point:
#     def __init__(self):
#         self.x = int(input("Enter X coordinate: "))
#         self.y = int(input("Enter Y coordinate: "))
#     def show(self):
#         print(f"Coordinates: ({self.x}, {self.y})")
#     def move(self):
#         self.x = int(input("Enter new X coordinate: "))
#         self.y = int(input("Enter new Y coordinate: "))
#     def dist(self, other_point):
#         return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
# p1 = Point()
# p2 = Point()
# p1.show()
# p2.show()
# print(f"Distance between points: {p1.dist(p2)}")
# p1.move()
# p1.show()


# class bank_akk:
#     def __init__(self):
#         self.owner = input("Enter akk owner name: ")
#         self.balance = float(input("Enter balance: "))
    
#     def deposit(self):
#         amount = float(input("Enter deposit: "))
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposit: {amount}")
#         else:
#             print("Deposit must be positive.")
    
#     def withdraw(self):
#         amount = float(input("Enter withdrawal: "))
#         if amount > self.balance:
#             print("Withdrawal denied")
#         elif amount > 0:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}")
#         else:
#             print("Withdrawal amount must be positive.")


# account = bank_akk()

# account.deposit()
# account.withdraw()
# account.withdraw()  


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# numbers = list(map(int, input("Enter numbers: ").split()))
# prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# print("Prime numbers:", prime_numbers)
