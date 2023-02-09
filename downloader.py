import yt_dlp

channel_url = "https://www.youtube.com/watch?v=brU5yLm9DZM&t=39s"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'data_audio/%(title)s.%(ext)s',
    'ignoreerrors': True,
    # 'playliststart': 1,
    # 'playlistend': 5,
    # 'download_archive': 'downloaded_videos.txt',
    'nooverwrites': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([channel_url])
