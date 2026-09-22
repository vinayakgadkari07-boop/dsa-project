import tkinter as tk
from tkinter import messagebox

# -------------------------------------------------------------
# PROGRAM: Online Food Order Queue Management System (GUI)
# DATA STRUCTURE: Queue (FIFO - First In, First Out)
# AUTHOR: DSA Assignment
# -------------------------------------------------------------

# Global list acting as the Queue Data Structure
food_queue = []
MAX_LIMIT = 5


# Function to Add Order (Enqueue Operation)
def add_order():
    name = entry_name.get().strip()
    food = entry_food.get().strip()

    # Input Validation
    if name == "" or food == "":
        messagebox.showwarning("Warning", "Please enter both Customer Name and Food Item!")
        return

    # Check for Queue Overflow
    if len(food_queue) >= MAX_LIMIT:
        messagebox.showwarning("Queue Full", "Queue capacity reached (Max 5 orders)!")
        return

    # Create formatted order string
    order_text = name + " ---> " + food
    
    # ENQUEUE: Add item to the rear of the queue
    food_queue.append(order_text)

    # Clear text fields
    entry_name.delete(0, tk.END)
    entry_food.delete(0, tk.END)

    # Refresh visual listbox
    update_queue_display()
    messagebox.showinfo("Success", "Order placed successfully!")


# Function to Serve Order (Dequeue Operation)
def serve_order():
    # Check for Queue Underflow
    if len(food_queue) == 0:
        messagebox.showinfo("Queue Empty", "No pending orders to serve!")
        return

    # DEQUEUE: Remove item from index 0 (Front of the Queue - FIFO)
    served_item = food_queue.pop(0)

    # Refresh visual listbox
    update_queue_display()
    messagebox.showinfo("Order Served", "Prepared & Served:\n\n" + served_item)


# Function to Update the GUI Listbox Display
def update_queue_display():
    listbox.delete(0, tk.END)  # Clear current display
    for index, order in enumerate(food_queue, start=1):
        listbox.insert(tk.END, f" Pos {index} | {order}")


# --- GUI WINDOW CREATION ---
window = tk.Tk()
window.title("Online Food Queue Management System")
window.geometry("400x480")
window.configure(bg="#f0f2f5")

# Header Section
label_title = tk.Label(window, text="🍔 Food Queue System 🍟", font=("Arial", 16, "bold"), bg="#f0f2f5", fg="#1a1a1a")
label_title.pack(pady=12)

label_sub = tk.Label(window, text="Data Structure: Queue (First-In, First-Out)", font=("Arial", 9, "italic"), bg="#f0f2f5", fg="#555555")
label_sub.pack(pady=(0, 10))

# Input Fields
label_name = tk.Label(window, text="Customer Name:", font=("Arial", 10, "bold"), bg="#f0f2f5")
label_name.pack(anchor="w", padx=45)
entry_name = tk.Entry(window, width=32, font=("Arial", 10))
entry_name.pack(pady=(2, 8))

label_food = tk.Label(window, text="Food Item:", font=("Arial", 10, "bold"), bg="#f0f2f5")
label_food.pack(anchor="w", padx=45)
entry_food = tk.Entry(window, width=32, font=("Arial", 10))
entry_food.pack(pady=(2, 10))

# Action Buttons
btn_add = tk.Button(window, text="➕ Place Order (Enqueue)", font=("Arial", 10, "bold"), bg="#28a745", fg="white", width=25, command=add_order)
btn_add.pack(pady=4)

btn_serve = tk.Button(window, text="🛎️ Serve Order (Dequeue)", font=("Arial", 10, "bold"), bg="#007bff", fg="white", width=25, command=serve_order)
btn_serve.pack(pady=4)

# Queue Display Area
label_queue = tk.Label(window, text="Current Orders in Queue:", font=("Arial", 10, "bold"), bg="#f0f2f5")
label_queue.pack(anchor="w", padx=45, pady=(12, 4))

listbox = tk.Listbox(window, width=38, height=7, font=("Courier", 10), bd=1, relief="solid")
listbox.pack()

# Start Application Loop
window.mainloop()
