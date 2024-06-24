import folium.plugins
import streamlit as st
import folium

from streamlit_folium import folium_static

from  utils.helpers import process_data

RAW_DATA_PATH = "./data/raw/zomato.csv"


st.set_page_config(
    page_title="Home",
    page_icon="📊",
    layout="wide"

)

def create_map(dataframe):
    f = folium.Figure(width=1920, height=1080)

    m = folium.Map(max_bounds=True, tiles="CartoDB positron")
    marker_cluster = folium.plugins.MarkerCluster().add_to(m)

    for _, line in dataframe.iterrows():
        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=folium.Popup(
                folium.Html(
                    (
                        f"<p><strong>{line['restaurant_name']}</strong></p>"
                        f"<br>Price: {line['average_cost_for_two']},00 ({line['currency']}) for two"
                        f"<br>Type: {line['cuisines']}"
                        f"<br>Aggragate Rating: {line['aggregate_rating']}/5.0"
                    ),
                    script=True,
                ),
                max_width=500,
            ),
            icon=folium.Icon(color=line["color_name"], icon="home", prefix="fa"),
        ).add_to(marker_cluster)

    folium.LayerControl().add_to(m)
    folium_static(m, width=1024, height=768)

def main():

    df = process_data(RAW_DATA_PATH)

    st.markdown("# Fome Zero!")

    st.markdown("## The Best Place to Find Your New Favorite Restaurant!")

    st.markdown("### We have the following brands on our platform:")

    tabs = st.columns(5)

    tabs[0].metric(
        "Registered Restaurants",
        f"{len(df):,}",
    )

    tabs[1].metric(
        "Registered Countries",
        f"{df['country'].nunique():,}",
    )

    tabs[2].metric(
        "Registered Cities",
        df['city'].nunique(),
    )

    tabs[3].metric(
        "Reviews Made on the Platform",
        f"{df['votes'].sum():,}",
    )

    tabs[4].metric(
        f"Types of Cuisines\nOffered",
        df['cuisines_'].nunique(),
    )

    create_map(df)

if __name__ == "__main__":
    main()