import asyncio
import aiohttp
import time
import random

# CONFIGURATION SÉCURISÉE (TON TOKEN EXTRAIT)
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzYmduYXR1cmUiOiJmZDlmYA4ZWUzMTNKMjBkODRkZWU3NGU5NTgxYTRIYWM2NzFkMWZkMjNhNjk4OGI1MGM5Tg1ODFkMzVmZDU2NWVjMTYwYTJhZjZmM2NkZmN1ZWU1MmZlNjM2MDQ3ZWJhZjBOTQ3NH0.2NAvYaGG3IjCzNVwxDNTcmDuiPw_uJy0CcgdnvUyxWW"
API_URL = "https://api.teneo.pro"

async def run_teneo():
    # Liste de navigateurs différents pour paraître humain
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    ]

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": random.choice(user_agents),
        "Origin": "https://teneo.pro",
        "Accept": "application/json"
    }

    print(f"🚀 Teneo Node Indétectable : Démarrage...")

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # On envoie une requête vide {} comme le fait l'extension officielle
                async with session.post(API_URL, headers=headers, json={}) as resp:
                    if resp.status == 200:
                        print(f"✅ Teneo : Heartbeat validé | {time.strftime('%H:%M:%S')} | Points récoltés")
                    elif resp.status == 401:
                        print("❌ Erreur : Token expiré ou mal copié !")
                        return
                    else:
                        print(f"⚠️ Statut inattendu : {resp.status}")

                # Délai aléatoire entre 25 et 45 secondes pour simuler un humain
                await asyncio.sleep(random.randint(25, 45))

            except Exception as e:
                print(f"❌ Erreur réseau : {e}. Reconnexion dans 60s...")
                await asyncio.sleep(60)

if __name__ == "__main__":
    try:
        asyncio.run(run_teneo())
    except KeyboardInterrupt:
        pass
