# Sending a response from the Twitter API to Google Sheets
When working with the Twitter API, there are numerous reasons you may want to transfer a response payload to [Google Sheets](https://www.google.com/sheets/about/). Google sheets are great for basic data analysis and sharing results quickly. This can be particularly useful for ad hoc analysis where you are working with stakeholders from different backgrounds.

## Setting up
Before you can use the Twitter API v2, you need an [approved developer account](https://developer.twitter.com/en/apply-for-access). Once you have an approved developer account, you need to create a Project, and an App inside of that Project. For more information about how to get started with the Twitter API, check out this [blog post](https://dev.to/twitterdev/step-by-step-guide-to-making-your-first-request-to-the-new-twitter-api-v2-42mi) and the [getting started](https://developer.twitter.com/en/docs/getting-started) section of our documentation. 

For this code sample, you’ll use [Python 3](https://www.python.org/downloads/). You also need to need to connect to the [Google Drive API](https://developers.google.com/drive). If you need any help getting set up be sure to check out this [helpful resource.](https://levelup.gitconnected.com/python-pandas-google-spreadsheet-476bd6a77f2b)

To get set up, install [pandas](https://pandas.pydata.org/), [gspread](https://gspread.readthedocs.io/en/latest/), [requests](https://requests.readthedocs.io/en/master/), and [oauth2client](https://pypi.org/project/oauth2client/). You’ll use pandas to transform the JSON payload response from the Twitter API to a tabular format, gspread to connect to Google Sheets, requests to connect to make an HTTP request to the Twitter API, and oauth2client to help with authentication using service accounts. You’ll also be importing [os](https://docs.python.org/3/library/os.html), but you do not need to install this first since this is included in the standard library of Python.

## Setting your environment variable for your bearer token

In order to connect to the Twitter API, you must first authenticate to the API. You can do this with your App’s bearer token. You obtain your bearer token in your App’s keys and tokens section inside of [the developer portal](https://developer.twitter.com/en/portal/dashboard). To ensure you don’t accidentally share your bearer token you can set an environment variable. To do this, inside of your terminal run the following and be sure to replace where it says your-bearer-token with your own.

```bash
export BEARER_TOKEN='your-bearer-token'
```

## Contributing

We welcome pull requests that add meaningful additions to these code samples, particularly for languages that are not yet represented here.

We feel that a welcoming community is important and we ask that you follow Twitter's
[Open Source Code of Conduct](https://github.com/twitter/code-of-conduct/blob/master/code-of-conduct.md)
in all interactions with the community.

## License

Copyright 2020 Twitter, Inc.

Licensed under the Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0
