import pandas as pd

def load_nuclear_data(file_path):
    df = pd.read_excel(file_path)
    df['station'] = df['station'].replace('ЮУАЕС', 'ПАЕС')
    df['index_dump'] = df['index_dump'].replace(r'<0,01\s*', 0, regex=True)
    df['index_dump'] = pd.to_numeric(df['index_dump'], errors='coerce')
    
    return df