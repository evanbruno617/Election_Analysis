# Add dependencies
import csv
from operator import countOf

import os

#Assign a variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save a file from path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize voter counter to 0
total_votes = 0

#necessary dictionaries and lists used to store county and candidate information
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

#used in calculating which candidate/county has the most votes
winning_candidate = ""
winning_count = 0
winning_percentage = 0
county_winning_count = 0
county_winning_percent = 0

#open election results and reads the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    #Read the header row
    headers = next(file_reader)
    print(headers)

    #iterates through csv file to store poll information
    for row in file_reader:
        #add to total vote count
        total_votes += 1
        #Gets candidate name from each row
        candidate_name = row[2]
        #Gets county name form each row
        county_name = row[1]

        #checks to see if the county has come up before if not adds to dictionary
        if county_name not in county_options:
            county_options.append(county_name)
            #sets value of county to 0
            county_votes[county_name] = 0
        #adds a vote to the county
        county_votes[county_name] += 1

        #checks to see if the candidate has come up before if not adds to dictionary
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #sets value of candidate ti 0
            candidate_votes[candidate_name] = 0
        #adds a vote to the candidate
        candidate_votes[candidate_name] += 1
#prints the total votes
print(F' Total Votes: {total_votes}')

#opens new file to organize the results
with open(file_to_save, "w") as txt_file:
    #heading of file with total votes counted
    election_results = (f"""
    
Election Results
--------------------------
Total Votes: {total_votes}
-------------------------- \n""")


    #saves heading to file
    txt_file.write(election_results)

    
    for candidate_name in candidate_votes:
        #get votes from each candidate
        votes = candidate_votes[candidate_name]

        #calculates percent of votes earned
        votes_percentage = (float(votes)/float(total_votes)) * 100

        #print each candidate, vote percentage, and amount of votes
        candidate_results = (f'{candidate_name}: {votes_percentage: .1f}% ({votes: ,}) \n')
        print(candidate_results)

        #saves candidate information to file
        txt_file.write(candidate_results)

        #calculates of candidates have the most votes
        if (votes > winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = votes_percentage
    #prints winning candidate and their vote information
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage: .2f}%\n"
        f"-----------------------\n"
    )
    print(winning_candidate_summary)
    #saves winner to file
    txt_file.write(winning_candidate_summary)

    #heading for county turnout
    county_turnout = (f"""
    
County Turnout
----------------------    \n""")
    #saves heading to file
    txt_file.write(county_turnout)


    for county_name in county_votes:
        #get votes from each county
        count_votes = county_votes[county_name]
        #calculates percent of votes
        county_votes_percentage = float(count_votes) / float(total_votes) * 100
        #prints county, percentage of votes, and vote total
        county_results = (f"{county_name}: {county_votes_percentage: .1f}% ({count_votes: ,})\n")
        print(county_results)

        #saves county information to file
        txt_file.write(county_results)

        #prints which county has the highest turnover
        if (count_votes > county_winning_count) and (county_votes_percentage > county_winning_percent):
            winning_candidate = county_name
            county_winning_count = count_votes
            county_winning_percent = county_votes_percentage

    highest_voter_turnout = (f"""
---------------------
County with highest turnout: {winning_candidate}
Amount of votes in county: {county_winning_count}
Percent of total votes: {county_winning_percent:.1f}%
---------------------\n""") 
    print(highest_voter_turnout)

    #saves winner to file
    txt_file.write(highest_voter_turnout)
