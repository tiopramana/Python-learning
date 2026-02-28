def mesin_atm():
    print("Selamat datang")
    saldo = 0

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
    
        pilihan_atm = input("Pilihan (1-4): ").strip()  # Strip whitespace and compare as string

        if pilihan_atm == "1":
            print(f"Saldo anda tersisa Rp.{saldo}")
        elif pilihan_atm == "2":
            try:
                deposit_input = input("Masukan Nominal Uang yang ingin dimasukan: ").strip()
                deposit = float(deposit_input)

                if deposit > 0:
                    saldo += deposit
                    print(f"Anda telah memasukan Rp.{deposit}. Saldo saat ini: Rp.{saldo}")
                else:
                    print("Masukan Nominal Uang Dengan Benar!")

            except ValueError:
                print("Invalid Input. Mohon Masukan Angka dengan benar!")
        elif pilihan_atm == "3":
            try:
                tarik_input = input("Masukan Nominal Yang Ingin Ditarik: ").strip()
                tarik_tunai = float(tarik_input)
                
                if 0 < tarik_tunai <= saldo:
                    saldo -= tarik_tunai
                    print(f"Rp.{tarik_tunai} Tarik Tunai berhasil! Saldo saat ini: Rp.{saldo}")
                elif tarik_tunai > saldo:
                    print("Saldo Tidak Cukup!")
                else: 
                    print("Masukan total nominal yang valid!")
            except ValueError:
                print("Masukan data yang valid!")
        elif pilihan_atm == "4":
            print("Terimakasih Telah Menggunakan ATM. Selamat Tinggal!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

mesin_atm()
