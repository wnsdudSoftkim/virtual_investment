@echo off
set price_list=btc_ eth_
set year_list=2017 2018 2019 2020 2021
set value=_1h
@REM (for %%price in (%price_list%) do (
@REM     (for %%year in (%year_list%) do (
@REM         mongoimport --db mydb --collection %%price%%year --type csv --headerline --ignoreBlanks --file C:\Users\lenovo\CoinData\%%price%%year.csv
@REM     )
@REM ))
@REM store 1m coin data
for %%a in (%price_list%) do (
    for %%b in (%year_list%) do (
        mongoimport --db mydb --collection %%a%%b_5m --type csv --headerline --ignoreBlanks --file C:\Users\lenovo\CoinData\5m\%%a%%b.csv
    )
)
