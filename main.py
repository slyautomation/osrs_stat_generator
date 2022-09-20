""" ---------------- ==== RUN =====---------- pyinstaller --noconsole --onefile pythonScriptName.spec"""

# Embedded file name: main.py
from PIL import Image
def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)

def create_digit_total(num):
    from PIL import Image
    length = len(str(num))
    num = str(num)
    #print(num)
    #print(num[0])
    #print(length)
    x = 0
    image_name_output = resourcePath('blank_image.png')
    mode = 'RGBA'
    w = length
    size = (25 * w, 60)
    color = (0, 0, 0, 0)
    im = Image.new(mode, size, color)
    im.save(image_name_output, 'PNG')
    im.close()
    background = Image.open(image_name_output)
    while x < length:
        filename = resourcePath(str(num[x]) + '.png')
        frontImage = Image.open(filename)
        background.paste(frontImage, (0 + x * 25, 0), frontImage.convert('RGBA'))
        x += 1
    #print("resource path:", os.path.abspath("."))
    background.save((resourcePath('images\\' + str(num) + 'total.png')), format='png')


def create_digit(num, skill):
    from PIL import Image
    length = len(str(num))
    if length > 1:
        image_name_output = resourcePath('blank_image.png')
        mode = 'RGBA'
        size = (50, 60)
        color = (0, 0, 0, 0)
        im = Image.new(mode, size, color)
        im.save(image_name_output, 'PNG')
        im.close()
        filename = resourcePath(str(num)[0] + '.PNG')

        filename1 = resourcePath(str(num)[1] + '.PNG')

        frontImage = Image.open(filename)
        secImage = Image.open(filename1)
        background = Image.open(image_name_output)
        background.paste(frontImage, (0, 0), frontImage.convert('RGBA'))
        background.paste(secImage, (24, 0), secImage.convert('RGBA'))
        background.save(resourcePath(('images/' + str(num) + skill + '.png')), format='png')
    else:
        filename = resourcePath(str(num) + '.png')
        frontImage = Image.open(filename)
        frontImage.save(resourcePath(('images\\' + str(num) + skill + '.png')), format='png')


def generate_stat_card_ttf(name):
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
    filename = resourcePath('Card.png')

    img = Image.open(filename)

    draw = ImageDraw.Draw(img)
    draw.fontmode = '1'
    font = ImageFont.FreeTypeFont('RuneScape-Chat-Bold-07.ttf', 13)
    strength = draw.text((40, 10), '73', (255, 255, 0), font=font)
    img.save(resourcePath('sample-out.png'))


def create_copy():
    filename1 = resourcePath('Card.png')
    copy = Image.open(filename1)
    copy.save(resourcePath('New.png'), format='png')


def generate_stat_card(num, skill):
    from PIL import Image
    create_digit(num, skill)
    filename = resourcePath('images\\' + str(num) + skill + '.png')
    filename1 = resourcePath('New.png')
    if num < 10:
        size = (10, 10)
    else:
        size = (15, 15)
    frontImage = Image.open(filename)
    background = Image.open(filename1)
    frontImage.thumbnail(size, Image.NORMAL)
    frontImage = frontImage.convert('RGBA')
    background = background.convert('RGBA')
    dict = {'attack':(42, 13),
     'strength':(42, 45),
     'defence':(42, 77),
     'ranged':(42, 109),
     'prayer':(42, 141),
     'magic':(42, 173),
     'runecrafting':(42, 205),
     'construction':(42, 237),
     'health':(105, 13),
     'agility':(105, 45),
     'herblore':(105, 77),
     'thieving':(105, 109),
     'crafting':(105, 141),
     'fletching':(105, 173),
     'slayer':(105, 205),
     'hunter':(105, 237),
     'mining':(168, 13),
     'smithing':(168, 45),
     'fishing':(168, 77),
     'cooking':(168, 109),
     'firemaking':(168, 141),
     'woodcutting':(168, 173),
     'farming':(168, 205)}
    dict_2 = {'attack':(59, 26),
     'strength':(59, 58),
     'defence':(59, 90),
     'ranged':(59, 122),
     'prayer':(59, 154),
     'magic':(59, 186),
     'runecrafting':(59, 218),
     'construction':(59, 250),
     'health':(122, 26),
     'agility':(122, 58),
     'herblore':(122, 90),
     'thieving':(122, 122),
     'crafting':(122, 154),
     'fletching':(122, 186),
     'slayer':(122, 218),
     'hunter':(122, 250),
     'mining':(185, 26),
     'smithing':(185, 58),
     'fishing':(185, 90),
     'cooking':(185, 122),
     'firemaking':(185, 154),
     'woodcutting':(185, 186),
     'farming':(185, 218)}
    background.paste(frontImage, dict[skill], frontImage.convert('RGBA'))
    if num < 10:
        background.paste(frontImage, dict_2[skill], frontImage.convert('RGBA'))
    else:
        background.paste(frontImage, (dict_2[skill][0] - 5, dict_2[skill][1]), frontImage.convert('RGBA'))
    background.save(resourcePath('New.png'), format='png')


