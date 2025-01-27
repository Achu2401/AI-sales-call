import uuid
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from setup import config
import pandas as pd

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def authenticate_google_account():
    service_account_file = config["google_creds"]
    if not service_account_file:
        raise ValueError("Service account credentials path is missing in env_setup.py.")
    return service_account.Credentials.from_service_account_file(service_account_file, scopes=SCOPES)

def store_data_in_sheet(sheet_id, chunks, summary, overall_sentiment):
    creds = authenticate_google_account()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    call_id = str(uuid.uuid4())
    print(f"Call ID: {call_id}")

    values = []
    if chunks:
        first_chunk, first_sentiment, _ = chunks[0]
        values.append([call_id, first_chunk, first_sentiment, summary, overall_sentiment])
    for chunk, sentiment, _ in chunks[1:]:
        values.append(["", chunk, sentiment, "", ""])

    header = ["Call ID", "Chunk", "Sentiment", "Summary", "Overall Sentiment"]
    all_values = [header] + values

    body = {'values': all_values}
    try:
        result = sheet.values().append(
            spreadsheetId=sheet_id,
            range="Sheet1!A1",
            valueInputOption="RAW",
            body=body
        ).execute()
        print(f"{result.get('updates').get('updatedCells')} cells updated in Google Sheets.")
        st.write(f"{result.get('updates').get('updatedCells')} cells updated in Google Sheets.")
    except Exception as e:
        print(f"Error updating Google Sheets: {e}")
        st.write(f"Error updating Google Sheets: {e}")

def fetch_call_data(sheet_id, range_name="Sheet1!A1:E"):
    """
    Fetch previously saved call data from Google Sheets and return it as a pandas DataFrame.
    :param sheet_id: ID of the Google Sheet.
    :param range_name: The range to fetch data from.
    :return: pandas DataFrame containing the call data.
    """
    creds = authenticate_google_account()
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    try:
        result = sheet.values().get(spreadsheetId=sheet_id, range=range_name).execute()
        rows = result.get('values', [])
        if rows:
            # Convert rows to a pandas DataFrame
            header = rows[0]
            data = rows[1:]  # Skip the header row
            df = pd.DataFrame(data, columns=header)
            print(f"Fetched {len(df)} rows of data from Google Sheets.")
            st.write(f"Fetched {len(df)} rows of data from Google Sheets.")
            return df
        else:
            print("No data found in the sheet.")
            st.write("No data found in the sheet.")
            return pd.DataFrame()  # Return an empty DataFrame if no data
    except Exception as e:
        print(f"Error fetching data from Google Sheets: {e}")
        st.write(f"Error fetching data from Google Sheets: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
