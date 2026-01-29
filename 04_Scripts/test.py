"""
RevOps Data Analysis Script - PTV Logistics Assessment
======================================================

This script performs comprehensive analysis on sales opportunities dataset
to extract business insights and identify operational improvements.

Author: Svitlana Kovalivska
Date: January 2026
Purpose: RevOps Data Analyst Technical Assessment

Dataset: opportunities.xlsx (2,621 opportunities)
Sections: 5 analytical tasks demonstrating data manipulation and business logic
"""

import numpy
import pandas

############ SECTION 1 #############
# DATA EXTRACTION AND PREPARATION
# ================================
# Objective: Load dataset and extract each column into separate numpy arrays
# Business Value: Foundation for all subsequent analysis, ensures data accessibility

# Load the opportunities dataset from Excel file
# Path adjusted for script location in 04_Scripts directory
df = pandas.read_excel('../02_Data_Analysis/opportunities.xlsx')

# COMPLETE TASK 1 HERE:
# Extract each column from the dataset into separate arrays for efficient processing
# Using .values converts pandas Series to numpy arrays for faster computation

ids = df['ID'].values                    # Unique opportunity identifiers
products = df['ProductName'].values      # Product/service being sold
customers = df['CustomerName'].values    # Customer company names
acvs = df['ACV'].values                 # Annual Contract Value (revenue impact)
statuses = df['Status'].values          # Deal status (Open, Won, Lost)
closedates = df['CloseDate'].values     # Expected/actual close dates
startdates = df['StartDate'].values     # Contract start dates

# Display extraction results for validation
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
# DATA QUALITY ISSUE IDENTIFICATION
# ==================================
# Objective: Find opportunities with data integrity issues
# Business Value: Identify deals requiring immediate attention and status updates
# Problem: Open deals with past close dates indicate stale pipeline data

# COMPLETE TASK 2 HERE
# Find opportunities that are still open but have CloseDate in 2025
# These represent data quality issues requiring immediate remediation

print("SECTION 2 RESULTS:")
print("Overdue open deals (CloseDate in 2025 but still Open):")

# Initialize list to store problematic opportunity IDs
open_deals_2025 = []

# Iterate through all opportunities to identify data quality issues
for i in range(len(df)):
    # Convert numpy datetime64 to pandas datetime to access year attribute
    # This handles datetime format compatibility between pandas and numpy
    close_year = pandas.to_datetime(closedates[i]).year
    
    # Business logic: If deal is still "Open" but close date was in 2025, it's overdue
    if statuses[i] == 'Open' and close_year == 2025:
        open_deals_2025.append(ids[i])
        print(ids[i])  # Output each problematic opportunity ID

# Provide business context for the findings
print(f"\nSECTION 2 ANALYSIS RESULTS:")
print(f"Found {len(open_deals_2025)} opportunities that are still open but should have been closed in 2025.")
print(f"These deals require status updates as they are overdue for closure.")
print(f"Recommended Action: Sales operations should review and update these records immediately.")

####################################
############ SECTION 3 #############
####################################

# CONFIRMED REVENUE CALCULATION
# ==============================
# Objective: Calculate total ACV for confirmed won deals starting in 2026
# Business Value: Provides accurate revenue forecast for financial planning
# Scope: Only includes deals with "Won" status to ensure revenue certainty

print("\nSECTION 3 RESULTS:")

# COMPLETE TASK 3 HERE:
# Calculate total ACV of all Won deals that start in 2026
# This represents confirmed, contracted revenue for the upcoming year

won_acv_2026 = 0  # Initialize accumulator for total ACV

# Process each opportunity to identify confirmed 2026 revenue
for i in range(len(df)):
    # Extract year from start date for filtering
    start_year = pandas.to_datetime(startdates[i]).year
    
    # Business logic: Only count deals that are Won (confirmed) and start in 2026
    # This ensures we're only including contracted revenue, not potential revenue
    if statuses[i] == 'Won' and start_year == 2026:
        won_acv_2026 += acvs[i]  # Add ACV to running total
        
print(won_acv_2026)  # Raw number for immediate reference

# Provide business-formatted output with context
print(f"\nSECTION 3 ANALYSIS RESULTS:")
print(f"Total ACV of all Won deals starting in 2026: ${won_acv_2026:,.0f}")
print(f"This represents confirmed revenue from successfully closed deals for 2026.")
print(f"Financial Impact: Provides certainty for revenue planning and resource allocation.")

####################################
############ SECTION 4 #############
####################################

