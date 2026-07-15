from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .groq_helper import ask_groq # 🔄 Groq helper import kiya

@csrf_exempt
def gemini_chat_view(request): # Aap chahein to view ka naam badal kar groq_chat_view bhi rakh sakte hain
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_prompt = data.get("prompt", "")
            
            if not user_prompt:
                return JsonResponse({"error": "Prompt dena zaroori hai!"}, status=400)
            
            # 🔄 Yahan Groq function ko call kiya
            ai_response = ask_groq(user_prompt)
            
            return JsonResponse({"status": "success", "response": ai_response})
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
            
    return JsonResponse({"error": "Sirf POST requests allowed hain"}, status=405)