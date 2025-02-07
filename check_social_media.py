platforms = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Facebook": "https://www.facebook.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/{}",
}

def check_username(username):
    available_platforms = []
    for platform, url in platforms.items():
        response = requests.get(url.format(username))
        if response.status_code == 404:
            available_platforms.append(platform)
    return available_platforms

if __name__ == "__main__":
    username = input("Masukkan username yang ingin diperiksa: ")
    available_platforms = check_username(username)
    if available_platforms:
        print(f"Username '{username}' tersedia di: {', '.join(available_platforms)}")
    else:
        print(f"Username '{username}' tidak tersedia di platform yang diperiksa.")
