import pandas

DATA_PATH = "18_nato_alphabet/nato_phonetic_alphabet.csv"

data = pandas.read_csv(DATA_PATH)

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
phonetic = [data_dict[letter] for letter in word if letter in data_dict.keys()]
print(phonetic)
