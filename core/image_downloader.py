import os
import hashlib
import requests


class ImageDownloader:

    def __init__(self, save_directory="assets/images"):
        self.save_directory = save_directory
        os.makedirs(self.save_directory, exist_ok=True)

    def _generate_filename(self, image_url):
        """
        Generate deterministic filename using MD5 hash of image URL.
        Prevents duplicate downloads.
        """
        hash_object = hashlib.md5(image_url.encode())
        return hash_object.hexdigest() + ".jpg"

    def download(self, image_url):
        if not image_url:
            return None

        filename = self._generate_filename(image_url)
        filepath = os.path.join(self.save_directory, filename)

        # Skip if already downloaded
        if os.path.exists(filepath):
            print("Image already exists. Skipping download.")
            return filepath

        try:
            response = requests.get(image_url, timeout=10)
            response.raise_for_status()

            with open(filepath, "wb") as f:
                f.write(response.content)

            print("Image downloaded:", filename)
            return filepath

        except Exception as e:
            print("Failed to download image:", e)
            return None