-- PARTE 1: VISÃO GERAL DA TABELA ORDERS

-- 1.1: quantidade total de linhas, data minima e data maxima da coluna created_at
SELECT COUNT(*) as total_linhas, MIN(created_at) as data_minima, MAX(created_at) as data_maxima
FROM orders;

-- PARTE 2: ANÁLISE DE VALORES NUMÉRICOS

-- 2.1: valor mínimo, máximo e médio da coluna total
SELECT MIN(total) as valor_minimo, MAX(total) as valor_maximo, AVG(total) as valor_medio
FROM orders;