SELECT
    h.hacker_id, 
    name
FROM Submissions s
JOIN Hackers h ON s.hacker_id = h.hacker_id
JOIN Challenges c ON s.challenge_id = c.challenge_id
JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
WHERE s.score = d.score
GROUP BY h.hacker_id,name
HAVING COUNT(s.hacker_id)>1
ORDER BY COUNT(s.hacker_id) DESC, s.hacker_id ASC;