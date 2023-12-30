import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def descriptives(df, unique_values_bool, unique_values_max_count, normality_tests_bool, normality_tests_bins):
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