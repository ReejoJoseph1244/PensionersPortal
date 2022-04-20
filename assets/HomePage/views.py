from http.client import HTTPResponse
from sqlite3 import Cursor
from django.shortcuts import render
from django.http import HttpResponse
from MySQLdb import _mysql
import mysql.connector as sqltor
from .models import NSAP_deatils
from .models import CENSUS_Detail
import pandas as pd

# Create your views here.

def home(request):
    mycon = sqltor.connect(host="localhost",user="root",passwd="",database="pensionersdetails")
    cursor = mycon.cursor()
    cursor.execute("SELECT SUM(Total_Beneficiary) FROM homepage_nsap_deatils")
    sql_data1 = pd.DataFrame(cursor.fetchone())
    sql_data1.columns = cursor.column_names
    getting=sql_data1.loc[0][0]

    cursor.execute("select SUM(Total_Males + Total_Females) from homepage_census_detail where age>=60")
    sql_data2 = pd.DataFrame(cursor.fetchone())
    sql_data2.columns = cursor.column_names
    eligible=sql_data2.loc[0][0]

    miscount = eligible-getting

    #Statewise fetching
    State_list=['Andaman and Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Delhi','Goa','Gujrat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshwadeep','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajashthan','Sikkim','Tamil Nadu','Telangana','Dadar and Nagar','Daman and Diu','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']
    def State_fetch(temp):
        cursor.execute("SELECT SUM(Total_Beneficiary) FROM homepage_nsap_deatils where State = (%s)",(temp,))
        sql_data3 = pd.DataFrame(cursor.fetchone())
        sql_data3.columns = cursor.column_names
        #print(sql_data3.loc[0][0])
        return sql_data3.loc[0][0]

    class district:
        Andaman_and_Nicobar = State_fetch(State_list[0])
        Andhra_Pradesh = State_fetch(State_list[1])
        Arunachal_Pradesh = State_fetch(State_list[2])
        Assam = State_fetch(State_list[3])
        Bihar = State_fetch(State_list[4])
        Chandigarh = State_fetch(State_list[5])
        Chhattisgarh = State_fetch(State_list[6])
        Delhi = State_fetch(State_list[7])
        Goa = State_fetch(State_list[8])
        Gujrat = State_fetch(State_list[9])
        Haryana = State_fetch(State_list[10])
        Himachal_Pradesh = State_fetch(State_list[11])
        Jammu_and_Kashmir = State_fetch(State_list[12])
        Jharkhand = State_fetch(State_list[13])
        Karnataka = State_fetch(State_list[14])
        Kerala = State_fetch(State_list[15])
        Ladakh = State_fetch(State_list[16])
        Lakshwadeep = State_fetch(State_list[17])
        Madhya_Pradesh = State_fetch(State_list[18])
        Maharashtra = State_fetch(State_list[19])
        Manipur = State_fetch(State_list[20])
        Meghalaya = State_fetch(State_list[21])
        Mizoram = State_fetch(State_list[22])
        Nagaland = State_fetch(State_list[23])
        Odisha = State_fetch(State_list[24])
        Puducherry = State_fetch(State_list[25])
        Punjab = State_fetch(State_list[26])
        Rajashthan = State_fetch(State_list[27])
        Sikkim = State_fetch(State_list[28])
        Tamil_Nadu = State_fetch(State_list[29])
        Telangana = State_fetch(State_list[30])
        Dadar_and_Nagar = State_fetch(State_list[31]) + State_fetch(State_list[32])
        Tripura = State_fetch(State_list[33])
        Uttarakhand = State_fetch(State_list[34])
        Uttar_Pradesh = State_fetch(State_list[35])
        West_Bengal = State_fetch(State_list[36])


    

    return render(request,'home.html',{'getting':getting,'eligible':eligible,'miscount':miscount,'district':district,'State_list':State_list})

