import pytz
import datetime

data = datetime.datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

data_final = datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data.strftime("%d/%m/%Y %H:%M")) #Horario timezone diferente