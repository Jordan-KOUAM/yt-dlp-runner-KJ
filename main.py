import sys
import json
from yt_dlp import YoutubeDL

url = sys.argv[1]
output_filename = sys.argv[2] if len(sys.argv) > 2 else "output.json"

with YoutubeDL({'dump_single_json': True, 'extract_flat': True}) as ydl:
    result = ydl.extract_info(url, download=False)

with open(output_filename, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

