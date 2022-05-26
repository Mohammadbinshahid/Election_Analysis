from lib2to3.pgen2.token import PERCENT


x = 0
while x <= 5:
    print(x)
    x = x + 1

Counties= ["Arapahoe", "Denver","Jefferson"]
for County in Counties:
    print(County)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for i in range(len(Counties)):
    print(Counties[i])

counties_tuple = ("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])

Counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for County in Counties_dict:
    print(County)

for county in Counties_dict.keys():
    print(county)

for voters in Counties_dict.values():
    print(voters)

for County in Counties_dict:
    print(Counties_dict[County])

for key, value in Counties_dict.items():
    print(key, value)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):

      print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:

     print(county_dict['registered_voters'])

for county_dict in voting_data:
    print(county_dict['county'])

interest = 10
print("Your interest for the year is $" + str(interest))

my_votes = 100000

total_votes = 500000

my_votes = int(input("How many votes did you get in the election? "))

total_votes = int(input("What is the total votes in the election? "))

print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))

candidate_votes = 100000
candidate_votes = int(input("How many votes did the candidate get in the election? "))

total_votes = 300000
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (

    f"You received {candidate_votes} number of votes."

    f"The total number of votes in the election was {total_votes}."

    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes")

print(message_to_candidate)