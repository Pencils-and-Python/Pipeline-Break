# src/utilities/cleanup_mapping.py
"""
Module to clean up the mapping file.

How to use:
    breaks_2019_clean = unify_break_data(breaks_2019_raw, 2019)
    breaks_2021_clean = unify_break_data(breaks_2021_raw, 2021)
    breaks_2022_clean = unify_break_data(breaks_2022_raw, 2022)

Then concatenate and move forward with modeling:
    all_breaks = pd.concat([breaks_2019_clean, breaks_2021_clean, breaks_2022_clean])
"""
def unify_break_data(df, year):
    # Standardize column names
    df = df.rename(columns={
        'ObjectId': 'break_id',
        'FID': 'break_id',
        'fullDate': 'date',
        'Date': 'date',
        'Actual_Fin': 'date',
        'location': 'location_text',
        'Location': 'location_text',
        'Address': 'location_text',
        'X': 'x_coord',
        'Y': 'y_coord',
        'x2': 'x_coord',
        'y2': 'y_coord',
        'leakClass': 'leak_type',
        'Work_Order': 'leak_type',
        'Descriptio': 'leak_type'
    })

    # Parse date
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Extract date parts
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.day_name()
    df['week_of_year'] = df['date'].dt.isocalendar().week

    # Add year tag if needed
    df['source_year'] = year

    return df
