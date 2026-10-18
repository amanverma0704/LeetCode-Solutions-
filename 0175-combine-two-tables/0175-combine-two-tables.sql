/* Write your T-SQL query statement below */
SELECT p.firstName,p.lastName,a.city,a.state
FROM Person AS p
FULL JOIN Address AS a ON p.personID = a.personID
WHERE p.personID IS NOT NULL

