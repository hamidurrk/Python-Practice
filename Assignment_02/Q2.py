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
    totalList = []
    for i in range(len(string_to_match)):
        matchList.append(0)
        totalList.append(0)
    print(matchList)
    for i in range(len(subStringList)):
        searchString = subStringList[i]
        print('Searching %s' %searchString)
        k = 0
        for j in range(len(file_contents) - len(subStringList[i]) + 1):
            currentString = file_contents[j:j + len(subStringList[i])]
            print(currentString)
            k += 1
            totalList[len(subStringList[i])-1] += 1
            if currentString == searchString:
                if matchList[len(searchString)-1] == 0:
                    num_matches = 0

                num_matches += 1
                matchList[len(subStringList[i])-1] = num_matches

print('Number of matches: ')
print(matchList)
print(totalList)

accuracy = []
for i in range(len(matchList)):
    accuracy.append((matchList[i]/totalList[i]) * 100)
    print('%d character match found in %d places with occurance probability of %.2f%%' % (i+1, matchList[i], accuracy[i]))
    

print(accuracy)