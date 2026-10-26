# #class

# class Person:
#     # class attributes
#     address1 = 'sırakapılar mah 1527 sokak demirayak apt kat:3 no:9'
#     address2 = 'fesleğen mah 999 sokak no:8 kat:2 i.özdemir apt'



#     # constructor (yapıcı metod)
#     def __init__(self, name, year):
#         # objects attributes
#         self.name = name
#         self.year = year 
    
    
#     # methods
#     def intro(self):
#         print('Hello there. I am ' + self.name)

#     def calculateAge(self):
#         return 2025 - self.year


# # object (instance)
# p1 = Person(name = 'talha', year = 2006)
# p2 = Person(name = 'selin', year = 2007)

# p1.intro()
# p2.intro()

# print(f'adım : {p1.name} ve yaşım : {p1.calculateAge()}')
# print(f'adım : {p2.name} ve yaşım : {p2.calculateAge()}')



class Circle:
    #Class object attributes
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods 
    def cevre_hesapla(self):
        return 2 * self.pi + self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f'c1 : alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}')
print(f'c2 : alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}')