import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

class LogView(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Label for the log area
        self.label = ttk.Label(self, text="Logs do Processo", font=("Helvetica", 10, "bold"))
        self.label.pack(anchor=W, pady=(0, 5))
        
        # Scrolled Text for logging
        self.text_area = ScrolledText(
            self, 
            height=15, 
            autohide=True, 
            state=DISABLED,
            font=("Consolas", 9)
        )
        self.text_area.pack(fill=BOTH, expand=YES)
        
        # Configure tags for different log levels
        self.text_area.text.tag_configure("info", foreground="white")
        self.text_area.text.tag_configure("error", foreground="#ff6b6b")
        self.text_area.text.tag_configure("success", foreground="#51cf66")

    def log(self, message: str, level: str = "info"):
        self.text_area.text.configure(state=NORMAL)
        tag = level if level in ["info", "error", "success"] else "info"
        self.text_area.text.insert(END, f"{message}\n", tag)
        self.text_area.text.see(END)
        self.text_area.text.configure(state=DISABLED)

    def clear(self):
        self.text_area.text.configure(state=NORMAL)
        self.text_area.text.delete(1.0, END)
        self.text_area.text.configure(state=DISABLED)
