# Last updated: 7/5/2026, 6:26:39 PM
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    return patients[
        patients["conditions"]
        .str.contains(r'(^| )DIAB1', regex=True, na=False)
    ]