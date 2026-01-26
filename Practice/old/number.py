import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database setup
conn = sqlite3.connect('boy.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS product (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    price REAL NOT NULL)''')
conn.commit()

# Functions
def add_product():
    name, qty, price = validate_input()
    if name:
        cursor.execute("INSERT INTO product (name, quantity, price) VALUES (?, ?, ?)",
                      (name, qty, float(price)))
        conn.commit()
        messagebox.showinfo("Успех", "Товар успешно добавлен!")
        clear_fields()
        show_products()

def update_product():
    name, qty, price = validate_input()
    if name:
        cursor.execute("UPDATE product SET quantity = ?, price = ? WHERE name = ?",
                      (qty, float(price), name))
        if cursor.rowcount > 0:
            conn.commit()
            messagebox.showinfo("Успех", "Товар успешно обновлен!")
            clear_fields()
            show_products()
        else:
            messagebox.showerror("Ошибка", "Товар не найден!")

def delete_product():
    name = name_entry.get().strip()
    if name:
        cursor.execute("DELETE FROM product WHERE name = ?", (name,))
        if cursor.rowcount > 0:
            conn.commit()
            messagebox.showinfo("Успех", "Товар успешно удален!")
            clear_fields()
            show_products()
        else:
            messagebox.showerror("Ошибка", "Товар не найден!")
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, введите название товара!")

def show_products():
    product_list.delete(*product_list.get_children())
    cursor.execute("SELECT * FROM product")
    for product in cursor.fetchall():
        product_list.insert('', 'end', values=(product[0], product[1], product[2], f"{product[3]:.2f}"))

def clear_fields():
    name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    name_entry.focus_set()

def search_product():
    name = name_entry.get().strip()
    if name:
        product_list.delete(*product_list.get_children())
        cursor.execute("SELECT * FROM product WHERE name LIKE ?", ('%' + name + '%',))
        for product in cursor.fetchall():
            product_list.insert('', 'end', values=(product[0], product[1], product[2], f"{product[3]:.2f}"))
        if not cursor.rowcount:
            messagebox.showinfo("Результат поиска", "Товары не найдены!")
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, введите название товара для поиска!")

def validate_input():
    name = name_entry.get().strip()
    qty = quantity_entry.get().strip()
    price = price_entry.get().strip()
    if not name or not qty.isdigit() or not price.replace('.', '', 1).isdigit():
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные данные!")
        return None, None, None
    return name, int(qty), price

# UI Setup
root = tk.Tk()
root.title("Система управления складом")
root.geometry("800x600")
root.configure(bg="#f5f6f5")

# Style configuration
style = ttk.Style()
style.theme_use('clam')
style.configure("TButton", font=('Helvetica', 11), padding=10)
style.configure("TLabel", font=('Helvetica', 11), background="#f5f6f5")
style.configure("Treeview.Heading", font=('Helvetica', 11, 'bold'))
style.configure("Treeview", font=('Helvetica', 10))

# Main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Header
header = ttk.Label(main_frame, text="Управление складом", font=('Helvetica', 18, 'bold'))
header.pack(pady=(0, 20))

# Input frame
input_frame = ttk.LabelFrame(main_frame, text="Детали товара", padding=10)
input_frame.pack(fill="x", pady=10)

# Input fields
fields = [
    ("Название товара:", "name_entry"),
    ("Количество:", "quantity_entry"),
    ("Цена:", "price_entry")
]

for i, (label_text, var_name) in enumerate(fields):
    ttk.Label(input_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
    entry = ttk.Entry(input_frame, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
    globals()[var_name] = entry

# Buttons frame
button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)

buttons = [
    ("Добавить товар", add_product, "#4CAF50"),
    ("Обновить товар", update_product, "#2196F3"),
    ("Удалить товар", delete_product, "#F44336"),
    ("Найти товар", search_product, "#FF9800"),
    ("Показать все", show_products, "#9C27B0")
]

for i, (text, command, color) in enumerate(buttons):
    btn = ttk.Button(button_frame, text=text, command=command, style=f"{text}.TButton")
    btn.grid(row=0, column=i, padx=5)
    style.configure(f"{text}.TButton", background=color, foreground="white")

# Product list
product_list_frame = ttk.LabelFrame(main_frame, text="Список товаров", padding=10)
product_list_frame.pack(fill="both", expand=True, pady=10)

product_list = ttk.Treeview(product_list_frame, columns=("ID", "Название", "Количество", "Цена"), show="headings", height=12)
product_list.heading("ID", text="ID")
product_list.heading("Название", text="Название")
product_list.heading("Количество", text="Количество")
product_list.heading("Цена", text="Цена")
product_list.column("ID", width=50)
product_list.column("Название", width=200)
product_list.column("Количество", width=100)
product_list.column("Цена", width=100)
product_list.pack(fill="both", expand=True)

# Scrollbar
scrollbar = ttk.Scrollbar(product_list_frame, orient="vertical", command=product_list.yview)
scrollbar.pack(side="right", fill="y")
product_list.configure(yscrollcommand=scrollbar.set)

# Initial display
show_products()
name_entry.focus_set()

root.mainloop()
conn.close()