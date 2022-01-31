from pathlib import Path

import requests
from main import parse_arguments


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/100')
    response.raise_for_status()
    links = response.json()['links']['flickr_images']
    for number, link in enumerate(links, 1):
        response = requests.get(link)
        response.raise_for_status()
        with open(f'images/spacex{number}.jpg', 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    args = parse_arguments()
    image_dir = args.image_dir

    Path(image_dir).mkdir(parents=True, exist_ok=True)

    fetch_spacex_last_launch()
