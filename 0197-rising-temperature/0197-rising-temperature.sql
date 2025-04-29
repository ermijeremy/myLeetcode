SELECT 
    w1.id
FROM 
    Weather w1, weather w2
WHERE 
    DATEDIFF(w1.recordDate, w2.recordDate) = 1 and 
    w1.temperature > w2.temperature;