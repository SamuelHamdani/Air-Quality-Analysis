import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

aotizhongxin_df = pd.read_csv("./Data/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
changping_df = pd.read_csv("./Data/PRSA_Data_Changping_20130301-20170228.csv")
dingling_df = pd.read_csv("./Data/PRSA_Data_Dingling_20130301-20170228.csv")
dongsi_df = pd.read_csv("./Data/PRSA_Data_Dongsi_20130301-20170228.csv")
guanyuan_df = pd.read_csv("./Data/PRSA_Data_Guanyuan_20130301-20170228.csv")
gucheng_df = pd.read_csv("./Data/PRSA_Data_Gucheng_20130301-20170228.csv")
huairou_df = pd.read_csv("./Data/PRSA_Data_Huairou_20130301-20170228.csv")
nongzhanguan_df = pd.read_csv("./Data/PRSA_Data_Nongzhanguan_20130301-20170228.csv")
shunyi_df = pd.read_csv("./Data/PRSA_Data_Shunyi_20130301-20170228.csv")
tiantan_df = pd.read_csv("./Data/PRSA_Data_Tiantan_20130301-20170228.csv")
wanliu_df = pd.read_csv("./Data/PRSA_Data_Wanliu_20130301-20170228.csv")
wanshouxigong_df = pd.read_csv("./Data/PRSA_Data_Wanshouxigong_20130301-20170228.csv")

aotizhongxin_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
changping_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
dingling_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
dongsi_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
guanyuan_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
gucheng_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
huairou_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
nongzhanguan_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
shunyi_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
tiantan_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
wanliu_df['wd'].fillna(value="Cannot Be Determined", inplace=True)
wanshouxigong_df['wd'].fillna(value="Cannot Be Determined", inplace=True)

table = [aotizhongxin_df, changping_df, dingling_df, dongsi_df, guanyuan_df,
       gucheng_df, huairou_df, nongzhanguan_df, shunyi_df, tiantan_df,
       wanliu_df, wanshouxigong_df]

columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']

for df in table:
  for col in columns:
    df[col].interpolate(method='linear', inplace=True)

china_air_df = pd.concat([aotizhongxin_df, changping_df, dingling_df, dongsi_df, guanyuan_df, gucheng_df, huairou_df, nongzhanguan_df, shunyi_df, tiantan_df, wanliu_df, wanshouxigong_df], ignore_index=True)

china_air_df.dropna(inplace=True)

china_air_df.index = china_air_df['No']

china_air_df.drop('No', axis=1, inplace=True)

year_station_df = china_air_df.groupby(['year', 'station'])[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']].mean().round(2)

st.title('Proyek Analisis Data : Air Quality Dataset \n Oleh : Samuel Christian Hamdani')

col1, col2 = st.columns(2)

with col1:
    st.image("./image/Foto Diri.jpg", width=250)

with col2:
    st.markdown(
        """
        # About Me
        Hello I'm Samuel, I'm a final year student at Gunadarma University majoring in Information System, i'm an data analyst enthusiast which have experienced in using various programming language such as Python, HTMl, CSS, Javascript, SQL, and Java. Nice to meet you all
        """
    )

st.write("""
         # About This Project:
         This is a project assignment where i trained my data analysis skills by learn how to analyze data using Air Quality dataset in beijing. Here is the detail about the dataset:\n
         The dataset contains 9357 instances of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality Chemical Multisensor Device. The device was located on the field in a significantly polluted area, at road level,within an Italian city. Data were recorded from March 2004 to February 2005 (one year) representing the longest freely available recordings of on field deployed air quality chemical sensor devices responses. Ground Truth hourly averaged concentrations for CO, Non Metanic Hydrocarbons, Benzene, Total Nitrogen Oxides (NOx) and Nitrogen Dioxide (NO2) and were provided by a co-located reference certified analyzer. Evidences of cross-sensitivities as well as both concept and sensor drifts are present as described in De Vito et al., Sens. And Act. B, Vol. 129,2,2008 (citation required) eventually affecting sensors concentration estimation capabilities. Missing values are tagged with -200 value.

         Attribute Information:\n
         0 Date (DD/MM/YYYY)\n
         1 Time (HH.MM.SS)\n
         2 True hourly averaged concentration CO in mg/m^3 (reference analyzer)\n
         3 PT08.S1 (tin oxide) hourly averaged sensor response (nominally CO targeted)\n
         4 True hourly averaged overall Non Metanic HydroCarbons concentration in microg/m^3 (reference analyzer)\n
         5 True hourly averaged Benzene concentration in microg/m^3 (reference analyzer)\n
         6 PT08.S2 (titania) hourly averaged sensor response (nominally NMHC targeted)\n
         7 True hourly averaged NOx concentration in ppb (reference analyzer)\n
         8 PT08.S3 (tungsten oxide) hourly averaged sensor response (nominally NOx targeted)\n
         9 True hourly averaged NO2 concentration in microg/m^3 (reference analyzer)\n
         10 PT08.S4 (tungsten oxide) hourly averaged sensor response (nominally NO2 targeted)\n
         11 PT08.S5 (indium oxide) hourly averaged sensor response (nominally O3 targeted)\n
         12 Temperature in Â°C\n
         13 Relative Humidity (%)\n
         14 AH Absolute Humidity\n

         To see the dataset, click this link : https://drive.google.com/file/d/1RhU3gJlkteaAQfyn9XOVAz7a5o1-etgr/view?usp=share_link
""")

st.write ("""
          ## Business Questions
          1. How did the level of air pollution develop in each city from 2013-2017?\n
          2. How did pollution levels develop from 2013 - 2017?\n
          3. Which cities have the highest and lowest levels of air pollution? What are the scores?\n
""")

tab1, tab2, tab3 = st.tabs(["Question 1", "Question 2", "Question 3"])
with tab1:
    st.header("How did the level of air pollution develop in each city from 2013-2017?")
    avgpm25_year_station = year_station_df.groupby(['year', 'station'])['PM2.5'].mean().unstack()
    vis11, ax = plt.subplots(figsize=(12, 6))
    avgpm25_year_station.plot(kind='line', ax=ax)
    ax.set_title('Rata-rata PM2.5 per Tahun dan Stasiun')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Rata-rata PM2.5')
    ax.legend(title='Stasiun', loc='upper left')
    ax.grid(True)
    st.pyplot(vis11)
    st.write("""
             #### Average PM2.5 per Year and Station\n
             The visualization shows that PM2.5 levels in Beijing have generally decreased from 2013 to 2017, but there are significant variations among different stations. Some stations consistently have higher levels than others, and there may be seasonal fluctuations in PM2.5 levels for some stations.
    """)
    vis12, ax2 = plt.subplots(figsize=(12, 6))
    sns.heatmap(avgpm25_year_station, annot=True, cmap='viridis', fmt=".2f", ax=ax2)
    ax2.set_title('Heatmap Rata-rata PM2.5 per Tahun dan Stasiun')
    ax2.set_xlabel('Stasiun')
    ax2.set_ylabel('Tahun')
    st.pyplot(vis12)
    st.write("""
             #### Heatmap of Average PM2.5 per Year and Station\n
             The heatmap shows that PM2.5 levels in Beijing have generally decreased from 2013 to 2017, but there are significant variations among different stations. Some stations consistently have higher levels than others, and there may be seasonal fluctuations in PM2.5 levels for some stations. Overall, the heatmap provides a visual representation of the spatial and temporal variations in PM2.5 levels across the different stations in Beijing.
    """)
 
with tab2:
    st.header("How did pollution levels develop from 2013 - 2017?")
    avgpm25_year_station = year_station_df.groupby('year')['PM2.5'].mean()
    vis2, ax = plt.subplots(figsize=(12, 6))
    avgpm25_year_station.plot(kind='line', ax=ax)
    ax.set_title('Rata-rata PM2.5 per Tahun')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Rata-rata PM2.5')
    ax.grid(True)
    st.pyplot(vis2)
    st.write("""
            #### Average PM2.5 per Year\n
            The line graph shows that the average PM2.5 levels in Beijing have generally decreased from 2013 to 2017. There was a sharp decline between 2014 and 2016, followed by a slight increase in 2017. Overall, the trend indicates a positive improvement in air quality during the period.
    """)
 
with tab3:
    st.header("Which cities have the highest and lowest levels of air pollution? What are the scores?")
    avgpm25_by_station = year_station_df.groupby('station')['PM2.5'].mean().sort_values(ascending=False)
    vis31, ax = plt.subplots(figsize=(12, 6))
    ax.bar(avgpm25_by_station.index, avgpm25_by_station.values)
    ax.set_title('Urutan Tingkat Polusi Stasiun Berdasarkan Rata-rata PM2.5')
    ax.set_xlabel('Station')
    ax.set_ylabel('Rata-rata PM2.5')
    ax.tick_params(axis='x', rotation=45)
    labels = ax.get_xticklabels()
    plt.setp(labels, ha="right")
    st.pyplot(vis31)
    st.write("""
            #### Station Pollution Level Ranking Based on Average PM2.5\n
            The bar chart ranks the stations in Beijing based on their average PM2.5 levels. Aotizhongxin has the highest average PM2.5 level, while Dingling has the lowest. Several other stations, including Gucheng, Dongsi, Wanshouxigong, Wangliu, Guanyuan, Tiantan, Nongzhanguan, Shunyi, Changping, and Huairou, have relatively high average PM2.5 levels. In contrast, Wanliu has a relatively low average PM2.5 level. Overall, the bar chart clearly shows the differences in PM2.5 levels among the different stations in Beijing.
    """)
    vis32, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(year_station_df.groupby('station')['PM2.5'].mean().to_frame(), annot=True, cmap='BuPu', fmt=".2f", ax=ax)
    ax.set_title('Heatmap Rata-rata PM2.5 per Tahun')
    ax.set_xlabel('Stasiun')
    ax.set_ylabel('Tahun')
    st.pyplot(vis32)
    st.write("""
            #### Heatmap Average PM2.5 per Year In Different Stations\n
            The heatmap visually represents the average PM2.5 levels per year for different stations in Beijing from 2013 to 2017. Darker colors indicate lower levels, while lighter colors represent higher levels. The heatmap clearly shows the spatial and temporal variations in PM2.5 levels across the different stations, allowing for easy identification of trends and patterns.
    """)

st.write("""
        # Conclusion
        Based on the analysis of air quality data in Beijing from 2013-2017, it can be concluded that:
        1. Fluctuating Air Pollution Levels: In general, air pollution levels in Beijing, especially PM2.5 concentrations, fluctuate from year to year and between cities. There are some cities that tend to have higher pollution levels than others.

        2. Pollution Increasing and Decreasing Trends: Several cities show significant trends of increasing or decreasing PM2.5 concentrations during the observation period. This indicates that there are factors that affect air quality in different cities differently.

       3.  Differences in Air Quality Between Cities: There are significant differences in air pollution levels between cities. Some cities consistently have higher pollution levels than others. This could be due to various factors such as population density, industrial activity, too many motorized vehicle users, or indiscriminate waste disposal.

        4. Seasonal Influence: There is a possibility of seasonal influences on air quality in Beijing, although this has not been explicitly identified in this analysis. It is important to further analyze the data by paying attention to seasonal patterns to gain more comprehensive insights.

        5. Solutions to overcome pollution: From the analysis results, there needs to be a comprehensive air pollution control effort, including reducing emissions from motor vehicles, industry, and other sources.
""")

st.write("Follow me on linkedin : www.linkedin.com/in/samuel-christian-hamdani")

st.caption('Copyright (c) Samuel Christian Hamdani 2024')