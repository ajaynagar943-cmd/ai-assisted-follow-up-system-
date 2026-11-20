use noshowguard ;
SELECT c.clinic_name, c.city, COUNT(*) appointments, SUM(a.no_show) no_shows,
ROUND(100.0 * SUM(a.no_show) / COUNT(*), 1) no_show_pct
FROM clinics c INNER JOIN appointments a ON c.clinic_id = a.clinic_id
GROUP BY c.clinic_name,c.city
-- HAVING appointments >= 95
ORDER BY no_show_pct DESC;