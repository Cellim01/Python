# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:56:16 2024

@author: user
"""

import pandas as pd


             #Car sales  data
             
             
             
df = pd.read_csv(r"C:\Users\user\Desktop\Car_sales.csv")




            #Delete unused data

df = df.dropna()

df = df.drop ( "Wheelbase" , axis=1 )   

df = df.drop ( "Width" , axis=1 )    

df = df.drop ( "Curb_weight" , axis=1 )

df = df.drop ( "Length" , axis=1 )   

df = df.drop ( "__year_resale_value" , axis=1 ) 

df = df.drop ( "Fuel_capacity" , axis=1 )        

df = df.drop ( "Power_perf_factor" , axis=1 )   

df = df.drop ( "Fuel_efficiency" , axis=1 )
   



                   #FİLTRELEME




        # FONKSİYONLAR 
        
        
def beygir_filtre ():
    
    beygir_min = int(input("Minimum Beygir : "))

    beygir_max = int(input("Maaksimum Beygir : "))

    beygir_liste = df[ (df["Horsepower"] >= beygir_min) & df["Horsepower"] <= beygir_max ]

    print(beygir_liste)



def marka_filtre ():
    
    marka_name = input(" Marka ismi : ")

    marka_liste = df[ df["Manufacturer"] == marka_name ]["Model"]

    print(marka_liste)




def fiyat_filtre():
    
    fiyat_min = float(input(" Minimum Fiyat : "))

    fiyat_max = float(input( "Maksimum fiyat : "))

    fiyat_liste = df[(df["Price_in_thousands"] >= fiyat_min) & (df["Price_in_thousands"] <= fiyat_max)]

    print(fiyat_liste)



def hacim_filtre():
    
    motorhacmi_min = float(input(" Minimum Motor hacmi : "))

    motorhacmi_max = float(input(" Maksimum Motor hacmi : "))

    motor_liste = df[(df["Engine_size"] >= motorhacmi_min) & (df["Engine_size"] <= motorhacmi_max)]

    print(motor_liste)


         # FONKSİYONLAR BİTTİ

 
print("Merhaba , araçları nasıl sınıflandırmak istersin ? ")

print(" 1-) Beygir \n 2-) Marka \n 3-) Fiyat \n 4-) Motor Hacmi")


secim = int(input("Secim : "))

while (True):


    if (secim == 1):
        
        beygir_filtre()
        
    
    elif( secim == 2 ):
        
        marka_filtre()
        

    elif( secim == 3):
    
        fiyat_filtre()    
    

    elif ( secim == 4):
        
        hacim_filtre()
        
    secim = int(input("Devam etmek istiyor musun ? ( 1-2-3-4, çıkmak için 0): "))
   
    if secim == 0:
        
        break

  
print("Filtreleme sonlandı. ")




