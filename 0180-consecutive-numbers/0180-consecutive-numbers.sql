# Write your MySQL query statement belo
select distinct first.num as ConsecutiveNums from Logs first, Logs sec, Logs third
where first.id = sec.id-1 and sec.id = third.id-1 and first.num = sec.num and sec.num = third.num;