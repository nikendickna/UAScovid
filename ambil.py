import json
import requests

response = requests.get('https://api.kawalcorona.com/indonesia')
data_corona = response.json()[0]
print("Jumlah Pasien \n")
print("\t Positif\t: "+data_corona['positif'])
print("\t Sembuh\t\t: "+data_corona['sembuh'])
print("\t Meninggal\t: "+data_corona['meninggal'])
print("\n by:")
print("DICKNA NIKEN LARASAKTI")
print("170403010054")