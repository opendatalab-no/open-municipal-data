import pandas as pd

# read_file = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/42 - Forbruksanalyse-Bodø Kommune - Tverlandet Bo og Servicesenter - 10.10.2021 9.37.18.xls')
# read_file.to_csv (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Bodø/42o.csv', index = None, header=True)

read_file = pd.read_excel (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/EsaveExport_Trondheim Kommune_Trondheim_10121314.xls')
read_file.to_csv (r'/Users/erlendstav/Documents/SamÅpne/Datasett/Energidata/Trondheim/EsaveExport_Trondheim Kommune_Trondheim_10121314.csv', index = None, header=True)
