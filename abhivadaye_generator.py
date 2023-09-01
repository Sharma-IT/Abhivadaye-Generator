import os
import sys

# Resizes console window for Windows operating systems

CONSOLE_WIDTH = 135
CONSOLE_HEIGHT = 20

os.system(f'mode {CONSOLE_WIDTH},{CONSOLE_HEIGHT}')

# Resizes console window for Unix operating systems

rows = 20
columns = 135

sys.stdout.write("\x1b[8;{rows};{columns}t".format(rows=rows, columns=columns))
def get_input(prompt, input_type=str):
    while True:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            print("\nInvalid input. Please enter a valid value.")
            
def generate_abhivādaye_sanskrit(prāvāra, gotra, sūtrakāra, vedaśākhā, name):
    return f'''
चतुस्सगारा पर्यन्तं गो ब्रह्मणेभ्यः
शुभम भवतु {prāvāra}
त्रिय रुषेय प्रवरणविथा {gotra} गोत्र
{sūtrakāra} सूत्रहा {vedaśākhā}
{name} शर्मः अहम् भो अभिवादये॥'''

def generate_abhivādaye_english(prāvāra, gotra, sūtrakāra, vedaśākhā, name):
    return f'''
chatussagara paryantam go brahmaṇebhyaḥ
shubham bhavatu {prāvāra}
triy ariṣayaḥ pravaraṇa vitā {gotra} gotra
{sūtrakāra} sūtraḥ {vedaśākhā}
{name} śarmaḥ aham bho abhivādaye ॥'''

def generate_abhivādaye_file(abhivādaye, lang_choice):
    filename = "abhivādaye_output.txt"
    lang = "Sanskrit" if lang_choice.upper() == 'S' else "English"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Generated abhivādaye in {lang}:")
        file.write(abhivādaye)

    print(f"\nGenerated abhivādaye has been saved in '{filename}'.")

def generate_abhivādaye():
    lang_choice = input("\nEnter 'S' for Sanskrit or 'E' for English or 'exit' to exit script: ")

    if lang_choice.upper() == 'S':
        abhivādaye = abhivādaye_sanskrit_inputs()
        generate_abhivādaye_file(abhivādaye, lang_choice)
    elif lang_choice.upper() == 'E':
        abhivādaye = abhivādaye_english_inputs()
        generate_abhivādaye_file(abhivādaye, lang_choice)
    elif lang_choice.lower() == 'exit':
        raise SystemExit
    else:
        print("Invalid choice. Please enter 'S' for Sanskrit or 'E' for English.")

def abhivādaye_english_inputs():
    prāvāra = get_input("\nEnter names of Ṛṣayoḥ (i.e. prāvāra, e.g., Aangirasa, Bharaspatya, Bharadwajasya): ")
    gotra = get_input("\nEnter gotra: ")
    sūtrakāra = get_input("\nEnter sūtrakāra: ")
    vedaśākhā = get_input("\nEnter vedaśākhā: ")
    name = get_input("\nEnter your first name: ")

    abhivādaye_english_inputs = generate_abhivādaye_english(prāvāra, gotra, sūtrakāra, vedaśākhā, name)
    print("\nGenerated abhivādaye in English:")
    print(abhivādaye_english_inputs)
    return abhivādaye_english_inputs

def abhivādaye_sanskrit_inputs():
    prāvāra = get_input("\nEnter names of Ṛṣayoḥ in Sanskrit (i.e. prāvāra, e.g., आङ्गिरस, भारस्पत्य, भारद्वाजस्य): ")
    gotra = get_input("\nEnter gotra: ")
    sūtrakāra = get_input("\nEnter sūtrakāra: ")
    vedaśākhā = get_input("\nEnter vedaśākhā: ")
    name = get_input("\nEnter your first name: ")

    abhivādaye_sanskrit_inputs = generate_abhivādaye_sanskrit(prāvāra, gotra, sūtrakāra, vedaśākhā, name)
    print("\nGenerated abhivādaye in Sanskrit:")
    print(abhivādaye_sanskrit_inputs)
    return abhivādaye_sanskrit_inputs

def save_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def load_from_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    else:
        return None

def main():
    print('''
अभिवादये जननी | abhivādaye generator

Created by Shubham Sharma. śrī viśvāmitra, śrī ātkila, śrī kātya. kātyāyana gotraḥ. kātyāyana sūtraḥ. śukla yajurvedaḥ, śaunaka śākhā.

Note: Devanāgarī characters may not display correctly. Copy and paste output into a text editor with Uincode support.''')

    while True:
        print('''
Choose an option:

1. Generate abhivādaye

2. Load abhivādaye

3. Exit''')

        choice = get_input("\nEnter your choice: ", int)

        if choice == 1:
            generate_abhivādaye()
        elif choice == 2:

            filename = 'abhivādaye_output.txt'
            
            if content := load_from_file(filename):

                print("\nLoaded abhivādaye:\n")
                print(content)

            else:
                print(f"\nFile '{filename}' not found.")
                    
        elif choice == 3:
            print("\nExiting the program.\n")
            break
        
        else:
            print("\nInvalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()