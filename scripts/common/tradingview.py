import time
from helium import (
    start_chrome,
    kill_browser,
    click,
    write,
    press,
    go_to,
    wait_until,
    refresh,
    Text,
    Button,
    S,
    ENTER,
    BACK_SPACE,
)


LONG = 1.5
SHORT = 0.25
LOAD = 10


class TradingView:
    @staticmethod
    def sign_in(
        username: str, password: str, url: str = "https://tradingview.com", options=None
    ):
        """Sign into Tradingview"""

        if options is not None:
            start_chrome(url, maximize=True, options=options)
        else:
            start_chrome(url, maximize=True)
        click("open user menu")
        click("Sign in")
        click("Email")
        write(username, into="Username or Email")
        write(password, into="Password")
        click("Sign in")
        time.sleep(LONG)
        click("Accept All")
        time.sleep(SHORT)
        refresh()
        # click(S(".tv-header__hamburger-menu"))
        # click("Chart")
        # wait_until(Text("Chart"))

    @staticmethod
    def set_download_folder(path: str):
        """Sets the download folder to the path given"""
        from selenium.webdriver import ChromeOptions

        options = ChromeOptions()
        prefs = {"download.default_directory": path}
        options.add_experimental_option("prefs", prefs)
        return options

    @staticmethod
    def end():
        """Closes the TV session"""
        kill_browser()

    @staticmethod
    def open_layout(url: str):
        """Opens the chart layout required"""
        go_to(url)

    @staticmethod
    def change_asset(asset: str):
        """Change chart to the given asset"""
        click(S("#header-toolbar-symbol-search"))
        time.sleep(LONG)
        write(asset, into="Symbol Search")
        press(ENTER)
        time.sleep(LONG)

    @staticmethod
    def change_periodicity(periodicity: str):
        """Change the candle periodicity"""
        click(S("#header-toolbar-intervals"))
        time.sleep(LONG)
        for char in list(periodicity):
            press(char)
            time.sleep(SHORT)
        press(ENTER)
        time.sleep(LONG)
        click(S("#header-toolbar-intervals"))
        time.sleep(SHORT)

    @staticmethod
    def scroll_to_date(date: str = "19800101"):
        """Scroll left to candle with date in YYYYMMDD format"""
        click(S(".icon-wNyKS1Qc"))
        time.sleep(LONG)
        for i in range(10):
            press(BACK_SPACE)
            time.sleep(SHORT)
        for char in list(date):
            press(char)
            time.sleep(SHORT)
        press(ENTER)
        time.sleep(LOAD)

    @staticmethod
    def download_csv():
        """Download to CSV using standard filenames"""
        click(S(".topLeftButton-4jH252RJ"))
        time.sleep(SHORT)
        click("Export chart")
        time.sleep(SHORT)
        click("Export")
