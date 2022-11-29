import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


st.sidebar.markdown("# Introduction")
st.sidebar.write("What is Statistics?")
header=st.container()
with header:
       st.header("STATISTICS for DATA SCIENCE")
       stat=Image.open("stat.jpg")
       st.image(stat)
       st.header("What is Statistics?")
       st.write("Statistics is a set of mathematical methods and tools that enable us to answer important questions about data. It is divided into two categories:")
       st.subheader("**1.Descriptive Statistics**")
       st.write("Descriptive statistics is the type of statistics which is used to summarize and describe the dataset. It is used to describe the characteristics of data. Descriptive statistics are generally used to determine if the sample is normally distributed. It is displayed through tables, charts, frequency distributions and is generally reported as a measure of central tendency.")
       st.subheader("**2.Inferential Statistics**")
       st.write("In Inferential statistics, we make an inference from a sample about the population. The main aim of inferential statistics is to draw some conclusions from the sample and generalise them for the population data. E.g. we have to find the average salary of a data analyst across India.")
       st.header("**Key Differences of Descriptive Statistics & Inferential Statistics**")
       col1,col2=st.columns(2)
       with col1:
              st.subheader("Descriptive Statistics")
              st.write("- It is concerned with describing the population under study. Sampling is not required.")
              st.write("- Collects, organizes, analyzes and presents the data in a meaningful way.")
              st.write("- The form of result is charts, Graphs, and tables.")
              st.write("- It describes a situation.")
              st.write("- It explains the data (already known) to summarize sample.")
                       
       with col2:
              st.subheader("Inferential Statistics")
              st.write("- It focuses on drawing conclusions about the populations, based on sample analysis.")
              st.write("- Compares data, test hypotheses and make predictions of the future outcome.")
              st.write("- The result is displayed in the form of probability.")
              st.write("- It explains the likelihood of the occurrence of an event.")
              st.write("- It attempts to reach the conclusions to learn about the population; that extends beyond the data available.")
               
st.write("**Also you can check:**")
st.write("https://www.kaggle.com/code/hilalmleykeyuksel/statistical-learning-tutorial")
st.write("https://github.com/muleykeyy/Statistics-for-Data-Science")
st.write("**Data Set:**")
st.write("https://www.kaggle.com/datasets/terminus7/pokemon-challenge")
