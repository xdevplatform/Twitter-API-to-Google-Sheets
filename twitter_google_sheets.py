import pandas as pd
import gspread
import os
import requests

from oauth2client.service_account import ServiceAccountCredentials


def connect_to_twitter():
    bearer_token = os.environ.get("BEARER_TOKEN")
    return {"Authorization": "Bearer {}".format(bearer_token)}


def make_request(headers):
    url = "https://api.twitter.com/2/tweets"
    params = {
        "tweet.fields": "author_id,created_at,lang",
        "ids": "21,1293593516040269825,1334542969530183683",
    }
    return requests.request("GET", url, headers=headers, params=params).json()


def make_df(response):
    return pd.DataFrame(response["data"])


def authenticate_to_google():
    scope = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "/path/to/your/file.json", scope
    )
    return credentials


def main():
    headers = connect_to_twitter()
    response = make_request(headers)
    df = make_df(response)
    credentials = authenticate_to_google()
    gc = gspread.authorize(credentials)
    workbook = gc.open_by_key("spreadsheet_id")
    sheet = workbook.worksheet("Sheet1")
    sheet.update("A1", [df.columns.values.tolist()] + df.values.tolist())


if __name__ == "__main__":
    main()
