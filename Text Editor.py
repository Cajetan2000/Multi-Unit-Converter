import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser




window = Tk()
window.title("IT Project")
# window.iconbitmap(default="flower.ico")

window.geometry("1200x640")
window.configure(bg='blue')

global current_file
current_file = False
global selected
selected = False


# create new file
def create_file():
    text_box.delete("1.0", END)
    window.title("New File")
    status_bar.config(text="New File      ")
    global current_file
    current_file = False


# open file function
def open_file():
    text_box.delete("1.0", END)
    # fetch file name
    text_file = filedialog.askopenfilename(initialdir="C:/project/", title="Open Files", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*html"), ("Python Files", "*py"), ("Word Documents", "*docx"),
        ("All Files", "*.*")))
    # Current_file
    if text_file:
        global current_file
        current_file = text_file
    name = text_file
    status_bar.config(text=f"{name}     ")
    name = name.replace("C:/User/", " ")
    window.title(f"{name}")
    # open file
    text_file = open(text_file, "r")
    content = text_file.read()
    # insert file into text_box
    text_box.insert(END, content)
    # close the opened file
    text_file.close()


# save_as function
def save_as():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/project/", title="Save File",
                                             filetypes=(
                                                 ("Text Files", "*.txt"), ("HTML Files", "*html"),
                                                 ("Python Files", "*py"),
                                                 ("Word Documents", "*docx"), ("All Files", "*.*")))
    if text_file:
        # update status bar
        name = text_file
        name = name.replace("C:/User/", " ")
        window.title(f"{name}")
        status_bar.config(text=f"Saved: {name}     ")

        # save file
        text_file = open(text_file, "w")
        text_file.write(text_box.get("1.0", END))
        # close file
        text_file.close()


def save_file():
    global current_file
    if current_file:
        text_file = open(current_file, "w")
        text_file.write(text_box.get("1.0", END))
        # close file
        text_file.close()
        status_bar.config(text=f"Saved: {current_file}     ")
    else:
        save_as()

    # cut function


def cut_text(e):
    global selected
    # check if keyboard is used
    if e:
        selected = window.clipboard_get()
    else:
        if text_box.selection_get():
            # get selected text
            selected = text_box.selection_get()
            # delete selected text
            text_box.delete("sel.first", "sel.last")
            # clear the clipboard and append
            window.clipboard_clear()
            window.clipboard_append(selected)


# copy function
def copy_text(e):
    global selected
    # check weather keyboard is used
    if e:
        selected = window.clipboard_get()

    if text_box.selection_get():
        # get selected text
        selected = text_box.selection_get()
        # clear the clipboard and append
        window.clipboard_clear()
        window.clipboard_append(selected)


# paste function
def paste_text(e):
    global selected
    # check if keyboard is used
    if e:
        selected = window.clipboard_get()
    else:
        if selected:
            position = text_box.index(INSERT)
            text_box.insert(position, selected)


