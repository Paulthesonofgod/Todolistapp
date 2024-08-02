contents = ["The lord is my shepherd", "God is great", "Baba I thank you"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/bonus/{filename}", 'w')
    file.write(content)
