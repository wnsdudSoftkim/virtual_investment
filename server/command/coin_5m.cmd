@echo off
set price_list=btc_ eth_
set year_list=2017 2018 2019 2020 2021
set value=_1h
set host="-"
for %%a in (%price_list%) do (
    for %%b in (%year_list%) do (
        mongoimport --uri %host%  --collection %%a%%b_5m --type csv --headerline --ignoreBlanks --file C:\Users\lenovo\CoinData\5m\%%a%%b.csv
    )
)