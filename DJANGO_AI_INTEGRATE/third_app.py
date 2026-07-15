import requests
import json

# Django server ka URL (Make sure your view URL matches this path)
URL = "http://127.0.0.1:8000/api/groq-chat/"  # Agar aapne urls.py me 'api/gemini-chat/' rakha hai toh yahi rehne dein

print("🤖 Welcome To AI Chat Console !")
print("Enter Prompt and press Enter . To close the chat type 'exit' or 'quit'.\n")

while True:
    # 🔄 User se dynamically input lena
    user_input = input("✍️  Your Prompt: ")
    
    # Loop se bahar nikalne ki condition
    if user_input.lower() in ['exit', 'quit']:
        print("\n👋 Chat is closing. Bye!")
        break
        
    # Agar user bina kuch type kiye enter daba de
    if not user_input.strip():
        print("⚠️  Prompt something!")
        continue

    # Bheje jaane wala data dynamically update ho gaya
    data_to_send = {
        "prompt": user_input
    }

    print("🚀 Django is sending request to API")

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
            print("\n✅ AI response:")
            print("-" * 50)
            print(result.get("response"))
            print("-" * 50)
            print("\n") # New line space ke liye
        else:
            print(f"\n❌ Error ! Status Code: {response.status_code}")
            print("Response:", response.text)

    except requests.exceptions.ConnectionError:
        print("\n❌ Connection Error: Does your django server is running? Run 'python manage.py runserver' first.")
        break