# Write your MySQL query statement below
select pt.Product_name, st.year, st.Price from sales st left join product pt on st.product_id = pt.product_id;