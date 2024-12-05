import pandas as pd
import streamlit as st
from plotly.express import line, bar, scatter


def plot_graph():
    x_axis = st.session_state.x_axis
    y_axis = st.session_state.y_axis
    graph_type = st.session_state.graph_type
    if graph_type == "line":
        fig = line(df, x=x_axis, y=y_axis)
    elif graph_type == "bar":
        fig = bar(df, x=x_axis, y=y_axis)
    else:
        fig = scatter(df, x=x_axis, y=y_axis)
    st.session_state.graph = fig


st.title("Graph Explorer")
st.markdown("---")
file = st.file_uploader("Upload a data file in excel or csv format", type=["xlsx", "csv"])
if file:
    df = pd.read_csv(file)
    st.selectbox(label="Select the columns to plot in x-axis", options=df.columns, key="x_axis")
    st.selectbox(label="Select the columns to plot in y-axis", options=df.columns, key="y_axis")
    st.selectbox(label="Select the type of graph to plot", options=["line", "bar", "scatter"], key="graph_type")
    st.button(label="Plot Graph", key="plot_graph", on_click=plot_graph)
    if "graph" in st.session_state:
        st.plotly_chart(st.session_state.graph)
