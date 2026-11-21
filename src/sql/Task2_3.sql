USE noshowguard;
SELECT (CASE
	WHEN a.lead_days BETWEEN 1 AND 7 THEN "1-7"
    WHEN a.lead_days BETWEEN 8 AND 14 THEN "8-14"
    WHEN a.lead_days BETWEEN 15 AND 30 THEN "15-30"
    WHEN a.lead_days >=31 THEN "31+"
END ) AS band,
 COUNT(*) appointments, SUM(a.no_show) no_shows,
ROUND(100.0 * SUM(a.no_show) / COUNT(*), 1) no_show_pct
FROM  appointments a 
GROUP BY band
ORDER BY MIN(lead_days);