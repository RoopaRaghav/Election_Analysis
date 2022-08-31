# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote


# Open the data file. "C:\Users\rkota\Desktop\Analysis Projects\Election_Analysis\Resources"
# "C:\Users\rkota\Desktop\Analysis Projects\Election_Analysis\Resources\election_results.csv"
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.


# Import the datetime class from the datetime module.
import datetime
from telnetlib import theNULL
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
 

# Import the CSV built-in module to pull on data from external CSV files
# and perform operations on them.
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    # print(headers)

    # Declarations and Initialisations
    total_votes =0
    candidate_options = []  
    candidate_votes = {}

    
    for row in file_reader:
        # print(row)
        total_votes +=1
        candidate_name = row[2]

        # Check the candidate name exists or not and add to the list accordingly
        if candidate_name not in candidate_options:
             # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #  Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
            
        #Add vote to that Candidates name
        candidate_votes[candidate_name] +=1

    # To get the winning candidate summary required initialisations
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    counter =0
    candidate_results =[]

    #  Print the candidate list.        
    # print(candidate_options)
    print(candidate_votes)

    # Track the winning candidate, vote count, and percentage.
    for candidate_name in candidate_votes :
        
        votes = candidate_votes[candidate_name]
        votes_Percentage = float(candidate_votes[candidate_name]) /float(total_votes) *100
        # Track the individual candidate results.
        candidate_results.append((f"{candidate_name}: {votes_Percentage:.1f}% ({votes})."))
        
            
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (votes_Percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = votes_Percentage

#print total no. of votes and candidate results string.
print(f"Total no. of votes is {total_votes}")
print(candidate_results)

 # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results)
    
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    i=0
     # Save the final vote count to the text file.
    txt_file.write(election_results)
    print(winning_candidate_summary)
    
    txt_file.write("-------------------------\n")

    for i in range(len(candidate_results)):
        txt_file.write(candidate_results[i] + "\n")
        
    txt_file.write("-------------------------\n")
    
    
    txt_file.write(winning_candidate_summary)
  

election_data.close()
txt_file.close()