import tkinter as tk

def exit_gui():
    root.destroy()

root = tk.Tk()
root.title("SFFDK SETUP")
root.iconbitmap('logo.ico')
root.configure(bg="grey")  # Set window background color to grey

# Create frame for text and text box
frame = tk.Frame(root, bg="lightblue", bd=2, relief="ridge", width=300, height=200)
frame.pack(pady=(5, 0), padx=5 ,fill="x")

# Create text in middle top
text_label = tk.Label(frame, text="SEET UP SFDK ON YOUR PC", bg="lightblue", bd=0, padx=10, pady=5, font=("Helvetica", 17))
text_label.pack(pady=(0, 5), fill="x")

# Create text box with same properties
text_box = tk.Text(frame, bg="lightblue", bd=0, padx=10, pady=5, width=30, height=30, font=("Helvetica", 12))
text_box.pack(pady=(0, 5), fill="x")

text_box.insert("end","To setup your SFDK on your computer do the following steps \n - Go the .exe file and run it if you have proper configuratiions on your PC you should be able to run it directly \n - or else use thhe .py file and install the follwoing packages using pip install package name (you will have to install python first go to python .org) \n +win10toast \n +pyserial ")

# Create button
button = tk.Button(root, text="Exit", command=exit_gui, bg="lightblue", bd=2, relief="solid", padx=10, pady=5, borderwidth=0, highlightthickness=0)
button.pack(pady=(5, 0), fill="x")

# Set border radius
root.wm_attributes("-transparentcolor", "white")  # Set transparent color to white 
root.geometry("600x700")  # Position window
root.mainloop()
