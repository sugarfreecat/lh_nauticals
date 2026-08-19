# LH Nauticals — Desafio Técnico Indicium AI / Indicium AI Technical Challenge

> 🇧🇷 Solução desenvolvida para o desafio técnico do processo seletivo da **Indicium AI**, utilizando dados da **LH Nauticals**.
> 🇺🇸 Solution developed for the **Indicium AI technical challenge**, using data from **LH Nauticals**.

Cada seção abaixo pode ser expandida/recolhida individualmente em português ou inglês.
Each section below can be expanded/collapsed individually in Portuguese or English.

---

## 📌 Sobre o projeto / About the project

<details>
<summary><strong>🇧🇷 Português</strong></summary>

O objetivo do desafio foi trabalhar com dados históricos de clientes, pedidos, produtos e categorias para extrair informações relevantes sobre o negócio e desenvolver soluções analíticas.

O projeto foi estruturado em diferentes etapas:

* Ingestão e tratamento dos dados;
* Modelagem e consultas em PostgreSQL;
* Análise de clientes e comportamento de compra;
* Construção de uma dimensão calendário;
* Desenvolvimento de um sistema de recomendação de produtos;
* Previsão de demanda;
* Desenvolvimento de um dashboard no Power BI.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

The goal of the challenge was to work with historical customer, order, product, and category data to extract relevant business insights and develop analytical solutions.

The project was organized into the following stages:

* Data ingestion and processing;
* PostgreSQL data modeling and SQL analysis;
* Customer behavior analysis;
* Calendar dimension creation;
* Product recommendation system;
* Demand forecasting;
* Power BI dashboard development.

</details>

---

## 🗂️ Estrutura dos dados / Data structure

<details>
<summary><strong>🇧🇷 Português</strong></summary>

O projeto utiliza os seguintes conjuntos de dados:

* `customers.csv` — informações dos clientes;
* `orders.csv` — pedidos realizados;
* `order_items.csv` — itens pertencentes aos pedidos;
* `product_variants.csv` — variantes dos produtos;
* `products.csv` — informações dos produtos;
* `categories.csv` — categorias dos produtos.

O relacionamento principal entre as tabelas segue o fluxo:

```text
customers
    │
    ▼
 orders
    │
    ▼
order_items
    │
    ▼
product_variants
    │
    ▼
 products
    │
    ▼
categories
```

A tabela `product_variants` é importante para relacionar os itens vendidos aos produtos correspondentes.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

The project uses the following datasets:

* `customers.csv` — customer information;
* `orders.csv` — customer orders;
* `order_items.csv` — items included in each order;
* `product_variants.csv` — product variants;
* `products.csv` — product information;
* `categories.csv` — product categories.

The main relationship between the tables follows this flow:

```text
customers
    │
    ▼
 orders
    │
    ▼
order_items
    │
    ▼
product_variants
    │
    ▼
 products
    │
    ▼
categories
```

The `product_variants` table plays an important role in connecting purchased items to their corresponding products.

</details>

---

## 🛠️ Tecnologias utilizadas / Technologies

<details>
<summary><strong>🇧🇷 Português</strong></summary>

* **Python** — ingestão, tratamento e análise dos dados;
* **PostgreSQL** — armazenamento, transformação e consultas SQL;
* **Pandas** — manipulação e análise dos dados;
* **Scikit-learn** — cálculo de similaridade para o sistema de recomendação;
* **Power BI** — visualização e construção do dashboard;
* **Docker** — execução do PostgreSQL em container;
* **Git/GitHub** — versionamento do projeto.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

* **Python** — data ingestion, processing, and analysis;
* **PostgreSQL** — data storage, transformation, and SQL analysis;
* **Pandas** — data manipulation and analysis;
* **Scikit-learn** — cosine similarity for the recommendation system;
* **Power BI** — data visualization and dashboard development;
* **Docker** — running PostgreSQL in a container;
* **Git/GitHub** — version control.

