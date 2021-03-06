import tkinter as tk
from readonly_text import ReadonlyText

_font_size = 12
_bg_color='#ffff64'
_fg_color='#000000'
_font = ("Segoe UI", _font_size)

class _Args:
    title = ''
    artist = ''

class Gui:
    def __init__(self, height, width, title):
        root = tk.Tk()
        root.wm_attributes("-topmost", 1)
        scrollbar = tk.Scrollbar(root)
        self.text = ReadonlyText(
            root, 
            height=height, 
            width=width, 
            bg=_bg_color, 
            fg=_fg_color, 
            state=tk.DISABLED,
            font=_font,
            padx = _font_size,
            pady = _font_size)
        root.resizable(False, False)
        root.title(title)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(side=tk.LEFT, fill=tk.Y)
        scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=scrollbar.set)

        root.update_idletasks()
        pad_x = 50
        pad_y = 100
        w = root.winfo_width()
        h = root.winfo_height()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = screen_width - w - pad_x
        y = screen_height - h - pad_y
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.root = root

    def set_text(self, text):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, 'reset')
        self.text.insert(tk.END, text)
        self.text.config(state=tk.DISABLED)

    def set_message(self, message, query):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, 'reset'),
        self.text.insert(tk.END, f'{message}\n', 'readonly')
        self.text.insert(tk.END, query)
        self.text.bind('<Return>', self.on_enter)

    def on_enter(self, event):
        event.widget.unbind('<Return>')
        event.widget.config(state=tk.DISABLED)
        readonly_index = event.widget.tag_ranges('readonly')
        if readonly_index and len(readonly_index) > 0:
            query = event.widget.get(readonly_index[-1], tk.END).strip()
            args = _Args()
            args.title = query
            self._on_enter_callback(None, args)

    def set_on_enter_callback(self, func):
        self._on_enter_callback = func

    def set_on_control_f_callback(self, func):
        self.root.bind('<Control-f>', func)

    def set_on_control_r_callback(self, func):
        self.root.bind('<Control-r>', func)
        
    def run(self):
        self.root.mainloop()