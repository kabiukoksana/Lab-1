import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
window = tk.Tk()
window.title("Лабораторна 1 - Задача про пікнік")
window.geometry("800x500")
left = tk.Frame(window, bg="#e0f2f1", bd=2, relief="groove")
left.pack(side="left", fill="both", padx=10, pady=10)
right = tk.Frame(window, bg="white", bd=2, relief="groove")
right.pack(side="right", fill="both", expand=True, padx=10, pady=10)
tk.Label(left, text="Імовірність дощу", bg="#e0f2f1",
         font=("Arial", 10, "bold")).pack(pady=5)

slider = tk.Scale(left, from_=0, to=1, resolution=0.01,
                  orient="horizontal", length=150)
slider.set(0.64)
slider.pack()
tk.Label(left, text="Корисність результатів:",
         bg="#e0f2f1", font=("Arial", 10, "bold")).pack(pady=10)
def add_entry(text, value):
    tk.Label(left, text=text, bg="#e0f2f1").pack()
    entry = tk.Entry(left, width=10, justify="center")
    entry.insert(0, value)
    entry.pack()
    return entry
v1 = add_entry("Вкрай погано:", "0")
v2 = add_entry("Погано:", "2")
v3 = add_entry("Посередньо:", "5")
v4 = add_entry("Чудово:", "8")
result_lis = tk.Label(left, text="Корисність (ліс): 0.00",
                      bg="#e0f2f1")
result_lis.pack(pady=(15, 2))

result_dim = tk.Label(left, text="Корисність (дім): 0.00",
                      bg="#e0f2f1")
result_dim.pack()
decision = tk.Label(left, text="", bg="#e0f2f1",
                    fg="green", font=("Arial", 10, "bold"))
decision.pack(pady=10)
fig, ax = plt.subplots(figsize=(4, 3))
canvas = FigureCanvasTkAgg(fig, master=right)
canvas.get_tk_widget().pack(fill="both", expand=True)
def calculate(event=None):
    try:
        a = float(v1.get())
        b = float(v2.get())
        c = float(v3.get())
        d = float(v4.get())
    except ValueError:
        return
    p = slider.get()
    q = 1 - p
    forest = p * a + q * d
    home = p * b + q * c
    result_lis.config(text=f"Корисність (ліс): {forest:.2f}")
    result_dim.config(text=f"Корисність (дім): {home:.2f}")
    if forest > home:
        decision.config(text="Рішення: Йти в ліс!")
    elif home > forest:
        decision.config(text="Рішення: Сидіти вдома B-)))")
    else:
        decision.config(text="Рішення: Однакова корисність")
    ax.clear()
    x = np.linspace(0, 1, 50)
    y1 = x * a + (1 - x) * d
    y2 = x * b + (1 - x) * c
    ax.plot(x, y1, color="magenta", label="Ліс")
    ax.plot(x, y2, color="blue", label="Дім")
    ax.set_title("Рішення про пікнік")
    ax.set_xlabel("Імовірність дощу")
    ax.set_ylabel("Корисність")
    ax.set_facecolor("#d1e7dd")
    ax.grid(True, color="black", linewidth=0.5)
    ax.legend(loc="center right")
    canvas.draw()
slider.config(command=calculate)
v1.bind("<KeyRelease>", calculate)
v2.bind("<KeyRelease>", calculate)
v3.bind("<KeyRelease>", calculate)
v4.bind("<KeyRelease>", calculate)
calculate()
window.mainloop()