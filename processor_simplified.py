
import processor_backend


#Software Firms

tech_firms_codes = ['AAPL','MSFT','GOOG','NTAP','ORCL','ADBE']
tech_firms_names = ['apple','microsoft','alphabet','netapp','oracle','adobe']

processor_backend.generate_data_plot('Tech',tech_firms_codes,tech_firms_names,'Quarterly','Days Sales In Receivables')


'''
#Investment Banks

investment_banks_codes = ['JPM','SCHW','C','GS','MS']
investment_banks_names = ['jpmorgan-chase','charles-schwab','citigroup','goldman-sachs','morgan-stanley']

processor_backend.generate_data_plot('Investment Banks',investment_banks_codes,investment_banks_names,'Annual','Days Sales In Receivables')

'''

