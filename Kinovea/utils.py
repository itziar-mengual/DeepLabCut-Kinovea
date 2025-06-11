import os

def get_excel_files(path):
    files_dict = {}
    for root, _, files in os.walk(path):
        for name in files:
            if name.endswith('.xlsx'):
                base_name = os.path.splitext(name)[0]
                file_path = os.path.join(root, name)
                if base_name not in files_dict:
                    files_dict[base_name] = file_path

    return list(files_dict.values())

def parse_filename(name):
    # Example: name = "01_01_G1_C"
    parts = name.split('_')
    return {
        'id': parts[0] if len(parts) > 0 else '',
        'group': parts[1] if len(parts) > 1 else '',
        'subject': parts[2] if len(parts) > 2 else '',
        'session': parts[3] if len(parts) > 3 else '',
    }
