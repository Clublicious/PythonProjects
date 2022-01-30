from tkinter import *
import random
from tkinter import messagebox

## Copyright Thomas Van Hoof

LENGHT_PASSWORD = ["5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","128","256","512","1024"]

def generating_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters= variable.get()
    nr_symbols = checked_state_symbols.get()
    nr_numbers = checked_state.get()
    how_many = passwords_entry.get()


    

    nr_letters = int(nr_letters)
    number = int(int(nr_letters) / 3)
    symbol = number
    letter = int(nr_letters) - number - symbol
    
    if how_many == '':
        messagebox.showinfo('Not Valid', f'Give amount of passwords')
    else:
        while int(how_many) != 0:
            letters_loop = 0
            symbols_loop = 0
            numbers_loop = 0
            everything = []
            if nr_symbols == 1 and nr_numbers == 1:
                while letters_loop != letter:
                    choice_letters = random.randrange(0,52)
                    everything.append(letters[choice_letters])
                    letters_loop += 1
                while symbols_loop != symbol:
                    choice_symbols = random.randrange(0,9)
                    everything.append(symbols[choice_symbols])
                    symbols_loop += 1
                while numbers_loop != number:
                    choice_numbers = random.randrange(0,10)
                    everything.append(numbers[choice_numbers])
                    numbers_loop += 1
            elif nr_symbols == 1:
                symbol = int(nr_letters / 2)
                letter = nr_letters - symbol
                while letters_loop != letter:
                    choice_letters = random.randrange(0,52)
                    everything.append(letters[choice_letters])
                    letters_loop += 1
                while symbols_loop != symbol:
                    choice_symbols = random.randrange(0,9)
                    everything.append(symbols[choice_symbols])
                    symbols_loop += 1
            elif nr_numbers == 1:
                number = int(nr_letters / 2)
                letter = nr_letters - number
                while letters_loop != letter:
                    choice_letters = random.randrange(0,52)
                    everything.append(letters[choice_letters])
                    letters_loop += 1
                while numbers_loop != number:
                    choice_numbers = random.randrange(0,10)
                    everything.append(numbers[choice_numbers])
                    numbers_loop += 1
            else:
                letter = nr_letters
                while letters_loop != letter:
                    choice_letters = random.randrange(0,52)
                    everything.append(letters[choice_letters])
                    letters_loop += 1


            random.shuffle(everything)

            everything = "".join(everything)
            how_many = int(how_many)
            if how_many == 1:
                output_text.insert(END,everything)
            else:
                output_text.insert(END,everything+"\n")
            how_many -= 1
            
        window.clipboard_clear()
        window.clipboard_append(output_text.get(1.0, 'end'))
        window.update()

def clear_screen_now():
    output_text.delete(1.0, 'end')

window = Tk()
window.title("Epic Password Generator")

titel_label = Label(text='(Epic) Password Generator', font=('Ariel', 24), fg='green')
titel_label.grid(column=0, row=0, columnspan=2)
letters_label = Label(text='Length of password? : ')
letters_label.grid(column=0, row= 1, sticky="e")
variable = StringVar(window)
variable.set(" Length ")
letters_entry = OptionMenu(window, variable, *LENGHT_PASSWORD)
letters_entry.grid(column=1, row=1, sticky='w')
numbers_label = Label(text='Include Numbers?: ')
numbers_label.grid(column=0, row= 2, sticky="e")
checked_state = IntVar()
numbers_entry = Checkbutton(text="(1234...)", variable=checked_state)
numbers_entry.grid(column=1, row=2, sticky='w')
symbols_label = Label(text='Include Symbols?: ')
symbols_label.grid(column=0, row= 3, sticky="e")
checked_state_symbols = IntVar()
symbols_entry = Checkbutton(text="(!#$%...)", variable=checked_state_symbols)
symbols_entry.grid(column=1, row=3, sticky='w')
passwords_label = Label(text='How many passwords?: ')
passwords_label.grid(column=0, row= 4, sticky="e")
passwords_entry = Entry()
passwords_entry.grid(column=1, row=4, sticky='w')

generate_button = Button(text='Generate Password', command=generating_password)
generate_button.grid(column=0, row=5, columnspan=2)

output_label = Label(text='Output Passwords')
output_label.grid(column=0, row=6, columnspan=2)
output_text = Text(height = 20, width = 52)
output_text.grid(column=0, row=7, columnspan=2)

clear_screen = Button(text='Clear Screen', command=clear_screen_now)
clear_screen.grid(column=0, row=8, columnspan=2)

copyright_label = Label(text='© Van Hoof Thomas')
copyright_label.grid(column=0, row=9, columnspan=2)



window.mainloop()