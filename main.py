import pandas as pd
from preprocessing_pipeline import preprocess_data
from load_model import load_model

url = 'https://raw.githubusercontent.com/REDi-school-ff22-Data-cycle/twitter-sentiment-analysis/main/twitter_sentiment_data.csv'


def import_data(url):
    df = pd.read_csv(url)
    return df


def main():
#    df = import_data(url)
#    preprocessed_df = preprocess_data(df)

#    print("Preprocessed df ", preprocessed_df.shape)
#    load_model()

#if __name__ == "__main__":
#    main()
