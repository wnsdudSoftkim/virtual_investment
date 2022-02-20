@echo off
set price_list=btc_ eth_
set year_list=2017 2018 2019 2020 2021
set value=_1h
set host="mongodb://flgkselql98:tjdnftkfka0501Q@investment-shard-00-00.9ea8t.mongodb.net:27017,investment-shard-00-01.9ea8t.mongodb.net:27017,investment-shard-00-02.9ea8t.mongodb.net:27017/Investment?ssl=true&replicaSet=atlas-9s1ro9-shard-0&authSource=admin&retryWrites=true&w=majority"
for %%a in (%price_list%) do (
    for %%b in (%year_list%) do (
        mongoimport --uri %host%  --collection %%a%%b_5m --type csv --headerline --ignoreBlanks --file C:\Users\lenovo\CoinData\5m\%%a%%b.csv
    )
)