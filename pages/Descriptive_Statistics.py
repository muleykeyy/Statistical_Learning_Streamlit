import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.figure_factory as ff
import plotly.express as px

df=pd.read_csv("pokemon.csv")
graphs,summary=st.tabs(["Graphical Summaries of Data","Summary Statistics"])
st.sidebar.markdown("# 📊 Descriptive Statistics")
st.sidebar.markdown("**📌Graphical Summaries of Data**")
st.sidebar.write("📍Histogram")
st.sidebar.write("📍Bar Graph")
st.sidebar.write("📍Scatter Plot")
st.sidebar.write("📍Pie Chart & Dot Plot")
st.sidebar.markdown("**📌Summary Statistics**")
st.sidebar.write("📍Mean (Average)")
st.sidebar.write("📍Median")
st.sidebar.write("📍Quantile")
st.sidebar.write("📍Outliers")
st.sidebar.write("📍Mode")
st.sidebar.write("📍Variance")
st.sidebar.write("📍Standard Deviation")

with graphs:
    header=st.container()
    with header:
        st.markdown("# 📈GRAPHICAL SUMMARIES of DATA")
        st.write("""It is best to use a graphical summary to communicate information, because people
prefer to look at pictures rather than at numbers.
There are many ways to visualize data. The nature of the data and the goal of the
visualization determine which method to choose.""")


    st.markdown("## HISTOGRAM")
    st.markdown("One of the best ways to describe a variable is to report the values that appear in the dataset and how many times each value appears.")
    st.markdown("This description is called the **distribution** of the variable.") 
    st.markdown("The most common representation of a distribution is a histogram, which is a graph that shows the **frequency** of each value.")
    fig=px.histogram(df["Defense"],x="Defense")
    st.plotly_chart(fig,use_container_width=True)
    st.markdown("Histogram gives two kinds of information about data:")
    st.markdown("**Density** (crowding): The height of the bar tells how many subjects there are for one unit on the horizontal scale.")
    st.markdown("**Percentages** (relative frequences): Those are given by:")
    st.markdown("**area = height x width**")

    st.markdown("## BAR GRAPH")
    st.write("When the data are quantitative (i.e. numbers), then they should be put on a number line.")
    st.write("This is because the ordering and the distance between the numbers convey important information.")
    gen=df["Generation"][0:10]
    st.bar_chart(gen,use_container_width=True)

    st.markdown("## SCATTER PLOT")
    st.write("The scatterplot is used to depict data that come as pairs.")
    st.write("The scatterplot visualizes the relationship between the two variables.")
    fig=px.scatter(df,x="Attack",y="Defense")
    st.plotly_chart(fig,use_container_width=True)

    st.markdown("## PIE CHART & DOT PLOT")
    st.markdown("The **dot plot** makes it easier to compare frequencies of various categories, while the **pie chart** allows more easily to eyeball what fraction of the total a category corresponds to.")
    fig=px.pie(df,values="Defense",names="Type 1")
    st.plotly_chart(fig,use_container_width=True)
    fig=px.scatter(df,y="Type 1",x="Defense")
    st.plotly_chart(fig,use_container_width=True)
  
with summary:
    header=st.container()
    with header:
        st.markdown("# 📑SUMMARY STATISTICS📝")
        st.write("Summary statistics is a part of descriptive statistics that summarizes and provides the gist of information about the sample data.")
        
        st.markdown("## MEAN (AVERAGE)")
        st.write("Mean is the average of the given numbers and is calculated by dividing the sum of given numbers by the total number of numbers.")
        col1,col2=st.columns(2)
        with col1:
            st.latex(r"""MEAN = ({\frac{1}{n}}\sum _{i=1}^{n}{x_{i}})""") 
        with col2:
            st.latex(r"""MEAN = (\frac{Sum\:of\: all\: the\: observations}{Total\: number\: of\: observations})""")
        
        code="""print("Mean of Speed: ",df.Speed.mean())"""
        st.code(code,language="python")

        st.markdown("## MEDIAN")
        st.write("The median represents the value less than which 50% of the data lies.")
        st.write("Median is the middle-most value (if the number of data points is odd) or the average of the two middle-most values (if the number of data points is even).")
        col1,col2=st.columns(2)
        with col1:
            st.markdown("#### Odd Number of Observations:")
            st.latex(r"""MEDIAN = (\frac{n+1}{2})^{th}\:term""")
        with col2:
            st.markdown("#### Even Number of Observations:")
            st.latex(r"""MEDIAN = \frac{(\frac{n}{2})^{th}\:term + (\frac{n}{2}+1)^{th}\:term)}{2}""")
        code="""print("Median of Attack: ",df.Attack.median())"""
        st.code(code,language="python")
        
        st.markdown("## QUANTILE")
        st.write("A generalization of the median is the quantile, which represents the value less than which a certain percentile of the data lies.")
        quantile=Image.open("quantile.png")
        st.image(quantile)
        st.markdown("#### First Quantile: (%25):")  
        st.write("The first quantile (Q1) is defined as the middle number between the smallest number (minimum) and the median of the data set.") 
        st.markdown("#### Second Quantile : (%50) Median")
        st.markdown("#### Third Quantile: (%75):")  
        st.write("The third quantile (Q3) is the middle value between the median and the highest value (maximum) of the data set.")
        code="""
        q1=df.Speed.quantile(0.25)
q2=df.Speed.quantile(0.50) # Median
q3=df.Speed.quantile(0.75)
        """
        st.code(code,language="python")
        
        st.markdown("## OUTLIERS")
        st.write("Check for outliers, which are extreme values that might be errors in measurement and recording, or might be accurate reports of rare events.")
        st.write("The **Interquartile Range (IQR)** is a measure of statistical dispersion, which is the spread of the data: **Q3-Q1**")
        code="""
        Q1=df.Attack.quantile(0.25)
Q3=df.Attack.quantile(0.75)
IQR=Q3-Q1
        """
        st.code(code,language="python")
        
        st.markdown("### Visualization of Outliers")
        fig=px.box(df,y="HP")
        st.plotly_chart(fig,use_container_width=True)
        
        st.markdown("## MODE")
        st.write("Most- common value(s)")
        code="""
        print("Mode of Speed: ",df.Speed.mode())
print("Mode of Attack: ",df.Attack.mode())
        """
        st.code(code,language="python")
        
        st.markdown("## VARIANCE")
        st.write("Spread distributions")
        st.latex(r"""VARIANCE = {\frac {1}{n}}\sum _{i=1}^{n}{(x_{i}-{\bar{x}})^2}""")
        code="""
        print("Variance of Speed: ",df.Speed.var())
print("Variance of Attack: ",df.Attack.var())
        """
        st.code(code,language="python")     
        
        st.markdown("## STANDARD DEVIATION")
        st.write("Square root of variance") 
        st.latex(r"""{S}^2 = {\frac {1}{n}}\sum _{i=1}^{n}{(x_{i}-{\bar{x}})^2}""")  
        code="""
        print("Standard Deviation of Speed: ",df.Speed.std())
print("Standard Deviation of Attack: ",df.Attack.std())
        """
        st.code(code,language="python")