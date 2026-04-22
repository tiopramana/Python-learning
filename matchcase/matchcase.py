# Match case statement adalah switch case milik python yang dimana case berisi kondisi
# yang harus match agar case tersebut bisa dijalankan

def day_of_week(day):
    match day:
        case 1:
            print("Its monday")
        case 2:
            print("Its tuesday")
        case 3:
            print("Its Wednesday")
        case 4:
            print("Its Thursday")
        case 5:
            print("Its friday")
        case 6: 
            print("Its saturday")
        case 7:
            print("Its sunday")
        case _:
            print("Not valid!")

while True:
    pilihan_hari = int(input("Masukan hari dalam angka : "))
    day_of_week(pilihan_hari)