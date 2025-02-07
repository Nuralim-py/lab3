# def ounces(q):
#     return q*28.3495231
# a = int(input("gram: "))
# o = ounces(a);
# print(o, "ounces")
# def c(f):
#     return  (5 / 9) * (f - 32)
# f = int(input("in F: "))
# c = c(f)
# print(c, "C")



# def solve(numheads, numlegs):
#     return (numlegs - 2*numheads)/2
# l = int(input("legs: "))
# h = int(input("Heads: "))
# s1 = solve(h, l)
# s2 = h - s1
# print(int(s1), "rabbits and", int(s2), "chickens")



# import math

# def prime(q):
#     for i in range(2, int(math.sqrt(q))):
#         if q%i==0:
#             return False
#         else:
#             return True
# list = [5, 19, 29, 11, 26, 15, 13, 8, 9]
# for i in list:
#     r = prime(i)
#     if r==True:
#         print(i, " ")




# def per(s):
#     if len(s) == 0:
#         return []
#     if len(s) == 1:
#         return [s]
#     result = []  
#     for i in range(len(s)):
#         char = s[i]
#         remaining = s[:i] + s[i+1:]
#         for perm in per(remaining):
#             result.append(char + perm) 
#     return result
# s = input()
# permutations = per(s)
# for perm in permutations:
#     print(perm)



# def rev(sent):
#     words = sent.split()
#     revers = words[::-1]
#     return ' '.join(revers)
# sentence = input()
# reverse = rev(sentence)
# print(reverse)




# def tf(q):
#     for i in range(len(q)-1):
#         if q[i]==3 and q[i]==q[i+1]:
#             return True
#     return False
# list = [1, 2, 3, 2, 3, 3, 5]
# r = tf(list)
# if r:
#     print(True)
# else:
#     print(False)



# def tf(q):
#     o = 0
#     s = 0
#     for i in range(len(q)):
#         if q[i]==0:
#             o+=1
#         elif q[i]==7:
#             s+=1
#     if(o==2 and s==1):
#         return True
# list = [0, 2, 3, 0, 3, 7, 5]
# r = tf(list)
# if r:
#     print(True)
# else:
#     print(False)



# def v(q):
#     return 4/3*3.14*q
# q = int(input("R: "))
# print("V=", v(q))



# def wtf(smth):
#     n = []
#     for i in smth:
#         if smth.count(i)==1:
#             n.append(i)
#     return n
    
# list = [1, 3, 4, 1, 5, 6, 0, 6, 8, 5, 10, 9]
# r = wtf(list)
# print(r)

# def chzh(q):
#     return q[::-1]
# q = input()
# r = chzh(q)
# if r==q:
#     print("Palindrome")
# else:
#     print("Not painrome")


# def his(q):
#     return q*"*"
# list = [5, 8, 3]
# for i in list:
#     print(his(i))



# import random
# def ch(q, r): 
#     if q == r:
#         return True
#     return False
# print("Hello! What is your name?")
# n = input()
# print("Well", n, "I am thinking of a number between 1 and 20.")
# print("Take a guess.")
# r = random.randint(1, 20) 
# x = int(input())
# l = 0
# u = 0
# while not ch(x, r): 
#     if x < r:
#         print("Your guess is too low.")
#         print("Take a guess.")
#         l += 1
#     elif x > r:
#         print("Your guess is too high.")
#         print("Take a guess.")
#         u += 1
#     x = int(input()) 
# print("Good job,", n, "You guessed my number in", l + u, "guesses!")



