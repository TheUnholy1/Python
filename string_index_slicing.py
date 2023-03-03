print("Slicing")
fruit = "mangosteen"
print(fruit[1:4])
print(fruit[:5])
print(fruit[5:])
print(fruit[:5] + fruit[5:])
print("\nindexing")
pets = "Cats & Dogs"
print(pets.index("&")) #should be 5
print(pets.index("C")) #should be 0

print("\nin Method")
print("Dragons" in pets) #False
print("Cats" in pets) #True 

print("\nlower and upper Methods")
str1 = "MOuNTaInS"
print(str1.lower()) #mountains
print(str1.upper()) #MOUNTAINS

print("\nstrip, lstrip, and rstrip method")

str2 = "  yes  "
print(str2.strip()) #removes white space
print(str2.lstrip()) #left white space
print(str2.rstrip()) #right white space

print("\ncount Method")

sentence = " letter e appeared for 6 times"
print(sentence.count("e")) #6

print("\nendswith Method")

tree = "forest"
print(tree.endswith("rest")) #True

print("\nisnumeric Method")
print(tree.isnumeric())#False

print("\njoin Method")

print(" ".join(["This","is","a","sentence"]))
print("...".join(["This","will","be","three dots"]))

print("\nsplit Method")

song = "Altough it hurts I'll be the first to say that"
print(song.split())
print(song.split("t"))

print("\nEnumerate Method")

to_do_list = [
    "brush",
    "drink water",
    "take a bath"]

for x, things  in enumerate (to_do_list):
    print(x, things.title())