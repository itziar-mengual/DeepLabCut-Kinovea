from extractor import extract_tables_from_excel
from utils import get_excel_files

if __name__ == '__main__':
    path = "/Users/admin/PycharmProjects/DeepLabCut - Kinovea/Kinovea"
    excel_files = get_excel_files(path)
    print(excel_files)

    df = extract_tables_from_excel(excel_files)
    print(df.head())
    df.to_csv('Data/data_parsed.csv', index=False, encoding='utf-8')
