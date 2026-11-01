"""Download public TacOT assets and verify their SHA-256 checksums."""
from pathlib import Path
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import time
SOURCE = "https://tacot-research.cuddlyteal512.chatgpt.site/assets/"
manifest = json.loads(Path("asset-manifest.json").read_text())
destination = Path("dist/assets")
destination.mkdir(parents=True, exist_ok=True)
def import_asset(item):
    name, expected = item
    path = destination / name
    if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == expected:
        return
    request = Request(SOURCE + name, headers={"User-Agent": "Mozilla/5.0", "Accept": "*/*"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=180) as response:
                data = response.read()
            break
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2)
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("Asset integrity check failed: " + name)
    path.write_bytes(data)
    print("Imported", name)
with ThreadPoolExecutor(max_workers=4) as executor:
    list(executor.map(import_asset, manifest.items()))
