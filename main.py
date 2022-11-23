import json
import requests
import pandas as pd
import csv
import re
from pprint import pprint
from conector import modelo as mo
from controlador import controlador as con
from datetime import datetime

from bs4 import BeautifulSoup
from scrap import scrap_cg

# head, data = scrap_cg.main_scrap()
# # funcion cargar datos en bd
# new_data = []
# for d in data:
#     nd = []
#     for e,i in enumerate(d):
#         if i != '\nN/A\n':
#             if e == 0:
#                 nd.append(re.sub("\\n$|\\n?","",i))
#             else:
#                 nd.append(float(re.sub("\\n|\\n?|\,","",i).replace('$', '')))
#         else:
#             nd.append(re.sub("\\n$|\\n?","",i))
#     new_data.append(nd)
# for d in new_data:
#     con.cargar_historico(d)

a = con.precios_por_fecha()
#print(a)
# b = [x[0] for x in a]
df = pd.DataFrame(a, columns = ['Fecha', 'Open price', 'Close price'])
print(df)
