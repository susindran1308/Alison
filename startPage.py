import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry("200x100+500+300")
    v = tk.StringVar()

    tk.Label(root,
             text="""Choose a language:""",
             justify=tk.LEFT,
             padx=20).pack()
    tamil = tk.Radiobutton(root,
                           text="Tamil",
                           padx=20,
                           variable=v,
                           value="ta")
    tamil.pack(anchor=tk.W)

    english = tk.Radiobutton(root,
                             text="English",
                             padx=20,
                             variable=v,
                             value="en")
    english.pack(anchor=tk.W)

    v.set(None)
    tk.Button(root, text="-> GO <-", command=root.destroy).pack()

    root.mainloop()
    return v.get()

