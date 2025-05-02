import tkinter as tk
from tkinter import ttk
import random
import time
import threading

# ------------------ Sorting Algorithms ------------------ #
def bubble_sort(data, draw_data, delay):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            draw_data(data, ['red' if x == j or x == j+1 else 'blue' for x in range(len(data))])
            time.sleep(delay)
    draw_data(data, ['green' for x in range(len(data))])
    sort_button.config(state=tk.NORMAL)
    generate_button.config(state=tk.NORMAL)

def merge_sort(data, draw_data, delay):
    def merge_sort_rec(data, left, right):
        if left < right:
            middle = (left + right) // 2
            merge_sort_rec(data, left, middle)
            merge_sort_rec(data, middle+1, right)
            merge(data, left, middle, right)
            draw_data(data, ['green' if x >= left and x <= right else 'blue' for x in range(len(data))])
            time.sleep(delay)

    def merge(data, left, middle, right):
        left_copy = data[left:middle+1]
        right_copy = data[middle+1:right+1]
        l = r = 0
        for i in range(left, right+1):
            if l < len(left_copy) and (r >= len(right_copy) or left_copy[l] <= right_copy[r]):
                data[i] = left_copy[l]
                l += 1
            else:
                data[i] = right_copy[r]
                r += 1

    merge_sort_rec(data, 0, len(data)-1)
    draw_data(data, ['green' for x in range(len(data))])
    sort_button.config(state=tk.NORMAL)
    generate_button.config(state=tk.NORMAL)

def quick_sort(data, draw_data, delay):
    def quick_sort_rec(data, low, high):
        if low < high:
            pi = partition(data, low, high)
            quick_sort_rec(data, low, pi - 1)
            quick_sort_rec(data, pi + 1, high)

    def partition(data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                draw_data(data, ['red' if x == i or x == j else 'blue' for x in range(len(data))])
                time.sleep(delay)
        data[i+1], data[high] = data[high], data[i+1]
        draw_data(data, ['red' if x == i+1 or x == high else 'blue' for x in range(len(data))])
        time.sleep(delay)
        return i + 1

    quick_sort_rec(data, 0, len(data)-1)
    draw_data(data, ['green' for x in range(len(data))])
    sort_button.config(state=tk.NORMAL)
    generate_button.config(state=tk.NORMAL)

def selection_sort(data, draw_data, delay):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
            draw_data(data, ['red' if x == j or x == min_idx else 'blue' for x in range(len(data))])
            time.sleep(delay)
        data[i], data[min_idx] = data[min_idx], data[i]
        draw_data(data, ['green' if x <= i else 'blue' for x in range(len(data))])
    draw_data(data, ['green' for x in range(len(data))])
    sort_button.config(state=tk.NORMAL)
    generate_button.config(state=tk.NORMAL)

# ------------------ GUI Functions ------------------ #
def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 5

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
        canvas.create_text(x0+2, y0, anchor=tk.SW, text=str(data[i]), font=("Arial", 9))

    window.update_idletasks()

def generate():
    global data
    try:
        size = int(size_entry.get())
    except ValueError:
        size = 50

    data = [random.randint(1, 100) for _ in range(size)]
    draw_data(data, ['blue' for x in range(len(data))])
    sort_button.config(state=tk.NORMAL)

def start_sorting():
    global data
    sort_button.config(state=tk.DISABLED)
    generate_button.config(state=tk.DISABLED)
    delay = 1.01 - speed_scale.get()

    algorithm = algo_menu.get()
    if algorithm == "Bubble Sort":
        thread = threading.Thread(target=bubble_sort, args=(data, draw_data, delay))
    elif algorithm == "Merge Sort":
        thread = threading.Thread(target=merge_sort, args=(data, draw_data, delay))
    elif algorithm == "Quick Sort":
        thread = threading.Thread(target=quick_sort, args=(data, draw_data, delay))
    elif algorithm == "Selection Sort":
        thread = threading.Thread(target=selection_sort, args=(data, draw_data, delay))
    else:
        return

    thread.daemon = True
    thread.start()

# ------------------ GUI Setup ------------------ #
window = tk.Tk()
window.title("Visualizador de Algoritmos de Ordenação")
window.maxsize(900, 600)
window.config(bg="white")

UI_frame = tk.Frame(window, width=900, height=200, bg="white")
UI_frame.grid(row=0, column=0, sticky="w", padx=2, pady=2)

canvas = tk.Canvas(window, width=600, height=380, bg="white")
canvas.grid(row=1, column=0, sticky="w", padx=2, pady=2)

# UI Area
tk.Label(UI_frame, text="Tamanho:", bg="white").grid(row=0, column=0, sticky=tk.W, padx=2, pady=2)
size_entry = tk.Entry(UI_frame, width=5)
size_entry.grid(row=0, column=1, padx=2, pady=2)
size_entry.insert(0, "50")

algo_menu = ttk.Combobox(UI_frame, width=10, values=["Bubble Sort", "Merge Sort", "Quick Sort", "Selection Sort"], state="readonly")
algo_menu.grid(row=0, column=2, padx=2, pady=2)
algo_menu.current(0)

speed_scale = tk.Scale(UI_frame, from_=0.01, to=1.0, resolution=0.01, length=120,
                       digits=3, orient=tk.HORIZONTAL, label="Velocidade")
speed_scale.grid(row=0, column=3, padx=2, pady=2)
speed_scale.set(1.0)

generate_button = tk.Button(UI_frame, text="Gerar", command=generate, bg="lightgray")
generate_button.grid(row=0, column=4, padx=2, pady=2)

sort_button = tk.Button(UI_frame, text="Ordenar", command=start_sorting, bg="lightgreen")
sort_button.grid(row=0, column=5, padx=2, pady=2)
sort_button.config(state=tk.DISABLED)

window.mainloop()