#importing libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import os
st.title("Mahaveer Gruh Vastu Bhandar")
st.image('shop3.jpeg', width=700, output_format="JPEG")
st.markdown("## Shop Data Analytics ")
st.markdown("This application is a Streamlit dashboard to analyze the data of Shop")
st.sidebar.markdown("This application is a Streamlit dashboard to analyze the data of Shop ")

st.image('shop1.jpg', width=700, output_format="JPG")
#inseting image in the sidebar
st.sidebar.image('shop.jpg', use_column_width=True)

#st.markdown.image('shop1.jpg', use_column_width=True)

DATA_URL = "salesdata - Sheet1 - Copy.csv"
f=os.path.exists(DATA_URL)
print(f)
@ st.cache_data (persist=True)# for fast update and store data in harddisk
def load_data():
 data = pd.read_csv(DATA_URL)#for reading the datasheet
 #data['ts'] = pd.Timestamp(data['ts'],unit='s')#for converting time to pandas format
 data.dropna(axis=1)#for removing nill values from column
 return data
data=load_data()
print(data)
check_Box = st.sidebar.checkbox(label="Display Datasheet")
if check_Box:
 st.write(data)
 
###########for Branch/Sector data###################
st.sidebar.markdown("### Branch Data")
select = st.sidebar.selectbox('Visualization type',['Histogram','Pie chart'],key='1')
Branch_status = data['Branch'].value_counts()
Branch_status = pd.DataFrame({'Branch_status':Branch_status.index,'Count Status':Branch_status.values})
check_Box = st.sidebar.checkbox(label="Display Branch/Sector Data")
if check_Box:
    st.write(Branch_status)
if not st.sidebar.checkbox("Hide",True,key='2'):
    st.markdown("### Branch Data")
    if select == "Histogram":
        fig = px.histogram(Branch_status,x='Branch_status', y='Count Status',color='Count Status',height=500)
        st.plotly_chart(fig)
    else:
        fig =px.pie(Branch_status, values='Count Status',names='Branch_status')
        st.plotly_chart(fig)
    st.markdown("x---------------------------------------------------------------------------------------------------")
 
###########for Customer type data###################
st.sidebar.markdown("### Customer Type Data")
select = st.sidebar.selectbox('Visualization type',['Bar plot','Pie chart'],key='3')
cus_status = data['Customer_type'].value_counts()
cus_status = pd.DataFrame({'cus_status':cus_status.index,'Count Status':cus_status.values})
check_Box = st.sidebar.checkbox(label="Display Customer_type Data")
if check_Box:
    st.write(cus_status)
if not st.sidebar.checkbox("Hide",True,key='4'):
    st.markdown("### Customer Type Data")
    if select == "Bar plot":
        fig = px.bar(cus_status,x='cus_status', y='Count Status',color='Count Status',height=500)
        st.plotly_chart(fig)
    else:
        fig =px.pie(cus_status,values='Count Status',names='cus_status')
        st.plotly_chart(fig)
    st.markdown("x---------------------------------------------------------------------------------------------------")
 
############for Gender Data###################
st.sidebar.markdown("### Gender Data")
select = st.sidebar.selectbox('Visualization type',['Bar plot','SunburstPlot'],key='5')
Gender_status = data['Gender'].value_counts()
Gender_status = pd.DataFrame({'Gender_status':Gender_status.index,'Count Status':Gender_status.values})
check_Box = st.sidebar.checkbox(label="Display Gender Data")
if check_Box:
    st.write(Gender_status)
if not st.sidebar.checkbox("Hide",True,key='6'):
    st.markdown("### Gender Data")
    if select == "Bar plot":
        fig = px.bar(Gender_status,x='Gender_status', y='Count Status',color='Count Status',height=600)
        st.plotly_chart(fig)
    else:
        fig =px.sunburst(Gender_status,path=['Gender_status','Count Status'] )
        st.plotly_chart(fig)
    st.markdown("x---------------------------------------------------------------------------------------------------")

############for Product Analysis ###################
st.sidebar.markdown("### Product Analysis")
select = st.sidebar.selectbox('Visualization type',['Bar plot','Pie chart'],key='7')
Product_status = data['Product_line']
Gender_status=data['Gender']
Pro_status = pd.DataFrame({'Product_status':Product_status,'Gender_status':Gender_status})
check_Box = st.sidebar.checkbox(label="Display Product Data")
if check_Box:
    st.write(Pro_status)
if not st.sidebar.checkbox("Hide",True,key='8'):
    st.markdown("### Product Analysis")
    if select == "Bar plot":
        fig = px.bar(Pro_status,x='Gender_status', y='Product_status',color='Product_status',height=600)
        st.plotly_chart(fig)
    else:
        fig =px.sunburst(Pro_status,path=['Product_status','Gender_status'],color='Product_status',color_discrete_map={'Male':'gold', 'Female':'darkblue'})
        st.plotly_chart(fig)
    st.markdown("x---------------------------------------------------------------------------------------------------")

