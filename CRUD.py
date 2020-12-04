import pymysql
import matplotlib.pyplot as plt
import numpy as np
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  db="my_python"
)
myCursor = mydb.cursor()

mydb.commit()
myCursor.execute("SELECT sujet FROM atb WHERE id=3")
result = myCursor.fetchone()

for x in result:
  print(x)

myCursor.execute("SELECT sujet FROM atb WHERE id=7")
result1 = myCursor.fetchone()
for z in result1:
  print(z)

  y = np.array([85, 25, 25, 15])
  lables = x, z, 'SPA', 'PHI'

  plt.pie(y, labels=lables, autopct='%1.1f%%', explode=(0.1, 0, 0.1, 0.1))
  plt.show()
