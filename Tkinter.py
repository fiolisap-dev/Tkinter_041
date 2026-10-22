import tkinter as tk
from tkinter import ttk

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x650")
root.resizable(False, False)

# Membuat frame utama
main_frame = ttk.Frame(root, padding=25)
main_frame.pack(fill="both", expand=True)

# Label judul aplikasi
judul = ttk.Label(
    main_frame,
    text="APLIKASI PREDIKSI PRODI PILIHAN",
    font=("Arial", 16, "bold")
)
judul.pack(pady=(0, 10))

# Label petunjuk
petunjuk = ttk.Label(
    main_frame,
    text="Masukkan nilai 10 mata pelajaran (0-100)"
)
petunjuk.pack(pady=(0, 15))

# Daftar mata pelajaran
mata_pelajaran = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Informatika",
    "IPA",
    "IPS",
    "PPKn",
    "Pendidikan Agama",
    "Seni Budaya",
    "PJOK"
]

# Tempat menyimpan input nilai
input_nilai = {}

# Frame untuk input nilai
form_frame = ttk.Frame(main_frame)
form_frame.pack()

# Membuat 10 label dan input nilai
for i, mapel in enumerate(mata_pelajaran):
    label = ttk.Label(form_frame, text=mapel, width=22)
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    entry = ttk.Entry(form_frame, width=25)
    entry.grid(row=i, column=1, padx=10, pady=5)

    input_nilai[mapel] = entry


# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    hasil.config(
        text="Hasil Prediksi Prodi: Teknologi Informasi"
    )


# Tombol hasil prediksi
tombol = ttk.Button(
    main_frame,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
tombol.pack(pady=20)

# Label luaran hasil prediksi
hasil = ttk.Label(
    main_frame,
    text="Hasil Prediksi Prodi: -",
    font=("Arial", 12, "bold"),
    foreground="blue"
)
hasil.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()