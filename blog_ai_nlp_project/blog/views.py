import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# DIRECT API KEY SETUP (Not recommended for production)
openai.api_key = "sk-YourAPIKey"


@csrf_exempt
def suggest_titles(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('content', '')

            if not content:
                return JsonResponse({'error': 'Content is required'}, status=400)

            # OpenAI completion request using Chat API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an assistant that suggests catchy blog post titles. Provide 3 short, creative suggestions based on the blog content."
                    },
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                max_tokens=100,
                n=1,
                temperature=0.7
            )

            # Extract suggestions from the response
            suggestions = response.choices[0].message.content.strip().split('\n')
            cleaned = [s.strip("-• ").strip() for s in suggestions if s.strip()]

            return JsonResponse({'suggested_titles': cleaned[:3]})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
