import pandas as pd
import os

path = os.path.join("C:\\Users\\andre\\Documents\\Data Science\\DS-201\\Final Project\\Code\\data\\")

def open_csv():
    while True:
        file_name = input("Enter file name: ")
        file_path = os.path.join(path, file_name + ".csv")
        if os.path.exists(file_path):
            try:
                df = pd.read_csv(file_path)
                print("✅ File loaded successfully!")
                return df
            except pd.errors.ParserError:
                print("❌ The file couldn't be parsed as a CSV")
                pass
        else:
            print("File not found")

def save_csv(df):
    while True:
        file_name = input("Enter file name: ")
        file_path = os.path.join(path, file_name + ".csv")
        if os.path.exists(file_path):
            try:
                df.to_csv(file_path, index=False)
                print("✅ File saved successfully!")
            except pd.errors.ParserError:
                print("❌ The file couldn't be parsed as a CSV")
                pass
        else:
            print("File not found")