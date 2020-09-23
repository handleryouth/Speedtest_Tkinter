import tkinter as tk
from tkinter import ttk, messagebox
import speedtest
from DPI_AWARENESS import setting_dpi



BLACK_FRAME = "#000000"
WHITE_FRAME = "#FFFFFF"
SAILOR_BLUE = "#7DADDE"
BLUE_CLICKED = "#103D6A"


def Uploading():
    for i in range(1, (n.get() + 1)):
        Upload = command.upload()
        M_Upload = Upload / 10**6
        result = f'-- {i}. Result--\nYour upload speed is {M_Upload:.2f} Mbps\n'
        display['state'] = "normal"
        display.insert(tk.END, result)
        display['state'] = "disabled"


def Downloading():
    for i in range(1, (n.get() + 1)):
        Download = command.download()
        M_Download = Download / 10**6
        result = f'-- {i}. Result--\nYour download speed is {M_Download:.2f} Mbps\n'
        display['state'] = "normal"
        display.insert(tk.END, result)
        display['state'] = "disabled"

def both():
    root.title("Speedtest but Tkinter (Processing, Please wait !)")
    if n.get() >= 5 :
        warning_sign = tk.messagebox.askquestion(title= "Warning", message= f"Do you wish to proceed?\nYour internet will be laggy !", icon = "warning")
        if warning_sign == 'yes':
            for i in range(1, (n.get() + 1)):
                Upload = command.upload()
                M_Upload = Upload / 10 ** 6
                Download = command.download()
                M_Download = Download / 10 ** 6
                result = f'-- {i}. Result--\nYour download speed is {M_Download:.2f} Mbps\nYour upload speed is {M_Upload:.2f} Mbps\n'
                display['state'] = "normal"
                display.insert(tk.END, result)
                display['state'] = "disabled"
            root.title("Speedtest but Tkinter")
        else:
                root.title("Speedtest but Tkinter")
    else:
        for i in range(1, (n.get() + 1)):
            Upload = command.upload()
            M_Upload = Upload / 10 ** 6
            Download = command.download()
            M_Download = Download / 10 ** 6
            result = f'-- {i}. Result--\nYour download speed is {M_Download:.2f} Mbps\nYour upload speed is {M_Upload:.2f} Mbps\n'
            display['state'] = "normal"
            display.insert(tk.END, result)
            display['state'] = "disabled"
            root.title("Speedtest but Tkinter")


def clear():
    display['state'] = "normal"
    display.delete('1.0', "end-1c")
    display['state'] = "disabled"

setting_dpi()
root = tk.Tk()
root.resizable(False, False)
style = ttk.Style()
style.theme_use("clam")

style.configure("black_frame.TFrame", background = BLACK_FRAME)
style.configure("White_Letter.TLabel", background = BLACK_FRAME, foreground = WHITE_FRAME)
style.configure("Command_Button.TButton", background = WHITE_FRAME, foreground = BLACK_FRAME)
style.map("Command_Button.TButton", background=[("active", SAILOR_BLUE), ("pressed", BLUE_CLICKED)])


root.title("Speedtest but Tkinter")
command = speedtest.Speedtest()

upper = ttk.Frame(root, style="black_frame.TFrame")
upper.grid(sticky = "EW", ipady = 40)

button_container = ttk.Frame(root, style="black_frame.TFrame")
button_container.grid(row = 2, sticky ="EW")
button_container.columnconfigure((0, 1, 2), weight = 1)

down = ttk.Frame(root, style="black_frame.TFrame")
down.grid(row = 5, sticky = "EW", ipady = 40)

for_loop = ttk.Frame(root)
for_loop.grid(row = 3)


welcome = ttk.Label(upper, text="Welcome to TKinter Speedtest", style =  "White_Letter.TLabel", font = "Ink_Free 15 underline bold")
welcome.grid(row = 0, column = 0, pady= (5, 5))
welcome.place(relx = 0.5, rely = 0.3, anchor = "center")

inputting = ttk.Label(upper, text="Please choose a command !", style = "White_Letter.TLabel", font = "Segoe_UI 10")
inputting.grid(row = 1, column = 0, sticky = "EW")
inputting.place(relx = 0.5, rely = 0.8, anchor = "center")

n = tk.IntVar(value = 1)

looping = ttk.Label(for_loop, text = "Looping :")
looping.grid(row = 3, column = 0, pady = (5,5), padx = (10, 10))
looping_spinbox = ttk.Spinbox(for_loop,
            from_ = 1,
            to = 20,
            increment = 1,
            justify = 'center',
            textvariable = n,
            width = 10
        )
looping_spinbox.grid(row = 3, column = 1, padx = (10, 10))


upload_button = ttk.Button(button_container, text = "Upload", command = Uploading, style = "Command_Button.TButton")
download_button = ttk.Button(button_container, text = "Download", command = Downloading, style = "Command_Button.TButton")
both = ttk.Button(button_container, text = "Both", command = both, style = "Command_Button.TButton")
clear_button = ttk.Button(button_container, text = "Clear", command = clear, style = "Command_Button.TButton")

upload_button.grid(row = 2, column = 0, sticky = "EW", padx = 5, pady = 5 )
download_button.grid(row = 2, column = 1, sticky = "EW", padx = 5, pady = 5)
both.grid(row = 2, column = 2, sticky = "EW", padx = 5, pady = 5)
clear_button.grid(row = 2, column = 3, sticky = "EW", padx = 5, pady = 5)

display = tk.Text(root, height = 15, state='disabled', cursor = 'arrow')
display.grid(row = 4, columnspan = 1)

text_scroll = ttk.Scrollbar(root, orient="vertical", command=display.yview)
text_scroll.grid(row=4,column = 3, sticky = 'ns')
display["yscrollcommand"] = text_scroll.set

down_bar = ttk.Label(down, text = "Original Design by Handleryouth", style = "White_Letter.TLabel" )
down_bar.grid(row = 5, sticky = "EW")
down_bar.place( relx = 0.5, rely = 0.5, anchor = "center")


root.mainloop()


