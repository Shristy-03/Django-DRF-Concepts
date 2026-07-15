import os
from groq import Groq
from django.conf import settings

def ask_groq(prompt):
    try:
        api_key = getattr(settings, "GROQ_API_KEY", None)
        
        if not api_key:
            return "Error: settings.py me GROQ_API_KEY nahi mili!"
            
        client = Groq(api_key=api_key)
        
        # 🔄 YAHAN MODEL NAME UPDATE KIYA HAI
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant", # Naya supported aur super-fast model
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
        )
        
        return completion.choices[0].message.content
        
    except Exception as e:
        return f"Groq API Error: {str(e)}"