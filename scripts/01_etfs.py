from common.run import run

PERIODICITIES = ["60", "4H", "1D", "3D", "1W"]

US_SECTOR_ETFS = [
    "XLE",
    "XLRE",
    "XLV",
    "XLU",
    "XLP",
    "XLB",
    "XLK",
    "XLF",
    "XLY",
    "XLI",
    "XLC",
]

US_SMALL_CAP_SECTOR_ETFS = [
    "PSCE",
    "PSCM",
    "PSCC",
    "PSCU",
    "PSCI",
    "PSCF",
    "PSCT",
    "PSCH",
    "PSCD",
]

GLOBAL_SECTOR_ETFS = [
    "IXC",
    "IXJ",
    "KXI",
    "JXI",
    "MXI",
    "IXG",
    "IXN",
    "EXI",
    "RXI",
    "IXP",
]

MARKET_ETFS = [
    "SPY",
    "QQQ",
    "DIA",
    "MDY",
    "IJR",
    "IWC",
    "ACWI",
    "VEA",
    "SPDW",
    "ADRE",
    "BKF",
]

BOND_ETFS = ["TIP", "TLT", "PHB", "BND", "BWX"]

CURRENCY_ETFS = ["UUP", "CYB", "FXB", "FXE", "FXY"]

COMMODITY_ETFS = [
    "UNG",
    "BNO",
    "USO",
    "UGA",
    "DBO",
    "WEAT",
    "JO",
    "CORN",
    "GRU",
    "FUE",
    "CANE",
    "NIB",
    "DBB",
    "SOYB",
    "DBA",
    "GLD",
    "SLV",
    "PPLT",
    "PALL",
    "JJN",
    "JJT",
    "JJU",
    "REMX",
    "SLX",
    "JJC",
    "DBE",
    "GSG",
    "BCI",
]

ASSETS = (
    BOND_ETFS
    + CURRENCY_ETFS
    # + US_SMALL_CAP_SECTOR_ETFS
    # + GLOBAL_SECTOR_ETFS
    # + MARKET_ETFS
    # + COMMODITY_ETFS
    # + US_SECTOR_ETFS
)

if __name__ == "__main__":
    run(ASSETS, PERIODICITIES)
