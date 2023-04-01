# Find missing data
pd.[isna/isnull]([np.nan/None)
# opposite check:
pd.[notnull/notna]([np.nan/None])
# can check series or dataframes
pd.notnull(pd.Series([1, np.nan, 7]))

pd.notnull(s).sum() # number of null values
# use to filter data
s[pd.notnull(s)] # returns only values that aren't null
# isnull and notnull are also methods of Series and dataframes, so can be used like so:
s.isnull()
s[s.notnull()]

# dropping null values
s.dropna()

# Working with dataframes
df.dropna() # by default, drops any row w/ at least one null val
df.dropna(axis=1) # switch to drop any column w/ nulls
df.dropna(how='all') # drops rows w/ all nulls
df.dropna(thresh=3) # keeps any rows w/ at least 3 valid vals

# Filling in nulls
s.fillna(0) # fill in w/ 0
s.fillna(method='ffill') # fills null w/ closest values from top/eft
s.fillna(method='bfill') # fills null w/ closest values from bottom/right
# Note that the above two methods may not work for some extremes

# Filling in dataframes
df.fillna({'Column1': 0, 'Col2': df['Col'].mean()}) # fills in each null in row w/ correpsonding val
df.fillna(method='ffill', axis=0) # fills forward w/ column
df.fillna(method='ffill', axis=1) # fills forward w/ row

# Cleaning nonnull vals
df['Sex'].unique() # returns array of unique values
df['Sex'].value_counts() # returns count of each unique val
df['Sex'].replace('D', 'F') # replace all occurrences of D to F
df['Sex'].replace({'D': 'F', 'N': 'M'})

# duplicates
s.duplicated() # returns series w/ bool values of whether each index is duplicate, works top-down
    s.duplicated(keep='last') # works bottom-up
    s.duplciated(keep=False) # treat all as duplicate(doesn't return True for first nor last)
s.drop_duplicates() # excludes duplicates, same parameters as duplicated()

# duplicates in dataframe
players.duplicated() # by default, checks that all columns are duplicated
players.duplicated(subset=['Name']) # only checks if name is duplicated

# Splitting strings
df['Data'].str.split('-') # splits string by -
    df['Data'].str.split('-', expand=True) # convert split string into dataframe
df['Country'].str.contains('U') # returns bool val
df['Country'].str.strip() # removes blank spacess
df['Country'].str.replace(' ', '') # replaces blanks w/ empty

import matplotlib.pyplot as plt

# default built-in method; keep in mind that it's not OOP, so hard to understand which figure correlates
# create new figure
plt.figure(figsize=(12, 6)) # width, height
plt.title("My Plot") # set plot title
plt.subplot(1, 2, 1) # rows, columns, panel selected
plt.plot(x, x**2)

# OOP; objects correlate to graphs
