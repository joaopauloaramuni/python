import tkinter as tk
from qr_gui import QRCodeGUI

def main():
    root = tk.Tk()
    app = QRCodeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()