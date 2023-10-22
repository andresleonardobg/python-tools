import pandas as pd

def split_information_into_unique_files(file_name: str, column_data_split: str):
    '''
    split data into unique files based in the data of column what you need to split
    '''
    df = pd.read_excel(file_name)
    column_data = getattr(df, column_data_split)
    for i in column_data.unique():
        df2 = df[df[column_data_split]==i]
        df2.to_excel(f"{i}.xlsx",index=False)

