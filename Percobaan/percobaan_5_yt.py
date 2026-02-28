import yt_dlp 
import os

def download_video_yt():
    print("Welcome to Tinstaller Video 😊")
    video_link = input("Silahkan Masukan Link Video Youtube yang ingin di Download : ").strip()
    destination = input("Masukan Destination Folder untuk menyimpan Video (pastikan Folder Tersebut Sudah Ada): ")

    if not os.path.exists(destination):
        print("Folder tidak ditemukan Harap memasukan nama folder dengan benar")
        return
    
    print("\nPilihan Untuk Mendowload")
    print("1. Video dengan resolution terbaik 😊")
    print("2. Audio dengan mudah")
    
    pilihan_download = input("Masukan Pilihan anda : ").strip()

    ydl_opts = {}

    if pilihan_download == "1":
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{destination}/%(title)s.%(ext)s',
            }

    elif pilihan_download == "2":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferedformat' : 'mp3',
                'preferredquality' : '192'
            }],
            'outtmpl': f'{destination}/%(title)s.%(ext)s',
        }
    else:
        print("Pilihan Tidak Valid, Silahkan Coba Ulang")
        return

    try: 
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_link])
        print(f"File Berhasil terdownload dan terimpan ke {destination}")
    except Exception as e:
        print(f"Terjadi Error silahkan Ulang: {e}")

download_video_yt()
