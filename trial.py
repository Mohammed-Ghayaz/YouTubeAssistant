import yt_dlp

def get_subtitles(video_url: str, lang: str = "en"):
    ydl_opts = {
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": [lang],
        "subtitlesformat": "srt",   # ✅ get SRT directly, no ffmpeg
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        subs = info_dict.get("subtitles", {}) or info_dict.get("automatic_captions", {})

        if not subs:
            return None

        # Prefer SRT
        lang_subs = subs.get(lang, [])
        srt_url = None
        for sub in lang_subs:
            if sub.get("ext") == "srt":
                srt_url = sub["url"]
                break

        if not srt_url and lang_subs:  # fallback: take first available
            srt_url = lang_subs[0]["url"]

        if not srt_url:
            return None

        # ✅ fetch subtitle file with timeout (to avoid 504 in Streamlit)
        import requests
        try:
            r = requests.get(srt_url, timeout=10)
            if r.status_code == 200:
                return r.text
        except requests.exceptions.RequestException:
            return None

    return "Subtitles not found"


# Example usage
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=MFSFcPsMsuE"
    srt_text = get_subtitles(url, "en")
    if srt_text:
        print(srt_text[:1000])  # print first part
    else:
        print("No subtitles found")
