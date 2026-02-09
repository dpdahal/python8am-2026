import tkinter as  tk 

app = tk.Tk()
app.title("My GUI App")
app.geometry("400x400")

nlb = tk.Label(app, text="Name:")
nlb.grid(row=0, column=0)
name = tk.Entry(app)
name.grid(row=0, column=1)

result = tk.StringVar()

def get_value():

    print(result.get())

button = tk.Button(app, text="Submit", command=get_value)
button.grid(row=1, column=0, columnspan=2)


app.mainloop()