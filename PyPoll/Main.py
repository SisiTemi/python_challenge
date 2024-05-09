import pandas as pd
import csv
#Load the data
df = pd.read_csv('C:/Users/temmw/python_challenge/PyPoll/Resources/election_data.csv')
print(df.columns)
# Calculate the total number of votes
total_votes = df["Ballot ID"].count()
# Calculate the number of votes for each candidate
candidates = df['Candidate'].unique()

# Calculate the percentages of votes for each candidate
candidate_votes = df['Candidate'].value_counts()
candidate_percentages = candidate_votes * 100

# Find the winner
winner = candidate_votes.idxmax()
#Analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
#Export Text file
import csv

with open('C:/Users/temmw/Downloads/PypollAnalysis.ipynb', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Total Votes: {369711}"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})"])
    writer.writerow(["-------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["-------------------------"])
