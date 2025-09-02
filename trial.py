import yt_dlp
import requests
import re

def get_subtitle_url(url, lang="en"):
    """
    Extracts subtitle URL (SRT) for a given YouTube video.
    Does not use ffmpeg.
    """
    ydl_opts = {
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": [lang],   # Choose language
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        subtitles = info.get("subtitles", {})
        auto_subs = info.get("automatic_captions", {})

        response = None
        if lang in subtitles:
            response = subtitles[lang]
        elif lang in auto_subs:
            response = auto_subs[lang]

        if response:
            subtitle_url = [r['url'] for r in response if r['ext'] == 'srt']
            return subtitle_url[0] if subtitle_url else None

    return None


def get_subtitles(subtitle_url):
    """
    Downloads and cleans SRT subtitles from a given subtitle URL.
    """
    if not subtitle_url:
        return "No subtitles available"

    r = requests.get(subtitle_url)
    srt_data = r.text

    def clean_srt(srt_text):
        cleaned = []
        for line in srt_text.splitlines():
            # Skip subtitle indices and timestamps
            if re.match(r'^\d+$', line):  
                continue
            if re.match(r'^\d\d:\d\d:\d\d,\d\d\d', line):  
                continue
            if not line.strip():
                continue
            cleaned.append(line.strip())
        return " ".join(cleaned)

    return clean_srt(srt_data)

