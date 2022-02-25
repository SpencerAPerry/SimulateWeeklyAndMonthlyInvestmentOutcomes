# Import the necessary libraries
from datetime import datetime
import random
import pandas as pd

# Set up the normal compound interest function
def compound_interest(principal: int, rate: float, years: int, annualCompoundRate: int = 1) -> float:
    return round(principal*(1 + (rate/annualCompoundRate))**(annualCompoundRate*years), 2)

# Definte the investment_forcasting function.
def investment_simulating_annual(principal: int, years: int, weeklyInvestmentHypotheticals: list, annualIncreaseRateHypotheticals: list, lowRate: int, highRate: int, startYear = datetime.now().year, annualCompoundRate: int = 1):
    """
    principal                       = Initial investment or amount already invested in the stock market
    years                           = The number of years you want to forcast forward from the start_year
    weeklyInvestmentHypotheticals   = A list of how much you could invest each week of a year.
    annualIncreaseRateHypotheticals = A list of rates describing how much more you plan to invest each year (0.05 = 5% more per year).
    lowRate                        = The lowest annual rate of return you want to simulate. Ex: 4, 3, 5.5, etc.
    highRate                       = The highest annual rate of return you want to simulate. Ex: 6, 8, 5.5, etc.
    startYear                      = The starting year of the simulation. Defaults to the current year.
    annualCompoundRate              = How many times per year do you want the interest to compound in your simulation? Defaults to 1 per year.
    """
    # Set up some useful dictionaries and a master df
    df = pd.DataFrame([])
    total_invested_dictionary = {}
    annual_add_dictionary = {}
    principal_dictionary = {}

    # Iterate through hypothetical annual investment increases and weekly investment starts
    # To set up nested dictionaries for each case.
    for annual_increase_rate in annualIncreaseRateHypotheticals:
        total_invested_dictionary[annual_increase_rate] = {}
        annual_add_dictionary[annual_increase_rate] = {}
        principal_dictionary[annual_increase_rate] = {}
        for weekly_investment_made in weeklyInvestmentHypotheticals:
            total_invested_dictionary[annual_increase_rate][weekly_investment_made] = principal
            annual_add_dictionary[annual_increase_rate][weekly_investment_made] = 52 * weekly_investment_made
            principal_dictionary[annual_increase_rate][weekly_investment_made] = principal
    # Iterate through years, then through annual investment increases, then through weekly investment starts
    for year in range(years):
        # Use a standard interest rate for each year
        annual_percent = float(random.randint(round(lowRate * 10), round(highRate * 10)))/1000
        for annual_increase in annualIncreaseRateHypotheticals:
            for weekly_add in weeklyInvestmentHypotheticals:
                # Reset the dictionary with each year/increase/investment combo
                annual_df = {}
                # Add interest to last year's principal
                principal_dictionary[annual_increase][weekly_add] = compound_interest(principal_dictionary.get(annual_increase).get(weekly_add), annual_percent, years = 1, annualCompoundRate = annualCompoundRate)
                # After year 1, add the annual increase to weekly investment
                if year > 0:
                    annual_add_dictionary[annual_increase][weekly_add] = round(annual_add_dictionary.get(annual_increase).get(weekly_add) + (annual_increase * annual_add_dictionary.get(annual_increase).get(weekly_add)), 2)
                else:
                    annual_add_dictionary[annual_increase][weekly_add] = round(annual_add_dictionary.get(annual_increase).get(weekly_add), 2)
                # Add this year's investment to the running total investment dictionary
                total_invested_dictionary[annual_increase][weekly_add] = total_invested_dictionary.get(annual_increase).get(weekly_add) + annual_add_dictionary.get(annual_increase).get(weekly_add)
                # How much money is in our portfolio at the end of the year?
                principal_dictionary[annual_increase][weekly_add] = principal_dictionary.get(annual_increase).get(weekly_add) + annual_add_dictionary.get(annual_increase).get(weekly_add)
                #print(f'Year: {year + start_year}; Value: {principal_dictionary.get(annual_increase).get(weekly_add)}; Annual Add: {annual_add_dictionary.get(annual_increase).get(weekly_add)}, Annual %: {annual_percent}')

                annual_df['year'] = year + startYear
                annual_df['annual_percent_interest'] = annual_percent
                annual_df['initial_weekly_investment'] = weekly_add
                annual_df['rate_of_annual_investment_increase'] = annual_increase
                annual_df['annual_investment'] = annual_add_dictionary.get(annual_increase).get(weekly_add)
                annual_df['end_of_year_total'] = principal_dictionary.get(annual_increase).get(weekly_add)
                df = pd.concat([df, pd.DataFrame([annual_df])], ignore_index = True)

    #print(f'Total Invested: {total_invested_dictionary}')

    return df

