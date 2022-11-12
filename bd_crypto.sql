CREATE DATABASE IF NOT EXISTS cryptos;

use cryptos;

CREATE table IF NOT EXISTS crypto (
    id_entrada int not null auto_increment primary key,
    fecha varchar(50),
    markecap varchar(50),
    volumen varchar(50),
    open_price varchar(50),
    close_price varchar(50)
)