# bold funtion
def bold_text():
    # create a font
    bold_font = font.Font(text_box, text_box.cget("font"))
    bold_font.configure(weight="bold")
    # create a tag
    text_box.tag_configure("bold", font=bold_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "bold" in current_tags:
        text_box.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_box.tag_add("bold", "sel.first", "sel.last")


# italics function
def italics_text():
    # create a font
    italics_font = font.Font(text_box, text_box.cget("font"))
    italics_font.configure(slant="italic")
    # create a tag
    text_box.tag_configure("italic", font=italics_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "italic" in current_tags:
        text_box.tag_remove("italic", "sel.first", "sel.last")
    else:
        text_box.tag_add("italic", "sel.first", "sel.last")




# font size function
def two_fonts():
    # create a font
    two_font = font.Font(text_box, text_box.cget("font"))
    two_font.configure(weight=0, size=2)
    # create a tag
    text_box.tag_configure("two", font=two_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has been set

    if "two " in current_tags:
        text_box.tag_remove("two", "sel.first", "sel.last")
    else:
        text_box.tag_add("two", "sel.first", "sel.last")


def three_fonts():
    # create a font
    three_font = font.Font(text_box, text_box.cget("font"))
    three_font.configure(size=3)
    # create a tag
    text_box.tag_configure("three", font=three_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "three" in current_tags:
        text_box.tag_remove("three", "sel.first", "sel.last")
    else:
        text_box.tag_add("three", "sel.first", "sel.last")


def four_fonts():
    # create a font
    four_font = font.Font(text_box, text_box.cget("font"))
    four_font.configure(size=4)
    # create a tag
    text_box.tag_configure("four", font=four_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "four" in current_tags:
        text_box.tag_remove("four", "sel.first", "sel.last")
    else:
        text_box.tag_add("four", "sel.first", "sel.last")


def five_fonts():
    # create a font
    five_font = font.Font(text_box, text_box.cget("font"))
    five_font.configure(size=5)
    # create a tag
    text_box.tag_configure("five", font=five_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "five" in current_tags:
        text_box.tag_remove("five", "sel.first", "sel.last")
    else:
        text_box.tag_add("five", "sel.first", "sel.last")


def six_fonts():
    # create a font
    six_font = font.Font(text_box, text_box.cget("font"))
    six_font.configure(size=6)
    # create a tag
    text_box.tag_configure("six", font=six_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "six" in current_tags:
        text_box.tag_remove("six", "sel.first", "sel.last")
    else:
        text_box.tag_add("six", "sel.first", "sel.last")


def seven_fonts():
    # create a font
    seven_font = font.Font(text_box, text_box.cget("font"))
    seven_font.configure(size=7)
    # create a tag
    text_box.tag_configure("seven", font=seven_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "seven" in current_tags:
        text_box.tag_remove("seven", "sel.first", "sel.last")
    else:
        text_box.tag_add("seven", "sel.first", "sel.last")


def eight_fonts():
    # create a font
    eight_font = font.Font(text_box, text_box.cget("font"))
    eight_font.configure(size=8)
    # create a tag
    text_box.tag_configure("eight", font=eight_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "eight" in current_tags:
        text_box.tag_remove("eight", "sel.first", "sel.last")
    else:
        text_box.tag_add("eight", "sel.first", "sel.last")


def nine_fonts():
    # create a font
    nine_font = font.Font(text_box, text_box.cget("font"))
    nine_font.configure(size=9)
    # create a tag
    text_box.tag_configure("nine", font=nine_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "nine" in current_tags:
        text_box.tag_remove("nine", "sel.first", "sel.last")
    else:
        text_box.tag_add("nine", "sel.first", "sel.last")


def ten_fonts():
    # create a font
    ten_font = font.Font(text_box, text_box.cget("font"))
    ten_font.configure(size=10)
    # create a tag
    text_box.tag_configure("ten", font=ten_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "ten" in current_tags:
        text_box.tag_remove("line", "sel.first", "sel.last")
    else:
        text_box.tag_add("ten", "sel.first", "sel.last")


def eleven_fonts():
    # create a font
    eleven_font = font.Font(text_box, text_box.cget("font"))
    eleven_font.configure(size=11)
    # create a tag
    text_box.tag_configure("eleven", font=eleven_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "eleven" in current_tags:
        text_box.tag_remove("eleven", "sel.first", "sel.last")
    else:
        text_box.tag_add("eleven", "sel.first", "sel.last")


def twelve_fonts():
    # create a font
    twelve_font = font.Font(text_box, text_box.cget("font"))
    twelve_font.configure(size=12)
    # create a tag
    text_box.tag_configure("twelve", font=twelve_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "twelve" in current_tags:
        text_box.tag_remove("twelve", "sel.first", "sel.last")
    else:
        text_box.tag_add("twelve", "sel.first", "sel.last")


def thirteen_fonts():
    # create a font
    thirteen_font = font.Font(text_box, text_box.cget("font"))
    thirteen_font.configure(size=13)
    # create a tag
    text_box.tag_configure("line", font=thirteen_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "line" in current_tags:
        text_box.tag_remove("line", "sel.first", "sel.last")
    else:
        text_box.tag_add("line", "sel.first", "sel.last")


def fourteen_fonts():
    # create a font
    fourteen_font = font.Font(text_box, text_box.cget("font"))
    fourteen_font.configure(size=14, )
    # create a tag
    text_box.tag_configure("fourteen", font=fourteen_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "fourteen" in current_tags:
        text_box.tag_remove("capo", "sel.first", "sel.last")

    else:
        text_box.tag_add("fourteen", "sel.first", "sel.last")

#font style functions
def rockwell():
    # create a font
    arial_font = font.Font(text_box, text_box.cget("font"))
    arial_font.configure(family="Rockwell" )
    # create a tag
    text_box.tag_configure("rock", font=arial_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "rock" in current_tags:
        text_box.tag_remove("rock", "sel.first", "sel.last")

    else:
        text_box.tag_add("rock", "sel.first", "sel.last")

def brush_script_mt():
    # create a font
    brush_font = font.Font(text_box, text_box.cget("font"))
    brush_font.configure(family="Brush Script MT")
    # create a tag
    text_box.tag_configure("brush", font=brush_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "brush" in current_tags:
        text_box.tag_remove("brush", "sel.first", "sel.last")

    else:
        text_box.tag_add("brush", "sel.first", "sel.last")

def calibri():
    # create a font
    cali_font = font.Font(text_box, text_box.cget("font"))
    cali_font.configure(family="Calibri")
    # create a tag
    text_box.tag_configure("cali", font=cali_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "cali" in current_tags:
        text_box.tag_remove("cali", "sel.first", "sel.last")

    else:
        text_box.tag_add("cali", "sel.first", "sel.last")

def calibri_light():
    # create a font
    calibri_font = font.Font(text_box, text_box.cget("font"))
    calibri_font.configure(family="Calibri Light")
    # create a tag
    text_box.tag_configure("calit", font=calibri_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "calit" in current_tags:
        text_box.tag_remove("calit", "sel.first", "sel.last")

    else:
        text_box.tag_add("calit", "sel.first", "sel.last")

def candara():
    # create a font
    candara_font = font.Font(text_box, text_box.cget("font"))
    candara_font.configure(family="Candara")
    # create a tag
    text_box.tag_configure("canda", font=candara_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "canda" in current_tags:
        text_box.tag_remove("canda", "sel.first", "sel.last")

    else:
        text_box.tag_add("canda", "sel.first", "sel.last")

def ink_free():
    # create a font
    ink_font = font.Font(text_box, text_box.cget("font"))
    ink_font.configure(family="Ink Free")
    # create a tag
    text_box.tag_configure("ink", font=ink_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "ink" in current_tags:
        text_box.tag_remove("ink", "sel.first", "sel.last")

    else:
        text_box.tag_add("ink", "sel.first", "sel.last")

def lucida_handwriting():
    # create a font
    lucida_font = font.Font(text_box, text_box.cget("font"))
    lucida_font.configure(family="Lucida Handwriting")
    # create a tag
    text_box.tag_configure("lucid", font=lucida_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "lucid" in current_tags:
        text_box.tag_remove("lucid", "sel.first", "sel.last")

    else:
        text_box.tag_add("lucid", "sel.first", "sel.last")

def times_new_roman():
    # create a font
    times_new_font = font.Font(text_box, text_box.cget("font"))
    times_new_font.configure(family="Times New Roman  ")
    # create a tag
    text_box.tag_configure("times", font=times_new_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has beeen set

    if "times" in current_tags:
        text_box.tag_remove("times", "sel.first", "sel.last")

    else:
        text_box.tag_add("times", "sel.first", "sel.last")



# underline
def text_underline():
    # create a font
    underline_font = font.Font(text_box, text_box.cget("font"))
    underline_font.configure(underline=True)
    # create a tag
    text_box.tag_configure("line", font=underline_font)
    # define current tags
    current_tags = text_box.tag_names("sel.first")
    # if statement to see if tag has been set

    if "line" in current_tags:
        text_box.tag_remove("line", "sel.first", "sel.last")
    else:
        text_box.tag_add("line", "sel.first", "sel.last")


# change selected text color
def text_color():
    # choose color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        status_bar.config(text=my_color)
        # create a font color
        color_font = font.Font(text_box, text_box.cget("font"))

        # create a tag
        text_box.tag_configure("colored", font=color_font, foreground=my_color)
        # define current tags
        current_tags = text_box.tag_names("sel.first")
        # if statement to see if tag has beeen set

        if "colored" in current_tags:
            text_box.tag_remove("colored", "sel.first", "sel.last")
        else:
            text_box.tag_add("colored", "sel.first", "sel.last")


#fuctions for


#bakground colo
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        text_box.config(bg=my_color)


# all text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        text_box.config(fg=my_color)


# count number of words and char
def num_chr_words():
    text_content = text_box.get("1.0", END)
    # turn content into number
    characters_in_texbox = len(text_content)
    words_in_textbox = len(text_content.split())
    # update status bar
    status_bar.config(text=str(characters_in_texbox - 1) + "Characters, " + str(words_in_textbox) + "Words")


# initialize the number of words and char count
def init_word_char_count():
    num_chr_words()
    status_bar.after(1000, init_word_char_count)


# toolbar frame
toolbar_frame = Frame(window)
toolbar_frame.pack(fill=X)

# create frame
frame = Frame(window, bg="red")
frame.pack(padx=8, pady=8)

# creat a sscroll bar
text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)
# Horizontal scrollbar
horizon_scrol = Scrollbar(frame, orient="horizontal")
horizon_scrol.pack(side=BOTTOM, fill=X)
# creat text box
text_box = Text(frame, width=120, height=30, font=("helvetica", 12), background="white", foreground="black", undo=True,
                yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=horizon_scrol.set)
text_box.pack()

# configure
text_scroll.config(command=text_box.yview)
horizon_scrol.config(command=text_box.xview)
# create main menu
m_menu = Menu(window)
window.config(menu=m_menu)

# create file menu
file_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="save", command=save_file)
file_menu.add_command(label="save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)


# creat edit menu
edit_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut        ", command=lambda: cut_text(False), accelerator="Ctrl+X")
edit_menu.add_command(label="Copy     ", command=lambda: copy_text(False), accelerator="Ctrl+C")
edit_menu.add_command(label="Paste     ", command=lambda: paste_text(False), accelerator="Ctrl+V")
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=text_box.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=text_box.edit_redo, accelerator="Ctrl+Y")

# color menu
color_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selected Text", command=text_color)
color_menu.add_command(label="All Text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# fonts menu
font_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="Font Size", menu=font_menu)
font_menu.add_command(label="2", command=two_fonts)
font_menu.add_command(label="3", command=three_fonts)
font_menu.add_command(label="4", command=four_fonts)
font_menu.add_command(label="5", command=five_fonts)
font_menu.add_command(label="6", command=six_fonts)
font_menu.add_command(label="7", command=seven_fonts)
font_menu.add_command(label="8", command=eight_fonts)
font_menu.add_command(label="9", command=nine_fonts)
font_menu.add_command(label="10", command=ten_fonts)
font_menu.add_command(label="11", command=eleven_fonts)
font_menu.add_command(label="12", command=twelve_fonts)
font_menu.add_command(label="13", command=thirteen_fonts)
font_menu.add_command(label="14", command=fourteen_fonts)
#text style menu
style_menu = Menu(m_menu, tearoff=False)
m_menu.add_cascade(label="Font Style", menu=style_menu)
style_menu.add_command(label="Rockwell", command=rockwell)
style_menu.add_command(label="Brush Script MT", command=brush_script_mt)
style_menu.add_command(label="Calibri", command=calibri)
style_menu.add_command(label="Calibri Light", command=calibri_light)
style_menu.add_command(label="Candara", command=candara)
style_menu.add_command(label="Ink Free", command=ink_free)
style_menu.add_command(label="Lucida Handwriting", command=lucida_handwriting)
style_menu.add_command(label="Times New Roman", command=times_new_roman)



# stutus bar
status_bar = Label(frame, text="Ready   ", anchor=E)
status_bar.pack(side=BOTTOM, fill=X, ipady=10)

window.bind("<Control-Key-x>", cut_text)
window.bind("<Control-Key-c>", copy_text)
window.bind("<Control-Key-v>", paste_text)

# create button

# bold button
bold_botton = Button(toolbar_frame, text="Bold", command=bold_text)
bold_botton.grid(row=0, column=0, sticky=W, padx=7)
# italics button
italics_botton = Button(toolbar_frame, text="Italics", command=italics_text)
italics_botton.grid(row=0, column=1, padx=7)

# text color button
text_color_button = Button(toolbar_frame, text="Text Color", command=text_color)
text_color_button.grid(row=0, column=5, padx=7)
# text underline button
text_underline_button = Button(toolbar_frame, text="Underline", command=text_underline)
text_underline_button.grid(row=0, column=6, padx=7)

init_word_char_count()
window.mainloop()
