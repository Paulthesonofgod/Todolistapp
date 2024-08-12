date = input("Enter today's date: ")
Bible_Passage = input("Where in the Bible did you study:")
journal = input("What did you learn:\n")

with open(f"../journal/{date}.txt", 'w') as file:
    file.write(Bible_Passage + 2 * "\n")
    file.write(journal)
