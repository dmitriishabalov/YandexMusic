from utils.extract import extract_data
from utils.load import load_data


if __name__ == '__main__':
    chart_df = extract_data()
    load_data(chart_df)
