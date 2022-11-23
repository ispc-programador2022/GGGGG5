import mysql.connector

class Conectar():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = '127.0.0.1',
                port = 3306,
                user = 'root',
                db = 'cryptos'
            )
        except mysql.connector.Error as error_ocurrido:
            print('Error en la conexion, error: ', error_ocurrido)

    def cargar_historico(self, coin):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            sql = 'INSERT INTO crypto VALUES(%s, %s, %s, %s, %s, %s)'
            data = (
                coin.getIdEntrada(),
                coin.getDate(),
                coin.getMarketCap(),
                coin.getVolumen(),
                coin.getOpenPrice(),
                coin.getClosePrice()
            )
            cursor.execute(sql, data)
            self.conexion.commit()
            self.conexion.close()

    def precios_fecha(self):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            sql = "SELECT fecha, open_price, close_price FROM crypto "
            cursor.execute(sql)
            res = cursor.fetchall()
            self.conexion.close()
            return res

class Coin():
    def __init__(self, id_entrada, date, marketcap, volumen, open_price, close_price):
        self.id_entrada = id_entrada
        self.date = date
        self.marketcap = marketcap
        self.volumen = volumen
        self.open_price = open_price
        self.close_price = close_price

    def getIdEntrada(self):
        return self.id_entrada
    def getDate(self):
        return self.date
    def getMarketCap(self):
        return self.marketcap
    def getVolumen(self):
        return self.volumen
    def getOpenPrice(self):
        return self.open_price
    def getClosePrice(self):
        return self.close_price


