import json
import requests
import pandas as pd
import csv
from pprint import pprint
from conector import modelo as mo
from controlador import controlador as con

from bs4 import BeautifulSoup
from scrap import scrap_cg

head, data = scrap_cg.main_scrap()
for d in data:
    con.cargar_historico(d)

