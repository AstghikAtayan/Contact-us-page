class Helpers:

    def __init__(self, browser):
        self.browser = browser

    def open_url(self, url):
        self.browser.get(url)
        self.browser.maximize_window()

    def close_browser(self):
        if self.browser:
            self.browser.quit()
