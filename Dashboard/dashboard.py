import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    st.image("./image/Visualisasi Air_Quality 1.1.png")
    st.write("""
             #### Average PM2.5 per Year and Station\n
             The visualization shows that PM2.5 levels in Beijing have generally decreased from 2013 to 2017, but there are significant variations among different stations. Some stations consistently have higher levels than others, and there may be seasonal fluctuations in PM2.5 levels for some stations.
    """)
    st.image("./image/Visualisasi Air_Quality 1.2.png")
    st.write("""
             #### Heatmap of Average PM2.5 per Year and Station\n
             The heatmap shows that PM2.5 levels in Beijing have generally decreased from 2013 to 2017, but there are significant variations among different stations. Some stations consistently have higher levels than others, and there may be seasonal fluctuations in PM2.5 levels for some stations. Overall, the heatmap provides a visual representation of the spatial and temporal variations in PM2.5 levels across the different stations in Beijing.
    """)
 
with tab2:
    st.header("How did pollution levels develop from 2013 - 2017?")
    st.image("./image/Visualisasi Air_Quality 2.png")
    st.write("""
            #### Average PM2.5 per Year\n
            The line graph shows that the average PM2.5 levels in Beijing have generally decreased from 2013 to 2017. There was a sharp decline between 2014 and 2016, followed by a slight increase in 2017. Overall, the trend indicates a positive improvement in air quality during the period.
    """)
 
with tab3:
    st.header("Which cities have the highest and lowest levels of air pollution? What are the scores?")
    st.image("./image/Visualisasi Air_Quality 3.1.png")
    st.write("""
            #### Station Pollution Level Ranking Based on Average PM2.5\n
            The bar chart ranks the stations in Beijing based on their average PM2.5 levels. Aotizhongxin has the highest average PM2.5 level, while Dingling has the lowest. Several other stations, including Gucheng, Dongsi, Wanshouxigong, Wangliu, Guanyuan, Tiantan, Nongzhanguan, Shunyi, Changping, and Huairou, have relatively high average PM2.5 levels. In contrast, Wanliu has a relatively low average PM2.5 level. Overall, the bar chart clearly shows the differences in PM2.5 levels among the different stations in Beijing.
    """)
    st.image("./image/Visualisasi Air_Quality 3.2.png")
    st.write("""
            #### Heatmap Average PM2.5 per Year In Different Stations\n
            The heatmap visually represents the average PM2.5 levels per year for different stations in Beijing from 2013 to 2017. Darker colors indicate lower levels, while lighter colors represent higher levels. The heatmap clearly shows the spatial and temporal variations in PM2.5 levels across the different stations, allowing for easy identification of trends and patterns.
    """)

st.write("""
        # Conclusion
         1. In the results of question 1, it can be seen that the PM2.5 levels at several stations fluctuate from year to year. Several stations show a significant increase or decrease in PM2.5 levels in certain years and have an increase until 2017.
         2. In the visualization results of question 2, it can be seen that in 2014 the pollution level in the Beijing area increased, then decreased drastically until 2016. Then in mid-2016, there was a significant increase until 2017.
         3. In the third visualization results, it is concluded that the city with the highest pollution level from 2013-2017 is Dongsi City with a value of 88.86, and the city with the lowest air pollution level is Dingling City with a value of 67.04
""")

st.write("Follow me on linkedin : www.linkedin.com/in/samuel-christian-hamdani")

st.caption('Copyright (c) Samuel Christian Hamdani 2024')