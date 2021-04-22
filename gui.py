import tkinter as tk
from tkinter import filedialog, Text
_bg_color='#ffff64'
_fg_color='#000000'
_font = ("Segoe UI", 12)

class Gui:
    def __init__(self, height, width):
        root = tk.Tk()
        root.wm_attributes("-topmost", 1)
        scrollbar = tk.Scrollbar(root)
        self.text = tk.Text(
            root, 
            height=height, 
            width=width, 
            bg=_bg_color, 
            fg=_fg_color, 
            state=tk.DISABLED,
            font=_font)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(side=tk.LEFT, fill=tk.Y)
        scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrollbar.set)
        self.__root = root
    def set_text(self, text):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, text)
        self.text.config(state=tk.DISABLED)
    def run(self):
        self.__root.mainloop()