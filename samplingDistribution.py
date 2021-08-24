import pandas as pd
import plotly.figure_factory as pf
import statistics as st
import random

df = pd.read_csv("medium_data.csv")
articleList = df["reading_time"].tolist()
print("Main-Mean -> {}".format(st.mean(articleList)))
print("Main-Stdev -> {}".format(st.stdev(articleList)))

def randomSmpls (size):
    sampleData = []
    for i in range(0,size):
        rand = random.randint(0,len(articleList)-1)
        sampleData.append(articleList[rand])
    return sampleData

def setup ():
    sampleMeans = []
    for i in  range(0,100):
        randSamples = randomSmpls(30)
        sampleMeans.append(st.mean(randSamples))
    return sampleMeans

def plotGraph ():
    Means = setup()
    fig = pf.create_distplot([Means],["Means of 1000 Samples"],show_hist=False)
    fig.show()

SamplingMeans = setup()
plotGraph()
print("Sampling-Mean -> {}".format(st.mean(SamplingMeans)))
print("Sampling-stdev -> {}".format(st.stdev(SamplingMeans)))