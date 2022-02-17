# Election Analysis
---
## Purpose 
---
The purpose of this election audit is to count the amount of votes from various different counties. I will use [Voting Data](https://github.com/evanbruno617/Election_Analysis/blob/main/Resources/election_results.csv) providing to me to calculate out which county has produced the most votes and which candidate has won the election. 


## Election Results
  
* A total of 369,711 votes were cast in this election. To find the total votes we iterated through the csv file with a for loop and count the amount of rows there are. This is completed by adding 1 to a variable every time a new row, vote, is intorduced. File reader is a variable set to read the election data provided.

![Total Votes](https://raw.githubusercontent.com/evanbruno617/Election_Analysis/main/Resources/total_count.png)

* Jefferson received 38,855 or 10.5% of the total votes. Denver recieved 306,055 or 82.8% of the total votes. Arapahoe received 24,801 or 6.7% of the total votes. This was calculated with a for loop by adding a vote to each county every time it showed up in a row. Using this if function ![If function](https://raw.githubusercontent.com/evanbruno617/Election_Analysis/main/Resources/Count_votes.png)
allows each county to be assigned to a key and a value. The value in this scenario is the votes from that county. Every time that county comes up in a row one vote is added to the value. The percentage of votes was calculated by dividing it by the total votes and multplying it by 100 in this for loop.
![Percentage/Winner](https://raw.githubusercontent.com/evanbruno617/Election_Analysis/main/Resources/Candidate_info_calculated.png)
* The County with the most votes is Denver. This was found out by using the for loop above to compare each county's votes. 
* Charles Casper Stockham had 85,213 or 23.0% of the total votes. Diana DeGette had 272,892 or 73.8% of the total votes. Raymon Anthony Doane had 11,606 or 3.1% of the total votes. This was calculated by using the if statement in the same for loop that the county's votes were calculated in. The percent of the counties votes were calculated in a simliar process to the counties using this for loop ![Candidate Calculation](https://raw.githubusercontent.com/evanbruno617/Election_Analysis/main/Resources/Candidate_info_calculated.png)
* Dianna DeGette won with 272,892 votes and 73.8% of the total votes. This was calculated the same way with Denver county by using this if statement above. 

## Summary

This script provided can be used for any future elections held. There are only a few modifications needed in order for it to be successful. First, voting data will be provided with new candidates. In this code here you'll need to replace the election_results.csv with the name of the new data sheet provided or if you already know where the sheet is located you can get rid of "os.path.join" and make the variable equal to the path of where the file is located. You are also able to edit what the heading of the information is by changing the information typed in "election_results" and "county_turnout". This data will prove to be very useful for your further elections as it quickly counts and collect all of the voting data in a timely manner no matter the amount of candidates nor counties used.