# PROBABILISTIC REVENUE FORECASTING
# ==================================
# Objective: Calculate expected ACV for March 2026 using probability-weighted approach
# Business Value: Provides realistic revenue forecast accounting for deal uncertainty
# Method: 100% weight for Won deals, 25% probability for Open deals (risk adjustment)

# COMPLETE TASK 4 HERE:
# Calculate expected ACV for March 2026 with 25% success rate for open deals
# This combines confirmed revenue with risk-adjusted potential revenue

total_expected_acv_032026 = 0  # Initialize total expected value accumulator
won_deals_march = 0            # Counter for confirmed deals
open_deals_march = 0           # Counter for potential deals

# PHASE 1: Add confirmed revenue from Won deals (100% probability)
# These represent contracted revenue with no execution risk
for i in range(len(df)):
    start_dt = pandas.to_datetime(startdates[i])  # Convert to datetime for month/year access
    
    # Filter for Won deals starting specifically in March 2026
    if statuses[i] == 'Won' and start_dt.year == 2026 and start_dt.month == 3:
        total_expected_acv_032026 += acvs[i]  # Full ACV value (100% probability)
        won_deals_march += 1

# PHASE 2: Add risk-adjusted potential revenue from Open deals (25% probability)  
# 25% represents historical win rate assumption for forecasting purposes
for i in range(len(df)):
    start_dt = pandas.to_datetime(startdates[i])
    
    # Filter for Open deals starting in March 2026
    if statuses[i] == 'Open' and start_dt.year == 2026 and start_dt.month == 3:
        # Apply 25% probability weight to account for win rate uncertainty
        total_expected_acv_032026 += acvs[i] * 0.25  # Risk-adjusted expected value
        open_deals_march += 1

print(total_expected_acv_032026)  # Raw calculation for verification

# Provide comprehensive business analysis
print(f"\nSECTION 4 ANALYSIS RESULTS:")
print(f"Expected ACV for March 2026: ${total_expected_acv_032026:,.0f}")
print(f"This includes {won_deals_march} confirmed Won deals + {open_deals_march} Open deals with 25% success probability.")
print(f"Risk-adjusted forecast combining guaranteed and potential revenue for March 2026.")
print(f"Business Application: Enables realistic pipeline planning and quota setting.")

####################################
############ SECTION 5 #############
####################################

# SALES PERFORMANCE TREND ANALYSIS
# =================================
# Objective: Calculate monthly win rates to assess sales department effectiveness over time
# Business Value: Identifies performance trends, seasonal patterns, and coaching opportunities
# Metric Choice: Win rate normalizes for activity volume and directly measures closing effectiveness

# COMPLETE TASK 5 HERE:
# Calculate monthly win rate throughout 2025 to assess sales department performance
# Win rate = (Won Deals / Total Closed Deals) × 100
# This metric shows how the ability to close deals changed over time

# Initialize dictionary to store monthly performance metrics
# Structure: {month: {'won': count, 'total': count}}
monthly_performance = {}

# Process each opportunity to build monthly performance dataset
for i in range(len(df)):
    close_dt = pandas.to_datetime(closedates[i])  # Convert to datetime for month extraction
    
    # Filter criteria: Only deals actually closed in 2025 (Won or Lost)
    # Excludes Open deals as they don't contribute to win rate calculation
    if close_dt.year == 2025 and statuses[i] in ['Won', 'Lost']:
        month = close_dt.month
        
        # Initialize month data structure if first encounter
        if month not in monthly_performance:
            monthly_performance[month] = {'won': 0, 'total': 0}
        
        # Increment total closed deals for the month
        monthly_performance[month]['total'] += 1
        
        # Increment won deals if status is Won
        if statuses[i] == 'Won':
            monthly_performance[month]['won'] += 1

# REPORTING SECTION: Calculate and display monthly win rates
print("Monthly Win Rates for 2025:")
print("Month | Win Rate | Won/Total Deals")
print("-" * 35)

for month in sorted(monthly_performance.keys()):
    # Calculate win rate percentage for the month
    win_rate = (monthly_performance[month]['won'] / monthly_performance[month]['total']) * 100
    won_count = monthly_performance[month]['won']
    total_count = monthly_performance[month]['total']
    
    print(f"Month {month:2d}: {win_rate:5.1f}% ({won_count}/{total_count})")

# TREND ANALYSIS: Compare first half vs second half performance
months = sorted(monthly_performance.keys())
win_rates = [(monthly_performance[month]['won'] / monthly_performance[month]['total']) * 100 
             for month in months]

# Split year into halves for trend comparison
first_half = [rate for month, rate in zip(months, win_rates) if month <= 6]
second_half = [rate for month, rate in zip(months, win_rates) if month > 6]

