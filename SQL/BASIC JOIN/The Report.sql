SELECT
    CASE
        WHEN Students.Marks > 69 THEN Students.Name
        ELSE NULL
    END AS passing,
    Grade,
    Marks
FROM Students
JOIN Grades ON Marks BETWEEN Min_Mark AND Max_Mark
ORDER BY Grade DESC, Name ASC,
CASE WHEN passing IS NULL THEN Grade END DESC,
CASE WHEN passing IS NULL THEN Marks END ASC;