import yt_dlp

def download_youtube(url):
    # กำหนด option สำหรับการดาวน์โหลด
    ydl_opts = {
        'format': 'best',  # ดาวน์โหลดคุณภาพดีที่สุด
        'outtmpl': '%(title)s.%(ext)s'  # ตั้งชื่อไฟล์ตามชื่อวิดีโอ
    }

    # ใช้ yt_dlp ดาวน์โหลดวิดีโอ
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # รับลิงก์ YouTube จากผู้ใช้
    video_url = input("กรุณาใส่ลิงก์ YouTube: ")
    download_youtube(video_url)
    print("ดาวน์โหลดเสร็จสิ้น!")