# Calculate trend if both halves have data
if first_half and second_half:
    avg_first_half = sum(first_half) / len(first_half)
    avg_second_half = sum(second_half) / len(second_half)
    trend = avg_second_half - avg_first_half  # Positive = improving, Negative = declining
    
    print(f"\nTrend Analysis:")
    print(f"First half 2025: {avg_first_half:.1f}%")
    print(f"Second half 2025: {avg_second_half:.1f}%")
    print(f"Trend: {trend:+.1f} percentage points")

# EXECUTIVE SUMMARY: Key insights and recommendations
print(f"\nSECTION 5 ANALYSIS RESULTS:")
print(f"SALES DEPARTMENT PERFORMANCE ANALYSIS FOR 2025")
print(f"="*50)
print(f"Key Findings:")

# Identify best and worst performing months for coaching insights
best_month = max(monthly_performance.keys(), 
                key=lambda x: (monthly_performance[x]['won']/monthly_performance[x]['total']))
worst_month = min(monthly_performance.keys(), 
                 key=lambda x: (monthly_performance[x]['won']/monthly_performance[x]['total']))

best_rate = (monthly_performance[best_month]['won']/monthly_performance[best_month]['total']) * 100
worst_rate = (monthly_performance[worst_month]['won']/monthly_performance[worst_month]['total']) * 100

print(f"• Best performing month: {best_month} with {best_rate:.1f}% win rate")
print(f"• Worst performing month: {worst_month} with {worst_rate:.1f}% win rate")
print(f"• Performance gap: {best_rate - worst_rate:.1f} percentage points")
print(f"• Overall trend: {'Declining' if trend < 0 else 'Improving'} by {abs(trend):.1f}pp")

# Calculate annual performance metrics
total_deals = sum(monthly_performance[m]['total'] for m in monthly_performance)
total_won = sum(monthly_performance[m]['won'] for m in monthly_performance)
overall_rate = (total_won / total_deals) * 100
print(f"• Annual win rate: {overall_rate:.1f}% ({total_won}/{total_deals} deals)")

# BUSINESS RECOMMENDATIONS based on trend analysis
if trend < -2:
    print(f"⚠️  RECOMMENDATION: Sales performance declined significantly in H2 2025.")
    print(f"   Consider reviewing sales processes, training, or market conditions.")
    print(f"   Suggested actions: Win/loss analysis, competitive assessment, sales coaching.")
elif trend > 2:
    print(f"✅ POSITIVE: Sales performance improved significantly in H2 2025.")
    print(f"   Identify and replicate success factors across the organization.")
else:
    print(f"📊 STABLE: Sales performance remained relatively consistent throughout 2025.")
    print(f"   Focus on optimizing processes to drive systematic improvements.")

"""
DETAILED REASONING FOR SECTION 5 METRIC SELECTION:
==================================================

METRIC CHOICE: Monthly Win Rate Analysis

Why Win Rate was Selected:
1. NORMALIZATION: Win rate normalizes for varying sales activity levels throughout the year,
   providing a fair comparison between months regardless of total opportunity volume.

2. DIRECT PERFORMANCE MEASURE: Win rate directly measures the sales team's effectiveness
   at converting qualified opportunities into closed-won deals, which is the core 
   responsibility of the sales function.

3. TREND IDENTIFICATION: Monthly win rates reveal performance patterns, seasonal effects,
   and the impact of process changes, training, or market conditions over time.

4. ACTIONABLE INSIGHTS: Win rate analysis enables specific coaching opportunities:
   - Identify best-performing periods to replicate success factors
   - Pinpoint declining periods for targeted intervention
   - Compare performance across different time periods for trend analysis

5. BUSINESS RELEVANCE: Win rate directly impacts revenue predictability and forecasting
   accuracy, making it a critical metric for RevOps optimization.

Alternative Metrics Considered:
- Total Won Deals: Doesn't account for opportunity volume variations
- Average Deal Size: Doesn't measure closing effectiveness
- Sales Cycle Length: Important but doesn't measure conversion success

IMPLEMENTATION METHODOLOGY:
- Time Period: 2025 full year for comprehensive trend analysis
- Calculation: (Won Deals / Total Closed Deals) × 100 per month
- Exclusions: Open deals excluded as they don't contribute to win rate
- Trend Analysis: H1 vs H2 comparison to identify performance direction

BUSINESS APPLICATION:
This analysis enables data-driven decisions for:
- Sales process optimization
- Training program timing and content
- Territory and quota planning
- Competitive response strategies
- Performance management and coaching focus areas
"""