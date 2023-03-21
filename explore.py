import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import string


def telco_churn_pie(train):
    '''
    Arguments: telco train dataset
    Actions:
        1. Creates pie chart with 'churn' as the focus
    Modules: matplotlib.pyplot as plt
    '''

    # create pie chart with labels and % 
    plt.pie(train['churn'].value_counts(), labels=["No", "Yes"], autopct='%.0f%%', explode=[0, 0.1])

    # give pie chart a title
    plt.title('Telco Churn Rate')

    # put a legend 
    plt.legend()

    # shows all graph features and graph
    plt.show()

    # exit the function
    return

def telco_core_services(train):
    '''
    Argument: telco train data
    Actions:
        1. Creates 2 sublots that show phone service and internet service types churn rate
    Modules: matplotlib.pyplot as plt, seaborn as sns
    '''

    # initialize target (y axis)
    target = 'churn'

    # assign subplot position
    plt.subplot(121)

    # creates bar plot with train data
    sns.barplot(data=train,

                    # x-axis represents phone_service 
                    x=train['phone_service'],

                    # y-axis represents rate of churn
                    y=target)

    # a red horizontal line that represents the mean churn rate
    plt.axhline(train[target].mean(), c='r')

    # Insert the title
    plt.title(f'Phone Services\n{target.capitalize()} Barplot')

    # label the x-axis
    plt.xlabel('Phone Service')

    # label the y axis
    plt.ylabel(target.capitalize())
    

    # assign subplot positions
    plt.subplot(122)

    # creates bar plot with train data
    sns.barplot(data=train,

                    # x-axis represents phone_service 
                    x=train['internet_service_type'],

                    # y-axis represents rate of churn
                    y=target)

    # a red horizontal line that represents the mean churn rate
    plt.axhline(train[target].mean(), c='r')

    # insert the title
    plt.title(f'Internet Service Type\n{target.capitalize()} Barplot')

    # label the x-axis
    plt.xlabel('Internet Service Type')

    # label the y axis
    plt.ylabel(target.capitalize())

    # formats subplots to be more appealing and not overlap as much
    plt.tight_layout()

    # shows all graphs and graph details
    plt.show()

    # exits function
    return

def chi_squared_single(train, col):
    '''
    Arguments: train data, a single column name
    Actions:
        1. Sts target to churn
        2. Sets alphas to 0.05
        3. Gets crosstab of churn and column argument
        4. Runs chi^2 contingency table
        5. Prints p-value and chi^2
        6. Prints statemnt of relationship depending on the p-value 
    Modules: scipy.stats as stats, pandas as pd
    '''

    # initialize variables
    target = 'churn'

    # set alpha
    α = 0.05

    # bind cross tab results to observed  
    observed = pd.crosstab(train[target], train[col])

    # conducts contingency test and assigns outputs to respective variables
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    # prints the p-value and chi2
    print(f'p-value: {round(p, 4)}\nchi2: {round(chi2,4)}')

    # replaces underscore with a space for use in print statements
    col = col.replace('_', ' ')

    # if the p-valyeus is less than the alpha
    if p < α:

        # prints statements of relationship
        print(f'There exists some relationship between {target} and {col}. \nWe \033[1mreject\033[0m the null hypothesis.')

    # if p-value grater than alpha
    else:

        # print statement of insignificant relationship
        print(f'There is not a significant relationship between {target} and {col}. \nWe \033[1mcannot reject\033[0m the Null Hypothesis.')

    # exit function
    return


def telco_internet_service_supports(train):
    '''
    Arguments: telco train dataset
    Actions:
        1. Creates 4 subplots for online_security, online_backup, device_protection, tech_support
        2. Subplots relflect each values churn rate
        3. Subployts have horizontal line representing overall churn rate
    Modules: string, seaborn as sns, matplotlib.pyplot as plt, pandas as pd
    '''
    
    # intiialize target variable as churn
    target = 'churn'
    
    # initializing variable for x axis
    col = 'online_security'
    
    # creatins title/label friendly column by replacing the underscore and capitalizing all first letters
    col_text = string.capwords(col.replace('_',' '))
    
    # assigning subplot position
    plt.subplot(221)
    
    # creatins a barplot with train data
    sns.barplot(data=train,
                    
                    # setting x axis to the variable previously initialized
                    x=train[col], 
                
                    # setting y axis to the target
                    y=target)
    
    # setting the overall average churn rate as a horizontal line in the graphs
    plt.axhline(train[target].mean(), c='r')
    
    # inserting the title
    plt.title(f'{col_text}\n{target.capitalize()} Barplot')
    
    # labeling the x axis
    plt.xlabel(f'{col_text}')
    
    # labeling the y axis
    plt.ylabel(target.capitalize())
    

    # initializing variable for x axis
    col2 = 'online_backup'
    # exit function
    
    # creatins title/label friendly column by replacing the underscore and capitalizing all first letters
    col2_text = string.capwords(col2.replace('_',' '))
    
    # assigning subplot position
    plt.subplot(222)
    
    # creatins a barplot with train data
    sns.barplot(data=train,
                    
                    # setting x axis to the variable previously initialized
                    x=train[col2], 
                
                    # setting y axis to the target
                    y=target)
    
    # setting the overall average churn rate as a horizontal line in the graphs
    plt.axhline(train[target].mean(), c='r')
    
    # inserting the title
    plt.title(f'{col2_text}\n{target.capitalize()} Barplot')    
    
    # labeling the x axis
    plt.xlabel(f'{col2_text}')
    
    # labeling the y axis
    plt.ylabel(target.capitalize())
    
    # formating the subplots to reduce overlap
    plt.tight_layout()
    

    # initializing variable for x axis
    col2 = 'device_protection'
    
    # creatins title/label friendly column by replacing the underscore and capitalizing all first letters
    col2_text = string.capwords(col2.replace('_',' '))
    
    # assigning subplot position
    plt.subplot(223)
    
    # creatins a barplot with train data
    sns.barplot(data=train,
                    
                    # setting x axis to the variable previously initialized
                    x=train[col2], 
                
                    # setting y axis to the target
                    y=target)
    
    # setting the overall average churn rate as a horizontal line in the graphs
    plt.axhline(train[target].mean(), c='r')
    
    # inserting the title
    plt.title(f'{col2_text}\n{target.capitalize()} Barplot')    
    
    # labeling the x axis
    plt.xlabel(f'{col2_text}')
    
    # labeling the y axis
    plt.ylabel(target.capitalize())
    
    # formating the subplots to reduce overlap
    plt.tight_layout()


    # initializing variable for x axis
    col2 = 'tech_support'
    
    # creatins title/label friendly column by replacing the underscore and capitalizing all first letters
    col2_text = string.capwords(col2.replace('_',' '))
    
    # assigning subplot position
    plt.subplot(224)
    
    # creatins a barplot with train data
    sns.barplot(data=train,
                    
                    # setting x axis to the variable previously initialized
                    x=train[col2], 
                
                    # setting y axis to the target
                    y=target)
    
    # setting the overall average churn rate as a horizontal line in the graphs
    plt.axhline(train[target].mean(), c='r')
    
    # inserting the title
    plt.title(f'{col2_text}\n{target.capitalize()} Barplot')    
    
    # labeling the x axis
    plt.xlabel(f'{col2_text}')
    
    # labeling the y axis
    plt.ylabel(target.capitalize())
    
    # formating the subplots to reduce overlap
    plt.tight_layout()
    
    # showing all the subplots together
    plt.show()
    
    # exit function
    return

