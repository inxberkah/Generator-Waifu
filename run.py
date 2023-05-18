import requests

#####################################################
## Author: https://github.com/inxberkah
## Thanks for API: https://github.com/elliottophellia
#####################################################

def download_waifu_image():
    url = "https://kyoko.rei.my.id/api/sfw.php"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        url_data = data['apiResult']['url'][0]

        png_response = requests.get(url_data)

        if png_response.status_code == 200:
            filename = url_data.split("/")[-1]

            with open(filename, 'wb') as file:
                file.write(png_response.content)

            print(f"Successfully downloaded waifu image: {filename}")
        else:
            print("Failed to download the waifu image.")
    else:
        print("Failed to retrieve data from the API.")

def get_quote_data():
    url = "https://kyoko.rei.my.id/api/quotes.php"

    response = requests.get(url)

    if response.status_code == 200:
        quotes_data = response.json()

        quote_info = quotes_data['apiResult'][0]
        indo_quote = quote_info['indo']
        character = quote_info['character']
        anime = quote_info['anime']

        print("Quote:")
        print(indo_quote)
        print("Character:", character)
        print("Anime:", anime)
    else:
        print("Failed to retrieve data from the API.")

def get_random_anime_data():
    url = "https://kyoko.rei.my.id/api/random.php"

    response = requests.get(url)

    if response.status_code == 200:
        random_data = response.json()

        anime_url = random_data['apiResult']['url'][0]['data']['url']
        anime_title = random_data['apiResult']['url'][0]['data']['title']
        anime_aired = random_data['apiResult']['url'][0]['data']['aired']['string']
        anime_data = {
            "title": anime_title,
            "url": anime_url,
            "aired": anime_aired
        }

        print("Anime Data:")
        print("Title:", anime_data['title'])
        print("URL:", anime_data['url'])
        print("Aired:", anime_data['aired'])
    else:
        print("Failed to retrieve data from the API.")

print("Silahkan pilih:")
print("1. Auto Download Waifu Image")
print("2. Random Quote Anime")
print("3. Random Anime Data")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    download_waifu_image()
elif choice == "2":
    get_quote_data()
elif choice == "3":
    get_random_anime_data()
else:
    print("Invalid choice.")
