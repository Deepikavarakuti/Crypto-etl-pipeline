from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():

    df = extract_data()

    df_transformed = transform_data(df)

    load_data(df_transformed)

    print("ETL Pipeline executed successfully!")

if __name__ == "__main__":
    run_pipeline()