from datetime import datetime
import os
from pathlib import Path

from urllib.parse import urlparse
from environs import Env
import requests
from main import parse_arguments


def cut_extension(url):
    parsed = urlparse(url)
    filename_extension = os.path.splitext(parsed.path)
    return filename_extension[-1]


def fetch_apod_nasa_urls(api_key, count=10):
    image_urls = []
    while len(image_urls) < count:
        response = requests.get(
            "https://api.nasa.gov/planetary/apod",
            params={"api_key": api_key, "count": count},
        )
        response.raise_for_status()
        for apod in response.json():
            if apod["media_type"] == "image":
                image_urls.append(apod['url'])
    return image_urls[:count]


def fetch_epic_nasa_urls(api_key):
    image_urls = []
    response = requests.get(
        "https://api.nasa.gov/EPIC/api/natural/images",
        params={"api_key": api_key},
    )
    response.raise_for_status()
    for image_metadata in response.json():
        image_name = image_metadata["image"]
        image_datetime = datetime.fromisoformat(image_metadata["date"])
        image_date = image_datetime.strftime("%Y/%m/%d")
        image_urls.append(
            f"https://api.nasa.gov/EPIC/archive/natural/{image_date}"
            f"/png/{image_name}.png"
        )
    return image_urls


def save_nasa_image(list_image_urls, api_key):
    for number, url in enumerate(list_image_urls, 1):
        response = requests.get(url, params={'api_key': api_key})
        response.raise_for_status()
        image_extension = cut_extension(url)
        with open(f'images/nasa{number}{image_extension}', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    env = Env()
    env.read_env()

    nasa_api_key = env.str('NASA_API_KEY')

    args = parse_arguments()
    image_dir = args.image_dir

    Path(image_dir).mkdir(parents=True, exist_ok=True)

    all_nasa_images = []
    epic_nasa_images = fetch_epic_nasa_urls(nasa_api_key)
    all_nasa_images.extend(epic_nasa_images)
    apod_nasa_images = fetch_apod_nasa_urls(nasa_api_key)
    all_nasa_images.extend(apod_nasa_images)
    save_nasa_image(all_nasa_images, nasa_api_key)
