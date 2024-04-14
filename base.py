import pandas as pd
import constant

class Base:

    def __init__(self) -> None:
        pass
    
    def read_file(self, sheet_name):
        df = pd.read_excel(constant.FILENAME, sheet_name=sheet_name)
        return df