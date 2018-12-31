init offset = -100
define NEWS_URL = "https://yggdrasil-studio.github.io/Discouraged-Workers/news/news.json"
define NEWS_CHECK_INTERVAL = 1.0
screen news(news):
    zorder 100
    modal True
    add "#000000c0"
    frame:
        xalign .5
        yalign .5
        xpadding 10
        ypadding 10
        xmaximum 820
        has vbox:
            spacing 10
        imagebutton idle NewsImage() action OpenURL(news["link"])
        label news["text"]:
            style "confirm_prompt" xalign .5
        textbutton _("{font=[gui.fontawesome]}{/font} Return") action Hide("news"):
            xalign .5
default persistent.news_last_checked = 0
default persistent.seen_news = 0
init python:
    import time, requests, certifi
    def news_thread():
        print("Checking the news.")
        ca_file = os.path.join(config.gamedir, certifi.where())
        if not os.path.exists(ca_file):
            ca_file = os.path.join(config.savedir, "cacert.pem")
            with open(ca_file, "wb") as f:
                f.write(renpy.file("python-packages/certifi/cacert.pem").read())
        now = time.time()
        if not config.developer:
            if now < persistent.news_last_checked + (NEWS_CHECK_INTERVAL * 86400):
                return
        persistent.news_last_checked = now
        if persistent.news:
            old_version = persistent.news["version"]
        else:
            old_version = 0
        news = requests.get(NEWS_URL, verify=ca_file).json()
        if news["version"] == old_version:
            return
        news["image_data"] = requests.get(news["image"], verify=ca_file).content
        news["image_data"] = requests.get(news["thumb"], verify=ca_file).content
        persistent.news = news
        return
    def run_news_thread():
        try:
            news_thread()
        except:
            import traceback
            traceback.print_exc()
    @renpy.pure
    class ShowNews(Action):
        def __call__(self):
            if not persistent.news:
                return
            persistent.seen_news = persistent.news["version"]
            renpy.show_screen("news", persistent.news)
            renpy.restart_interaction()
        def get_sensitive(self):
            return persistent.news is not None
    def HasUnseenNews():
        if persistent.news is None:
            return False
        return persistent.news["version"] > persistent.seen_news
    def NewsImage():
        if persistent.news is None:
            return Null()
        return im.Data(persistent.news["image_data"], persistent.news["image"])
    def NewsThumb():
        if persistent.news is None:
            return Null()
        return im.Data(persistent.news["image_data"], persistent.news["thumb"])
init 100 python:
    renpy.invoke_in_thread(news_thread)