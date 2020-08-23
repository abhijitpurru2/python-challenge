import csv

path = "Resources/election_data.csv"
with open(path, 'r') as electionData:
    election = csv.reader(electionData, delimiter=",")
    next(election)

    candidates = {}

    for row in election:
        if row[2] not in candidates.keys():
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

    totalVotes = sum([x for x in candidates.values()])
    output = f"Election Results\n-------------------------\nTotal Votes: {totalVotes}\n-------------------------\n"

    for row in candidates:
        candidateVotes = candidates[row]
        output += f"{row}: {round((candidateVotes/totalVotes)*100,3)}% ({candidateVotes})\n"

    winningCan = max(candidates, key=candidates.get)
    output += f"-------------------------\nWinner: {winningCan}\n-------------------------"
    print(output)

with open("analysis/output.txt", "w+") as data:
    data.write(output)