import tkinter as tk

#Mortgage function to run upon submit
def submit():
    loan = int(entry_a.get())
    term = int(entry_b.get())
    rate = float(entry_c.get())
    down = int(entry_d.get())

    months = term * 12
    rate_monthly = rate / 100 / 12
    payment = (rate_monthly / (1- (1+ rate_monthly) ** (-months))) * (loan - down)
    result = tk.Label(text = "$" + str(round(payment,2)))
    result.pack()

# Create Tkinter window GUI
window = tk.Tk()

#Creating Tkinter and entry boxes
label_a = tk.Label(text = "Please Enter desired loan amount: ")
label_a.pack()
entry_a = tk.Entry()
entry_a.pack()
label_b = tk.Label(text = "Please Enter the loan term: ")
label_b.pack()
entry_b = tk.Entry()
entry_b.pack()
label_c = tk.Label(text = "Please Enter the loan rate: ")
label_c.pack()
entry_c = tk.Entry()
entry_c.pack()
label_d = tk.Label(text = "Please Enter the down payment : ")
label_d.pack()
entry_d = tk.Entry()
entry_d.pack()

#Submit Button
MyButton = tk.Button(window, text = "Submit", width=10, command=submit)
MyButton.pack()

# Run the loop
window.mainloop()
