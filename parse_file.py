# parsing password hashes file to get rid of the plaintext and only have the password hash


file = open("hashes_parsed.txt", "w")

with open("hashes.txt") as f:
    for line in f:
        line2 = line.split(':')[0]
        file.write(line2)
        file.write('\n')

file.close()
