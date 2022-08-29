

# voting_data = [];

# voting_data.append({"county":"Arapahoe", "registered_voters": 422829});
# voting_data.append({"county":"Denver", "registered_voters": 463353});
# voting_data.append({"county":"Jefferson", "registered_voters": 432438});
# print(voting_data[0]);
# print(voting_data[1])
# print(voting_data[2])

# print("************************")
# voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})

# print(voting_data[0]);
# print(voting_data[1])
# print(voting_data[2])
# print(voting_data[3])

# print("************************")
# voting_data.pop(0);
# print(voting_data)

# voting_data.insert(2,{"county":"Denver", "registered_voters": 463353})
# voting_data.insert(1,{"county":"Jefferson", "registered_voters": 432438})
# print("************************")

# print(voting_data[0]);
# print(voting_data[1])
# print(voting_data[2])

# voting_data.insert(3,{"county":"Arapahoe", "registered_voters": 422829})

# print("************************")
# print(voting_data[0]);
# print(voting_data[1])
# print(voting_data[2])
# print(voting_data[3])

# # How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# #  Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# #What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#         print('Your grade is a B.')
# elif score >= 70:
#             print('Your grade is a C.')
# elif score >= 60:
#                 print('Your grade is a D.')
# else:
#                 print('Your grade is an F.')

# from itertools import count


# print("************************")



# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
# else:
#     print("No Entry")



# for county in counties:
# print(county)


# if counties[3] != 'Jefferson':
#     print(counties[2])

# for num in range(len(counties)):
#     print(counties[num])

# counties_tuples = ("Arapahoe","Denver","Jefferson")

# for i in range(len(counties_tuples)):

#       print(counties_tuples[i])






# for county in counties_tuples:

#       print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)


# for county in counties_dict.items():
#     print(county)

# for county in counties_dict.values():
#     print(county)
    

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))  


# for county_name, county_voters in counties_dict.items():
#     # print(county_name, county_voters)
#     # print(county_name+ "  has "+ str(county_voters) + " registered voters")
#     print(f"{county_name }  has  {county_voters:,}  registered voters")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes.")

# print(message_to_candidate)


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353},
                 {"county":"Jefferson", "registered_voters": 432438}]

for county_name in range(len(voting_data)):
    county = voting_data[county_name]["county"]
    voters_count = voting_data[county_name]["registered_voters"]
    print(f"{county} has {voters_count:,} registered voters.")

    print(f" {voting_data[county_name]['county']} " )

   # has {voting_data[county_name]["registered_voters"]} registered voters.")

    # print(f"{voting_data[county_name]["county"]} has  
    #    {voting_data[county_name]["registered_voters"]}
    #     registered voters." )
    # print(county_name, county_voters)
    # print(county_name+ "  has "+ str(county_voters) + " registered voters")
    # print(f"{county_name }  has  {voting_data["registered_voters"]:,}  registered voters")
           