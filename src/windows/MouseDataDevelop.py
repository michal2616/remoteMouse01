import Tkinter as tk

root = tk.Tk()


screen_width = root.winfo_vrootwidth()
screen_height = root.winfo_vrootheight()

print screen_width
print screen_height
root.config(cursor="none")
# while 1:
#
#     print "cos tam"