USE noshowguard;
WITH monthly AS (
SELECT SUBSTR(appt_date,1,7) month ,count(*) appointments,
ROUND(100.0 * SUM(no_show) / COUNT(*), 1) no_show_pct
FROM appointments
GROUP BY month
ORDER BY month
)
SELECT month,appointments,no_show_pct,
(no_show_pct - LAG(no_show_pct) OVER (ORDER BY month)) change_in_no_show_pct
FROM monthly;