def chi_squared_multiple(train, ls):
    '''
    Arguments: telco train dataset, list of columns to evaluate with a chi-squared test
    Action:
        1. Assings target as churn
        2. Sets alpha to 0.05
        3. Loops through each column in the list argyment
        4. Conducts chi^2 tests on each col with target
        5. Prints statement about relationship significance depending on p-value
    Modules: scipy.stats
    '''

    # Initialize target as churn
    target = 'churn'

    # set alhpa
    α = 0.05

    # for each columns in the list argumnet
    for col in ls:

        # print the column name in upper case
        print(f'\n\nVariable of Interest: {col.upper()}')

        # create crosstab of each column and the target values and assigned to variable observed
        observed = pd.crosstab(train[target], train[col])

        # conducted chi^2 continengcy test on observed and place results in respective variables
        chi2, p, degf, expected = stats.chi2_contingency(observed)

        # print the p-value and chi^2 
        print(f'p-value:{round(p, 4)}\nchi2: {round(chi2,4)}')

        # replace underscores with space for reader friendliness
        col = col.replace('_', ' ')

        # if the p-value is less than alpha
        if p < α:

            # prints stsatemtn about significant relationships
            print(f'There exists some relationship between {target} and the {col}. \nWe \033[1mreject\033[0m the null hypothesis.')

        # if p is greater than alpha
        else:

            # print about insignificant relationship
            print(f'There is not a significant relationship between {target} and {col}. \nWe \033[1mcannot reject\033[0m the Null Hypothesis.')

    # exit function 
    return

def telco_streaming_services(train):
    '''
    This function creates a subplot of two variables of interest
    Modules: string, matplotlib.pyplot as plt, seaborn as sns, pandas as pd
    '''
    
    target = 'churn'
    
    # initializing variable for x axis
    col = 'streaming_movies'
    
    # creating title/label friendly column by replacing the underscore and capitalizing all first letters
    col_text = string.capwords(col.replace('_',' '))
    
    # assigning subplot position
    plt.subplot(121)
    
    # creating a barplot with train data
    sns.barplot(data=train,
                
                    # setting x axis to the variable previously initialized
                    x=train[col], 
                    
                    # setting y axis to the target
                    y=target)
    
    # setting the overall average churn rate as a horizontal line in the graphs
    plt.axhline(train[target].mean(), c='r')
    
    # inserting the title
    plt.title(f'{col_text}\n{target.capitalize()} Barplot')
    
    # labeling the x axis
    plt.xlabel(f'{col_text}')
    
    # labeling the y axis
    plt.ylabel(target.capitalize())
    
    # initializing variable for x axis
    col2 = 'streaming_tv'
    
    # creating title/label friendly column by replacing the underscore and capitalizing all first letters
    col2_text = string.capwords(col2.replace('_',' '))
    
    # assigning subplot position
    plt.subplot(122)
    
    # creating a barplot with train data
    sns.barplot(data=train,
                
                    # setting x axis to the variable previously initialized
                    x=train[col2], 
                    
                    # setting y axis to the target
                    y=target)
    
    # setting the overall average churn rate as a horizontal line in the graphs
    plt.axhline(train[target].mean(), c='r')
    
    # inserting the title
    plt.title(f'{col2_text}\n{target.capitalize()} Barplot')    
    
     # labeling the x axis
    plt.xlabel(f'{col_text}')
    
    # labeling the y axis
    plt.ylabel(target.capitalize())
    
    # formating the subplots to reduce overlap
    plt.tight_layout()

    # showing all plaots
    plt.show()
    
    # exit function
    return

