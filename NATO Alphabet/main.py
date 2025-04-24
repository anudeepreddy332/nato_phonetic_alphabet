import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}
output_data = {}
is_on = True
while is_on:
    user_input = input("Enter a word: ").upper()
    if user_input == "EXIT":
        break
    output_list = [phonetic_dict[letter] for letter in user_input if letter != " "]
    output_data[user_input] = output_list
    print(output_list)

print(output_data)
df = pd.DataFrame({
    name: [" ".join(phonetics)] for name, phonetics in output_data.items()
}).T
df.columns = ["Phonetic Spelling"]
df.index.name = "Name"
print(df)
df.to_csv("nato_output_data.csv")