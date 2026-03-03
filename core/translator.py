import requests
import time


class TitleTranslator:

    def __init__(self):
        self.base_url = "https://api.mymemory.translated.net/get"

    def translate(self, text, source="es", target="en"):
        """
        Translate text using MyMemory free API.
        """

        params = {
            "q": text,
            "langpair": f"{source}|{target}"
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            translated_text = data["responseData"]["translatedText"]

            return translated_text

        except Exception as e:
            print("Translation failed:", e)
            return text  # fallback to original text