import tkinter as tk
import math

################################################
# Hesap makinesi uygulaması
#   1. Sayı girişi
#   2. İşlem seçimi
#   3. İkinci sayı girişi
#   4. Sonucun gösterilmesi
#
#   Github: EnesBuyuk
################################################

# Butonlara tıklanınca çalışacak fonksiyon
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Entryi temizleyen fonksiyon
def clear_entry():
    entry.delete(0, tk.END)

# Hesaplama yapan fonksiyon
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Logaritma hesaplayan fonksiyon
def calculate_log():
    try:
        input_value = float(entry.get())
        if input_value > 0:  # Sadece pozitif sayılar için logaritma
            result = math.log(input_value)
            entry.delete(0, tk.END)
            entry.insert(0, f"{result:.4f}")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, "Hata: Pozitif sayı giriniz")
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Hata: Geçersiz giriş")

window = tk.Tk() # Pencere oluşturma
window.title("Hesap Makinesi") # Pencere başlığı
window.resizable(False, False) # Pencere boyutunun değiştirilmesini engeller

entry = tk.Entry(window, width=16, font=("Arial", 20), borderwidth=0, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=15)

# Butonları oluşturma ve yerleştirme
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', 'OFF','+',
    'MOD', 'EXP','LOG','='
]

row = 1
col = 0

for button_value in buttons:
    if button_value == '=':
        tk.Button(window, text=button_value, width=8, height=2, borderwidth=0.5, bg="#FF0",command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif button_value == 'C':
        tk.Button(window, text=button_value, width=8, height=2, borderwidth=0.5,bg="#00c8ff",command=clear_entry).grid(row=row, column=col, padx=5, pady=5)
    elif button_value == 'OFF':
        tk.Button(window, text=button_value, width=8, height=2, borderwidth=0.5, bg="#F00", command=window.destroy).grid(row=row, column=col, padx=5, pady=5)
    elif button_value == 'MOD':
        tk.Button(window, text=button_value, width=8, height=2, borderwidth=0.5,
                  command=lambda: button_click('%')).grid(row=row, column=col, padx=5, pady=5)
    elif button_value == 'LOG':
        tk.Button(window, text=button_value, width=8, height=2, borderwidth=0.5,command=calculate_log).grid(row=row, column=col, padx=5, pady=5)
    elif button_value == 'EXP':
        tk.Button(window, text=button_value, width=8, height=2, borderwidth=0.5,command=lambda: button_click('**')).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(window, text=button_value, width=8, height=2, borderwidth=0.5,command=lambda value=button_value: button_click(value)).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop() # Pencereyi açık tutma
