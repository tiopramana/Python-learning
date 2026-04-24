# OOP Object Oriented Programming adalah Cara membuat program dengan menggabungkan 
# data (atribut) dan perilaku (method) ke dalam satu “objek”.

# Anggepan seperti manusia yang menjadi properti atau atribut memilik data nama, umur, tempat tinggal
# Lalu untuk behavior atau method yang akan dilakukan seperti berjalan, makan, tidur dll

# Yang dimana kita menggunakan class untuk mendefinisikan atribut dan method yang akan dijalankan
# Class adalah blueprint yang digunakan untuk mendesign struktur dan layout dari suatu objectnya

from car import Car  

car1 = Car("BMW M3 Competition", 2024, "Black", False)
car2 = Car("Supra Mk4", 2024, "Gray", True )

print(car1.model, car1.year, "color " + car1.color, "for sale = ",car1.for_sale)
print(car2.model, car2.year, "color " + car2.color, "for sale = ",car2.for_sale)

car1.drive()
car2.stop()