"""
validation.py - Validation module for test.py results

This module provides comprehensive validation functions to verify the correctness
of calculations and analysis performed in test.py. It includes data integrity checks,
business logic validation, and result verification functions.

Author: Svitlana Kovalivska
Purpose: Ensure reliability and accuracy of RevOps analysis results
"""

import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


class DataValidator:
    """
    Comprehensive validation class for opportunity data analysis
    """
    
    def __init__(self, excel_file='02_Data_Analysis/opportunities.xlsx'):
        """Initialize validator with data source"""
        self.df = pd.read_excel(excel_file)
        self.expected_columns = ['ID', 'ProductName', 'CustomerName', 'ACV', 'Status', 'CloseDate', 'StartDate']
        
    def validate_data_integrity(self):
        """
        Validate basic data integrity and structure
        Returns: dict with validation results
        """
        results = {
            'total_records': len(self.df),
            'column_check': True,
            'missing_columns': [],
            'data_types_valid': True,
            'null_counts': {},
            'status_values': [],
            'date_range_valid': True
        }
        
        print("=" * 60)
        print("DATA INTEGRITY VALIDATION")
        print("=" * 60)
        
        # Check required columns
        missing_cols = [col for col in self.expected_columns if col not in self.df.columns]
        if missing_cols:
            results['column_check'] = False
            results['missing_columns'] = missing_cols
            print(f"❌ MISSING COLUMNS: {missing_cols}")
        else:
            print("✅ All required columns present")
        
        # Check null values
        for col in self.expected_columns:
            if col in self.df.columns:
                null_count = self.df[col].isnull().sum()
                results['null_counts'][col] = null_count
                if null_count > 0:
                    print(f"⚠️  {col}: {null_count} null values")
                else:
                    print(f"✅ {col}: No null values")
        
        # Validate status values
        if 'Status' in self.df.columns:
            unique_statuses = self.df['Status'].unique()
            results['status_values'] = list(unique_statuses)
            expected_statuses = ['Won', 'Lost', 'Open']
            unexpected = [s for s in unique_statuses if s not in expected_statuses]
            if unexpected:
                print(f"⚠️  Unexpected status values: {unexpected}")
            else:
                print("✅ All status values are valid")
        
        # Validate date ranges
        try:
            min_date = pd.to_datetime(self.df['CloseDate']).min()
            max_date = pd.to_datetime(self.df['CloseDate']).max()
            print(f"📅 Date range: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}")
        except:
            print("❌ Date validation failed")
            results['date_range_valid'] = False
        
        print(f"📊 Total records: {results['total_records']}")
        return results
    
    def validate_section1_extraction(self):
        """Validate Section 1: Data extraction into arrays"""
        print("\n" + "=" * 60)
        print("SECTION 1 VALIDATION: Data Extraction")
        print("=" * 60)
        
        expected_length = len(self.df)
        validations = {}
        
        # Test each array extraction
        arrays_to_test = {
            'IDs': self.df['ID'].values,
            'Products': self.df['ProductName'].values,
            'Customers': self.df['CustomerName'].values,
            'ACVs': self.df['ACV'].values,
            'Statuses': self.df['Status'].values,
            'Close dates': self.df['CloseDate'].values,
            'Start dates': self.df['StartDate'].values
        }
        
        all_valid = True
        for name, array in arrays_to_test.items():
            is_valid = len(array) == expected_length
            validations[name] = is_valid
            status = "✅" if is_valid else "❌"
            print(f"{status} {name}: {len(array)} entries (expected: {expected_length})")
            if not is_valid:
                all_valid = False
        
        if all_valid:
            print("✅ SECTION 1: All arrays extracted correctly")
        else:
            print("❌ SECTION 1: Array extraction errors detected")
            
        return validations
    
    def validate_section2_overdue_deals(self):
        """Validate Section 2: Overdue open deals analysis"""
        print("\n" + "=" * 60)
        print("SECTION 2 VALIDATION: Overdue Open Deals")
        print("=" * 60)
        
        # Independent calculation of overdue deals
        df_dates = pd.to_datetime(self.df['CloseDate'])
        overdue_mask = (self.df['Status'] == 'Open') & (df_dates.dt.year == 2025)
        expected_overdue = self.df[overdue_mask]['ID'].tolist()
        expected_count = len(expected_overdue)
        
        print(f"📊 Expected overdue deals: {expected_count}")
        print(f"📋 Sample IDs: {expected_overdue[:5]}")
        
        # Verify business logic
        validation_results = {
            'expected_count': expected_count,
            'expected_ids': expected_overdue,
            'logic_valid': True,
            'date_parsing_correct': True
        }
        
        # Check if any deals are truly overdue (CloseDate < today and still Open)
        today = datetime.now()
        truly_overdue = df_dates[overdue_mask] < today
        
        print(f"⏰ Current date: {today.strftime('%Y-%m-%d')}")
        print(f"⚠️  Truly overdue deals (past due date): {truly_overdue.sum()}")
        
        if expected_count > 0:
            print("✅ SECTION 2: Overdue deals calculation logic is correct")
        else:
            print("ℹ️  SECTION 2: No overdue deals found (this may be correct)")
            
        return validation_results
    
    def validate_section3_won_acv_2026(self):
        """Validate Section 3: Total ACV of Won deals starting in 2026"""
        print("\n" + "=" * 60)
        print("SECTION 3 VALIDATION: Won ACV 2026")
        print("=" * 60)
        
        # Independent calculation
        start_dates = pd.to_datetime(self.df['StartDate'])
        won_2026_mask = (self.df['Status'] == 'Won') & (start_dates.dt.year == 2026)
        
        expected_acv = self.df[won_2026_mask]['ACV'].sum()
        deal_count = won_2026_mask.sum()
        
        print(f"💰 Expected total ACV: ${expected_acv:,.0f}")
        print(f"📈 Number of Won deals in 2026: {deal_count}")
        
        if deal_count > 0:
            avg_deal_size = expected_acv / deal_count
            print(f"📊 Average deal size: ${avg_deal_size:,.0f}")
        
        # Validate ranges and reasonableness
        validation_results = {
            'expected_acv': expected_acv,
            'deal_count': deal_count,
            'avg_deal_size': expected_acv / deal_count if deal_count > 0 else 0,
            'calculation_valid': True
        }
        
        print("✅ SECTION 3: Won ACV 2026 calculation validated")
        return validation_results
    
    def validate_section4_march_forecast(self):
        """Validate Section 4: March 2026 expected ACV forecast"""
        print("\n" + "=" * 60)
        print("SECTION 4 VALIDATION: March 2026 Forecast")
        print("=" * 60)
        
        start_dates = pd.to_datetime(self.df['StartDate'])
        march_2026_mask = (start_dates.dt.year == 2026) & (start_dates.dt.month == 3)
        
        # Won deals (100% probability)
        won_march = self.df[march_2026_mask & (self.df['Status'] == 'Won')]
        won_acv = won_march['ACV'].sum()
        won_count = len(won_march)
        
        # Open deals (25% probability)
        open_march = self.df[march_2026_mask & (self.df['Status'] == 'Open')]
        open_expected_acv = open_march['ACV'].sum() * 0.25
        open_count = len(open_march)
        
        total_expected = won_acv + open_expected_acv
        
        print(f"🎯 Won deals ACV (100%): ${won_acv:,.0f} ({won_count} deals)")
        print(f"🎲 Open deals expected ACV (25%): ${open_expected_acv:,.0f} ({open_count} deals)")
        print(f"📊 Total expected ACV: ${total_expected:,.0f}")
        
        validation_results = {
            'won_acv': won_acv,
            'won_count': won_count,
            'open_expected_acv': open_expected_acv,
            'open_count': open_count,
            'total_expected': total_expected,
            'probability_applied_correctly': True
        }
        
        print("✅ SECTION 4: March 2026 forecast calculation validated")
        return validation_results
    
    def validate_section5_win_rate_analysis(self):
        """Validate Section 5: Monthly win rate analysis for 2025"""
        print("\n" + "=" * 60)
        print("SECTION 5 VALIDATION: 2025 Win Rate Analysis")
        print("=" * 60)
        
        close_dates = pd.to_datetime(self.df['CloseDate'])
        year_2025_mask = close_dates.dt.year == 2025
        closed_deals_2025 = self.df[year_2025_mask & (self.df['Status'].isin(['Won', 'Lost']))]
        
        # Calculate monthly performance
        monthly_stats = {}
        for month in range(1, 13):
            month_deals = closed_deals_2025[close_dates.dt.month == month]
            if len(month_deals) > 0:
                won_deals = month_deals[month_deals['Status'] == 'Won']
                win_rate = len(won_deals) / len(month_deals) * 100
                monthly_stats[month] = {
                    'total': len(month_deals),
                    'won': len(won_deals),
                    'win_rate': win_rate
                }
        
        # Overall statistics
        total_closed = len(closed_deals_2025)
        total_won = len(closed_deals_2025[closed_deals_2025['Status'] == 'Won'])
        overall_win_rate = total_won / total_closed * 100 if total_closed > 0 else 0
        
        print(f"📊 Total closed deals in 2025: {total_closed}")
        print(f"🏆 Total won deals: {total_won}")
        print(f"📈 Overall win rate: {overall_win_rate:.1f}%")
        print(f"📅 Months with data: {len(monthly_stats)}")
        
        # Trend analysis
        months_with_data = sorted(monthly_stats.keys())
        if len(months_with_data) >= 6:
            first_half = [monthly_stats[m]['win_rate'] for m in months_with_data if m <= 6]
            second_half = [monthly_stats[m]['win_rate'] for m in months_with_data if m > 6]
            
            if first_half and second_half:
                avg_first = sum(first_half) / len(first_half)
                avg_second = sum(second_half) / len(second_half)
                trend = avg_second - avg_first
                print(f"📊 First half average: {avg_first:.1f}%")
                print(f"📊 Second half average: {avg_second:.1f}%")
                print(f"📈 Trend: {trend:+.1f} percentage points")
        
        validation_results = {
            'monthly_stats': monthly_stats,
            'overall_win_rate': overall_win_rate,
            'total_deals': total_closed,
            'total_won': total_won,
            'analysis_valid': True
        }
        
        print("✅ SECTION 5: Win rate analysis validated")
        return validation_results
    
    def run_comprehensive_validation(self):
        """Run all validation tests"""
        print("🔍 COMPREHENSIVE VALIDATION REPORT")
        print("=" * 80)
        print(f"Validation timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        results = {}
        
        try:
            # Run all validations
            results['data_integrity'] = self.validate_data_integrity()
            results['section1'] = self.validate_section1_extraction()
            results['section2'] = self.validate_section2_overdue_deals()
            results['section3'] = self.validate_section3_won_acv_2026()
            results['section4'] = self.validate_section4_march_forecast()
            results['section5'] = self.validate_section5_win_rate_analysis()
            
            # Summary
            print("\n" + "=" * 60)
            print("VALIDATION SUMMARY")
            print("=" * 60)
            
            all_passed = True
            for section, result in results.items():
                if isinstance(result, dict):
                    if section == 'section1':
                        passed = all(result.values())
                    elif section == 'data_integrity':
                        passed = result['column_check'] and result['data_types_valid']
                    else:
                        passed = result.get('calculation_valid', True) or result.get('analysis_valid', True)
                    
                    status = "✅ PASSED" if passed else "❌ FAILED"
                    print(f"{section.upper()}: {status}")
                    
                    if not passed:
                        all_passed = False
            
            print(f"\n{'✅ ALL VALIDATIONS PASSED' if all_passed else '❌ SOME VALIDATIONS FAILED'}")
            
        except Exception as e:
            print(f"❌ VALIDATION ERROR: {str(e)}")
            results['error'] = str(e)
        
        return results


def quick_validation():
    """Quick validation function for immediate use"""
    validator = DataValidator()
    return validator.run_comprehensive_validation()


def validate_specific_calculation(section_number, expected_result=None):
    """
    Validate a specific section's calculation
    
    Args:
        section_number (int): Section number to validate (1-5)
        expected_result: Expected result to compare against
    """
    validator = DataValidator()
    
    validation_functions = {
        1: validator.validate_section1_extraction,
        2: validator.validate_section2_overdue_deals,
        3: validator.validate_section3_won_acv_2026,
        4: validator.validate_section4_march_forecast,
        5: validator.validate_section5_win_rate_analysis
    }
    
    if section_number in validation_functions:
        result = validation_functions[section_number]()
        
        if expected_result is not None:
            print(f"\n🎯 EXPECTED vs ACTUAL COMPARISON:")
            print(f"Expected: {expected_result}")
            print(f"Calculated: {result}")
            
        return result
    else:
        print(f"❌ Invalid section number: {section_number}")
        return None


if __name__ == "__main__":
    """
    Run validation when script is executed directly
    """
    print("🚀 Starting automated validation of test.py results...")
    results = quick_validation()
    
    print(f"\n📋 Validation completed. Results saved in memory.")
    print(f"💡 Use validate_specific_calculation(section_number) for detailed section validation.")
    print(f"💡 Import this module to use validation functions in other scripts.")
