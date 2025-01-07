import pandas as pd
import matplotlib.pyplot as plt
import kagglehub

# Download the latest version of the dataset
path = kagglehub.dataset_download("pantanjali/unemployment-dataset")
print("Path to dataset files:", path)

# Load the data (assuming the dataset is a CSV file in the downloaded folder)
csv_file = path + "/unemployment analysis.csv"  # Adjust file name if necessary
df = pd.read_csv(csv_file)

# Verify the column names
print(df.columns)

# Filter rows for specific countries (United States, United Kingdom, Canada)
filtered_data = df[df['Country Name'].isin(['United States', 'United Kingdom', 'Canada'])]

# Check if filtered data is empty
if filtered_data.empty:
    print("No matching data found. Please check the column values or dataset.")
else:
    # Print the filtered data to confirm the result
    print(filtered_data)

    # Reshape the data from wide to long format
    long_data = filtered_data.melt(
        id_vars=['Country Name', 'Country Code'], 
        var_name='Year', 
        value_name='Unemployment Rate'
    )

    # Convert the 'Year' column to numeric
    long_data['Year'] = pd.to_numeric(long_data['Year'], errors='coerce')

    # Drop rows with missing unemployment rates
    long_data = long_data.dropna(subset=['Unemployment Rate'])

    # Create a plot for each country
    plt.figure(figsize=(10, 6))
    for country in ['United States', 'United Kingdom', 'Canada']:
        country_data = long_data[long_data['Country Name'] == country]
        plt.plot(country_data['Year'], country_data['Unemployment Rate'], label=country)

    # Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Unemployment Rate (%)')
    plt.title('Unemployment Rate by Year')
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()
