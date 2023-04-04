# define the filename of the random alphabet file
filename = 'random_chars.txt'

# define the string to match
string_to_match = 'example'

# open the file in read mode
with open(filename, 'r') as f:

    # read the entire file contents
    file_contents = f.read()

    # initialize the number of matches and partial matches to zero
    num_matches = 0
    num_partial_matches = 0

    # iterate through the file contents
    for i in range(len(file_contents) - len(string_to_match) + 1):
        #print(file_contents[i:i+len(string_to_match)])
        
        # check if the current substring matches the provided string
        if file_contents[i:i+len(string_to_match)] == string_to_match:
            num_matches += 1
            print ('num_matches')
        # check if the current substring partially matches the provided string
        elif string_to_match in file_contents[i:i+len(string_to_match)]:
            num_partial_matches += 1

    # calculate the accuracy of the match
    accuracy = (num_matches / (len(file_contents) - len(string_to_match) + 1)) * 100

    # print the results
    print('Number of matches: %d' % num_matches)
    print('Number of partial matches: %d' % num_partial_matches)
    print('Accuracy of match: %0.2f%%' % accuracy)
