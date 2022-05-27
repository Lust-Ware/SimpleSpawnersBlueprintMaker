import os
import re
import tkinter as tk
import tkinter.messagebox
import sys

root = tk.Tk()
root.withdraw()
tkinter.messagebox.showinfo("Information!","You MUST run Ark Code Generator first to get the blueprint locations!\nOtherwise this program will not work.")
regexx = r"SpawnDino (\".*\")"
Result = {}
res = ""
tick = 0


if os.path.isfile('./Output.txt'):
    with open('./Output.txt', 'r', encoding='utf-8') as f:
        readfiles = f.read()
else:
    tkinter.messagebox.showerror("Error!","Output.txt does not exist in this folder, make sure you run the ARK Code Generator first!")
    sys.exit(0)
    

Result[0] = re.findall(regexx, readfiles)

for stuff in Result[0]:
    if tick == 1000:
        with open('./NewOutput.txt', 'w', encoding='utf-8') as ff:
            ff.write(res)
        tkinter.messagebox.showinfo("Limit of 1000 Reached!","Your Blueprint paths is in the \"NewOutput.txt\" file.")
        sys.exit()
    res += ('{}'.format(stuff+";"))
    tick += 1

with open('./NewOutput.txt', 'w', encoding='utf-8') as ff:
    ff.write(res)

tkinter.messagebox.showinfo("Success!","Your Blueprint paths is in the \"NewOutput.txt\" file.")