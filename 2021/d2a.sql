CREATE VIEW IF NOT EXISTS positions
AS
SELECT
	SUM(realtot) AS dir_tot,
	dir
FROM
	(SELECT
		op,
		(CASE
			WHEN op="forward" THEN "horizontal"
			ELSE "vertical" END
		) AS dir,
		(CASE
			WHEN op="up" THEN -SUM(value)
			ELSE SUM(value) END
		) AS realtot
	FROM test GROUP BY op
	)
GROUP BY dir;

SELECT 
	(SELECT dir_tot FROM positions WHERE dir=='horizontal')*(SELECT dir_tot FROM positions WHERE dir=='vertical') AS answer
FROM
positions
LIMIT 1
;
