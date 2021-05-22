# Lab16

Parsing script for https://newsapi.org/ and https://finance.yahoo.com/

## Installation

Use the anaconda3 environment https://www.anaconda.com/products/individual

## Usage

```bash
main.py [-h] [--path PATH] [-f FROM_DATE] [-t TO_DATE] [-k KEYWORD]
               [-s SOURCES [SOURCES ...]] [-c COMPANIES [COMPANIES ...]]
               
###Example
main.py --path ./results -f 2021-04-20 -t 2021-05-15 -k Tesla -s reuters rt -c AAPL AMZN
```