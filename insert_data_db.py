from sqlalchemy import create_engine
import pandas as pd
import pymysql
from datetime import datetime

dataFrame = pd.read_csv("https://espinosadvlpr.github.io/Datos_Asignaturas_Inv_U.csv")
for indice in range(len(dataFrame)):
    date = datetime.strptime(dataFrame['birthdate'][indice], '%d/%m/%y')
    dataFrame['birthdate'][indice] = str(date.year)+'-'+str(date.month)+'-'+str(date.day)


tableName = "survey_data_csv"
sqlEngine = create_engine(
    'mysql+pymysql://root:a1d2m3i4n@127.0.0.1/gestion_datos', pool_recycle=3600)
dbConnection = sqlEngine.connect()

try:
    frame = dataFrame.to_sql(tableName, dbConnection, if_exists='append')
except ValueError as vx:
    print(vx)
except Exception as ex:
    print(ex)
else:
    print("Data successfully charged to table:", tableName)
finally:
    dbConnection.close()
"""
"""