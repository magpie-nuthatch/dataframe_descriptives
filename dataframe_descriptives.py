def descriptives(df, maxlength):
    try:
        print()
        print(f"Information for columns in current dataframe:")
        print(df.info())
        for column in df:
            df_loop = df.dropna(subset = column)
            print()
            print(f"Descriptives for column {column}:")
            print(df_loop[column].describe())
            if df_loop[column].dtype == "object" and len(df_loop[column].unique()) < maxlength:
                unique_values = sorted(df_loop[column].unique())
                print()
                print(f"Unique values in column {column}:")
                for value in unique_values:
                    print(value)
            print()
    except AttributeError:
        print("Descriptives unavailable for current dataframe.")

# When called, function returns descriptives of all columns in a dataframe.
        # Features include min, max, avg, etc. for numeric variables, and unique value counts and names for categorical variables.
        # Function requires 2 variables as input. These are the name of the dataframe (df) and the desired maximum length for the list of unique value names for each categorical variable.
# Example: descriptives(df_name, 20)