# Libraries
import pandas as pd
import plotly.express as px
import streamlit as st

from utils.helpers import convert_string_label

def generate_top_cities_by_mean_metric(df, metric, ascrending=True):
    """
    Generates a bar plot showing the top 7 cities with the highest or lowest mean value of a given metric.

    Parameters:
        df (pandas.DataFrame): The input DataFrame containing the data.
        metric (str): The name of the metric column to calculate the mean value for.
        ascrending (bool, optional): Whether to sort the cities in ascending or descending order based on the mean metric value. Defaults to True.

    Returns:
        plotly.graph_objects.Figure: The generated bar plot showing the top 7 cities with the highest or lowest mean value of the given metric.

    """

    mean_metric_by_city_country = (df.groupby(['city', 'country'])[metric].mean()
                                                            .sort_values(ascending=ascrending)
                                                            .reset_index(name='mean_' + metric)
                                                            .head(7))

    # Create a bar plot using Plotly Express
    fig = px.bar(mean_metric_by_city_country, x='city', y='mean_' + metric,
                height=500,  # Adjust the height as needed
                color='country',  # Color based on mean aggregate rating
                labels={'city': 'City', 'mean_' + metric: convert_string_label('mean_' + metric), 'country': 'Country'},
                category_orders={'city': mean_metric_by_city_country['city'].tolist()}) 

    return fig

def generate_top_cities_by_rating_count(df, above, value):
    """
    Generates a bar plot showing the top 7 cities with the highest or lowest count of restaurant IDs based on 
    the aggregate rating.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the data.
    - above (bool): Whether to filter the DataFrame for cities with an aggregate rating above or below 
      the given value.
    - value (float): The value to filter the DataFrame by.

    Returns:
    - plotly.graph_objs.Figure: The generated bar plot showing the top 7 cities with the highest or lowest 
      count of restaurant IDs based on the aggregate rating.

    """

    if above:
        filtered_df = df[df['aggregate_rating'] >= value]
    else:
        filtered_df = df[df['aggregate_rating'] <= value]

    count_agg_rating = (filtered_df
                        .groupby(['city', 'country'])['restaurant_id']
                        .count()
                        .sort_values(ascending=False)
                        .reset_index(name='count')
                        .head(7))
    

    # Create a bar plot using Plotly Express
    fig = px.bar(count_agg_rating, x='city', y='count',
                height=600,  # Adjust the height as needed
                color='country',  # Color based on mean aggregate rating
                labels={'city': 'City', 'count': 'Count', 'country': 'Country'},
                category_orders={'city': count_agg_rating['city'].tolist()}) 

    return fig

def generate_top_cities_by_unique_cuisines(df):
    """
    Generates a bar plot showing the top 10 cities with the highest number of unique cuisines.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the data.

    Returns:
    plotly.graph_objects.Figure: The generated bar plot showing the top 10 cities with the highest number of unique cuisines.

    This function groups the input DataFrame by the 'city' and 'country' columns and calculates the number of unique cuisines for each combination. It then sorts the resulting DataFrame in descending order based on the number of unique cuisines and selects the top 10 rows.

    The function then creates a bar plot using Plotly Express, where the 'city' column is used as the x-axis, the 'number_of_unique_cuisines' column is used as the y-axis, and the 'country' column is used to color the bars. The plot is labeled with appropriate names and category orders are set for the 'city' column.

    The resulting plot is returned as a Plotly Figure object.
    """

    # Group by 'city' and 'country' and calculate the number of unique cuisines
    unique_cuisine_by_city = (df.groupby(['city', 'country'])['cuisines_']
                               .nunique()
                               .sort_values(ascending=False)
                               .reset_index(name='number_of_unique_cuisines')
                               .head(10))
    
    # Create a bar plot using Plotly Express
    fig = px.bar(unique_cuisine_by_city, x='city', y='number_of_unique_cuisines',
                 height=600,  # Ajustar a altura conforme necessário
                 color='country',  # Colorir com base no país
                 labels={'city': 'City', 'number_of_unique_cuisines': 'Number of Unique Cuisines', 'country': 'Country'},
                 category_orders={'city': unique_cuisine_by_city['city'].tolist()})
    
    return fig

def main():
    st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide")

    # Import Dataset
    df = pd.read_csv("data/processed/data.csv")

    # ==============================================================================
    # Sidebar
    # ==============================================================================
    st.sidebar.markdown("## Filters")
    countries = st.sidebar.multiselect(
        "Choose the Countries You Want to View Information",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "India", "South Africa", "Canada", "Australia"],
        )

    # Filter by country
    df = df[df['country'].isin(countries)]

    # ==============================================================================
    # Sreamlit Layout
    # ==============================================================================
    st.markdown("# :cityscape: Cities Vision")


    with st.container():

        tab1, tab2 = st.columns(2)

        with tab1:
            st.markdown('### Top 7 Cities with the Highest Mean Aggregate Rating')
            fig = generate_top_cities_by_mean_metric(df, 'aggregate_rating', ascrending=False)
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.markdown('### Top 7 Cities with the Lowest Mean Aggregate Rating')
            fig = generate_top_cities_by_mean_metric(df, 'aggregate_rating', ascrending=True)
            st.plotly_chart(fig, use_container_width=True)

    with st.container():

        tab1, tab2 = st.columns(2)

        with tab1:
            st.markdown('### Top 7 Cities with the Highest Mean Average Price Rating')
            fig = generate_top_cities_by_mean_metric(df, 'price_range', ascrending=False)
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.markdown('### Top 7 Cities with the Lowest Mean Average Price Rating')
            fig = generate_top_cities_by_mean_metric(df, 'price_range', ascrending=True)
            st.plotly_chart(fig, use_container_width=True)

    with st.container():

        tab1, tab2 = st.columns(2)

        with tab1:
            st.markdown('### Cities with the most restaurants with an average rating above 4')
            fig = generate_top_cities_by_rating_count(df, above=True, value=4)
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.markdown('### Cities with the most restaurants with an average rating below 2.5')
            fig = generate_top_cities_by_rating_count(df, above=False, value=2.5)
            st.plotly_chart(fig, use_container_width=True)

    with st.container():
        st.markdown('### Cities with more different types of cuisine')
        fig = generate_top_cities_by_unique_cuisines(df)
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()