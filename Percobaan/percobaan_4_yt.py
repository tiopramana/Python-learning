from pytube import YouTube
import os

def download_video_yt():
    print("Selamat datang di tempat Pendownload Video Youtube")

    link_video_url = input("Masukan Link Video URL Disini: ").strip()

    try:
        # Create YouTube object
        yt = YouTube(link_video_url)

        print("\nPilihan Download:")
        print("1. Video")
        print("2. Audio")
        pilihan_download = input("Pilihan Download (1 Atau 2): ").strip()

        # Get destination folder
        destination = input("Masukan Tujuan Folder Agar tersimpan (pastikan folder sudah ada): ").strip()
        if not os.path.exists(destination):
            print("Folder tidak ditemukan. Mohon masukan folder yang benar!")
            return

        if pilihan_download == "1":
            # Download video
            print("Sedang memproses pendownloadan video...")
            yt.streams.get_highest_resolution().download(output_path=destination)
            print(f"Video berhasil terdownload ke folder: {destination}")
        elif pilihan_download == "2":
            # Download audio
            print("Sedang memproses ekstraksi audio dari video...")
            yt.streams.filter(only_audio=True).first().download(output_path=destination)
            print(f"Audio berhasil terdownload ke folder: {destination}")
        else:
            print("Pilihan tidak valid. Silakan jalankan program lagi.")
    except Exception as e:
        print(f"Terjadi error: {e}")

download_video_yt()
