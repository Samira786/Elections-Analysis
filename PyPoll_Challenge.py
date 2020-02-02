#dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#total votes initialized to zero
total_votes = 0
#candidate votes as a dictionary
candidate_votes = {}
#county votes as a dictionary
county_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#reading election date and skipping the first row
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
# Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate is not in the candidate_votes dictionary
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Print the county name from each row
        county_name = row[1]
        # If the candidate is not in the county_votes dictionary
        if county_name not in county_votes:
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1
    #Print to terminal and write to files
    with open(file_to_save, "w") as txt_file:
            #print election results title and total votes and write to file
            election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
            print(election_results, end="")
            # Save the final vote count to the text file.
            txt_file.write(election_results)
            #print county votes title
            votes_title = ("County Votes:\n")
            print(votes_title)
            txt_file.write(votes_title)
            #calculate largest turnout vote by county, votes by each county, percentage and write to file
            highest_count = 0
            highest_county_name = None
            # Iterate through the county vote dictionary keys and values
            for k, v in county_votes.items():
                # Calculate the percentage of votes.
                county_percent = float(v) / float(total_votes) * 100
                votes_summary = (
                f"{k}: {county_percent:.1f}% ({v:,})\n")
                print(votes_summary)
                txt_file.write(votes_summary)
                #Determine highest count of votes (largest turnout)
                if v > highest_count:
                    highest_count = v
                    highest_county_name = k
            turnout_results = (
                f"-------------------------\n"
                f"Largest County Turnout: {highest_county_name}\n"
                f"-------------------------\n")
            print(turnout_results)
            # Save the winning county to the text file.
            txt_file.write(turnout_results)
            # Determine the percentage of votes for each candidate by looping through the counts.
            # Iterate through the candidate list.
            for candidate in candidate_votes:
                # Retrieve vote count of a candidate.
                votes = candidate_votes[candidate]
                # Calculate the percentage of votes.
                vote_percentage = float(votes) / float(total_votes) * 100
                # Print each candidate, their voter count, and percentage to the # terminal
                candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
                print(candidate_results)
                #  Save the candidate results to our text file.
                txt_file.write(candidate_results)
                # Determine winning vote count and candidate
                # Determine if the votes is greater than the winning count.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                    winning_count = votes
                    winning_candidate = candidate
                    winning_percentage = vote_percentage
            # Print the winning candidates' results to the terminal.        
            winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
            print(winning_candidate_summary)
            # Save the winning candidate's results to the text file.
            txt_file.write(winning_candidate_summary)