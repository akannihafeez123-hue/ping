import requests

# List of your Choreo bot public endpoints
urls = [
    "https://f05fb0c8-be6e-4000-922f-8c579a81ee15-dev.e1-us-east-azure.choreoapis.dev/advance/enhancegodmodetradingengi/v1.0",
    "https://f05fb0c8-be6e-4000-922f-8c579a81ee15-dev.e1-us-east-azure.choreoapis.dev/institutionalincome/airdrop/v1.0",
    "https://f05fb0c8-be6e-4000-922f-8c579a81ee15-dev.e1-us-east-azure.choreoapis.dev/main/main/v1.0",
    "https://f05fb0c8-be6e-4000-922f-8c579a81ee15-dev.e1-us-east-azure.choreoapis.dev/mybindernote/mybindernote/v1.0",
    "https://f05fb0c8-be6e-4000-922f-8c579a81ee15-dev.e1-us-east-azure.choreoapis.dev/solana/solans/v1.0",
    "https://bot6.choreo.dev/endpoint",
    "https://bot7.choreo.dev/endpoint",
    "https://bot8.choreo.dev/endpoint",
    "https://bot9.choreo.dev/endpoint",
    "https://bot10.choreo.dev/endpoint",
"https://f05fb0c8-be6e-4000-922f-8c579a81ee15-dev.e1-us-east-azure.choreoapis.dev/advance/enhancegodmodetradingengi/v1.0
]
# Ping each URL once
for i, url in enumerate(urls, start=1):
    try:
        response = requests.get(url, timeout=10)
        print(f"Bot {i} pinged: {response.status_code}")
    except Exception as e:
        print(f"Bot {i} ping error: {e}")
