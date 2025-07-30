import pandas

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dictionary = {value["letter"]:value['code'] for (key,value) in df.iterrows()}
print(new_dictionary)
#TODO 2. use recursion and handle KeyError: 
def recursion_function():
    user_input = input("enter a word: ").upper()
    try:
        coded_names = [new_dictionary[code] for code in user_input]
    except KeyError:
        print("only letters in the alphabet please! ")
        recursion_function()
    else:
        print(coded_names)
recursion_function()
