import pandas as pd

# series; ordered sequence of items, can only hold uniform datatype
series = pd.Series([v1, v2, v2])
series.dtype # stores datatype of series
series.name = ""
# access using index, like a list
series[n]
series.index # return range of indexes, including step
# instead of meaningless number indexes, you can explicitly set the indexes
series.index = [
    "Index 1",
    "Index 2"
]
# setting indexes turns series into something like a map, rather than array; note that series is still ordered
# You can also set both the indexes and values at initizliation
pd.Series({
    "Index": val
}, name = "")
pd.Series([val1, val2], index=["index1", "index2"], name="")
# Alternatively, you can set an index to an existing series
pd.Series(series, index=["index1", "index2"])

# Indexing
# Instead of using custom index, you can explicitly use numeric index
series.iloc[-1] # returns last element
# You can select mult elements at once; returns a series
series[["index1", "index2"]]
series.iloc[[0, 1]]
# slicing works in pandas as well; note that the upper limit is inclusive
series["index1": "index2"] # from index1 tp index2, inclusive

# Boolean arrays, similar to numpy
series[series > 70] # filters out elements greated than 70
# boolean operations also work in boolean array
~(not), |(or), &(and)

# Data frames: Looks like excel
# data frame column is a series
df = pd.DataFrame({
    'Continent': [
        'America',
        'Europe'
    ],
    'HDI': [
        0.913,
        0.888
    ]
}, columns=['Continent', 'HDI']) # including columns argument is optional
df.index = [
    'Canada',
    'France'
]
df.columns # returns object of columns
df.index # returns object of the indexes
df.info() # returns columns and its types
df.size
df.shape # returns shape of dataframe
df.describe() # returns count, mean, std, min, max and range of each column
df.dtypes # shows type of each column
df.dtypes.value_counts() # returns number of each data type
#indexing
df.loc['Canada'] # select row by index
    # use second dimension to filter by column
    df.loc['Canada': 'France', 'HDI'] # from rows Canada to Italy, shows only HDI values
df.iloc[-1] # select row by sequential position
    df.iloc[1:3, 3] # returns rows 1-3, and return column 3
df['Continent'] # returns column

# conditional selection
# use conditioanl series as selection
df.loc[df['Population'] > 70] # returns any row whose population is greater than 70
# you can also specify which column to select
df.loc[df['Population'] > 70, ['Population', 'GDP']] # returns columns Population and GDP of rows w/ population > 70

# Dropping: returns new DataFrame, need to use inplace attribute to change original
df.drop(['Canada', 'Japan']) # drops specific rows
df.drop(columns=['Population', 'HDI']) # drops specific columns

# Adding new column
langs = pd.Series(
    ['French', 'German'],
    index=['France', 'Germany'],
    name='Language'
)
df['Language'] = langs

# Rename columns
df.rename(
    columns={
        'HDI': 'Human Development Index',
        'Annual Popcorn Consumption': 'APC'
    }, index={
        'United States': 'USA',
        'United Kingdom': 'UK',
        'Argentina': 'AR'
    })
# if column or row doesn't exist, nothing is changed

# Reading external data and plotting
df = pd.read_csv('filename', header=None) # reads csv file into dataframe, use header=None when there's no header row
df.head() # returns top
df.columns = ['Timestamp', 'Price'] # sets the column header of df
df.to_datetime(df['Timestamp']).head() # convert into time
df.set_index('Timestamp', inplace=True) # use column as index, like mapping
