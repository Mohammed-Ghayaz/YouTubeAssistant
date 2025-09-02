import yt_dlp
import requests
import re

def get_subtitle_url(url):
    ydl_opts = {
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],   # pick language code
        "skip_download": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        subtitles = info.get("subtitles", {})
        auto_subs = info.get("automatic_captions", {})

        if "en" in subtitles:
            response = subtitles["en"]
        elif "en" in auto_subs:
            response = auto_subs["en"]

    if response:
        subtitle_url = [r['url'] for r in response if r['ext'] == 'srt']
    
    return subtitle_url[0] if subtitle_url else None

def get_subtitles(subtitle_url):
    # Fetch subtitle file
    if subtitle_url:
        r = requests.get(subtitle_url)
        srt_data = r.text

    srt_data = "No subtitles available"

    # Clean: remove timestamps and numbers from SRT
    def clean_srt(srt_text):
        cleaned = []
        for line in srt_text.splitlines():
            # Skip subtitle indices and timestamps
            if re.match(r'^\d+$', line):  
                continue
            if re.match(r'^\d\d:\d\d:\d\d,\d\d\d', line):  
                continue
            if line.strip() == "":
                continue
            cleaned.append(line.strip())
        return " ".join(cleaned)

    transcript = clean_srt(srt_data)
    return transcript


