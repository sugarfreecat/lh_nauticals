-- ticket médio e diversidade de categorias para cada customer_id
with ticket_medio as (
    select customer_id, sum(total) / count(distinct id) as ticket_medio
    from orders
    where placed_at < now()
    group by customer_id
),
diversidade as (
    select o.customer_id, count(distinct p.category_id) as diversidade_categorias
    from orders o
    inner join order_items oi on oi.order_id = o.id
    inner join product_variants pv on pv.id = oi.product_variant_id
    inner join products p on p.id = pv.product_id
    where o.placed_at < now()
    group by o.customer_id
)
select d.customer_id as cliente_id, c.legal_name cliente_nome, d.diversidade_categorias, t.ticket_medio
from diversidade d
inner join ticket_medio t on t.customer_id = d.customer_id
inner join customers c on d.customer_id = c.id
order by t.ticket_medio desc;

-- 10 clientes com o maior ticket medio e com 13 ou + categorias
with ticket_medio as (
    select customer_id, avg(total) as ticket_medio
    from orders
    where placed_at < now()
    group by customer_id
),
diversidade as (
    select o.customer_id, count(distinct p.category_id) as diversidade_categorias
    from orders o
    inner join order_items oi on oi.order_id = o.id
    inner join product_variants pv on pv.id = oi.product_variant_id
    inner join products p on p.id = pv.product_id
    where o.placed_at < now()
    group by o.customer_id
    having count(distinct p.category_id) >= 13
)
select d.customer_id as cliente_id, c.legal_name cliente_nome, d.diversidade_categorias, t.ticket_medio
from diversidade d
inner join ticket_medio t on t.customer_id = d.customer_id
inner join customers c on d.customer_id = c.id
order by t.ticket_medio desc, d.customer_id asc
limit 10;

-- qual categoria de produto tem a maior quantidade total de itens comprados (sum(quantity)) para os 10 clientes anteriores
with ticket_medio as (
    select customer_id, sum(total) / count(distinct id) as ticket_medio
    from orders
    where placed_at < now()
    group by customer_id
),
diversidade as (
    select o.customer_id, count(distinct p.category_id) as diversidade_categorias
    from orders o
    inner join order_items oi on oi.order_id = o.id
    inner join product_variants pv on pv.id = oi.product_variant_id
    inner join products p on p.id = pv.product_id
    where o.placed_at < now()
    group by o.customer_id
    having count(distinct p.category_id) >= 13
),
top_10 as (
	select d.customer_id
	from diversidade d
	inner join ticket_medio tm on d.customer_id = tm.customer_id
	order by tm.ticket_medio desc, d.customer_id asc
	limit 10
)
select p.category_id as categoria_id, c.name as categoria_nome, sum(oi.quantity) as quantidade
from order_items oi
inner join orders o on oi.order_id = o.id
inner join product_variants pv on oi.product_variant_id = pv.id
inner join products p on pv.product_id = p.id
inner join top_10 on top_10.customer_id = o.customer_id
inner join categories c on c.id = p.category_id
where o.placed_at < now()
group by p.category_id, c.name
order by quantidade desc
limit 1;