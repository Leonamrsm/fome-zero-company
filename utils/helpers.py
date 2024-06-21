import inflection
import pandas as pd

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

def country_name(country_id):
    return COUNTRIES[country_id]

def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"
    
def color_name(color_code):
    return COLORS[color_code]

def get_first_order_statistics(dataframe):
    # Central Tendency Metrics
    mean = pd.DataFrame(dataframe.apply(np.mean)).T
    median = pd.DataFrame(dataframe.apply(np.median)).T

    # Dispersion Metrics
    min_ = pd.DataFrame(dataframe.apply(min)).T
    max_ = pd.DataFrame(dataframe.apply(max)).T
    range_ = pd.DataFrame(dataframe.apply(lambda x: x.max() - x.min())).T
    std = pd.DataFrame(dataframe.apply(np.std)).T
    skew = pd.DataFrame(dataframe.apply(lambda x: x.skew())).T
    kurtosis = pd.DataFrame(dataframe.apply(lambda x: x.kurtosis())).T

    # Metrics Concatenation
    m = pd.concat([min_, max_, range_, mean, median, std, skew, kurtosis]).T.reset_index()
    m.columns = ['attributes', 'min', 'max', 'range', 'mean', 'median', 'std', 'skew', 'kurtosis']
    
    return m

def process_data(file_path):
    df = pd.read_csv(file_path)

    df = rename_columns(df)

    df = df.drop_duplicates(subset=['restaurant_id'])

    df = df.dropna()

    # Change data types
    df['has_table_booking'] = df['has_table_booking'].astype(bool)
    df['has_online_delivery'] = df['has_online_delivery'].astype(bool)
    df['is_delivering_now'] = df['is_delivering_now'].astype(bool)

    df['country'] = df['country_code'].apply(country_name)
    df['price_type'] = df['price_range'].apply(create_price_tye)
    df['color_name'] = df['rating_color'].apply(color_name)

    print(df.dtypes)

    df["cuisines_"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

    df.to_csv("data/processed/data.csv", index=False)

    return df

def convert_string_label(input_string):
    # Substituir underscores por espaços
    output_string = input_string.replace('_', ' ')
    # Capitalizar a primeira letra de cada palavra
    output_string = output_string.title()
    return output_string