#!/usr/bin/env python3
"""
Command-line application to display current time in Prague and Johnson City, TN
and show Prague working hours converted to Johnson City time.
"""

from datetime import datetime
import pytz


def main():
    # Define timezones
    prague_tz = pytz.timezone("Europe/Prague")
    johnson_city_tz = pytz.timezone("America/New_York")  # Johnson City, TN uses Eastern Time
    
    # Get current time in both locations
    now_prague = datetime.now(prague_tz)
    now_johnson_city = datetime.now(johnson_city_tz)
    
    # Print current times
    print("=" * 60)
    print("CURRENT TIME".center(60))
    print("=" * 60)
    print(f"Prague:              {now_prague.strftime('%H:%M:%S %Y-%m-%d %Z')}")
    print(f"Johnson City, TN:    {now_johnson_city.strftime('%H:%M:%S %Y-%m-%d %Z')}")
    print()
    
    # Convert Prague working hours to Johnson City time
    print("=" * 60)
    print("WORKING HOURS".center(60))
    print("=" * 60)
    
    # Create datetime objects for Prague working hours (using today's date)
    today = now_prague.date()
    work_start_prague = prague_tz.localize(datetime(today.year, today.month, today.day, 8, 0))
    work_end_prague = prague_tz.localize(datetime(today.year, today.month, today.day, 16, 30))
    
    # Convert to Johnson City time
    work_start_jc = work_start_prague.astimezone(johnson_city_tz)
    work_end_jc = work_end_prague.astimezone(johnson_city_tz)
    
    print(f"Prague:              08:00 - 16:30")
    print(f"Johnson City, TN:    {work_start_jc.strftime('%H:%M')} - {work_end_jc.strftime('%H:%M')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
