USE noshowguard;
WITH clinic_rates AS (
SELECT c.clinic_name clinic,c.city city,
ROUND(100.0 * SUM(a.no_show) / COUNT(*), 1) no_show_pct
FROM clinics c INNER JOIN appointments a ON c.clinic_id = a.clinic_id
GROUP BY c.clinic_name,c.city
)
SELECT city,clinic , no_show_pct,
RANK() OVER (PARTITION BY city ORDER BY no_show_pct DESC) as rank_in_city,
(CASE
	WHEN no_show_pct > (SELECT AVG(no_show_pct) FROM clinic_rates) THEN 'above'
    WHEN no_show_pct < (SELECT AVG(no_show_pct) FROM clinic_rates) THEN 'below'
    WHEN no_show_pct= (SELECT AVG(no_show_pct) FROM clinic_rates) THEN 'equal'
END ) vs_overall
FROM clinic_rates
ORDER BY city,rank_in_city;

