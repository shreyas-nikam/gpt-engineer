import streamlit as st
import matplotlib.pyplot as plt

def plot_attribution_bar_chart(data):
    # Plot an attribution bar chart
    fig, ax = plt.subplots()
    data.plot(kind='bar', ax=ax)
    st.pyplot(fig)

def plot_contribution_bar_chart(data):
    # Plot a contribution bar chart
    fig, ax = plt.subplots()
    data.plot(kind='bar', stacked=True, ax=ax)
    st.pyplot(fig)

def plot_cumulative_line_chart(data):
    # Plot a cumulative line chart
    fig, ax = plt.subplots()
    data.cumsum().plot(ax=ax)
    st.pyplot(fig)