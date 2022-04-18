import getpass
from .tradingview import TradingView

DATE = "19500101"


def run(assets: list, periodicities: list, from_date=DATE):
    """
    Scrapes the maximum amount of candles available into a CSV file
    for the assets provided and for all the candle periodicities
    """

    print(f"Will fetch {len(assets) * len(periodicities)} CSV files ...")

    username = input("Enter TradingView username: ")
    password = getpass.getpass("Password: ")
    chart_url = input("Enter full TradingView chart URL: ")
    download_to = input(
        "Enter full path to download CSV files to (or blank for default) (no trailing slash): "
    )

    print(f"Initialising ...")
    if download_to:
        options = TradingView.set_download_folder(f"/{download_to}/")
    else:
        options = None
    TradingView.sign_in(username, password, options=options)
    TradingView.open_layout(chart_url)

    for asset in assets:
        TradingView.change_asset(asset)

        for periodicity in periodicities:

            try:
                TradingView.change_periodicity(periodicity)
                TradingView.scroll_to_date(from_date)
                TradingView.download_csv()
                print(f"Done: {asset} {periodicity}")
            except Exception as e:
                print(f"FAILED: {asset} {periodicity} - {e}")

    TradingView.end()
    print(f"Done.")
