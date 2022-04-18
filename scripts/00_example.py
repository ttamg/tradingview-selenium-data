from common.run import run

ASSETS = ["AAPL", "MSFT"]
PERIODICITIES = ["60", "4H", "1D", "3D", "1W"]


if __name__ == "__main__":
    run(ASSETS, PERIODICITIES)
