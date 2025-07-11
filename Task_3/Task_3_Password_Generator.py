from tkinter import*
from tkinter import messagebox
import random
import string


# Create window with custom theme colors
root = Tk()
root.title("Password Generator")
root.geometry("400x300")
root.configure(bg="beige")


# Function to generate password
def generate_password():
    try:
        lngth=int(lngth_e.get())
        if lngth < 6:
            messagebox.showwarning("Warning", "Password should be greater than 6 digits.")
            return
        
        # Define character sets
        all_chars=string.ascii_letters + string.digits + string.punctuation
        
        # Guarantee at least one from each type
        password=[
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        
        # Add remaining random characters
        password=password+random.choices(all_chars, k=lngth - 4)
        random.shuffle(password)

        # Display result
        result_entry.delete(0,END)
        result_entry.insert(0, ''.join(password))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")




# Password length input with label, focus, text color, and themed background
Label(root, text="Enter Password Length", font=("Cooper Black", 15), bg="beige", fg="black").pack(pady=5)
lngth_e = Entry(root, font=("Bodoni MT", 14), justify='center', fg="blue", bg="light yellow")
lngth_e.pack(padx=20, pady=15, ipady=3)
lngth_e.focus_set()  # Set focus to entry box

# Allow pressing Enter to trigger password generation
def on_enter(event):
    generate_password()
lngth_e.bind('<Return>', on_enter)


# Themed generate button
generate_bttn = Button(root, text="Generate Password", font=("Bell MT", 12), command=generate_password, bg="light blue", fg="black", activebackground="light yellow", activeforeground="black")
generate_bttn.pack(pady=12)



# Password result display with text color and themed background
Label(root, text="Generated Password", font=("Cooper Black", 18), bg="beige", fg="black").pack(pady=10)
result_entry = Entry(root, font=("Bodoni MT", 14), width=32, justify='center', fg="green", bg="light yellow")
result_entry.pack(padx=20, pady=15, ipady=8)

root.mainloop()
