import asyncio
import aiohttp
import time
import random

# CONFIGURATION
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzYmduYXR1cmUiOiJmZDlmYA4ZWUzMTNKMjBkODRkZWU3NGU5NTgxYTRIYWM2NzFkMWZkMjNhNjk4OGI1MGM5Tg1ODFkMzVmZDU2NWVjMTYwYTJhZjZmM2NkZmN1ZWU1MmZlNjM2MDQ3ZWJhZjBOTQ3NH0.2NAvYaGG3IjCzNVwxDNTcmDuiPw_uJy0CcgdnvUyxWW"

# La ligne ci-dessous est COMPLETE (fais défiler vers la droite si besoin)
API_URL = "https://api.teneo.pro/api/v2/heartbeat"

async def run_teneo():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
    ]

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": random.choice(user_agents),
        "Origin": "https://teneo.pro",
        "Accept": "application/json"
    }

    print("🚀 Teneo Node : Connexion au serveur de minage...")

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                # Envoi de la requête à l'adresse API V2 complète
                async with session.post(API_URL, headers=headers, json={}) as resp:
                    if resp.status == 200:
                        print(f"✅ Teneo : Heartbeat validé | {time.strftime('%H:%M:%S')} | +Points")
                    elif resp.status == 404:
                        print("❌ Erreur 404 : L'adresse est encore coupée !")
                    else:
                        print(f"⚠️ Statut : {resp.status}")

                # Attente aléatoire entre 25 et 45 secondes
                await asyncio.sleep(random.randint(25, 45))

            except Exception as e:
                print(f"❌ Erreur : {e}. Reconnexion...")
                await asyncio.sleep(60
        
if __name__ == "__main__":
    asyncio.run(run_teneo())

