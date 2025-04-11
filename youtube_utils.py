import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_youtube_transcript(video_url):
    video_id_match = re.search(r"v=([^&]+)", video_url)
    video_id = video_id_match.group(1) if video_id_match else video_url.split("/")[-1]
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['ar'])
        transcript = " ".join([item["text"] for item in transcript_list])
        return transcript
    except Exception as e:
        return f"❌ Could not retrieve transcript for this video in Arabic. Error: {e}"
