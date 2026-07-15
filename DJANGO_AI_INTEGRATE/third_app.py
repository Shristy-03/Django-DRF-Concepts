import requests
import json

# Django server ka URL (Make sure your view URL matches this path)
URL = "http://127.0.0.1:8000/api/groq-chat/"  # Agar aapne urls.py me 'api/gemini-chat/' rakha hai toh yahi rehne dein

print("🤖 AI Chat Console me aapka swagat hai!")
print("Type krein aur Enter dabayein. Chat band karne ke liye 'exit' ya 'quit' likhein.\n")

while True:
    # 🔄 User se dynamically input lena
    user_input = input("✍️  Aapka Sawal: ")
    
    # Loop se bahar nikalne ki condition
    if user_input.lower() in ['exit', 'quit']:
        print("\n👋 Chat band ho rahi hai. Bye!")
        break
        
    # Agar user bina kuch type kiye enter daba de
    if not user_input.strip():
        print("⚠️  Krpya kuch type karein!")
        continue

    # Bheje jaane wala data dynamically update ho gaya
    data_to_send = {
        "prompt": user_input
    }

    print("🚀 Django API ko request bhej rahe hain...")

    try:
        # POST request bhej rahe hain JSON data ke sath
        response = requests.post(
            URL, 
            data=json.dumps(data_to_send), 
            headers={"Content-Type": "application/json"}
        )
        
        # Status code check kar rahe hain
        if response.status_code == 200:
            result = response.json()
            print("\n✅ AI ka jawab:")
            print("-" * 50)
            print(result.get("response"))
            print("-" * 50)
            print("\n") # New line space ke liye
        else:
            print(f"\n❌ Error Aaya! Status Code: {response.status_code}")
            print("Response:", response.text)

    except requests.exceptions.ConnectionError:
        print("\n❌ Connection Error: Kya aapka Django server chal raha hai? Pehle 'python manage.py runserver' chalayein.")
        break