#IMPORTING LIBRARIES
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#DATAFRAME USED
df=pd.read_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv')

#FUNCTION FOR THE MAIN MENU
def menu():
    while True:
        print('''
TIME USE
1- Data Visualization
2- Data Analysis
3- Data Manipulation
4- Exit''')
        inp=int(input('Enter your choice:'))
        if inp==1:
            data_visualization()
        elif inp==2:
            data_analysis()
        elif inp==3:
            data_manipulation()
        elif inp==4:
            sys.exit()
#FUNCTION FOR DATA VISUALIZATION
def data_visualization():
    while True:
        print('''
DATA VISUALIZATION
1- Line Chart- Personal care Vs Sleep
2- Bar Chart- Eating Vs Study
3- Bar Chart- Homework Vs Free time study
4- Exit to Main Menu''')
        inp=int(input('Enter your choice:'))
        if inp==1:
            line_chart1()
        elif inp==2:
            bar_chart1()
        elif inp==3:
            bar_chart2()
        elif inp==4:
            break

#TO PLOT LINE CHART PERSONAL CARE VS SLEEP
def line_chart1():
    df=pd.read_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv')
    df.sort_values(by='Sleep',ascending=False,inplace=True)#sort in descending order
    df1=df.head(10)
    c=df1['Personal care']
    tm=df1['Sleep']
    plt.plot(c,tm)
    plt.xlabel('Personal care')
    plt.ylabel('Sleep')
    plt.show()

#TO PLOT BAR CHART EATING VS STUDY
def bar_chart1():
    df=pd.read_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv')
    df.sort_values(by='Study',ascending=False,inplace=True)#sort in descending order
    df1=df.head()
    x=np.arange(len(df1))
    c=df1['Eating']
    sm=df1['Study']
    plt.bar(x,sm,tick_label=c)
    plt.xlabel('Eating')
    plt.ylabel('Study')
    plt.grid()
    plt.show()

#TO PLOT BAR CHART HOMEWORK VS FREE TIME STUDY
def bar_chart2():
    df=pd.read_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv')
    df.sort_values(by='Free time study',ascending=False,inplace=True)#sort in descending order
    df1=df.head()
    x=np.arange(len(df1))
    c=df1['Homework']
    sm=df1['Free time study']
    plt.bar(x,sm,tick_label=c)
    plt.xlabel('Homework')
    plt.ylabel('Free time study')
    plt.grid()
    plt.show()

#FUNCTION FOR DATA ANALYSIS
def data_analysis():
    while True:
        df=pd.read_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv')
        print('''
DATA ANALYSIS
1- To print Top Records by Personal care
2- To print Top Records by Sleep
3- To print Top Records by Eating
4- To print the General Information of Dataframe
5- To Describe the Dataframe
6- To print specific Column Data
7- To print Maximum value for each column
8- Exit to Main Menu''')
        x=int(input('Enter your choice:'))
        if x==1:
            df.sort_values('Personal Care',ascending=False,inplace=True)
            nor=int(input('How many records to display:'))
            df1=df.head(nor)
            print(df1)
            print(df1[['GEO/ACL00','Personal Care']])
        elif x==2:
            df.sort_values('Sleep',ascending=False,inplace=True)
            nor=int(input('How many records to display:'))
            df1=df.head(nor)
            print(df1)
            print(df1[['GEO/ACL00','Sleep']])
        elif x==3:
            df.sort_values('Eating',ascending=False,inplace=True)
            nor=int(input('How many records to display:'))
            df1=df.head(nor)
            print(df1)
            print(df1[['GEO/ACL00','Eating']])
        elif x==4:
            print(df.info())
        elif x==5:
            print(df.describe())
        elif x==6:
            print('Name of Columns-',df.columns)
            cl=eval(input('enter the Column name to display:'))
            print(df[cl])
        elif x==7:
            print(df.apply(np.max))
        elif x==8:
            break

#FUNCTION FOR DATA MANIPULATION
def data_manipulation():
    while True:
        df=pd.read_csv("http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv")
        print("""
1. Deleting Row
2. Inserting Column
3. Deleting Columnn
4. Renaming Column
5. To go back to main Menu
        """)
        x=int(input("enter ur choice:"))
        if x==1:
            x=int(input('Enter row axis:'))
            df=df.drop(x,axis=0)
            df.to_csv("http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv",index=False)
            df=pd.read_csv("http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv")
            print(df)
        elif x==2:
            x=len(df.columns)
            cn=input('Enter new column name:')
            df[cn]='NaN'
            df.to_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv',index=False)
            df=pd.read_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv')
            print(df)
        elif x==3:
            x=input('Enter which column to delete:')
            df=df.drop(x,axis=1)
            df.to_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv',index=False)
            df=pd.read_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv')
            print(df)
        elif x==4:
            cn=input('Enter colum name which has to be changed:')
            ccn=input('Enter new column name:')
            df=df.rename(columns={cn:ccn})
            df.to_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv',index=False)
            df=pd.read_csv('http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tus_00week&lang=en.csv')
            print(df)
        elif x==5:
            break


menu()

            
        
            
        
    
        


        

