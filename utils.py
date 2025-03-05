import requests
import polars as pl

# See above - we've created an API key in a file called 'apikey', 
# in the same directory as this notebook
def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

# https://medium.com/@techworldthink/accessing-google-sheet-data-with-python-a-practical-guide-using-the-google-sheets-api-dc57759d387a
def get_google_raw_sheet_data(spreadsheet_id, sheet_name, api_key):
    """ Given a spreadsheet_id, sheet name and API key, 
        return the contents of that file
    """
    # Construct the URL for the Google Sheets API
    url = f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{sheet_name}!A1:Z?alt=json&key={api_key}'

    try:
        # Make a GET request to retrieve data from the Google Sheets API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        
        return data

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")
        return None


# Grab data from the excel sheet and construct a polars dataframe. 
def format_sheet_data(sheet_data):
    sheet_2025 = sheet_data["values"]
    abs_challenges = pl.DataFrame(sheet_2025[1:len(sheet_2025)], 
                                  schema = {key:str for key in sheet_2025[0]},
                                  orient="row")
    # By default, all columns come in as str types, so cast numerical columns as appropriate
    abs_challenges = abs_challenges.with_columns(
        pl.col("abs_index").cast(pl.Int32),
        pl.col("inning").cast(pl.Int8),
        pl.col("balls").cast(pl.Int8),
        pl.col("strikes").cast(pl.Int8),
        pl.col("outs_when_up").cast(pl.Int8),
        pl.col("game_date").cast(pl.Date)
    )

    return abs_challenges


def get_sheet_data():
    filename = 'apikey'
    spreadsheet_id = '11VW8sm80ezLvvxBL-tJeAtRQZsreRzDkr3KcSP17f8A'
    sheet_name = "2025"
    
    api_key = get_file_contents(filename)
    sheet_data = get_google_raw_sheet_data(spreadsheet_id, sheet_name, api_key)
    abs_challenges = format_sheet_data(sheet_data)
    return abs_challenges 


def get_ABS_universe(data):
    AZ_home_teams = ['SEA', 'SD', 'CWS', 'LAD', 'KC', 'TEX', 'CIN', 'CLE', 'COL', 'AZ']
    FL_home_teams = ['TOR', 'DET', 'NYY', 'PIT', 'PHI', 'NYM', 'STL', 'MIA']
    ABS_home_teams = AZ_home_teams + FL_home_teams

    # Filter on ABS relevant teams
    abs_relevant_pitches = data.filter(
        pl.col('home_team').is_in(ABS_home_teams)
    )

    # Filter to ball and strike pitches
    abs_relevant_pitches = abs_relevant_pitches.filter(
        pl.col('description').is_in(['ball', 'called_strike'])
    )

    return abs_relevant_pitches

