from filecmp import clear_cache


print("Hello World")
Counties= ["Arapahoe", "Denver", "Jefferson"]
Counties
Counties[0]
Counties[2]
len(Counties)
print(Counties[2])
print(Counties[-2])
Counties[0:2]
Counties.append("El Paso")
Counties
Counties.insert(2,"El Paso")
Counties
Counties.remove("El Paso")
Counties
Counties.pop(3)
Counties
Counties[2]= "El Paso"
Counties
my_tuple= ( )
Counties_tuple= ("Arapahoe", "Denver", "Jefferson")
len(Counties_tuple)
Counties_tuple[:-2]
Counties_tuple[:2]
Counties_tuple[:-1]
dict()
my_dictionary = dict()
Counties_dict={}
Counties_dict["Arapahoe"] = 422829
Counties_dict
Counties_dict["Denver"] = 463353
Counties_dict["Jefferson"] = 432438
Counties_dict
print(Counties_dict)
Counties_dict.items()
Counties_dict.keys()
Counties_dict.values()
Counties_dict.get("Denver")
Voting_data= []
Voting_data
Voting_data.append({"County":"Arapahoe", "registered_voters": 422829})
Voting_data.append({"County":"Denver", "registered_voters": 463353})
Voting_data.append({"County":"Jefferson", "registered_voters": 432438})
Voting_data
Counties.append ("El Paso")
Counties_dict["El Paso"]= 461149
Counties.remove("Arapahoe")
Voting_data.remove({"County":"Arapahoe", "registered_voters": 422829})
Voting_data
Voting_data.append({"County":"El Paso", "registered_voters": 461149})
Voting_data[2]=({"County": "Jefferson", "registered_voters":432438})
Voting_data[1]=({"County": "El Paso", "registered_voters": 461149})
Voting_data
Voting_data.insert(3,({"County":"Denver", "registered_voters": 463353}))
Voting_data.remove({"County":"Denver", "registered_voters": 463353})
Voting_data
Voting_data.remove({"County":"Jefferson", "registered_voters": 432438})
Voting_data.append({"County": "Arapahoe", "registered voters": 422829})
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
Counties = ["Arapahoe","Denver","Jefferson"]
if Counties[1] == 'Denver':
    print(Counties[1])
if Counties[3] != 'Jefferson':
   print(Counties[2])