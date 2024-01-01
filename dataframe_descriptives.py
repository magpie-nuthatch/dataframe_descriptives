def descriptives_d(df, maxlength):
    import pandas as pd
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
        
def descriptives_n(df, unique_values_bool, unique_values_max_count, normality_tests_bool, normality_tests_bins):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import scipy.stats as stats
    np.set_printoptions(suppress = True,
                    formatter = {'float_kind':'{:0.2f}'.format})
    try:
        print()
        print(f"Information on columns in current dataframe:")
        print(df.info())
        for column in df:
            df_loop = df.dropna(subset = column)
            print()
            print(f"Descriptives for column {column}:")
            print(df_loop[column].describe())
            if df_loop[column].dtype == "object" and unique_values_bool == True and len(df_loop[column].unique()) < unique_values_max_count:
                unique_values = sorted(df_loop[column].unique())
                print()
                print(f"Unique values in column {column}:")
                for value in unique_values:
                    print(value)
            else:
                pass
            print()
            if df_loop[column].dtype != "object" and normality_tests_bool == True:
                try:
                    fig = plt.figure(figsize = (10, 10))
                    ax = fig.add_subplot(111)
                    stats.probplot(df_loop[column],
                                plot = plt,
                                rvalue = True)
                    ax.set_title(f"QQ Plot for {column}")
                    plt.show()

                    df_loop.plot(kind = "hist", 
                                y = column, 
                                bins = normality_tests_bins, 
                                title = f"Histogram for {column}")
                    plt.show()

                    print(f"Statistical normality test for {column}")
                    print(stats.normaltest(df_loop[column]))
                except:
                    try:
                        print(f"Statistical normality test for {column}")
                        print(stats.normaltest(df_loop[column]))
                    except AttributeError:
                        print("Normality tests unavailable for current column.")
                    except:
                        pass
                print()
            else:
                pass
    except AttributeError:
        print("Descriptives unavailable for current dataframe.")

def descriptives_ht(df, rows):
    import pandas as pd
    print()
    print(f"Head of current dataframe, displaying first {rows} rows:")
    print(df.head(n = rows))
    print()
    print(f"Tail of current dataframe, displaying last {rows} rows:")
    print(df.head(n = rows))