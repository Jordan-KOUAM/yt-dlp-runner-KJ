import sys
import subprocess
import json

url = sys.argv[1]
result = subprocess.run(["yt-dlp", "--flat-playlist", "-J", url], capture_output=True, text=True)

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(json.loads(result.stdout), f, indent=2)
