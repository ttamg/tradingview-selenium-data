# tradingview-selenium-data

Simple Selenium (Python Helium) script to pull TradingView data into CSV files

## Objective

In order to perform useful backtesting and also create training data, it's useful to be able to download **TradingView** data as CSV data. This script uses a Python implementation of Selenum called Helium to pull of this data into CSV files.

Why use TradingView?

- TradingView can provide longer time series than some of the other data APIs, although you need to scroll left for it to load that data.

- Also TradingView will download data for your indicators into the CSV file also and that allows you to use that data in your backtests or ML training data.

- It allows you to work together with others that use TradingView or Pinescript for building out potential strategies and indicators

> _WARNING_ - Scraping data this way does not seem to be against [TradingView's current use policy](https://www.tradingview.com/policies/) but that might change. So check the use policy. And in any event, excessive scraping of any data is not the polite thing to do so keep this to the minimum and do so sparingly.

## Getting started

### Prerequisites

1. You need a paid **TradingView** account with permissions to download data as a CSV. You know if you have the right sort of account if you can use the _Export chart data ..._ option in the TradingView UI

1. Python 3.8+ installed on your machine and some ability to use it.

1. Google Chrome installed

1. Relevant chromedriver installed for your version of Chrome - https://chromedriver.chromium.org/downloads

### Installation

Clone the repo

    git clone https://github.com/ttamg/tradingview-selenium-data.git

Either, install using poetry. From the cloned project directory

    poetry install

Or alternatively install using pip from the cloned project directory

    pip install -r requirements.txt

## Scraping data

The scripts use the `TradingView` class that is in the `scripts.common.tradingview` module.  This is a simple set of **helium** methods that interact with the **TradingView** UI

The `TradingView` class has methods that do the following:

- Connect to TradingView and log in
- Navigate to the chart layout you wish to download (with all the indicators you have defined)
- Switch the asset or periodicity of the candles
- Scroll to load the candles from a particular start date (so as to fetch more data)
- Download the data as CSV

The class does not do anything particularly special beyond scraping and replicates what you would do with the UI yourself in the browser.  

The `run()` method in the `scripts.common.run` module is a method that loops over the assets and periodicities you provide to fetch and download the market data you require.  It calls the `TradingView` class at the relevant points. 

See the Python code in `scripts.common` for more information.

> _NOTE_ - some of the HTML tags on TradingView are a bit brittle so this may need some tweaks from time to time as TradingView update their UI.

## Scripts

See the example scripts in the `scripts` folder for examples on how to scrape data.

If all is set up correctly with your chromedriver the `00_example.py` file should run the script and download a few test CSV files

    python 00_example.py

## Issues

Note that the asset given picks up the top of the list asset with that ticker. On TradingView there are many assets options with the same ticker so this may not pick up quite what you want. It is not obvious how this can be improved without significant work.
