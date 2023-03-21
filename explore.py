import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import string

def determine_variable_type(train):
    '''
    Arguments: a train dataset
    Actions:
        1. Assigns columns names to categorical columns list or numerical columns list
            a. Categorical columns: the datatype is object or there are less than 10 unique values 
            b. Numerical columns: the datatype is not an object and thhere are 10 or more unique values
    Returns: explore_columns_list, categorical_column_list, numerical_column_list
    Modules: pandas
    
    '''
    # list comprehension that determines a col is  categorical if the data type is an object or there are less than 10 values
    cat_col = [col for col in train if train[col].dtype == 'O' or train[col].nunique() < 10]
    
    # list comprehension that complements the above
    num_col = [col for col in train if train[col].dtype != 'O' and train[col].nunique() >= 10]
    
    # full list of variables to explore
    explore_col = cat_col + num_col
    
    return explore_col, cat_col, num_col

def telco_churn_pie(train):

 
    plt.pie(train['churn'].value_counts(), labels=["No", "Yes"], autopct='%.0f%%', explode=[0, 0.1])
    plt.title('Telco Churn Rate')
    plt.legend()
    plt.show()
    
    return


def telco_core_services(train):
    '''
    This function creates a subplot of two variables of interest
    '''
    
    target = 'churn'
    plt.subplot(121)
    sns.barplot(data=train,
                    x=train['phone_service'], 
                    y=target)
    plt.axhline(train[target].mean(), c='r')
    plt.title(f'Phone Services\n{target.capitalize()} Barplot')
    plt.xlabel('Phone Service')
    plt.ylabel(target.capitalize())
    
    plt.subplot(122)
    sns.barplot(data=train,
                    x=train['internet_service_type'], 
                    y=target)
    plt.axhline(train[target].mean(), c='r')
    plt.title(f'Internet Service Type\n{target.capitalize()} Barplot')    
    plt.xlabel('Internet Service Type')
    plt.ylabel(target.capitalize())
    plt.tight_layout()
    plt.show()
    
    return

def chi_squared_single(train, col):
    '''
    Action:
    
    Modules: scipy.stats
    '''
    
    target = 'churn'
    α = 0.05
    observed = pd.crosstab(train[target], train[col])
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    print(f'p-value: {round(p, 4)}\nchi2: {round(chi2,4)}')
    col = col.replace('_', ' ')
    if p < α:
        print(f'There exists some relationship between {target} and {col}. \nWe \033[1mreject\033[0m the null hypothesis.')
    else:
        print(f'There is not a significant relationship between {target} and {col}. \nWe \033[1mcannot reject\033[0m the Null Hypothesis.')
    return 

def telco_internet_service_supports(train):
    '''
    This function creates a subplot of two variables of interest
    '''

    target = 'churn'
    col = 'online_security'
    col_text = string.capwords(col.replace('_',' '))
    plt.subplot(221)
    sns.barplot(data=train,
                    x=train[col], 
                    y=target)
    plt.axhline(train[target].mean(), c='r')
    plt.title(f'{col_text}\n{target.capitalize()} Barplot')
    plt.xlabel(f'{col_text}')
    plt.ylabel(target.capitalize())

    col2 = 'online_backup'
    col2_text = string.capwords(col2.replace('_',' '))
    plt.subplot(222)
    sns.barplot(data=train,
                    x=train[col2], 
                    y=target)
    plt.axhline(train[target].mean(), c='r')
    plt.title(f'{col2_text}\n{target.capitalize()} Barplot')    
    plt.xlabel(f'{col2_text}')
    plt.ylabel(target.capitalize())
    plt.tight_layout()


    col2 = 'device_protection'
    col2_text = string.capwords(col2.replace('_',' '))
    plt.subplot(223)
    sns.barplot(data=train,
                    x=train[col2], 
                    y=target)
    plt.axhline(train[target].mean(), c='r')
    plt.title(f'{col2_text}\n{target.capitalize()} Barplot')    
    plt.xlabel(f'{col2_text}')
    plt.ylabel(target.capitalize())
    plt.tight_layout()


    col2 = 'tech_support'
    col2_text = string.capwords(col2.replace('_',' '))
    plt.subplot(224)
    sns.barplot(data=train,
                    x=train[col2], 
                    y=target)
    plt.axhline(train[target].mean(), c='r')
    plt.title(f'{col2_text}\n{target.capitalize()} Barplot')    
    plt.xlabel(f'{col2_text}')
    plt.ylabel(target.capitalize())
    plt.tight_layout()
    plt.show()
    
    return