###########for Rating data ###################
st.sidebar.markdown("### Rating Data")
select = st.sidebar.selectbox('Visualization type',['Histogram','Funnel Plot'],key='9')
Rating_status = data['Rating'].value_counts()
Rating_status = pd.DataFrame({'Rating_status':Rating_status.index,'Count Status':Rating_status.values})
check_Box = st.sidebar.checkbox(label="Display Rating Data")
if check_Box:
    st.write(Rating_status)
if not st.sidebar.checkbox("Hide",True,key='10'):
    st.markdown("### Rating Data")
    if select == "Histogram":
        fig = px.histogram(Rating_status,x='Rating_status', y='Count Status',color='Rating_status',height=500)
        st.plotly_chart(fig)
    else:
        fig =px.funnel(Rating_status, x='Count Status',y='Rating_status',color='Rating_status')
        st.plotly_chart(fig)
    st.markdown("x---------------------------------------------------------------------------------------------------")

###########for Gross_income data ###################
st.sidebar.markdown("### Gross_income Data")
select = st.sidebar.selectbox('Visualization type',['Heat Map-2D','Scatter Plot'],key='11')
groincome_status = data['gross_income']
Product_status = data['Product_line']
Gender_status=data['Gender']
gro_status = pd.DataFrame({'groincome_status':groincome_status,'Product_status':Product_status,'Gender_status':Gender_status})
check_Box = st.sidebar.checkbox(label="Display grossIncome_Data")
if check_Box:
    st.write(gro_status)
if not st.sidebar.checkbox("Hide",True,key='12'):
    st.markdown("### Gross_income Data")
    if select == "Heat Map-2D":
        fig = px.density_heatmap(gro_status,x='Product_status', y='groincome_status')#,color='Product_status',height=500)
        st.plotly_chart(fig)
    else:
        fig =px.scatter(gro_status,x='groincome_status',y='Gender_status',size="groincome_status",color='Product_status')
        st.plotly_chart(fig) 
    st.markdown("x---------------------------------------------------------------------------------------------------")

###########for RatingVSProduct data ###################
st.sidebar.markdown("### RatingVSProduct Data")
select = st.sidebar.selectbox('Visualization type',['Histogram','Heat Map-2D'],key='13')
Product_status = data['Product_line']
Rat_status = data['Rating']
gross_status=data['gross_income']
ratP_status = pd.DataFrame({'Rat_status':Rat_status,'Product_status':Product_status,'gross_status':gross_status})
check_Box = st.sidebar.checkbox(label="Display RatingVSProduct Data")
if check_Box:
    st.write(ratP_status)
if not st.sidebar.checkbox("Hide",True,key='14'):
    st.markdown("### RatingVSProduct Data")
    if select == "Histogram":
        fig = px.histogram(ratP_status,x='Rat_status', y='gross_status',color='Product_status',height=500)
        st.plotly_chart(fig)
    else:
        fig =px.density_heatmap(ratP_status, y='gross_status',x='Rat_status', marginal_x="histogram", marginal_y="histogram")#,size="Rat_status",hover_name="Rat_status",color='Product_status')
        st.plotly_chart(fig) 
    st.markdown("x---------------------------------------------------------------------------------------------------")

###########for Payment data ###################
st.sidebar.markdown("### Payment Method Data")
select = st.sidebar.selectbox('Visualization type',['Histogram','Sunburst Plot'],key='15')
Payment_status = data['Payment'].value_counts()
#gross_status=data['gross_income']
Pay_status = pd.DataFrame({'Payment_status':Payment_status.index,'Count_status':Payment_status.values})
check_Box = st.sidebar.checkbox(label="Display Payment Data")
if check_Box:
    st.write(Pay_status)
if not st.sidebar.checkbox("Hide",True,key='16'):
    st.markdown("### Payment Method Analysis")
    if select == "Histogram":
        fig = px.histogram(Pay_status,x='Payment_status', y='Count_status',color='Payment_status',height=500)
        st.plotly_chart(fig)
    else:
        fig =px.sunburst(Pay_status,path=['Count_status','Payment_status'],values='Count_status')
        st.plotly_chart(fig)
    st.markdown("x---------------------------------------------------------------------------------------------------")

#Shop Info
st.markdown("## Address:")
st.markdown("### Mahaveer Gruh vastu bhandar, opp. Bus Stand , Dharmashi Line, Chatrapati Shivaji Maharaj Chowk, Solapur,Maharashtra")
st.markdown("#### Contact Number: +917620294494")  
