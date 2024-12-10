import streamlit as st
import pandas as pd
import numpy as np

# Function to load data
@st.cache
def load_data():
    data = pd.read_csv('sales_data.csv')  # Assuming the file is available locally
    return data

# Function to transform data
def transform_data(df):
    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'],errors='coerce')
    
    # Extract Year and Month from the Date column
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    
    # Calculate Sales to Profit Ratio
    df['Sales_to_Profit_Ratio'] = df['Sales'] / df['Profit']
    
    # Calculate Cumulative Sales
    df['Cumulative_Sales'] = df['Sales'].cumsum()
    
    return df

# Function to extract summary statistics
def get_summary_statistics(df):
    summary = df.describe()  # Returns count, mean, std, min, max, etc.
    return summary

# Main function to run the Streamlit app
def main():
    st.title("ETL Process for Sales Data")

    # Step 1: Extract
    st.header("Step 1: Extract")
    data = load_data()
    
    if not data.empty:
        st.write("Raw Data")
        st.write(data)

        # Step 2: Transform
        st.header("Step 2: Transform")
        transformed_data = transform_data(data)
        st.write("Transformed Data")
        st.write(transformed_data)

        # Step 3: Summary Statistics
        st.header("Step 3: Summary Statistics")
        summary_stats = get_summary_statistics(transformed_data)
        st.write("Summary Statistics")
        st.write(summary_stats)

        # Optional: Add visualizations or further analysis here
        st.header("Step 4: Visualizations (Optional)")

        # Example: Plot Cumulative Sales over Time
        st.subheader("Cumulative Sales Over Time")
        st.line_chart(transformed_data[['Date', 'Cumulative_Sales']].set_index('Date'))
        
    else:
        st.warning("No data to display. Please upload a CSV file.")

if __name__ == "__main__":
    main()
