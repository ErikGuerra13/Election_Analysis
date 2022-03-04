#allow us to read the csv file by importing the built-in module
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1 Initialize a total vote counter *Place variable before with open()
total_votes = 0

#Declare a new list to get candidate names *Place before with open()
candidate_options = []

#Create a dictionary to get total_votes for each candidate
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

     # Read and print the header row.
    headers = next(file_reader)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file with the total_votes
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        #Check if the candidate does not match any existing candidate.
        #Do this to only get the name of the candidates once
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking the candidates vote counts, equal each to 0
            candidate_votes[candidate_name] = 0

        #Increment the canidates votes by 1 when we run the file
        #Do this by moving the voute counter insde the for loop, aligned
        #with the if statement
        candidate_votes[candidate_name] += 1

#Save the results to a text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results, end="")
    #save the final vote count
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

     # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list
# for candidate_name in candidate_votes:

#     #Retrieve vote count of a candidate
#     votes = candidate_votes[candidate_name]

#     #Calculate the percentage of votes
#     vote_percentage = float(votes) / float(total_votes) * 100

#      # Print each candidate, their voter count, and percentage
#     #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
#     # Determine winning vote count and candidate
#     # Determine if the votes is greater than the winning count.
#     if (votes > winning_count) and (vote_percentage > winning_percentage):
#         # If true then set winning_count = votes and winning_percent =
#         # vote_percentage.
#         winning_count = votes
#         winning_candidate = candidate_name
#         winning_percentage = vote_percentage
#         # And, set the winning_candidate equal to the candidate's name.
#         winning_candidate = candidate_name
    

#     #Print out candidate winning candidate
#     winning_candidate_summary = (
#     f"-------------------------\n"
#     f"Winner: {winning_candidate}\n"
#     f"Winning Vote Count: {winning_count:,}\n"
#     f"Winning Percentage: {winning_percentage:.1f}%\n"
#     f"-------------------------\n")
# print(winning_candidate_summary)