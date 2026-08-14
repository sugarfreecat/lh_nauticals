-- calendario com dias da semana e cruzamento com a tabela de vendas
with dim_calendario as (
	select 
		day::date as data_exata, 
		case extract(isodow from day)
	        when 1 then 'Segunda-feira'
	        when 2 then 'Terça-feira'
	        when 3 then 'Quarta-feira'
	        when 4 then 'Quinta-feira'
	        when 5 then 'Sexta-feira'
	        when 6 then 'Sábado'
	        when 7 then 'Domingo'
	    end as dia_semana
	from generate_series((select min(placed_at) from orders), now(), '1 day') as t(day)
),
vendas_diarias as (
	select
        placed_at::date as data_exata,
        sum(total) as venda
    from orders
    where channel = 'pos'
    group by placed_at::date
)
select dc.dia_semana, avg(coalesce(vd.venda, 0)) as media_vendas
from dim_calendario dc
left join vendas_diarias vd on dc.data_exata = vd.data_exata
group by dc.dia_semana
order by media_vendas desc;