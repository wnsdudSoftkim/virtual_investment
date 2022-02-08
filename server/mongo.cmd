@echo off
set price_list=b_ c_ d_ s_ t_ u_
set year_list=2017 2018 2019 2020 2021

@REM (for %%price in (%price_list%) do (
@REM     (for %%year in (%year_list%) do (
@REM         mongoimport --db mydb --collection %%price%%year --type csv --headerline --ignoreBlanks --file C:\Users\lenovo\CoinData\%%price%%year.csv
@REM     )
@REM ))
@REM store 1m coin data
@REM for %%a in (%price_list%) do (
@REM     for %%b in (%year_list%) do (
@REM         mongoimport --db mydb --collection %%a%%b --type csv --headerline --ignoreBlanks --file C:\Users\lenovo\CoinData\%%a%%b.csv
@REM     )
@REM )
@REM store 1h coin data
for %%a in (%price_list%) do (
    for %%b in (%year_list%) do (
        mongoimport --db mydb --collection %%a%%b --type csv --headerline --ignoreBlanks --file C:\Users\lenovo\CoinData\%%a%%b_1h.csv
    )
)