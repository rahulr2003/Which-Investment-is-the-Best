
'''
Each folder of data consists of companies in the same industry.

The key-ratios which have been scraped from macrotrends.net are :

            - Day Sales in Recievables
            - Return on Equity (ROE)
            - Return on Assets (ROA)
            - Return on Investments (ROI)
            - Book Value per Share (BVPS)
            - Operating Cash Flow Per Share (OCFPS)
            - Free Cash Flow Per Share (FCFPS)

There are two files attributed to each company
            - Annual Data
            - Quarterly Data

'''


# Goal : Determine the best share to invest in (as of 2021 Q1)

'''
Test Command

generate_data_plot('Tech','AAPL','apple','Annual','Days Sales In Receivables')

'''

import csv
import matplotlib.pyplot as plt

def get_data(Type,company_code,company_name,frequency,field_name):

    filename = f'{Type}/{company_code}_{company_name}_{frequency}.csv'

    whole_data = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            whole_data.append(row)
    
    for i in whole_data:
        if i[0] == str(field_name):
            required_data_list = i
    
    return required_data_list
    csvfile.close()

def get_dates_list(frequency):
    filename = f'Tech/AAPL_apple_{frequency}.csv'

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        data = []

        for row in csvreader:
            data.append(row)

        dates_list = data[0][1:]

        return dates_list
            
    
def row_reversal(oned_list):

    length = len(oned_list)

    reversed_list = []

    for i in range(length,0,-1):
        reversed_list.append(oned_list[i-1])

    return reversed_list
    

def generate_data_plot(Type,companies_codes,companies_names,frequency,field_name):
    combinations = []

    for i in range(len(companies_codes)):
        combinations.append([companies_codes[i],companies_names[i]])

    data_lists = []
    
    for i in combinations:
        data_lists.append(get_data(Type,i[0],i[1],frequency,field_name)[1:])

    cols = len(data_lists[0])

    rows = len(data_lists)

    plotting_data = data_lists

    for i in range(rows):
        for j in range(cols):
            plotting_data[i][j] = float(data_lists[i][j])
    
    dates = get_dates_list(frequency)

    print(len(dates))
    
    if frequency == 'Annual':
        for i in plotting_data:
            if len(i) != 16:
                
                    
        for i in range(3,5):
            plotting_data[i] = plotting_data[i][:-1]
    elif frequency == 'Quarterly':
        for i in range(5,8):
            plotting_data[i] = plotting_data[i][:-1]
    
    data_for_plotting = []

    for i in plotting_data:
        data_for_plotting.append(row_reversal(i))

    print(len(data_for_plotting[0]))

    for i in plotting_data:
        print(len(i))
    '''
    num_companies = len(combinations)
    
    for i in range(num_companies):
        plt.plot(dates,data_for_plotting[i], label = str(combinations[i][0]))
    
    plt.xlabel('Dates')
    plt.ylabel(str(field_name))
    plt.title(f'{field_name} values for tech firms')
    plt.legend()
    plt.show()
    '''

  
    
    






