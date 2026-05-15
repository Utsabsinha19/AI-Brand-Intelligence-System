import pandas as pd

def load_dataset(file_path):

    df = pd.read_csv(file_path)

    possible_columns = [
        "text",
        "review",
        "comment",
        "feedback",
        "content"
    ]

    text_column = None

    for col in df.columns:
        if col.lower() in possible_columns:
            text_column = col
            break

    if text_column is None:
        raise Exception("No text column found")

    df = df[[text_column]]

    df.columns = ["text"]

    return df