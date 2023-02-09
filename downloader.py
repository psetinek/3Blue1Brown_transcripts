import yt_dlp

channel_url = "https://www.youtube.com/@3blue1brown/videos"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'data_audio/%(title)s.%(ext)s',
    'ignoreerrors': True,
    'nooverwrites': True
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([channel_url])
