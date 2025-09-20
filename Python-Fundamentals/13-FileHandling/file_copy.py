
fr = open("file.txt", "r")
fw = open("copy.txt", "w")

for line in fr:
    fw.write(line)

fr.close()
fw.close()