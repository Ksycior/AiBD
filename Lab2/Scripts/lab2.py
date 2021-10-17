import pandas as pd
import numpy as np

with open('../Original data/weather.txt') as f:
    lines = f.readlines()

new_new_item = ""

for item in lines:
    new_item = item.replace('S', ' ')
    new_item = new_item.replace('-9999', 'Nan')

    new_new_item += new_item[0:11] + "   " + new_item[11:15] + "   " + new_item[15:17] + "   " + \
                    new_item[17:21] + "   " + new_item[21:]

    final_version = new_new_item.replace("     ", "   ")
    final_version = final_version.replace("     ", "   ")
    final_version = final_version.replace("      ", "   ")
    final_version = final_version.replace("       ", "   ")

    new_new_item = final_version

with open("working_file.txt", "w") as text_file:
    text_file.write(new_new_item)

columns_names = ["id", "year", "month", "element"]
for i in range(1, 32):
    columns_names.append("m_{}".format(i))
data = pd.read_csv('working_file.txt', sep="   ", names=columns_names, header=None, engine='python')

data = data.melt(id_vars=["id", "year", "month", "element"], var_name=["day"], value_name="temp")
data.update(pd.DataFrame({"day": [day[2:] for day in data["day"]]}))

data = (data.pivot_table(index=["year", "month", "day", "id"],
                         columns="element", values="temp", aggfunc='first').reset_index().rename_axis(None, axis=1))

data = (data.assign(date=lambda x: x.day.astype("str").str.zfill(2) + "." + x.month.astype("str").
                    str.zfill(2) + "." + x.year.astype("str")).drop(["day", "month", "year"], axis=1))

data['date'] = pd.to_datetime(data['date'], format='%Y.%m.%d', errors='ignore')
data = (data.filter(items=["date", "PRCP", "TMAX", "TMIN"]))

print(data)

data.to_csv("../Results/final_data.csv")