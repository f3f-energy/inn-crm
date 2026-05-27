import urllib.request
import json

TOKEN = "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"
GIST_ID = "dc604652e59c3126043b3a7a3a6e02a4"

print("Lendo index.html...")
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

print(f"Arquivo lido: {len(content)} bytes")
print("Atualizando Gist...")

payload = json.dumps({
    "description": "INN CRM Solar - Innovatis Energia",
    "files": {
        "inn.html": {
            "content": content
        }
    }
}).encode("utf-8")

req = urllib.request.Request(
    f"https://api.github.com/gists/{GIST_ID}",
    data=payload,
    method="PATCH"
)
req.add_header("Authorization", f"token {TOKEN}")
req.add_header("Content-Type", "application/json")
req.add_header("User-Agent", "INN-Deploy")

try:
    r = urllib.request.urlopen(req, timeout=30)
    print(f"Gist atualizado! Status: {r.status}")
except urllib.error.HTTPError as e:
    print(f"Erro HTTP: {e.code} - {e.read().decode()}")
except Exception as e:
    print(f"Erro: {e}")
