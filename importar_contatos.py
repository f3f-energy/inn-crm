import urllib.request
import json
import time

SUPA_URL = "https://nmzifhqivuhdfwlelmxp.supabase.co"
SUPA_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5temlmaHFpdnVoZGZ3bGVsbXhwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQxMTgzNzgsImV4cCI6MjA4OTY5NDM3OH0.AFi43M_euM7iztzOyCamh1HGen3SiBUXQtfknBoWTcc"

print("Lendo contatos...")
with open("contatos.json", "r", encoding="utf-8") as f:
    contatos = json.load(f)

print(f"Total: {len(contatos)} contatos para importar")

sucesso = 0
erros = 0
LOTE = 50

for i in range(0, len(contatos), LOTE):
    lote = contatos[i:i+LOTE]
    payload = json.dumps(lote).encode("utf-8")
    req = urllib.request.Request(
        f"{SUPA_URL}/rest/v1/leads",
        data=payload,
        method="POST"
    )
    req.add_header("apikey", SUPA_KEY)
    req.add_header("Authorization", f"Bearer {SUPA_KEY}")
    req.add_header("Content-Type", "application/json")
    req.add_header("Prefer", "resolution=ignore-duplicates,return=minimal")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            sucesso += len(lote)
            print(f"OK: {sucesso}/{len(contatos)}")
    except Exception as e:
        erros += len(lote)
        print(f"Erro lote {i}: {e}")
    time.sleep(0.2)

print(f"\nConcluido!")
print(f"Sucesso: {sucesso}")
print(f"Erros:   {erros}")
input("\nPressione Enter para fechar...")
