"""
A python script contataining a small function to get claims data
from https://patentsview.org/download/claims by year.
"""


def get_patents_view_claims_data(from_year: int, to_year: int) -> pd.DataFrame:
  """
  function to get data from https://patentsview.org/download/claims by year.

  parameter:
  ---------
  `from_year` & `to_year` are the ranges of the years of which data are needed.
  If you want data for single year, simply give same value for both (I know its
  a naive approach :p)

  Return:
  ------
  A merged pandas.DataFrame object for the given range of years.
  """
  year_range = range(from_year, to_year + 1)
  list_of_link = [f"https://s3.amazonaws.com/data.patentsview.org/claims/g_claims_{year}.tsv.zip" for year in year_range]
  list_of_df = [pd.read_csv(df_link, compression='zip', sep="\t") for df_link in list_of_link]
  for year, df in zip(year_range, list_of_df):
    df['year'] = year
  return pd.concat(list_of_df)
