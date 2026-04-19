# Variable scope adalah variable yang memiliki akses dan hanya dapat dilihat 
# pada function itu aja yang hanya visible didalam nya aja 

# Scope resolution using (LEGB) = Local -> Enclosed -> Global -> Built in

def func1(): # Ini local scope
    a = "Halo"
    print(a)

def func2():
    b = "Hehe"
    print(b)

func1()
func2()
# def who():
#     name = input("Masukan nama : ")
#     froms = input("Masukan lokasi : ")

#     return name, froms

# user, froms = who() # ini global 

# def greeting_to(name, froms):
#     print(f"Halo {name} from {froms}")

# greeting_to(user, froms)

def luar(): #Enclosed 
    hitung = 0
    def dalam():
        nonlocal hitung
        hitung += 1
        return hitung
    return dalam
