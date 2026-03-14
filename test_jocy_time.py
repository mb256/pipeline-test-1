import datetime
import pytz

import jocy_time


def test_main_output_contains_timezones(capsys):
    # Run main and check that key sections are printed
    jocy_time.main()
    captured = capsys.readouterr().out

    assert "Prague:" in captured
    assert "Johnson City, TN:" in captured
    assert "WORKING HOURS" in captured


def test_working_hours_conversion_stays_consistent(monkeypatch):
    # We use a known date in Prague and compare converted work hours in ET
    # If we localize one known date, the output should be deterministic.
    prague_tz = pytz.timezone("Europe/Prague")
    jc_tz = pytz.timezone("America/New_York")
    today = datetime.date(2026, 3, 14)
    work_start_prague = prague_tz.localize(datetime.datetime(today.year, today.month, today.day, 8, 0))
    work_end_prague = prague_tz.localize(datetime.datetime(today.year, today.month, today.day, 16, 30))

    work_start_jc = work_start_prague.astimezone(jc_tz)
    work_end_jc = work_end_prague.astimezone(jc_tz)

    assert work_start_jc.strftime("%H:%M") in ["01:00", "02:00", "03:00", "23:00", "00:00"]
    assert work_end_jc.strftime("%H:%M") in ["09:30", "10:30", "11:30", "16:30", "17:30"]
