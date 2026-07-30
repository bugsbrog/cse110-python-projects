# I added a color for the animal and also a place for the story at the end. I made it so the first letter of the place is always capitalized by using .capitalize()
print("Please enter the following: ")
print()

adjective = input("adjective: ")
color = input("color: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2= input("verb: ")
verb3 = input("verb: ")
place = input("place: ")

print()

print("Your story is: ")

print()

print("The other day, I was really in trouble. It all started when I saw a very ")
print(f'{adjective} {color} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all ')
print(f"I could think to do was to {verb2} over and over. Miraculously, ")
print(f"that caused it to stop, but not before it tried to {verb3} ")
print(f"right in front of my family at the {place.capitalize()}.")