def univariate_stats(train):
    '''
    Parameters: *only* a train dataset as an argument
    Actions:
        1. Creates univariate datavisuals for all variables in the dataset
        2. Displays summary statistics for variables with more than 5 unique values
    Returns: prints summary stats and graphs to understand the data
    Modules: searborn, matplotlib.pyplot, 
    '''
    explore_col, cat_col, num_col = determine_variable_type(train)
    
    for col in explore_col:
        if col in cat_col:
            sns.countplot(data=train, x=col,)
            plt.title(f'Barplot of {col.capitalize()}')
            plt.show()
            print(f'Value Frequency of {col.capitalize()}')
            print(pd.concat([train[col].value_counts(),
            train[col].value_counts(normalize=True)],
                 axis=1))
            print('\n\n------------------------------------------------------------------------------------------\n------------------------------------------------------------------------------------------\n\n')
        elif col in num_col:
            plt.subplot(121)
            plt.hist(train[col])
            plt.title(f'Histogram of {col.capitalize()}')
            
            plt.subplot(122)
            sns.boxplot(data=train, x=col)
            plt.title(f'Boxplot of {col.capitalize()}')
            plt.show()
            
            print(f'Summary statistics of {col.capitalize()}:\n')
            print(train[col].describe())
            print('\n\n------------------------------------------------------------------------------------------\n------------------------------------------------------------------------------------------\n\n')
    return

def bivariate_stats(train, focus = 'all'):
    '''
    
    '''
    explore_col, cat_col, num_col = determine_variable_type(train)
    
    target = 'churn'
    
    if focus == 'all':
        for col in cat_col:
            if col != target:
                sns.barplot(data=train,
                            x=col, 
                            y=target)
                plt.axhline(train[target].mean(), c='r')
                plt.title(f'{target.capitalize()} by {col.capitalize()} Barplot')
                plt.show()

        for col in num_col:
            if col != target:
                plt.subplot(121)
                sns.barplot(data=train,
                           x=target,
                           y=col)
                plt.axhline(train[col].mean(), c='r')

                plt.subplot(122)
                sns.boxplot(data=train,
                           x=target,
                           y=col)
                plt.axhline(train[col].mean(), c='r')
                plt.show()
    elif focus == 'cat':
        for col in cat_col:
            if col != target:
                sns.barplot(data=train,
                            x=col, 
                            y=target)
                plt.axhline(train[target].mean(), c='r')
                plt.title(f'{target.capitalize()} by {col.capitalize()} Barplot')
                plt.show()
    elif focus == 'num':
        for col in num_col:
            if col != target:
                plt.subplot(121)
                sns.barplot(data=train,
                           x=target,
                           y=col)
                plt.axhline(train[col].mean(), c='r')

                plt.subplot(122)
                sns.boxplot(data=train,
                           x=target,
                           y=col)
                plt.axhline(train[col].mean(), c='r')
                plt.show()
    return


def chi_squared_multiple(train, ls):
    '''
    Action:
    
    Modules: scipy.stats
    '''
    
    target = 'churn'
    α = 0.05
    for col in ls:
        print(f'\n\nVariable of Interest: {col.upper()}')
        observed = pd.crosstab(train[target], train[col])
        chi2, p, degf, expected = stats.chi2_contingency(observed)
        print(f'p-value:{round(p, 4)}\nchi2: {round(chi2,4)}')
        col = col.replace('_', ' ')
        if p < α:
            print(f'There exists some relationship between {target} and the {col}. \nWe \033[1mreject\033[0m the null hypothesis.')
        else:
            print(f'There is not a significant relationship between {target} and {col}. \nWe \033[1mcannot reject\033[0m the Null Hypothesis.')
    return

def telco_streaming_services(train):
    '''
    This function creates a subplot of two variables of interest
    '''
    import string

    target = 'churn'
    col = 'streaming_movies'
    col_text = string.capwords(col.replace('_',' '))
    plt.subplot(121)
    sns.barplot(data=train,
                    x=train[col], 
                    y=target)
    plt.axhline(train[target].mean(), c='r')
    plt.title(f'{col_text}\n{target.capitalize()} Barplot')
    plt.xlabel(f'{col_text}')
    plt.ylabel(target.capitalize())

    col2 = 'streaming_tv'
    col2_text = string.capwords(col2.replace('_',' '))
    plt.subplot(122)
    sns.barplot(data=train,
                    x=train[col2], 
                    y=target)
    plt.axhline(train[target].mean(), c='r')
    plt.title(f'{col2_text}\n{target.capitalize()} Barplot')    
    plt.xlabel(f'{col2_text}')
    plt.ylabel(target.capitalize())
    plt.tight_layout()

    plt.tight_layout()
    plt.show()
    
    return
