-- Groups by Score
SELECT score, COUNT(*) as number FROM second_table GROUP BY score DESC;
