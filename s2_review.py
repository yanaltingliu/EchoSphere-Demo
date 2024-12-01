from tkinter import Tk, Label, Button, Listbox

# Contributions (Mocked)
contributions = [
    "Healthcare workers during COVID",
    "Remote learning experience",
    "Community resilience stories",
]

# GUI setup
root = Tk()
root.title("EchoSphere Contribution Review")
root.geometry("600x400")

status_label = Label(root, text="Review Contributions", font=("Helvetica", 16))
status_label.pack(pady=10)

contribution_listbox = Listbox(root, width=50, height=10)
contribution_listbox.pack(pady=10)
for contribution in contributions:
    contribution_listbox.insert("end", contribution)

def categorize_contribution():
    selected = contribution_listbox.get("active")
    print(f"Categorized: {selected}")
    contribution_listbox.delete("active")
    status_label.config(text=f"Categorized: {selected}")

categorize_button = Button(root, text="Categorize", command=categorize_contribution)
categorize_button.pack(pady=20)

root.mainloop()
