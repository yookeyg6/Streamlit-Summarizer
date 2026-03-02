import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Ошибка: API ключ не найден. Проверьте файл .env")
    sys.exit(1)

client = genai.Client(api_key=api_key)

try:
    with open("article.txt", "r", encoding="utf-8") as f:
        article_text = f.read()
except FileNotFoundError:
    print("Файл article.txt не найден.")
    sys.exit(1)

prompt = f"""
Выдели 5 главных мыслей из этого текста списком:
{article_text}
"""

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    summary_text = response.text
except Exception as e:
    print("Ошибка запроса к Gemini:", e)
    sys.exit(1)

try:
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary_text)
except Exception as e:
    print("Ошибка при сохранении файла:", e)
    sys.exit(1)

print("Суммаризация завершена. Результат сохранён в summary.txt")