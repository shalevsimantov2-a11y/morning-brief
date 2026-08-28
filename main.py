name: Daily Morning Brief Dispatcher

on:
  schedule:
    - cron: '0 4 * * *'
  workflow_dispatch:

jobs:
  run-brief:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python 3.11
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install yfinance reportlab python-bidi arabic-reshaper requests

      - name: Run Morning Brief & Send Email
        env:
          GMAIL_USER: ${{ secrets.GMAIL_USER }}
          GMAIL_APP_PASSWORD: ${{ secrets.GMAIL_APP_PASSWORD }}
          RECIPIENT_EMAIL: ${{ secrets.RECIPIENT_EMAIL }}
        run: |
          python main.py
