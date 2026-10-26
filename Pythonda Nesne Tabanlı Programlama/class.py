#class

class Person:
    # class attributes
    address1 = 'sırakapılar mah 1527 sokak demirayak apt kat:3 no:9'
    address2 = 'fesleğen mah 999 sokak no:8 kat:2 i.özdemir apt'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # objects attributes
        self.name = name
        self.year = year 
        print('init metodu çalıştı.')
    
    
    # methods


# object (instance)
p1 = Person(name = 'talha', year = 2006)
p2 = Person(name = 'selin', year = 2007)

# updating
p1.name = 'Çağan'
# accessing object attributes 
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address2}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address1}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)