def generate_total(total):
    from PIL import Image
    create_digit_total(total)
    filename = resourcePath('images\\' + str(total) + 'total.png')
    filename1 = resourcePath('New.png')
    if total > 999:
        size = (25, 25)
    else:
        if total > 99:
            size = (19, 19)
        else:
            size = (15, 15)
    frontImage = Image.open(filename)
    background = Image.open(filename1)
    frontImage.thumbnail(size, Image.NORMAL)
    frontImage = frontImage.convert('RGBA')
    background = background.convert('RGBA')
    position = (155, 250)
    if total > 999:
        background.paste(frontImage, position, frontImage.convert('RGBA'))
    else:
        if total > 99:
            background.paste(frontImage, (position[0] + 3, position[1]), frontImage.convert('RGBA'))
        else:
            background.paste(frontImage, (position[0] + 5, position[1]), frontImage.convert('RGBA'))
    background.save(resourcePath('New.png'), format='png')

import os

def ensure_dir():
    directory = os.path.dirname(resourcePath('images'))
    #print(directory)
    if not os.path.exists(resourcePath('images')):
        os.makedirs(resourcePath('images'))

ensure_dir()
skill_list = [
 'attack',
 'strength',
 'defence',
 'ranged',
 'prayer',
 'magic',
 'runecrafting',
 'construction',
 'health',
 'agility',
 'herblore',
 'thieving',
 'crafting',
 'fletching',
 'slayer',
 'hunter',
 'mining',
 'smithing',
 'fishing',
 'cooking',
 'firemaking',
 'woodcutting',
 'farming']

import tkinter
from tkinter import *
from PIL import Image, ImageTk
test = []
root = Tk()

root.title('OSRS Stat Generator')
root.geometry('670x600')
root.configure(background='#40362C')
Font_tuple = ('Unispace', 15)
filename = resourcePath('osrs_title_2.png')
image1 = Image.open(filename)
image1 = image1.convert('RGBA')
h = (500, 500)
image1.thumbnail(h, Image.NORMAL)
test1 = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test1, background='#40362C', anchor=CENTER, justify=CENTER)
label1.image = test1
label1.grid(column=0, columnspan=5, sticky='e')
x = 1
while x < 9:
    lbl = Label(root, text=(skill_list[(x - 1)]), background='#40362C', fg='yellow', padx=20)
    lbl.configure(font=Font_tuple)
    lbl.grid(column=0, row=x)
    x += 1

x = 9
while x < 17:
    lbl = Label(root, text=(skill_list[(x - 1)]), background='#40362C', fg='yellow')
    lbl.configure(font=Font_tuple)
    lbl.grid(column=2, row=(x - 8))
    x += 1

x = 17
while x < 24:
    lbl = Label(root, text=(skill_list[(x - 1)]), background='#40362C', fg='yellow')
    lbl.configure(font=Font_tuple)
    lbl.grid(column=4, row=(x - 16))
    x += 1

x = 1
while x < 9:
    txt = Entry(root, width=5, background='#40362C', fg='yellow')
    txt.insert(-1, 1)
    txt.configure(font=Font_tuple)
    test.append(txt)
    txt.grid(column=1, row=x)
    x += 1

x = 9
while x < 17:
    txt = Entry(root, width=5, background='#40362C', fg='yellow')
    txt.configure(font=Font_tuple)
    txt.insert(-1, 1)
    test.append(txt)
    txt.grid(column=3, row=(x - 8))
    x += 1

x = 17
while x < 24:
    txt = Entry(root, width=5, background='#40362C', fg='yellow')
    txt.configure(font=Font_tuple)
    txt.insert(-1, 1)
    test.append(txt)
    txt.grid(column=5, row=(x - 16))
    x += 1

total = 0
t = 0
while t < len(test):
    total += int(test[t].get())
    t += 1

lbl = Label(root, text=('Total Level: ' + str(total)), background='#40362C', fg='yellow', anchor=CENTER)
lbl.configure(font=Font_tuple)
lbl.grid(column=4, row=8, columnspan=2)



def clicked():
    x = 0
    create_copy()
    total = 0
    t = 0
    while t < len(test):
        total += int(test[t].get())
        t += 1

    lbl = Label(root, text=('Total Level: ' + str(total)), background='#40362C', fg='yellow', anchor=CENTER)
    lbl.configure(font=Font_tuple)
    lbl.grid(column=4, row=8, columnspan=2)
    while x < 23:
        generate_stat_card(int(test[x].get()), skill_list[x])
        x += 1

    generate_total(int(total))
    result = tkinter.Toplevel()
    result.title('OSRS Stat Result')
    result.configure(background='#40362C')
    canvas = Canvas(result, width=300, height=300)
    canvas.pack()
    filename = resourcePath('New.png')

    img = PhotoImage(file=filename)
    canvas.create_image(20, 20, anchor=NW, image=img)
    import os, glob
    basePath = os.path.abspath(".")
    files = glob.glob(basePath + '/images/*')
    for f in files:
        os.remove(f)
    frontImage = Image.open(filename)
    #print(basePath)
    frontImage.save(basePath + '\\Result.png', format='png')
    #print('skills stats generated!!!')
    result.mainloop()


btn = Button(root, text='Generate Stats', fg='yellow',
  command=clicked,
  background='#40362C',
  pady=0)
btn.grid(column=2, row=10, columnspan=2, pady=20)
btn.configure(font=Font_tuple)
root.mainloop()