import numpy as np

def portfolio_return(yrs,avg_return,volatility,principal):
    np.random.seed(123)
    rates = np.random.normal(loc=avg_return, scale=volatility, size=yrs)
    # Calculate the return at the end of the period
    end_return = principal
    for x in rates:
        end_return = end_return * (1 + x)
    return end_return

result = portfolio_return(yrs = 5, avg_return = 0.07, volatility = 0.15, principal = 1000)
print("Portfolio return after 5 years = {}".format(result))

# Run 1,000 iterations and store the results
sims, rets = 1000, []

for i in range(sims):
    rets.append(portfolio_return(yrs = 10, avg_return = 0.07,
                                 volatility = 0.3, principal = 10000))

# Calculate the 95% CI
lower_ci = np.percentile(rets,2.5)
upper_ci = np.percentile(rets,97.5)
print("95% CI of Returns: Lower = {}, Upper = {}".format(lower_ci, upper_ci))