CREATE DATABASE IF NOT EXISTS cryptos;

use cryptos;

CREATE table IF NOT EXISTS crypto (
    id_entrada int not null auto_increment primary key,
    fecha date,
    marketcap float,
    volumen float,
    open_price float,
    close_price float
)