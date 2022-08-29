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
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
 

# Import the CSV built-in module to pull on data from external CSV files
# and perform operations on them.

import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
print(file_to_load)
# Open the election results and read the file.
# election_data = open(file_to_load, 'r')
# print(election_data)
# To do: perform analysis.

# with open(file_to_load,"r") as election_data:
#      for i in range(100):
#         print(election_data.readline(i))
# print(election_data)
    




# Close the file.
# election_data.close()


# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# election_data = open(file_to_load,"r")

# file_reader = csv.reader(election_data)

# # for row in file_reader:
# #     print(row)
# # Using the open() function with the "w" mode we will write data to the file.
# analysis_data =open(file_to_save, "w")
# analysis_data.write("My first file writing")
# analysis_data.writelines(election_data.readlines())
# election_data.close()
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#   file_reader = csv.reader(election_data)

#  # Read and print the header row.
# headers = next(file_reader)
# print(headers)

# analysis_data.close()
# election_data.close()

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
    print(headers)

    election_data.close()