# Definte the investment_forcasting function.
def investment_simulating_monthly(principal: int, years: int, monthlyInvestmentHypotheticals: list, investmentIncreaseRateHypotheticals: list, lowRate: int, highRate: int, startYear = datetime.now().year, annualCompoundRate: int = 1):
    """
    principal                       = Initial investment or amount already invested in the stock market
    years                           = The number of years you want to forcast forward from the start_year
    monthlyInvestmentHypotheticals   = A list of how much you could invest each week of a year.
    annualIncreaseRateHypotheticals = A list of rates describing how much more you plan to invest each year (0.05 = 5% more per year).
    lowRate                        = The lowest annual rate of return you want to simulate. Ex: 4, 3, 5.5, etc.
    highRate                       = The highest annual rate of return you want to simulate. Ex: 6, 8, 5.5, etc.
    startYear                      = The starting year of the simulation. Defaults to the current year.
    annualCompoundRate              = How many times per year do you want the interest to compound in your simulation? Defaults to 1 per year.
    """
    # Set up some useful dictionaries and a master df
    df = pd.DataFrame([])
    total_invested_dictionary = {}
    monthly_add_dictionary = {}
    principal_dictionary = {}

    # Iterate through hypothetical annual investment increases and weekly investment starts
    # To set up nested dictionaries for each case.
    for monthly_investment_increase_rate in investmentIncreaseRateHypotheticals:
        total_invested_dictionary[monthly_investment_increase_rate] = {}
        monthly_add_dictionary[monthly_investment_increase_rate] = {}
        principal_dictionary[monthly_investment_increase_rate] = {}
        for monthly_investment_made in monthlyInvestmentHypotheticals:
            total_invested_dictionary[monthly_investment_increase_rate][monthly_investment_made] = principal
            monthly_add_dictionary[monthly_investment_increase_rate][monthly_investment_made] = monthly_investment_made
            principal_dictionary[monthly_investment_increase_rate][monthly_investment_made] = principal
    # Iterate through years, then through annual investment increases, then through weekly investment starts
    for year in range(years):
        for month in range(1, 13):
            # Use a standard interest rate for each month
            monthly_percent = float(random.randint(round(lowRate * 1000), round(highRate * 1000)))/1000
            for monthly_investment_increase_rate in investmentIncreaseRateHypotheticals:
                for monthly_add in monthlyInvestmentHypotheticals:
                    # Reset the dictionary with each month/increase/investment combo
                    monthly_df = {}
                    # Add interest to last year's principal
                    principal_dictionary[monthly_investment_increase_rate][monthly_add] = compound_interest(principal_dictionary.get(monthly_investment_increase_rate).get(monthly_add), monthly_percent, years = 1, annualCompoundRate = annualCompoundRate)
                    # After year 1, add the annual increase to weekly investment
                    if year > 0 or month > 1:
                        monthly_add_dictionary[monthly_investment_increase_rate][monthly_add] = round(monthly_add_dictionary.get(monthly_investment_increase_rate).get(monthly_add) + (monthly_investment_increase_rate * monthly_add_dictionary.get(monthly_investment_increase_rate).get(monthly_add)), 2)
                    else:
                        monthly_add_dictionary[monthly_investment_increase_rate][monthly_add] = round(monthly_add_dictionary.get(monthly_investment_increase_rate).get(monthly_add), 2)
                    # Add this year's investment to the running total investment dictionary
                    total_invested_dictionary[monthly_investment_increase_rate][monthly_add] = total_invested_dictionary.get(monthly_investment_increase_rate).get(monthly_add) + monthly_add_dictionary.get(monthly_investment_increase_rate).get(monthly_add)
                    # How much money is in our portfolio at the end of the month?
                    principal_dictionary[monthly_investment_increase_rate][monthly_add] = principal_dictionary.get(monthly_investment_increase_rate).get(monthly_add) + monthly_add_dictionary.get(monthly_investment_increase_rate).get(monthly_add)
                    #print(f'Year: {year + start_year}; Value: {principal_dictionary.get(annual_increase).get(monthly_add)}; Annual Add: {annual_add_dictionary.get(annual_increase).get(monthly_add)}, Annual %: {annual_percent}')

                    monthly_df['year'] = year + startYear
                    monthly_df['month'] = month
                    monthly_df['date'] = datetime(year + startYear, month, 1)
                    monthly_df['monthly_percent_interest'] = monthly_percent
                    monthly_df['initial_monthly_investment'] = monthly_add
                    monthly_df['monthly_investment_increase_rate'] = monthly_investment_increase_rate
                    monthly_df['monthly_investment'] = monthly_add_dictionary.get(monthly_investment_increase_rate).get(monthly_add)
                    monthly_df['end_of_month_total'] = principal_dictionary.get(monthly_investment_increase_rate).get(monthly_add)
                    df = pd.concat([df, pd.DataFrame([monthly_df])], ignore_index = True)

    return df