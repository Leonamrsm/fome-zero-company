# Libraries
import pandas as pd
import plotly.express as px
import streamlit as st


from utils.helpers import convert_string_label

def get_barplot_count_column_by_country(df, column, label):
    """
    Generate a bar plot showing the count of unique values for a given column by country.

    Parameters:
    - df (pandas.DataFrame): The DataFrame containing the data.
    - column (str): The name of the column to count unique values for.
    - label (str): The label to use for the y-axis of the plot.

    Returns:
    - fig (plotly.graph_objs.Figure): The Plotly figure object representing the bar plot.
    """


    # Group the data by country and count the unique restaurant IDs
    top_countries = (df.groupby('country')[column]
                        .nunique()  # Count unique restaurant IDs
                        .sort_values(ascending=False)  # Sort in descending order
                        .reset_index(name=label))

    # Criar o gráfico de barras
    fig = px.bar(top_countries, x='country', y=label,
                labels={'country': 'Country', label: convert_string_label(label)},
                text=label,
                height=550,
                color='country')

    # Ajustar a exibição dos rótulos de texto
    fig.update_traces(textposition='outside')

    # Remove the legend
    fig.update_layout(showlegend=False)

    return fig

def calculate_average_metric_by_country(df, metric):

    average_ratings = (df.groupby('country')[metric]
                        .mean()
                        .sort_values(ascending=False)
                        .reset_index(name = 'mean_' + metric))
    average_ratings['mean_' + metric] = round(average_ratings['mean_' + metric], 1)
    average_ratings.columns = ['Country', convert_string_label('mean_' + metric)]
    return average_ratings


def main():

    st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

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
    df_filtered = df[df['country'].isin(countries)]

    # ==============================================================================
    # Sreamlit Layout
    # ==============================================================================
    st.markdown("# :earth_asia: Countries Vision")


    with st.container():

        st.markdown('## Number of Restaurants by Country')
        fig = get_barplot_count_column_by_country(df_filtered, 'restaurant_id', 'number_of_restaurants')
        st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.markdown('## Number of Registered Cities by Country')
        fig = get_barplot_count_column_by_country(df_filtered, 'city', 'number_of_cities')
        st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.markdown('## Average Rating of Restaurants by Country')
        average_ratings = calculate_average_metric_by_country(df_filtered, 'aggregate_rating')
        
        col1, col2 = st.columns(2)

        with col1:
            # Create a choropleth map using Plotly Express
            fig = px.choropleth(average_ratings, 
                                locations='Country', 
                                locationmode='country names',
                                color='Mean Aggregate Rating',
                                hover_name='Country',
                                color_continuous_scale='Bluered_r')  # Color scale   

            # Show the map
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:

            # Create a bar plot using Plotly Express
            fig = px.bar(average_ratings, x='Country', y='Mean Aggregate Rating',
                        color='Mean Aggregate Rating',  # Color based on mean aggregate rating
                        color_continuous_scale='Bluered_r')  # Color palette

            # Show the map
            st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.markdown('## Average Price Rating of Restaurants by Country')        
        average_price_ratings= calculate_average_metric_by_country(df_filtered, 'price_range')
        
        col1, col2 = st.columns(2)

        with col1:

            # Create a choropleth map using Plotly Express
            fig = px.choropleth(average_price_ratings, 
                                locations='Country', 
                                locationmode='country names',
                                color='Mean Price Range',
                                hover_name='Country',
                                color_continuous_scale='Bluered_r')  # Color scale   

            # Show the map
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:

            # Create a bar plot using Plotly Express
            fig = px.bar(average_price_ratings, x='Country', y='Mean Price Range',
                        color='Mean Price Range',  # Color based on mean aggregate rating
                        color_continuous_scale='Bluered')  # Color palette

            # Show the map
            st.plotly_chart(fig, use_container_width=True)         

if __name__ == "__main__":
    main()