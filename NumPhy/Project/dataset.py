# Sample raw data as a list
raw_data = [
   
]

# Function to break raw data into 3 columns
def break_into_three_columns(data):
    # Create a list of tuples, each containing 3 consecutive data items
    grouped_data = [data[i:i+3] for i in range(0, len(data), 3)]
    
    # Display the grouped data
    for row in grouped_data:
        print(row)

# Call the function with the raw data
break_into_three_columns(raw_data)