</details>

---

## 🐳 Docker

<details>
<summary><strong>🇧🇷 Português</strong></summary>

O PostgreSQL utilizado no projeto foi executado em um **container Docker**, o que facilita a reprodução do ambiente sem exigir a instalação do PostgreSQL diretamente na máquina.

**Subindo o container:**

```bash
docker compose up -d
```

**Verificando se o container está rodando:**

```bash
docker ps
```

**Parando o container:**

```bash
docker compose down
```

> 💡 As credenciais (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`) devem ser as mesmas configuradas no script de ingestão em Python.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

The PostgreSQL instance used in this project was run inside a **Docker container**, which makes the environment easy to reproduce without installing PostgreSQL directly on the host machine.

**Starting the container:**

```bash
docker compose up -d
```

**Checking that the container is running:**

```bash
docker ps
```

**Stopping the container:**

```bash
docker compose down
```

> 💡 The credentials (`POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`) should match the ones configured in the Python ingestion script.

</details>

---

## 🏗️ Engenharia de Dados / Data Engineering

<details>
<summary><strong>🇧🇷 Português</strong></summary>

Os arquivos CSV foram carregados para um banco PostgreSQL utilizando Python.

O processo de ingestão foi desenvolvido para identificar os tipos das colunas e gerar a estrutura necessária para o banco de dados.

Após a ingestão, foram utilizadas consultas SQL e views para preparar os dados para as análises e visualizações.

Entre as transformações realizadas estão:

* tratamento e validação dos dados;
* relacionamento entre pedidos, clientes e produtos;
* agregações de vendas;
* criação de métricas de clientes;
* criação de uma dimensão de datas;
* preparação dos dados utilizados no Power BI.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

The CSV files were loaded into a PostgreSQL database using Python.

The ingestion process was designed to infer column types and generate the necessary database structure.

After ingestion, SQL queries and views were used to prepare the data for analysis and visualization.

The main transformations included:

* data validation and processing;
* relationships between orders, customers, and products;
* sales aggregations;
* customer-level metrics;
* calendar dimension creation;
* preparation of datasets for Power BI.

</details>

---

## 👥 Análise de clientes / Customer Analysis

<details>
<summary><strong>🇧🇷 Português</strong></summary>

Foi realizada uma análise do comportamento dos clientes considerando métricas como:

* faturamento total;
* frequência de compras;
* ticket médio;
* diversidade de categorias consumidas.

Também foi realizada uma segmentação de clientes considerados **Elite**, utilizando critérios definidos durante a análise.

Esses clientes foram posteriormente utilizados em análises específicas no dashboard, permitindo observar sua contribuição para o faturamento e seu comportamento ao longo do tempo.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

Customer behavior was analyzed using metrics such as:

* total revenue;
* purchase frequency;
* average order value;
* category diversity.

A group of **Elite customers** was also identified based on criteria defined during the analysis.

These customers were then used in specific dashboard analyses to evaluate their contribution to revenue and their behavior over time.

</details>

---

## 📅 Dimensão calendário / Calendar Dimension

<details>
<summary><strong>🇧🇷 Português</strong></summary>

Foi criada uma dimensão de datas utilizando `generate_series` no PostgreSQL.

A dimensão contempla todas as datas do período analisado, inclusive dias sem vendas.

Isso permite realizar análises temporais de forma consistente, evitando que dias sem movimentação sejam simplesmente removidos dos resultados.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

A calendar dimension was created using PostgreSQL's `generate_series`.

The dimension contains every date within the analyzed period, including dates with no sales.

This allows time-based analyses to remain consistent and prevents days without transactions from being automatically excluded from the results.

</details>

---

## 🤖 Sistema de recomendação / Recommendation System

<details>
<summary><strong>🇧🇷 Português</strong></summary>

Foi desenvolvido um sistema de recomendação baseado na interação entre clientes e produtos.

Inicialmente, foi construída uma matriz **Cliente × Produto**, na qual:

* as linhas representam clientes;
* as colunas representam produtos;
* o valor indica se o cliente comprou ou não determinado produto.

A matriz foi transformada em uma representação binária de presença/ausência e, posteriormente, foi utilizada a **similaridade de cosseno** para identificar produtos com padrões de compra semelhantes.

**Limitação:** uma das principais limitações desse método é que ele considera apenas a presença ou ausência de uma compra. Por exemplo, um cliente que comprou determinado produto uma vez possui a mesma representação que um cliente que comprou o mesmo produto vinte vezes. Dessa forma, o modelo não considera a frequência ou intensidade de compra, podendo recomendar produtos que apenas compartilham clientes, sem diferenciar adequadamente compras ocasionais de compras recorrentes.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

A product recommendation system was developed based on customer-product interactions.

First, a **Customer × Product** interaction matrix was created, where:

* rows represent customers;
* columns represent products;
* values indicate whether a customer purchased a given product.

The matrix was converted into a binary presence/absence representation and **cosine similarity** was then used to identify products with similar purchase patterns.

**Limitation:** one of the main limitations of this approach is that it only considers whether a purchase occurred, rather than how frequently the product was purchased. For example, a customer who purchased a product once has the same representation as a customer who purchased it twenty times. Therefore, the model does not capture purchase frequency or intensity, which means it may recommend products simply because they share customers, without distinguishing occasional purchases from recurring purchasing behavior.

</details>

---

## 📈 Previsão de demanda / Demand Forecasting

<details>
<summary><strong>🇧🇷 Português</strong></summary>

Para a previsão de demanda, foi utilizado como baseline um modelo de **média móvel dos últimos três meses**.

O produto utilizado na avaliação foi: **Bússola de Bordo 702**

O período de treinamento foi limitado a **31/12/2025**, enquanto o primeiro trimestre de 2026 foi utilizado como período de teste.

**Resultados:**

| Mês            | Vendas reais | Vendas previstas |
| -------------- | -----------: | ---------------: |
| Janeiro/2026   |           79 |            38    |
| Fevereiro/2026 |           68 |            40    |
| Março/2026     |           60 |            33    |

O **MAE (Mean Absolute Error)** obtido foi de aproximadamente **31,49**.

A soma das previsões para o primeiro trimestre de 2026 foi de aproximadamente **113 unidades**.

O resultado indica que o baseline possui limitações para representar completamente o comportamento da demanda. Uma possível evolução seria utilizar modelos capazes de considerar tendência, sazonalidade e outras variáveis relevantes.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

For demand forecasting, a **three-month moving average** was used as the baseline model.

The evaluated product was: **Bússola de Bordo 702**

The training period was limited to **December 31, 2025**, while the first quarter of 2026 was used as the test period.

**Results:**

| Month         | Actual sales | Forecast |
| ------------- | -----------: | -------: |
| January 2026  |           79 |    38.67 |
| February 2026 |           68 |    40.22 |
| March 2026    |           60 |    33.63 |

The resulting **MAE (Mean Absolute Error)** was approximately **31.49**.

The total forecast for the first quarter of 2026 was approximately **113 units**.

The results indicate that the baseline has limitations when representing the complete demand pattern. A potential improvement would be to use forecasting models capable of capturing trend, seasonality, and other relevant variables.

</details>

---

## 📊 Dashboard

<details>
<summary><strong>🇧🇷 Português</strong></summary>

Foi desenvolvido um dashboard no **Power BI** para apresentar os principais indicadores e análises obtidos durante o projeto.

O dashboard foi organizado em diferentes páginas, incluindo:

**Visão Geral** — faturamento total; número de pedidos; clientes atendidos; quantidade de itens vendidos; evolução do faturamento ao longo do tempo.

**Clientes** — clientes com maior ticket médio; categorias mais consumidas pelos clientes Elite; evolução mensal do faturamento dos clientes Elite.

**Vendas** — faturamento por dia da semana; evolução do volume de vendas; vendas reais versus previsões.

**Produtos** — produtos com maior faturamento; produtos com maior volume vendido; análise por categoria.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

A **Power BI dashboard** was developed to present the main KPIs and analyses produced throughout the project.

The dashboard was organized into different pages:

**Overview** — total revenue; number of orders; number of customers served; total items sold; revenue evolution over time.

**Customers** — customers with the highest average order value; most purchased categories among Elite customers; monthly revenue generated by Elite customers.

**Sales** — revenue by day of the week; monthly sales volume evolution; actual sales versus forecasts.

**Products** — highest-revenue products; highest-volume products; category-level analysis.

</details>

---

## 🔎 Principais insights / Key Insights

<details>
<summary><strong>🇧🇷 Português</strong></summary>

* existência de variações sazonais no volume de vendas;
* maiores volumes no início do ano;
* redução das vendas após o início do ano;
* retomada do crescimento a partir de aproximadamente agosto;
* crescimento geral do volume/faturamento ao longo do período analisado;
* concentração relevante de faturamento em determinados produtos e clientes.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

* seasonal variations in sales volume;
* higher sales volumes at the beginning of the year;
* a decline after the beginning of the year;
* renewed growth starting around August;
* an overall growth trend in sales/revenue over the analyzed period;
* significant revenue concentration among certain products and customers.

</details>

---

## ▶️ Como executar o projeto / How to Run

<details>
<summary><strong>🇧🇷 Português</strong></summary>

**1. Clonar o repositório**

```bash
git clone https://github.com/sugarfreecat/lh_nauticals
cd lh_nauticals
```

**2. Subir o PostgreSQL com Docker**

Suba o container do PostgreSQL utilizando o `docker-compose.yml` disponível na seção [🐳 Docker](#-docker):

```bash
docker compose up -d
```

Configure as credenciais de conexão (usuário, senha, banco e porta) de acordo com o que foi definido no `docker-compose.yml`.

**3. Gerar o script schema.sql**

```bash
cd ingestion
python schema.py
```

**4. Executar a ingestão**

```bash
cd ingestion
python loading.py
```

**5. Executar as análises**

Os scripts Python relacionados à previsão de demanda e ao sistema de recomendação podem ser executados individualmente.

**6. Abrir o dashboard**

Abra o arquivo `.pbix` utilizando **Power BI Desktop**.

</details>

<details>
<summary><strong>🇺🇸 English</strong></summary>

**1. Clone the repository**

```bash
git clone https://github.com/sugarfreecat/lh_nauticals
cd lh_nauticals
```

**2. Start PostgreSQL with Docker**

Start the PostgreSQL container using the `docker-compose.yml` file from the [🐳 Docker](#-docker) section:

```bash
docker compose up -d
```

Set the connection credentials (user, password, database, and port) according to what was defined in `docker-compose.yml`.

**3. Generate the schema.sql script**

```bash
cd ingestion
python schema.py
```

**3. Run the ingestion process**

```bash
cd ingestion
python loading.py
```

**5. Run the analyses**

The Python scripts for demand forecasting and product recommendation can be executed independently.

**6. Open the dashboard**

Open the `.pbix` file using **Power BI Desktop**.

</details>

---

## 📁 Estrutura do projeto / Project Structure

```text
.
├── data/
│   └── *.csv
│
├── sql/
│   ├── schema.sql
│   └── views/
│
├── python/
│   ├── ingestion/
│   ├── forecasting/
│   └── recommendation/
│
├── dashboard/
│   └── *.pbix
│
├── docker-compose.yml
│
└── README.md
```

---

## 👩‍💻 Autora / Author

**Giovanna Simões**

🇧🇷 Projeto desenvolvido como parte do **desafio técnico da Indicium AI — LH Nauticals**.
🇺🇸 Project developed as part of the **Indicium AI — LH Nauticals technical challenge**.
