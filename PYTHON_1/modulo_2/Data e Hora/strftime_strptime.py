import datetime

data_atual = datetime.datetime.now()

print(data_atual.strftime("%d/%m/%Y %a"))

data_spring = "19/03/2025 12:46"

mascara_ptbr = "%d/%m/%Y %H:%M"
data1 = datetime.datetime.strptime(data_spring, mascara_ptbr)
print(data1.strftime("%d/%m/%Y %H:%M"))

data_spring2 = "2025-12-12 16:30"

mascara_en = "%Y-%m-%d %H:%M"
data2 = datetime.datetime.strptime(data_spring2, mascara_en)
print(data2)