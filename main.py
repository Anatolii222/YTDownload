import sys
import yt_dlp
def downloadMP4(link):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def downloadMP3(link):
    ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.mp3'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
if (len(sys.argv) == 3):
    if (sys.argv[2] == "mp3"):
        downloadMP3(sys.argv[1])
    else:
        downloadMP4(sys.argv[1])
else:
    print("CLI menu YTdownload")
    print("1. Download MP4")
    print("2. Download MP3")
    print("3. Exit")
    answer = input("Please write number: ")
    if (answer == "1"):
            link = input("Write URL: ")
            downloadMP4(link)
    if (answer == "2"):
        link = input("Write URL: ")
        downloadMP3(link)
    else:
        exit(0)


