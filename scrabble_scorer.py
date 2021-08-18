# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = 0

    for char in word:

        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   print("Let's play some Scrabble!\n")
   user_input = input("Enter a word.")

   return user_input


def simple_scorer(word):
    score = 0
    for letter in word.lower():
        score += 1

    return score

def vowel_bonus_scorer(word):
    vowels = "aeiou"
    score = 0
    for letter in word.lower():
        if letter in vowels:
            score += 3
        else:
            score += 1

    return score

def scrabble_scorer(word):
    score = 0

    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]

    return score

scoring_algorithms = ()

def scorer_prompt():
    scorer_prompt = "Which scoring algorithm would you like to use?"
    user_selection = 3

    while user_selection > 2:
        for index, algorithm in enumerate(scoring_algorithms):
            print(f'{index} - {algorithm["name"]}: {algorithm["description"]}')

        user_selection = int(input("Enter 0, 1, or 2:"))
    
    selected_score_algorithm_dict = scoring_algorithms[user_selection]

    return selected_score_algorithm_dict 

def transform(chosen_dict):
    new_dict = {}

    for (key, value) in chosen_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict

new_point_structure = transform(old_point_structure)

simple_scorer_dict = {
    "name": "Simple Scorer",
    "description": "Each letter is worth 1 point.",
    "score_function": simple_scorer
}

vowel_bonus_scorer_dict = {
    "name": "Bonus Vowels",
    "description": "Vowels are 3 pts, consonants are 1 pt.",
    "score_function": vowel_bonus_scorer
}

old_scrabble_scorer_dict = {
    "name": "Scrabble",
    "description": "The traditional scoring algorithm.",
    "score_function": scrabble_scorer
}

scoring_algorithms = (
    simple_scorer_dict,
    vowel_bonus_scorer_dict, 
    old_scrabble_scorer_dict
)

def run_program():
    word = initial_prompt()
    selected_score_algorithm_dict = scorer_prompt()
    score = selected_score_algorithm_dict["score_function"](word)
    
    print(f'''
The word you entered was "{word}".
You selected the "{selected_score_algorithm_dict["name"]}" scoring algorithm which {selected_score_algorithm_dict["description"]}.
Your word is worth {score} points!''')

run_program()
