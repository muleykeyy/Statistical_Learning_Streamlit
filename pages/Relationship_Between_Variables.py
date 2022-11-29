import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.figure_factory as ff
import plotly.express as px
df=pd.read_csv("pokemon.csv")

st.sidebar.markdown("# 🪢Relationship Between Variables")
st.sidebar.write("📍Correlation")
st.sidebar.write("📍Covariance")
st.sidebar.write("📍Pearson's Correlation")
st.sidebar.write("📍Spearsman's Correlation")
header=st.container()
with header:
    st.markdown("## CORRELATION")
    st.write("Strength of the relationship between two variables")
    st.table(df.corr())
    st.info("If the correlation value of two variable is **1**: they are **positively correlated** with each other.")
    st.info("If the correlation value of two variable is **-1**: they are **negatively correlated** with each other.")
    st.info("If the correlation value of two variable is **0**: there is **no correlation** between them.")
    correlation=df.corr()
    
    st.markdown("### Visualization of Correlation (Heat Map)")
    f,ax = plt.subplots(figsize=(10,10))
    sns.heatmap(correlation, annot=True, linewidths=0.5, fmt= '.2f',ax=ax,cmap="YlGnBu")
    st.pyplot(f)
    st.warning("Do not forget correlation is not causation. 😉😉😉", icon="⚠️")
    
    st.markdown("## COVARIANCE")
    st.write("Measure of the tendency of two variables to vary together.")
    
    code="""np.cov(df.Speed,df.Attack)
print("Covariance between Speed and Attack : ",df.Speed.cov(df.Attack))"""
    st.code(code,language="python")
    
    st.markdown("## PEARSON'S CORRELATION")
    st.write("It is the ratio between the covariance of two variables and the product of their standard deviations.")
    st.write("It is a measure of **linear correlation** between two sets of data.")
    st.latex(r"""p_{i} = \frac{(x_{i}-{\bar{x}})}{S_{x}}\frac{(y_{i}-{\bar{y}})}{S_{y}}""")
    code="""p1=df.loc[:,["Speed","Attack"]].corr(method="pearson")
p2=df.Attack.cov(df.Speed)/(df.Attack.std()*df.Speed.std())
print('Pearson correlation: ')
print(p1)
print('Pearson correlation: ',p2)"""
    st.code(code,language="python")
    st.info("If Pearson’s correlation is near **0**, it is tempting to conclude that there is **no relationship** between the variables.")
    st.info("That conclusion is not valid. Pearson’s correlation only measures linear relationships.")
    
    st.warning("Pearson’s correlation works well if the relationship between variables is linear and if the variables are roughly normal. But it is not robust in the presence of outliers.")

    st.markdown("## SPEARSMAN'S RANK CORRELATION")
    st.write("Spearman’s rank correlation is an alternative that mitigates the effect of outliers and skewed distributions.")    
    st.write("To compute Spearman’s correlation, we have to compute the **rank** of each value.")
    code="""
    data_rank=df.rank()
spearman_corelation=data_rank.loc[:,["Speed","Attack"]].corr(method="pearson")
print("Spearman's correlation: ")
print(spearman_corelation)
    """
    st.code(code,language="python")

    st.info("If the relationship is nonlinear, Pearson’s correlation tends to underestimate the strength of the relationship, and Pearson’s correlation can be affected (in either direction) if one of the distributions is skewed or contains outliers.")
    st.info("Spearman’s rank correlation is more robust.")
    
    