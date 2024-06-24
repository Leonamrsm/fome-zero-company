import pandas as pd
import plotly.express as px
import streamlit as st

from utils.helpers import convert_string_label

def get_cuisines_mean_metric_barplot_fig(df, ascending, metric):

    df_aux = (df.groupby('cuisines_')[metric]
                                 .mean()
                                 .sort_values(ascending=ascending)
                                 .reset_index(name='mean_aggregate_rating'))
            
    # Create a bar plot using Plotly Express
    fig = px.bar(df_aux, x='cuisines_', y='mean_aggregate_rating',
                labels={'cuisines_': convert_string_label('cuisines_'), 'mean_aggregate_rating': convert_string_label(metric)},
                color='cuisines_') 
    
    fig.update_layout(showlegend=False)

    return fig

def generate_top_cuisines_metrics(df, top_n):
    """
    Generates metrics for the top cuisines based on aggregate rating.
    
    Parameters:
    - df: DataFrame containing the data to be analyzed.
    - top_n: Number of top cuisines to consider.
    
    Returns:
    This function does not return anything. It generates metrics for the top cuisines.
    """

    df_cuisine = df.sort_values(by='aggregate_rating', ascending=False).head(top_n).reset_index(drop=True)

    if len(df_cuisine) > 0:

        with st.container():

            if len(df_cuisine) >= 5:
                iters = 5
            else:
                iters = len(df_cuisine)
            
            tabs = st.columns(iters)
            
            for i in range(iters):
                with tabs[i]:
                    st.metric(
                        label=f"{df_cuisine.loc[i, 'cuisines_']}: {df_cuisine.loc[i, 'restaurant_name']}",
                        value=f"{df_cuisine.loc[i, 'aggregate_rating']}/5.0",
                        help=f"""
                        País: {df_cuisine.loc[i, 'country']}\n
                        Cidade: {df_cuisine.loc[i, 'city']}\n
                        Price scale: {df_cuisine.loc[i, 'price_range']}/4
                        """)

def main():
    st.set_page_config(page_title="Cuisines", page_icon="🍽️", layout="wide")

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


    cuisines = st.sidebar.multiselect(
        "Choose Types of Cuisine",
        df.loc[:, "cuisines_"].unique().tolist(),
        default=["Home-made", "BBQ", "Japanese", "Brazilian", "Arabian", "American", "Italian"],
        )
    
    top_n = st.sidebar.slider(
        "Select the number of Restaurants you want to view", 1, 20, 10
    )

    # ==============================================================================
    # Sreamlit Layout
    # ==============================================================================
    st.markdown("# 🍽️ Cuisines Vision")


    df_filtered = df[(df['country'].isin(countries)) & (df['cuisines_'].isin(cuisines))] 
    if len(df_filtered) < top_n:
        top_n = len(df_filtered)

    generate_top_cuisines_metrics(df_filtered, top_n=top_n)

    with st.container():

        st.markdown(f"## Top {top_n} Restaurants with Highest Mean Aggregate Rating")     
        
        selected_columns = ['restaurant_name', 'country', 'city', 'cuisines_', 'average_cost_for_two', 'votes']

        st.dataframe(df_filtered
                     .groupby(selected_columns)['aggregate_rating']
                     .mean()
                     .sort_values(ascending=False)
                     .reset_index(name='mean_aggregate_rating')
                     .head(top_n))

    with st.container():

        st.markdown(f"### Mean Aggregate Rating by Cuisines")
        fig = get_cuisines_mean_metric_barplot_fig(df_filtered, ascending=False, metric='aggregate_rating')
        st.plotly_chart(fig, use_container_width=True)

    with st.container():

        st.markdown(f"### Price Range by Cuisines")
        fig = get_cuisines_mean_metric_barplot_fig(df_filtered, ascending=False, metric='price_range')
        st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()