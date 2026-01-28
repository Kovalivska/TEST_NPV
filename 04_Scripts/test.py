import numpy
import pandas

############ SECTION 1 #############
df = pandas.read_excel('opportunities.xlsx')

# COMPLETE TASK 1 HERE:
# Extract each column from the dataset into separate arrays
ids = df['ID'].values
products = df['ProductName'].values
customers = df['CustomerName'].values
acvs = df['ACV'].values
statuses = df['Status'].values
closedates = df['CloseDate'].values
startdates = df['StartDate'].values

print("SECTION 1 RESULTS:")
print(f"IDs array: {len(ids)} entries")
print(f"Products array: {len(products)} entries") 
print(f"Customers array: {len(customers)} entries")
print(f"ACVs array: {len(acvs)} entries")
print(f"Statuses array: {len(statuses)} entries")
print(f"Close dates array: {len(closedates)} entries")
print(f"Start dates array: {len(startdates)} entries")
print("All columns successfully extracted into separate arrays.\n")




############ SECTION 2 #############
# COMPLETE TASK 2 HERE
# Find opportunities that are still open but have CloseDate in 2025
# These need to be updated as they should have been closed by now
print("SECTION 2 RESULTS:")
print("Overdue open deals (CloseDate in 2025 but still Open):")
open_deals_2025 = []
for i in range(len(df)):
    # Convert numpy datetime64 to pandas datetime to access year attribute
    close_year = pandas.to_datetime(closedates[i]).year
    if statuses[i] == 'Open' and close_year == 2025:
        open_deals_2025.append(ids[i])
        print(ids[i])

print(f"\nSECTION 2 ANALYSIS RESULTS:")
print(f"Found {len(open_deals_2025)} opportunities that are still open but should have been closed in 2025.")
print(f"These deals require status updates as they are overdue for closure.")

####################################
############ SECTION 3 #############
####################################

print("\nSECTION 3 RESULTS:")
# COMPLETE TASK 3 HERE:
# Calculate total ACV of all Won deals that start in 2026
won_acv_2026 = 0
for i in range(len(df)):
    # Check if deal is Won and starts in 2026
    start_year = pandas.to_datetime(startdates[i]).year
    if statuses[i] == 'Won' and start_year == 2026:
        won_acv_2026 += acvs[i]
        
print(won_acv_2026)

print(f"\nSECTION 3 ANALYSIS RESULTS:")
print(f"Total ACV of all Won deals starting in 2026: ${won_acv_2026:,.0f}")
print(f"This represents confirmed revenue from successfully closed deals for 2026.")

####################################
############ SECTION 4 #############
####################################

# COMPLETE TASK 4 HERE:
# Calculate expected ACV for March 2026 with 25% success rate for open deals
total_expected_acv_032026 = 0
won_deals_march = 0
open_deals_march = 0

# Add all Won deals that start in March 2026 (100% probability)
for i in range(len(df)):
    start_dt = pandas.to_datetime(startdates[i])
    if statuses[i] == 'Won' and start_dt.year == 2026 and start_dt.month == 3:
        total_expected_acv_032026 += acvs[i]
        won_deals_march += 1

# Add expected value from Open deals that start in March 2026 (25% probability)
for i in range(len(df)):
    start_dt = pandas.to_datetime(startdates[i])
    if statuses[i] == 'Open' and start_dt.year == 2026 and start_dt.month == 3:
        total_expected_acv_032026 += acvs[i] * 0.25
        open_deals_march += 1

print(total_expected_acv_032026)

print(f"\nSECTION 4 ANALYSIS RESULTS:")
print(f"Expected ACV for March 2026: ${total_expected_acv_032026:,.0f}")
print(f"This includes {won_deals_march} confirmed Won deals + {open_deals_march} Open deals with 25% success probability.")
print(f"Risk-adjusted forecast combining guaranteed and potential revenue for March 2026.")

####################################
############ SECTION 5 #############
####################################

# COMPLETE TASK 5 HERE:
# Calculate monthly win rate throughout 2025 to assess sales department performance
# This metric shows how the ability to close deals changed over time

