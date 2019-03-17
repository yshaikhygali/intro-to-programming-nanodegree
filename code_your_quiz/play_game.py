# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

parts_of_speech = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""


def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return word
    return None


def play_game(ml_string, parts_of_speech):
    replaced = []
    # your code here
    ml = ml_string.split(' ')
    for m in ml:
        if word_in_pos(m, parts_of_speech) is None:
            replaced.append(m)
        else:
            replaced.append('corgi,')

    return ' '.join(replaced)


print(play_game(test_string, parts_of_speech))
print(word_in_pos('PLAC', parts_of_speech))
