LETTER_PATH = "16_mail_merge/Input/Letters/starting_letter.txt"
NAMES_PATH = "16_mail_merge/Input/Names/invited_names.txt"
OUTPUT_PATH = "16_mail_merge/Output/ReadyToSend"
REPLACE_TEXT = "[name]"

with open(LETTER_PATH) as starting_letter:
    initial_text = starting_letter.read()
    with open(NAMES_PATH) as names:
        for name in names.readlines():
            final_name = name.strip().title()
            new_text = initial_text.replace(REPLACE_TEXT, final_name)
            new_file = OUTPUT_PATH + f"/letter_for_{final_name}.txt"
            with open(new_file, mode="w") as output:
                output.write(new_text)
