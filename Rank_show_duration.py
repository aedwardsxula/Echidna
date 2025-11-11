import pandas as pd

def rank_tv_shows_by_duration(df, top_n=10):
    
    if "Date" not in df.columns or "Runtime" not in df.columns:
        raise ValueError("Expected columns 'Date' and 'Runtime' in DataFrame.")

    tv_df = df.copy()

    tv_df["Runtime"] = pd.to_numeric(tv_df["Runtime"], errors="coerce")

    tv_df = tv_df.dropna(subset=["Runtime"])

    ranked_tv = tv_df.sort_values(by="Runtime", ascending=False)

    return ranked_tv[["Title", "Date", "Runtime", "Genre", "Rating"]].head(top_n)
