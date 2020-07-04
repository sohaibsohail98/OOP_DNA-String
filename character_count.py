def dataset_string(string1):
    dict = {}  # Empty dictionary

    for s in string1:
        keys = dict.keys()  # initialising the keys in the dictionary
        if s in keys:
            dict[
                s] += 1  # If it finds the character in a string, it adds 1 to the tally of how many characters there are
        else:
            dict[
                s] = 1  # Everytime, there is a new character, it adds 1 and the process repeats. It continues to find more characters
    return dict


print(dataset_string("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))