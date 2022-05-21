from requests import get


class META():
    def __init__(self):
        self.url = "https://metavoid.info/api"

    def  animeimage(self, anime_name, type):
        try:
            url = f"{self.url}/animeimage/{type}/{anime_name}"
            response = url
            return response
        except  Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)
    
    def yt_dl(self, yt_url):
        try:
            url = f"{self.url}/ytdl?link={yt_url}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)
    
    def wallpaper(self, site, query, page):
        try:
            url = f"{self.url}/wall/{site}?search={query}&page={page}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def truth(self):
        try:
            url = f"{self.url}/truth"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def dare(self):
        try:
            url = f"{self.url}/dare"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def vanitas(self, user):
        try:
            url = f"{self.url}/vanitas/user={user}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def wiki(self, query, lang):
        try:
            url = f"{self.url}/wiki?search={query}&lang={lang}"        
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def insta_dl(self, url):
        try:
            url = f"{self.url}/igdl?link={url}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)
    
    def fb_dl(self, url):
        try:
            url = f"{self.url}/fbdl?link={url}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def twitter_dl(self, url):
        try:
            url = f"{self.url}/twitter?link={url}"
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def translate(self, text, lang):
        try:
            url = f"{self.url}/translate/text={text}/language={lang}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def urban(self, text, page):
        try:
            url = f"{self.url}/urban?search={text}&page={page}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def urban_random(self):
        try:
            url = f"{self.url}/urban/random"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def torrent_nyaa(self, text, page):
        try:
            url = f"{self.url}/torrent/nyaa?search={text}&page={page}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

   def chatbot(self, message):
        try:
            url = f"{self.url}/api/chatbot?message={message}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)


    def torrent_1337x(self, text, page):
        try:
            url = f"{self.url}/torrent/1337x?search={text}&page={page}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def mangadl(self, manga, chapterno):
        try:
            url = f"{self.url}/mangadl?manga={manga}&chapter={chapterno}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def manga_search(self, text, page):
        try:
            url = f"{self.url}/manga?search={text}&page={page}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)


    def manga_detail(self, text):
        try:
            url = f"{self.url}/manga/detail?id={text}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

    def gogoanimedl(self, text):
        try:
            url = f"{self.url}/anime/gogodl?link={text}"           
            response = get(url, timeout=5)
            return response.json()
        except Exception as e:
            return "An error occured report on @metavoidsupport\n\n{}".format(e)

