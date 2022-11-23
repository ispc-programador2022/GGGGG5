from conector import modelo as mo


def cargar_historico(d):
    con = mo.Conectar()

    fecha = d[0]
    mc = d[1]
    vol = d[2]
    op = d[3]
    cp = d[4]
    moneda = mo.Coin(0, fecha, mc, vol, op, cp)
    con.cargar_historico(moneda)


def precios_por_fecha():
    ''' devuelve un lista de tuplas.
    [("fecha", "open_price", "close_price"), ... ()]
    '''
    con = mo.Conectar()
    a = con.precios_fecha()
    return a