# Import pandas
import pandas as pd

# Load the customer_data
customer_data = pd.read_csv('data')

# Load the app_purchases
app_purchases = pd.read_csv('pdata')

# Print the columns of customer data
print(customer_data.columns)

# Print the columns of app_purchases
print(app_purchases.columns)

# Merge on the 'uid' field
uid_combined_data = app_purchases.merge(customer_data, on=['uid'], how='inner')

# Examine the results
print(uid_combined_data.head())
print(len(uid_combined_data))

purchase_summary = purchase_data.agg({'price': ['mean', 'median'], 'age': ['mean', 'median']})

# Group the data
grouped_purchase_data = purchase_data.groupby(by = ['device', 'gender'])

# Aggregate the data
purchase_summary = grouped_purchase_data.agg({'price': ['mean', 'median', 'std']})

# Examine the results
print(purchase_summary)

# Compute max_purchase_date
max_purchase_date = current_date - timedelta(days=28)

# Filter to only include users who registered before our max date
purchase_data_filt = purchase_data[purchase_data.reg_date < max_purchase_date]

# Filter to contain only purchases within the first 28 days of registration
purchase_data_filt = purchase_data_filt[(purchase_data_filt.date <=
                        purchase_data_filt.reg_date + timedelta(days=28))]

# Output the mean price paid per purchase
print(purchase_data_filt.price.agg('mean'))
# Set the max registration date to be one month before today
max_reg_date = current_date - timedelta(days=28)

# Find the month 1 values
month1 = np.where((purchase_data.reg_date < max_reg_date) &
                 (purchase_data.date <= purchase_data.reg_date + timedelta(days=28)),
                 purchase_data.price, np.NaN)

# Update the value in the DataFrame
purchase_data['month1'] = month1

# Group the data by gender and device
purchase_data_upd = purchase_data.groupby(by=['gender', 'device'], as_index=False)

# Aggregate the month1 and price data
purchase_summary = purchase_data_upd.agg(
                        {'month1': ['mean', 'median'],
                        'price': ['mean', 'median']})

# Examine the results
print(purchase_summary)

# Group the data and aggregate first_week_purchases
user_purchases = user_purchases.groupby(by=['reg_date', 'uid']).agg({'first_week_purchases': ['sum']})

# Reset the indexes
user_purchases.columns = user_purchases.columns.droplevel(level=1)
user_purchases.reset_index(inplace=True)

# Find the average amount purchased per user per day
user_purchases = user_purchases.groupby(by=['reg_date']).agg({'first_week_purchases': ['mean']})
user_purchases.columns = user_purchases.columns.droplevel(level=1)
user_purchases.reset_index(inplace=True)

# Plot the results
user_purchases.plot(x='reg_date', y='first_week_purchases')
plt.show()

# Pivot the data
country_pivot = pd.pivot_table(user_purchases_country, values=['first_week_purchases'], columns=['country'], index=['reg_date'])
print(country_pivot.head())

# Compute 7_day_rev
daily_revenue['7_day_rev'] = daily_revenue.revenue.rolling(window=7, center=False).mean()

# Compute 28_day_rev
daily_revenue['28_day_rev'] = daily_revenue.revenue.rolling(window=28, center=False).mean()

# Compute 365_day_rev
daily_revenue['365_day_rev'] = daily_revenue.revenue.rolling(window=365, center=False).mean()

# Plot date, and revenue, along with the 3 rolling functions (in order)
daily_revenue.plot(x='date', y=['revenue', '7_day_rev', '28_day_rev', '365_day_rev', ])
plt.show()

# Pivot user_revenue
pivoted_data = pd.pivot_table(user_revenue, values ='revenue', columns=['device', 'gender'], index='month')
pivoted_data = pivoted_data[1:(len(pivoted_data) -1 )]

# Create and show the plot
pivoted_data.plot()
plt.show()

# Merge and group the datasets
purchase_data = demographics_data.merge(paywall_views,  how='inner', on=['uid'])
purchase_data.date = purchase_data.date.dt.floor('d')

# Group and aggregate our combined dataset
daily_purchase_data = purchase_data.groupby(by=['date'], as_index=False)
daily_purchase_data = daily_purchase_data.agg({'purchase': ['sum', 'count']})

# Find the mean of each field and then multiply by 1000 to scale the result
daily_purchases = daily_purchase_data.purchase['sum'].mean()
daily_paywall_views = daily_purchase_data.purchase['count'].mean()
daily_purchases = daily_purchases * 1000
daily_paywall_views = daily_paywall_views * 1000

print(daily_purchases)
print(daily_paywall_views)

#SENSITIVITY TEST

large_sensitivity = 0.5

# Find the conversion rate lift with the sensitivity above
large_conversion_rate = conversion_rate * (1 + large_sensitivity)

# Find how many more users per day that translates to
large_purchasers = daily_paywall_views * large_conversion_rate
purchaser_lift = large_purchasers - daily_purchases

print(large_conversion_rate)
print(large_purchasers)
print(purchaser_lift)

# Find the number of paywall views
n = purchase_data.purchase.count()

# Calculate the quantitiy "v"
v =  conversion_rate * (1 - conversion_rate)

# Calculate the variance and standard error of the estimate
var = v / n
se = var**0.5

print(var)
print(se)

# Look at the impact of sample size increase on power
n_param_one = get_power(n=1000, p1=p1, p2=p2, cl=cl)
n_param_two = get_power(n=2000, p1=p1, p2=p2, cl=cl)

# Look at the impact of confidence level increase on power
alpha_param_one = get_power(n=n1, p1=p1, p2=p2, cl=0.8)
alpha_param_two = get_power(n=n1, p1=p1, p2=p2, cl=0.95)

# Compare the ratios
print(n_param_two / n_param_one)
print(alpha_param_one / alpha_param_two)

# Merge the demographics and purchase data to only include paywall views
purchase_data = demographics_data.merge(paywall_views, how='inner', on=['uid'])

# Find the conversion rate
conversion_rate = (sum(purchase_data.purchase) / purchase_data.purchase.count())

# Desired Power: 0.95
# CL 0.90
# Percent Lift: 0.1
p2 = conversion_rate * (1 + 0.1)
sample_size = get_sample_size(power=0.95, p1=conversion_rate, p2=p2, cl=0.90)
print(sample_size)

# Compute and print the results
results = ab_test_results.groupby('group').agg({'uid':pd.Series.nunique})
print(results)
# Find the overall number of unique users using "len" and "unique"
unique_users = len(ab_test_results.uid.unique())

# Find the percentage in each group
results = results / unique_users * 100
print(results)
# Find the unique users in each group, by device and gender
results = ab_test_results.groupby(by=['group', 'device', 'gender']).agg({'uid': pd.Series.nunique})

# Find the overall number of unique users using "len" and "unique"
unique_users = len(ab_test_results.uid.unique())

# Find the percentage in each group
results = results / unique_users * 100
print(results)
