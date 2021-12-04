select count(id) as answer from (select id,(value-LAG(value,1) OVER (order by id)) as difference from stdin) where difference>0;
