import tkinter as tk
def save_event():
    event = event_entry.get()
    time = time_entry.get()
    priority = priority_var.get()
    if event and time:
        result = f"{event} at {time} - {priority.lower()}\n"
        display_box.insert(tk.END, result)
        start_index = f"end-{len(result)}c"
        end_index = "end"
        if priority == "High":
            display_box.tag_add("high_priority", start_index, end_index)
        elif priority == "Medium":
            display_box.tag_add("medium_priority", start_index, end_index)
        else:
            display_box.tag_add("low_priority", start_index, end_index)
        event_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
    else:
        display_box.insert(tk.END, "Please enter both event and time!\n")
window = tk.Tk()
window.title("Event Manager")
window.geometry("350x350")
tk.Label(window, text="Event").pack()
event_entry = tk.Entry(window, width=30)
event_entry.pack(pady=5)
tk.Label(window, text="Time").pack()
time_entry = tk.Entry(window, width=30)
time_entry.pack(pady=5)
tk.Label(window, text="Priority").pack()
priority_var = tk.StringVar(value="High")
priority_menu = tk.OptionMenu(window, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=5)
save_button = tk.Button(window, text="Save", command=save_event)
save_button.pack(pady=10)
display_box = tk.Text(window, height=10, width=40)
display_box.pack(pady=10)
display_box.tag_config("high_priority", foreground="red")
display_box.tag_config("medium_priority", foreground="orange")
display_box.tag_config("low_priority", foreground="green")
window.mainloop()
