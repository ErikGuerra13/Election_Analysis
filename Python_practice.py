# counties = ["Arapahoe", "Denver", "Jefferson"]
# print(counties)

# #to get the first county in the list
# print(counties[0])

# #Slicing
# print(counties[0:2])

#Add items to the list using append()
# counties.append("El Paso")
# print(counties)

#Specify where on a list to add a item
# counties.insert(2, "El Paso")
# print(counties)

#Remove a instance 
# counties.remove("El Paso")
# print(counties)

#Remove all instances using pop()
# counties.pop(3)
# print(counties)

# #Change elements inside a list using list[index]
# # counties[2] = "El Paso"
# # print(counties)


# #Creating dictionaries
# # counties_dict = {'Araphoe': 422829,
# #                 'Denver': 463253,
# #                 'Jefferson': 432438
# #                 }
# # print(counties_dict)

# #list of dictionaries
# # voting_data = []
# # voting_data.append({"county":"Arapahoe", "Registered_Voters":422829})
# # voting_data.append({"county": "Denver", "Registered_Voters": 463353})
# # voting_data.append({"county": "Jeffereson", "Registered_Voters": 432438})
# # print(voting_data)


# #Using if statements
# counties = ["Arapahoe","Denver","Jefereson"]
# if counties[1] == 'Denver':
#     print(counties[1])


# # #if-else statements
# # #What is the score?
# # score = int(input("What is your test score? "))

# # # Determine the grade.
# # if score >= 90:
# #     print('Your grade is an A.')
# # else:
# #     if score >= 80:
# #         print('Your grade is a B.')
# #     else:
# #         if score >= 70:
# #             print('Your grade is a C.')
# #         else:
# #             if score >= 60:
# #                 print('Your grade is a D.')
# #             else:
# #                 print('Your grade is an F.')


# #if-elif-else statements
# # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

#Using Membership operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#using While loops
x = 0
while x <= 5:
    print(x)
    x = x + 1

#using for loops to iterate through lists and Tuples
for county in counties:
    print(county)

#using F-strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Print Multiple F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)



