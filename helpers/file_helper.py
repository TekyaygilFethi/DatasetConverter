import pandas as pd

def read_file(uploaded_file, extension):
    if extension == "csv":
        return pd.read_csv(uploaded_file, encoding="utf-8")

    if extension == "xlsx":
        xlsx_file = pd.ExcelFile(uploaded_file, engine='openpyxl')
        df = pd.read_excel(uploaded_file)
        xlsx_file.book.encoding = 'utf-8'
        return df

    if extension == "parquet":
        return pd.read_parquet(uploaded_file)

def convert_file(df, file_name, extension):
    if extension == "csv":
        return df.to_csv(encoding='utf-8-sig', index=False)

    if extension == "xlsx":
        excel_data = pd.ExcelWriter(file_name)
        df.to_excel(excel_data, index=False)
        excel_data.save()

        with open(excel_data, 'rb') as f:
            data = f.read()
            return data

    if extension == "parquet":
        return df.to_parquet(index=False)

    return True
