
from marvel import Marvel
from keys import public_key, private_key

m = Marvel(public_key, private_key)

chars = m.characters
all_chars = chars.all()["data"]["results"]
# print(all_chars)
# print(all_chars[0]["name"])
# for i in range(0,len(all_chars)):
#     print(all_chars[i]["name"])

for char in all_chars:
     #print(char["comics"]["items"],char["name"])
     print("Character is:")
     print(char["name"])
     print("-----------------------")
     count=0
     for comic in char["comics"]["items"]:
         print(comic["name"])
         count+=1
     print(f"Number of times Character appeared in the Comics {count}")
     print("\n###############\n")