# Create a dictionary to store monthly performance
monthly_performance = {}

for i in range(len(df)):
    # Only consider deals that were actually closed in 2025 (Won or Lost)
    close_dt = pandas.to_datetime(closedates[i])
    if close_dt.year == 2025 and statuses[i] in ['Won', 'Lost']:
        month = close_dt.month
        
        if month not in monthly_performance:
            monthly_performance[month] = {'won': 0, 'total': 0}
        
        monthly_performance[month]['total'] += 1
        if statuses[i] == 'Won':
            monthly_performance[month]['won'] += 1

# Calculate and print monthly win rates
print("Monthly Win Rates for 2025:")
for month in sorted(monthly_performance.keys()):
    win_rate = (monthly_performance[month]['won'] / monthly_performance[month]['total']) * 100
    print(f"Month {month:2d}: {win_rate:5.1f}% ({monthly_performance[month]['won']}/{monthly_performance[month]['total']})")

# Calculate overall trend
months = sorted(monthly_performance.keys())
win_rates = [(monthly_performance[month]['won'] / monthly_performance[month]['total']) * 100 
             for month in months]

# Simple trend analysis: compare first half vs second half of year
first_half = [rate for month, rate in zip(months, win_rates) if month <= 6]
second_half = [rate for month, rate in zip(months, win_rates) if month > 6]

if first_half and second_half:
    avg_first_half = sum(first_half) / len(first_half)
    avg_second_half = sum(second_half) / len(second_half)
    trend = avg_second_half - avg_first_half
    
    print(f"\nTrend Analysis:")
    print(f"First half 2025: {avg_first_half:.1f}%")
    print(f"Second half 2025: {avg_second_half:.1f}%")
    print(f"Trend: {trend:+.1f} percentage points")

print(f"\nSECTION 5 ANALYSIS RESULTS:")
print(f"SALES DEPARTMENT PERFORMANCE ANALYSIS FOR 2025")
print(f"="*50)
print(f"Key Findings:")
best_month = max(monthly_performance.keys(), key=lambda x: (monthly_performance[x]['won']/monthly_performance[x]['total']))
worst_month = min(monthly_performance.keys(), key=lambda x: (monthly_performance[x]['won']/monthly_performance[x]['total']))
best_rate = (monthly_performance[best_month]['won']/monthly_performance[best_month]['total']) * 100
worst_rate = (monthly_performance[worst_month]['won']/monthly_performance[worst_month]['total']) * 100

print(f"• Best performing month: {best_month} with {best_rate:.1f}% win rate")
print(f"• Worst performing month: {worst_month} with {worst_rate:.1f}% win rate")
print(f"• Performance gap: {best_rate - worst_rate:.1f} percentage points")
print(f"• Overall trend: {'Declining' if trend < 0 else 'Improving'} by {abs(trend):.1f}pp")

total_deals = sum(monthly_performance[m]['total'] for m in monthly_performance)
total_won = sum(monthly_performance[m]['won'] for m in monthly_performance)
overall_rate = (total_won / total_deals) * 100
print(f"• Annual win rate: {overall_rate:.1f}% ({total_won}/{total_deals} deals)")

if trend < -2:
    print(f"⚠️  RECOMMENDATION: Sales performance declined significantly in H2 2025.")
    print(f"   Consider reviewing sales processes, training, or market conditions.")
elif trend > 2:
    print(f"✅ POSITIVE: Sales performance improved significantly in H2 2025.")
else:
    print(f"📊 STABLE: Sales performance remained relatively consistent throughout 2025.")

"""
REASONING FOR SECTION 5 METRIC:
I chose monthly win rate as the performance metric because it directly measures
the sales department's effectiveness in closing deals over time. This metric
accounts for both the number of deals attempted and successfully closed each month,
providing insight into sales team performance trends. By comparing first vs second
half of 2025, we can identify if the team improved, declined, or remained stable.
Win rate is more meaningful than just counting won deals, as it normalizes for
varying sales activity levels throughout the year.
"""