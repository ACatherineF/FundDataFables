import yfinance as yf


class Dataset:
    def __init__(self, start_date, end_date, ticker_symbol):
        self.start_date = start_date
        self.end_date = end_date
        self.ticker_symbol = ticker_symbol
        self.dataset = self._fetch_dataset()


    def _fetch_dataset(self):
        df = yf.download(self.ticker_symbol, self.start_date, self.end_date)
        return df

    def save_to_csv(self, path):
        self.dataset.to_csv(path, index=False)

    def get_dataset_info(self):
        print(self.dataset.info())
