import pandas as pd
import os
from utils import parse_filename

def extract_tables_from_excel(file_paths):
    data_blocks = []

    for file_path in file_paths:
        try:
            df = pd.read_excel(file_path, sheet_name=0, header=None)
            file_data_blocks = {}

            # Detect all table names in column 0 that are strings and not NaN
            # First 2 are Key images and Positions (not used)
            table_markers = df[0][df[0].notna() & df[1].isna()].reset_index().iloc[2:]

            for i in range(len(table_markers)):
                table_name = str(table_markers.iloc[i, 1])
                start_row = table_markers.iloc[i, 0] + 3
                end_row = (df[start_row:].index[df[start_row:].isnull().all(axis=1)][0]
                           if df[start_row:].isnull().all(axis=1).any()
                           else df.shape[0])
                table_data = df.iloc[start_row:end_row, :3].copy()

                if table_data.shape[1] < 3:
                    continue

                # Normalize column names
                table_data.columns = ['Time (s)', 'X (px)', 'Y (px)']
                table_data.rename(columns={
                    'X (px)': f'{table_name}_X',
                    'Y (px)': f'{table_name}_Y'
                }, inplace=True)

                file_data_blocks[table_name] = table_data[['Time (s)', f'{table_name}_X', f'{table_name}_Y']]

            # Merge all tables on 'Time (s)'
            if file_data_blocks:
                tables = list(file_data_blocks.keys())
                merged_df = file_data_blocks[tables[0]]
                for table in tables[1:]:
                    merged_df = pd.merge(merged_df, file_data_blocks[table], on='Time (s)', how='outer')

                # Add metadata from filename
                filename = os.path.basename(file_path).replace('.xlsx', '')
                metadata = parse_filename(filename)

                for key, value in metadata.items():
                    merged_df[key] = value

                data_blocks.append(merged_df)

        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    if data_blocks:
        final_df = pd.concat(data_blocks, ignore_index=True)
        final_df.rename(columns={'Time (s)': 'time'}, inplace=True)

        xy_columns = [col for col in final_df.columns if col.endswith('_X') or col.endswith('_Y')]
        final_df[['time'] + xy_columns] = final_df[['time'] + xy_columns].apply(pd.to_numeric, errors='coerce')
        return final_df

    return pd.DataFrame()