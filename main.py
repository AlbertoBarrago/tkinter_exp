import tkinter as tk

window = tk.Tk()
window.title("alBz")
window.minsize(450, 200)
window.grid_columnconfigure(0, weight=1)
window.config(padx=10, pady=10)

# Label
title_label = tk.Label(window, text="alBz App", font=("Helvetica", 20), fg="red")
title_label.grid(column=0, row=0, padx=10, pady=10, sticky="ew")

# Tagline
tagline = tk.Label(window, text="€uro to Do$$ar")
tagline.grid(column=0, row=2, padx=10, pady=10)


# Input
def inputValue():
    dollar = input_value.get()
    dollars = float(dollar) * 1.09
    result.config(text=f"The result is: ${dollars:.2f}")


input_value = tk.Entry(window, width=10)
input_value.focus_set()
input_value.grid(column=0, row=5, columnspan=2)

# Result
result = tk.Label(window, text="The result is: $0.00")
result.grid(column=0, row=6, columnspan=2)

# Button send
button_send_val = tk.Button(window, text="Calculate", command=inputValue)
button_send_val.grid(column=0, row=7, pady=10, padx=10)

window.mainloop()
