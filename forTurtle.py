class TurtleMsg:
    def msgForTurtle(input_str):
        tokens = input_str.split()
        # Create a list of lists
        result_list = []
        # Iterate over the tokens and create sublists
        for i in range(0, len(tokens), 2):
            word = tokens[i].capitalize()  # Capitalize the first letter of the word
            number = int(tokens[i + 1])
            result_list.append([word, number])
        return result_list