from common.run import run

PERIODICITIES = ["60", "4H", "1D", "3D"]

ASSETS = [
    "ADAUSDT",
    "ATOMUSDT",
    "ALGOUSDT",
    "BATUSDT",
    "BNBUSDT",
    "BTCUSDT",
    "SOLUSDT",
    "CELRUSDT",
    "CVCUSDT",
    "DASHUSDT",
    "FTTUSDT",
    "ENJUSDT",
    "EOSUSDT",
    "ETHUSDT",
    "MATICUSDT",
    "HOTUSDT",
    "LUNAUSDT",
    "LTOUSDT",
    "IOTAUSDT",
    "LINKUSDT",
    "LTCUSDT",
    "MFTUSDT",
    "MTLUSDT",
    "NANOUSDT",
    "NEOUSDT",
    "AAVEUSDT",
    "OMGUSDT",
    "QTUMUSDT",
    "RLCUSDT",
    "RVNUSDT",
    "TOMOUSDT",
    "TRXUSDT",
    "VETUSDT",
    "WANUSDT",
    "WAVESUSDT",
    "XLMUSDT",
    "MANAUSDT",
    "XRPUSDT",
    "XTZUSDT",
    "AVAXUSDT",
    "ZILUSDT",
    "ZRXUSDT",
    "THETAUSDT",
    "SUSHIUSDT",
    "DOTUSDT",
]


if __name__ == "__main__":
    run(ASSETS, PERIODICITIES)
