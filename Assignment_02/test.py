filename = 'random_chars.txt'

string_to_match = 'fabiha'

def genSubString(string):
    subString = []
    for i in range(len(string)):
        for j in range(len(string) - i + 1):
            if string[j:j+i] != '':
                subString.append(string[j:j+i])
    subString.append(string)
    return subString

subStringList = genSubString(string_to_match)
print(subStringList)
print(len(subStringList))


with open(filename, 'r') as f:

    file_contents = f.read()

    num_matches = 0
    num_partial_matches = []
    matchList = []
    for i in range(len(string_to_match)):
        matchList.append(0)
    print(matchList)
    for i in range(len(subStringList)):
        searchString = subStringList[i]
        print('Searching %s' %searchString)
        for j in range(len(file_contents) - len(subStringList[i]) + 1):
            currentString = file_contents[j:j + len(subStringList[i])]
            print(currentString)
            if currentString == searchString:
                if matchList[len(searchString)-1] == 0:
                    num_matches = 0

                num_matches += 1
                matchList[len(subStringList[i])-1] = num_matches

print('Number of matches: ')
print(matchList)

for i in range(len(matchList)):
    print('%d character match found in %d places' % (i+1, matchList[i]))