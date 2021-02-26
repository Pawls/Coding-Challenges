SELECT
    Hackers.hacker_id AS this_id, 
    name
FROM Hackers
JOIN
(SELECT 
    Submissions.hacker_id,
    COUNT(*) AS totals
FROM Submissions
JOIN Challenges ON Submissions.challenge_id = Challenges.challenge_id
JOIN Difficulty ON Challenges.difficulty_level = Difficulty.difficulty_level
WHERE Submissions.score = Difficulty.score
GROUP BY Submissions.hacker_id) tots ON Hackers.hacker_id = tots.hacker_id
WHERE tots.totals>1
ORDER BY tots.totals DESC, this_id ASC;