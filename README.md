# 1. Business problem

The company Fome Zero is a restaurant marketplace. In other words, its core business is to facilitate the meeting and negotiations of customers and restaurants. Restaurants register on the Fome Zero platform, which provides information such as address, type of cuisine served, whether they have reservations, whether they make deliveries and also an evaluation note on the restaurant's services and products, among other information.

## 1.1. The challenge

The company Fome Zero is a restaurant marketplace. In other words, its core business is to facilitate the meeting and negotiations of customers and restaurants. Restaurants register on the Fome Zero platform, which provides information such as address, type of cuisine served, whether they have reservations, whether they make deliveries and also an evaluation note on the restaurant's services and products, among other information.

The CEO needs to better understand the business to be able to make the best strategic decisions and further leverage Zero Hunger, and to do this, he needs an analysis to be carried out on the company's data and dashboards to be generated, based on these analyses, to answer the following questions:

### General

 1. How many unique restaurants are registered?

 2. How many unique countries are registered?

 3. How many unique cities are registered?

 4. What is the total number of assessments carried out?

 5. What are the total types of cuisine registered?

### Country

 1. What is the name of the country that has the most registered cities?

 2. What is the name of the country that has the most registered restaurants?

 3. What is the name of the country that has the most registered restaurants with a price level equal to 4?

 4. What is the name of the country that has the greatest number of different types of cuisine?

 5. What is the name of the country that has the largest number of evaluations carried out?

 6. What is the name of the country that has the largest number of restaurants that deliver?

 7. What is the name of the country that has the largest number of restaurants that accept reservations?

 8. What is the name of the country that has, on average, the highest number of registered evaluations?

 9. What is the name of the country that has, on average, the highest recorded average score?

 10. What is the name of the country that has, on average, the lowest recorded average score?

 11. What is the average price of a dish for two per country?

### City

 1. What is the name of the city that has the most registered restaurants?

 2. What is the name of the city that has the most restaurants with an average rating above 4?

 3. What is the name of the city that has the most restaurants with an average rating below 2.5?

 4. What is the name of the city that has the highest average price for a dish for two?

 5. What is the name of the city that has the largest number of different types of cuisine?

 6. What is the name of the city that has the largest number of restaurants that take reservations?

 7. What is the name of the city that has the largest number of restaurants that deliver?

 8. What is the name of the city that has the largest number of restaurants that accept online orders?

### Restaurants

 1. What is the name of the restaurant that has the most reviews?

 2. What is the name of the restaurant with the highest average rating?

 3. What is the name of the restaurant that has the highest price for one dish for two people?

 4. What is the name of the Brazilian cuisine restaurant that has the lowest average rating?

 5. What is the name of the Brazilian cuisine restaurant, which is from Brazil, and has the highest average rating?

 6. Are restaurants that accept online orders also, on average, the restaurants that have the most registered reviews?

 7. Are the restaurants that take reservations also, on average, the restaurants that have the highest average price for a dish for two people?

 8. Do Japanese cuisine restaurants in the United States of America have a higher average serving price for two people than American steakhouses (BBQ)?

- Types of Cuisine

 1. Of the restaurants that have Italian cuisine, what is the name of the restaurant with the highest average rating?

 2. Of the restaurants that have Italian cuisine, what is the name of the restaurant with the lowest average rating?

 3. Of the restaurants that have American cuisine, what is the name of the restaurant with the highest average rating?

 4. Of the restaurants that have American cuisine, what is the name of the restaurant with the lowest average rating?

 5. Of the restaurants that serve Arabic cuisine, what is the name of the restaurant with the highest average rating?

 6. Of the restaurants that serve Arabic cuisine, what is the name of the restaurant with the lowest average rating?

 7. Of the restaurants that have Japanese cuisine, what is the name of the restaurant with the highest average rating?

 8. Of the restaurants that have Japanese cuisine, what is the name of the restaurant with the lowest average rating?

 9. Of the restaurants that offer homemade cuisine, what is the name of the restaurant with the highest average rating?

10. Of the restaurants that offer homemade cuisine, what is the name of the restaurant with the lowest average rating?

11. What type of cuisine has the highest average value for a dish for two people?

12. What type of cuisine has the highest average score?

13. What type of cuisine does the most restaurants accept online orders and deliver?

The CEO also asked for a dashboard to be generated that would allow him to visualize the main information from the questions he asked. The CEO needs this information as quickly as possible, since he is also new to the company and will use it to better understand the company Fome Zero to be able to make more assertive decisions.

# 2. Assumptions assumed for the analysis

1. Marketplace was the assumed business model
2. The three views created in the dashboards were: Countries View, Cities View and Types of Cuisine view.
3. Only the first type of cuisine was considered among restaurants that have more than 1 type of cuisine. E.g.: if the type of cuisine of a restaurant is *“Italian, Pizza, Fresh Fish”, only “Italian” was considered in the analyses.*

# 3. Solution strategy

A strategic panel was developed to visualize how restaurants are distributed across countries, cities and types of cuisine and an overview of all registered restaurants.

For each view, the following set of metrics was obtained:

## 3.1. Countries Vision

1. Number of restaurants per country.
2. Number of cities with registered restaurants per country.
3. Average rating of restaurants by country.
4. Average price of restaurants by country.

## 3.2. Cities Vision

1. Top 7 cities with the highest average rating for restaurants.
2. Top 7 cities with the lowest average aggregate rating for restaurants.
3. Top 7 cities with the highest average restaurant prices.
4. Top 7 cities with the lowest average restaurant prices.
5. Top 7 cities with the most restaurants registered with an average rating above 4.
6. Top 7 cities with the most restaurants registered with an average rating below 2.5.
7. Top 10 cities with the highest number of registered restaurants with different types of cuisine.

## 3.3. Cuisines Vision
1. Metrics showing the top 5 restorations with the highest ratings.
2. Table showing details of the top n restaurants with the highest reviews.
3. Bar graph: Aggregate Average Score X Type of Cuisine.
4. Bar graph: Average Price Variation Index of Restaurants X Type of Cuisine.

# 4. Top 3 Data Insights

- The country with the lowest average aggregate score for restaurants is Brazil.
- Singapore is the country with the highest average restaurant price index.
- The city of Muntinlupa in the Philippines is the city with the highest average score for registered restaurants (4.9/5.0).

# 5. The final product of the project

Panel, online, hosted in a Cloud and available for access on any device connected to the internet.

The panel can be accessed through this link: https://fome-zero-company-leonamrsm.streamlit.app/

# 6. Conclusion

The objective of this project is to create a set of graphs and/or tables that display these metrics in the best possible way for the CEO.

Strategies can be created from the graphs to improve the average ratings of registered restaurants.

# 7. Next Steps

1. Create new filters
2. Add new business insights.
3. Improve the distribution of graphs and metrics in each view.
