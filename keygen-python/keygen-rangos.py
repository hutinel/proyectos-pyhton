import datetime

ahora = datetime.datetime.now()
mes = ahora.strftime("%b")
dia_numero = ahora.strftime("%d")
ano_numero = ahora.strftime("%Y")
print("#" + mes.upper() + dia_numero + ano_numero + ".j")
