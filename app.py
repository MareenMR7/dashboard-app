import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px


cw=pd.read_csv(r"D:\archive\country_wise_latest.csv")
ccc=pd.read_csv(r"D:\archive\covid_19_clean_complete.csv")
dw=pd.read_csv(r"D:\archive\day_wise.csv")
fg=pd.read_csv(r"D:\archive\full_grouped.csv")
usa=pd.read_csv(r"D:\archive\usa_county_wise.csv")
wd=pd.read_csv(r"D:\archive\worldometer_data.csv")

st.sidebar.header("Covid-19 Data Visualization")
st.sidebar.image(r"D:\archive\download.jpg")
st.sidebar.write("this is a data visualization of covid-19 data and its analysis for the year 2020,it contains various graphs and charts to analyze the data")






st.sidebar.write("")
st.sidebar.markdown("made with ❤️ by Eng.[Mareen MR7](https://github.com/MareenMR7/Mareen-MR7)")


a1,a2,a3=st.columns(3)
a1.header("Total Files : 6")
a2.metric("Total Cases",wd["TotalCases"].max())
a3.metric("Total Deaths",wd["TotalDeaths"].max())


r1,r2,r3,r4,r5,r6=st.columns((2,2,2,2,2,2))
with r1:
     cwl= st.button("country wise latest")
with r2:
     cd= st.button("covid-19 data visualization")
with r3:
     dwa= st.button("day wise analysis")
with r4:
     fgd= st.button("full grouped data")
with r5:
     usc= st.button("usa-county wise")
with r6:
     wod= st.button("world-ometer data")




st.header("Country Wise Analysis:")
fig=px.bar(data_frame=cw,
           x="WHO Region",
           y="New recovered",
           color="Country/Region")
st.plotly_chart(fig,use_container_width=True)
c1,c2=st.columns((5,5))
with c1:
    fig=px.pie(data_frame=cw,
           names="WHO Region",
           values="Deaths",
           color="Country/Region")
    st.plotly_chart(fig,use_container_width=True)
with c2:
    fig=px.line(data_frame=cw,
                x="New cases",
                y="New deaths",
                markers=True)
    st.plotly_chart(fig,use_container_width=True)
fig=px.bar(data_frame=cw,
           x="WHO Region",
           y="New deaths",
           color="Country/Region")
st.plotly_chart(fig,use_container_width=True)
st.header("covid-19 data visualization:")
r1,r2=st.columns((1,1))
with r1:
    fig=px.line(data_frame=ccc,
               x="Date",
               y="Confirmed",)
    st.plotly_chart(fig,use_container_width=True)
with r2:
    fig=px.area(data_frame=ccc,
                x="Date",
                y="Recovered")
    st.plotly_chart(fig,use_container_width=True)
st.header("day Wise Analysis:")
fig=px.area(data_frame=dw,
            x="Date",
            y="Deaths")
st.plotly_chart(fig,use_container_width=True)
fig=px.area(data_frame=dw,
            x="Date",
            y="Recovered")
st.plotly_chart(fig,use_container_width=True)
fig=px.scatter(data_frame=dw,
            x="Date",
            y="Confirmed")
st.plotly_chart(fig,use_container_width=True)
st.header("full grouped data:")
fig=px.pie(data_frame=fg,
           names="WHO Region",
           values="Deaths")
st.plotly_chart(fig,use_container_width=True)
st.header("Worldometer data:")
fig=px.bar(data_frame=wd,
        x="Country/Region",
        y="TotalRecovered")
st.plotly_chart(fig,use_container_width=True)
fig=px.bar(data_frame=wd,
        x="Country/Region",
        y="TotalDeaths")
st.plotly_chart(fig,use_container_width=True)
fig=px.pie(data_frame=wd,
        names="Country/Region",
        values="TotalCases")
st.plotly_chart(fig,use_container_width=True)
st.write("")
st.write("")
st.subheader("finally this is the end of the project and thanks for visiting our dashboard")
t1,t2=st.columns(2)
with t1:
     st.header("introduced by:")
with t2:
     st.image(r"D:\archive\IMG_1984.JPG")
     st.header("Eng.Mareen MR7")

