"""
services/wage_calculator.py — M-06: Wage Calculation
No ML. Pure arithmetic: days_worked * daily_wage.
Stub — implement in Day 6.
"""


async def recalculate_wage(
    *,
    worker_id: str,
    project_id: str,
    db_client=None,
) -> dict:
    """
    Recalculate expected_wage for a worker on a project.
    Called after every attendance change.

    Returns updated wage_record dict.
    Raises ValueError if worker has no active contract on this project.

    Logic (Day 6):
      1. Count attendance rows WHERE worker_id + project_id + status IN ('present','half_day')
         (half_day counts as 0.5)
      2. Get daily_wage from contracts row
      3. Upsert wage_records: days_worked, daily_wage, recalculate status
      4. Compare expected_wage vs minimum_wages reference table — flag if below minimum
    """
    # TODO (M-06 Day 6)
    raise NotImplementedError("wage_calculator — implement in Day 6 (M-06)")
