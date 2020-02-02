#In this project, our final Python script will need to be able to deliver the following information
# when the script is run:
#•  Total number of votes cast
#•  A complete list of candidates who received votes
#•  Total number of votes each candidate received
#•  Percentage of votes each candidate won
#•  The winner of the election based on popular vote
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#variable
total_votes = 0
#list or array
candidate_options = []
#dictionary = key + value - declaring empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row[0])
        #for i in range(len(row)):
        #    print(row[1])
    # Read and print the header row.
    headers = next(file_reader)
    #print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
#for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
 #   votes = candidate_votes[candidate]
 #   # 3. Calculate the percentage of votes.
 #   vote_percentage = int(votes) / int(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
 #   print(f"{candidate}: received {vote_percentage:.1f}% of the vote.")
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
# Print the total votes.
#print(total_votes)
# Print the candidate list.
#print(candidate_options)
# Print the candidate vote dictionary.
#print(candidate_votes)