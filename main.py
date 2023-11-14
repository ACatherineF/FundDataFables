from data.dataset import Dataset
from datetime import datetime


def main():
    start_date = input('Enter start date - Format YYYY-mm-dd \n')
    end_date = input('Enter end date -  Format YYYY-mm-dd\n')
    ticker_symbol = input('For which stock? Enter the ticker symbol. \n')
    start_date = datetime.strptime(start_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d').strftime('%Y-%m-%d')
    #TODO : Confirm that ticker_symbol is a valid stock

    dataset = Dataset(start_date, end_date, ticker_symbol)
    print(dataset.get_dataset_info())


if __name__ == "__main__":
    main()

