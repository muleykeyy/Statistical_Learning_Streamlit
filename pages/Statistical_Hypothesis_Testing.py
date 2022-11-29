import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.figure_factory as ff
import plotly.express as px
import scipy.stats as stats
import pylab
df=pd.read_csv("pokemon.csv")

st.sidebar.markdown("# 🧮Statistical Hypothesis Testing")
st.sidebar.write("📍z-Test    📍t-Test ")
st.sidebar.write("📍P-Value")
st.sidebar.write("📍One Sample T-Test")
st.sidebar.write("📍Shapiro-Wilk Test")
st.sidebar.write("📍Homogeneity of Variance")
st.sidebar.write("📍Two Sample Test")
st.sidebar.write("📍Dependent T-Test")
st.sidebar.markdown("# 🖋️ Analysis of Categorical Variables")
st.sidebar.write("📍Chi-Square Test")
header=st.container()
with header:
    st.markdown("# 🧮STATISTICAL HYPOTHESIS TESTING")
    st.write("The goal of classical hypothesis testing is to answer the question, **“Given a sample and an apparent effect, what is the probability of seeing such an effect by chance?”**")
    st.write("1. The first step is to quantify the size of the apparent effect by choosing a **test statistic**.")
    st.write("2. The second step is to define a **null hypothesis**, which is a model of the system based on the assumption that the apparent effect is not real. H0")
    st.write("3. The third step is to compute a **p-value**, which is the probability of seeing the apparent effect if the null hypothesis is true.")
    st.write("4. The last step is to interpret the result. If the p-value is low, the effect is said to be **statistically significant**, which means that it is unlikely to have occurred by chance.")
    table=Image.open("table.png")
    st.image(table)
    
    
    col1,col2=st.columns(2)
    with col1:
        st.markdown("## z-TEST")
        st.write("A z-test is a statistical test used to determine whether two population means are different when the variances are known and the sample size is large.")
        st.latex(r"""z = (\frac{observed\: - \:expected}{Standard\:Error}) """) 
    with col2:
        st.markdown("## t-TEST")
        st.write("Small modifications of z-test.(Sample size is small)")
        
    st.markdown("## P-VALUE")
    st.write("A statistical measurement used to validate a hypothesis against observed data.")
    st.write("Reject H0:")
    st.info("If p value > 0.10 → “Not Significant” ")
    st.info("If p value ≤ 0.10 → “Marginally Significant”")
    st.info("If p value ≤ 0.05 → “Significant”")
    st.info("If p value ≤ 0.01 → “Highly Significant”")
    
    code="""
    from scipy.stats import ttest_rel
    statistic, p_value = ttest_rel(df.HP,df.Defense)
    print('p-value: ',p_value)
output: p-value:  0.0002512305750711713
    """
    st.code(code,language="python")
    code="""
    
p-value<0.05
    output: True
    """
    st.code(code,language="python")
    st.warning("P-Value is smaller than 0.05. So H0 is rejected")
    
    st.markdown("## ONE SAMPLE T-TEST")
    st.write("The One Sample T-Test examines whether the mean of a population is statistically different from a known or hypothesized value.")
    code="""
    stats.describe(df.HP)
    output:    DescribeResult(nobs=800, minmax=(1, 255), mean=69.25875, 
    variance=652.0193225907384, skewness=1.5652824223266586, 
    kurtosis=7.179466278186133)
    """
    st.code(code,language="python")
    graph=Image.open("graph.png")
    st.image(graph)    
    
    st.markdown("## SHAPIRO-WILK TEST")
    st.info("H0: Population is normally distributed.")
    st.info("H1: Population is not normally distributed.")
    code="""
    from scipy.stats import shapiro
shapiro(df.HP)
print("T Test Statistics: ",shapiro(df.HP)[0])
print("P Value : ",shapiro(df.HP)[1])
    output:   T Test Statistics:  0.9158304333686829
              P Value :  1.1518300198312678e-20
    """
    st.code(code,language="python")
    st.warning("P-Value is smaller than 0.05. H0 is rejected.")
    
    st.markdown("## HOMOGENEITY OF VARIANCE")
    st.write("The assumption of homogeneity of variance is an assumption of the independent samples t-test stating that all comparison groups have the same variance.")
    st.info("H0: Variances are homogeneous")
    st.info("H1: Variances are not homogeneous")
    
    code="""
    stats.levene(df["Speed"],df["Attack"])
    output: LeveneResult(statistic=4.099512378524714, pvalue=0.04306159762659687)
    """
    st.code(code,language="python")
    st.warning("P-Value is smaller than 0.05. H0 is rejected. They are **not** homogeneous")
    
    st.markdown("## TWO SAMPLE T-TEST")
    st.write("Two-sample t-test is used to test whether the **unknown population means of two groups** are equal or not.")
    st.info("H0: Means are equal")
    st.info("H1: Means are not equal")
    code="""
    stats.ttest_ind(df["Speed"],df["Attack"],equal_var=False)
        output: Ttest_indResult(statistic=-6.9621682797744935, pvalue=4.897628155049799e-12)
    """
    st.code(code,language="python")
    st.warning("P-Value is smaller than 0.05. H0 is rejected.")
    
    st.markdown("## DEPENDENT T-TEST")
    st.write("Compares the means of **two related groups** to determine whether there is a statistically significant difference between these means.")
    st.info("H0: Means are equal")
    st.info("H1: Means are not equal")
    code="""
    tTestResult,p_value=stats.ttest_rel(df.Attack,df.Defense)
print("t-Test Result= %.5f , P-Value= %.5f" % (tTestResult,p_value))
        output: t-Test Result= 4.32557 , P-Value= 0.00002
    """
    st.code(code,language="python")
    st.warning("P-Value is smaller than 0.05. H0 is rejected.")
    
    st.markdown("# 🖋️ANALYSIS of CATEGORICAL VARIABLES ")
    
    st.markdown("## CHI-SQUARE TEST")
    st.write("Chi - Square is a test for independence between **categorical variables**.")
    st.info("H0: The two categorical variables have no relationship")
    st.info("H1: There is a relationship between two categorical variables")
    code="""
    from scipy.stats import chi2_contingency
    stat, p_value, dof, expected =chi2_contingency(contingency)
print("P-Value= %.10f" % (p_value))
        output: P-Value= 0.0000000000
    """
    st.code(code,language="python")
    st.warning("P-Value is smaller than 0.05. H0 is rejected. There is relation between variables.")
    st.markdown("#### CONTINGENCY TABLE")
    st.write("Displays the (multivariate) frequency distribution of the variables.")
    contingency=pd.crosstab(df["Legendary"],df["Type 1"])
    st.table(contingency)
    
    