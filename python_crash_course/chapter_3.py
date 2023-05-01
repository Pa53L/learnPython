import filler
# ex 3.4
print(f"{filler.filler} ex 3.4 {filler.filler}")
guests = ['Pasha', 'Sasha', 'Petya', 'Kolya']
for guest in guests:
    print(f"Приглашаю тебя на вечеринку, {guest.title()}")

# ex 3.5
print(f"{filler.filler} ex 3.5 {filler.filler}")
leave_guest = guests[1]
guests[1] = 'John'

for guest in guests:
    print(f"Приглашаю тебя на вечеринку, {guest.title()}")

print(f"А {leave_guest} не сможет присутствовать")

# ex 3.6
print(f"{filler.filler} ex 3.6 {filler.filler}")
guests.insert(0, 'Lerra')
guests.insert(2, 'Jim')
guests.append('Anya')

for guest in guests:
    print(f"Приглашаю тебя на вечеринку, {guest.title()}")

# ex 3.7
print(f"{filler.filler} ex 3.7 {filler.filler}")
print("\nПриглашаю двух гостей\n")

while len(guests) > 2:
    print("Сожалею, что не могу пригласить тебя,", guests.pop())

for guest in guests:
    print(f"\tПриглашаю тебя на вечеринку, {guest.title()}")

del guests[1]
del guests[0]

print(len(guests))
print(guests)