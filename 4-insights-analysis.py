
import pandas as pd
#import pandasql as psql

# Load data from the CSV file generated in data_ingestion.py
df = pd.read_csv('tourism_dataset_local.csv')

# 1. Group data by 'Country' and calculate the average 'Rating' for each country

# Python version (uncomment this to use the pandas version)
grouped_df = df.groupby('Country').agg({'Rating': 'mean'}).reset_index()
grouped_df['Rating'] = grouped_df['Rating'].round(2)

# SQL Equivalent (uncomment this to use the SQL version via pandasql)
#query_avg_rating_by_country = '''
#  SELECT Country, ROUND(AVG(Rating), 2) AS Rating
#  FROM df
#  GROUP BY Country
# '''
#grouped_df = psql.sqldf(query_avg_rating_by_country, locals())

# 2. Identify top 3 categories with the highest average rating

# Python version (uncomment this to use the pandas version)
top_categories = df.groupby('Category').agg({'Rating': 'mean'}).sort_values(by='Rating', ascending=False).head(3)
top_categories['Rating'] = top_categories['Rating'].round(2)

# Reset the index of top_categories to ensure 'Category' is written to the CSV
top_categories = top_categories.reset_index()

# SQL Equivalent (uncomment this to use the SQL version via pandasql)
#query_top_3_categories = '''
#    SELECT Category, ROUND(AVG(Rating), 2) AS Rating
#    FROM df
#    GROUP BY Category
#    ORDER BY Rating DESC
#   LIMIT 3
#'''
#top_categories = psql.sqldf(query_top_3_categories, locals())

# Open the file with newline='' to avoid adding extra newlines
with open('Sreehari-Butla.csv', 'w', newline='') as f:
    # Write header for the grouped data
    f.write('Country-wise Average Rating:\n')
    f.write('\n')
    # Write the country aggregation data to CSV
    grouped_df.to_csv(f, index=False)

    # Write a blank line to separate the sections
    f.write('\n')

    # Write header for the top categories
    f.write('Top 3 Categories by Average Rating:\n')
    f.write('\n')
    # Write the top categories data to CSV, including 'Category'
    top_categories.to_csv(f, index=False)

print("Both grouped data and top categories saved to 'Sreehari-Butla.csv' with correct formatting.")
