import streamlit as st
from data_handler import load_data, modify_data
from graphs import plot_attribution_bar_chart, plot_contribution_bar_chart, plot_cumulative_line_chart

def main():
    st.title("Interactive Portfolio Return Attribution Demo")

    # Load initial data
    data = load_data()

    # Sidebar for user inputs
    st.sidebar.header("Adjust Parameters")
    st.sidebar.subheader("Attribution Factors")
    st.sidebar.text("Modify the values to see changes in graphs")

    # Example sliders for user input
    st.sidebar.slider("ST Revisions", min_value=-10.0, max_value=10.0, value=0.0)
    st.sidebar.slider("Flow", min_value=-10.0, max_value=10.0, value=0.0)
    st.sidebar.slider("Sector", min_value=-10.0, max_value=10.0, value=0.0)

    # Modify data based on user input
    modified_data = modify_data(data)

    # Display graphs
    st.subheader("Attribution Bar Chart")
    plot_attribution_bar_chart(modified_data)

    st.subheader("Contribution Bar Chart")
    plot_contribution_bar_chart(modified_data)

    st.subheader("Cumulative Line Chart")
    plot_cumulative_line_chart(modified_data)

if __name__ == "__main__":
    main()