import tkinter as tk
from tkinter import messagebox

# Function to calculate Simple Interest and Compound Interest
def calculate_interest():
    try:
        # Fetch the inputs from the user
        principal = float(entry_principal.get())
        time = float(entry_time.get())
        rate = float(entry_rate.get())
        
        # Calculate Simple Interest
        simple_interest = (principal * time * rate) / 100
        
        # Calculate Compound Interest
        compound_interest = principal * (1 + rate / 100) ** time - principal
        
        # Show the results in the labels
        label_simple_interest_result.config(text=f"Simple Interest: {simple_interest:.2f}")
        label_compound_interest_result.config(text=f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all fields.")

# Create the main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("400x300")

# Add labels and entry widgets
label_principal = tk.Label(root, text="Principal Amount:")
label_principal.pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack(pady=5)

label_time = tk.Label(root, text="Time Period (in years):")
label_time.pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)

label_rate = tk.Label(root, text="Rate of Interest (in %):")
label_rate.pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack(pady=5)

# Button to calculate interest
button_calculate = tk.Button(root, text="Calculate Interest", command=calculate_interest)
button_calculate.pack(pady=10)

# Labels to show results
label_simple_interest_result = tk.Label(root, text="Simple Interest: ")
label_simple_interest_result.pack(pady=5)

label_compound_interest_result = tk.Label(root, text="Compound Interest: ")
label_compound_interest_result.pack(pady=5)

# Start the GUI event loop
root.mainloop()
