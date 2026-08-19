import pandas as pd
from pathlib import Path

CSV_DIR = Path(__file__).resolve().parent.parent.parent / "data"
products_csv = CSV_DIR / "products.csv"
product_variants_csv = CSV_DIR / "product_variants.csv"
orders_csv = CSV_DIR / "orders.csv"
order_items_csv = CSV_DIR / "order_items.csv"

def load_data():
    products = pd.read_csv(products_csv)
    product_variants = pd.read_csv(product_variants_csv)
    orders = pd.read_csv(orders_csv)
    order_items = pd.read_csv(order_items_csv)

    return products, product_variants, orders, order_items

def merge_data(products, product_variants, orders, order_items):
    orders_items = orders.merge(
        order_items,
        left_on="id",
        right_on="order_id"
    )[["order_id","placed_at", "product_variant_id", "quantity"]]

    orders_items_variants = orders_items.merge(
        product_variants,
        left_on="product_variant_id",
        right_on="id"
    )[["order_id", "placed_at", "product_id", "quantity"]]

    unified_df = orders_items_variants.merge(
        products,
        left_on="product_id",
        right_on="id"
    )[["placed_at", "quantity", "name"]]

    return unified_df

def prepare_data(unified_df):
    bussola_df = unified_df[unified_df["name"] == "Bússola de Bordo 702"].copy()
    bussola_df["placed_at"] = pd.to_datetime(bussola_df["placed_at"])
    bussola_df = bussola_df.set_index("placed_at").sort_index()

    monthly = bussola_df["quantity"].resample("ME").sum()
    full_months = pd.date_range(start=monthly.index.min(), end=monthly.index.max(), freq="ME") # para garantir que o resample
    monthly = monthly.reindex(full_months, fill_value=0) # não está deixando nenhum mês sem vendas escapar

    return monthly

def split_data(monthly):
    training = monthly[monthly.index <= "2025-12-31"]
    test = monthly[(monthly.index > "2025-12-31") & (monthly.index <= "2026-03-31")]

    return training, test

def predict_sales(training, test):
    predictions = []
    history = list(training)

    for _ in test:
        prediction = sum(history[-3:]) / 3
        predictions.append(prediction)
        history.append(prediction)

    return predictions

def format_predictions(test, predictions):
    results = pd.DataFrame({
        "mes": test.index,
        "vendas_reais": test.values,
        "vendas_previstas": predictions
    })

    return results

def mean_absolute_error(results):
    return (results["vendas_reais"] - results["vendas_previstas"]).abs().mean()

def total_sum_of_sales(results):
    return results["vendas_previstas"].sum()

if __name__ == "__main__":
    products, product_variants, orders, order_items = load_data()
    unified_df = merge_data(products, product_variants, orders, order_items)
    monthly = prepare_data(unified_df)
    training, test = split_data(monthly)

    predictions = predict_sales(training, test)
    results = format_predictions(test, predictions)
    mae = mean_absolute_error(results)
    total_predicted = total_sum_of_sales(results)
    print(results)
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"Soma Total da Previsão de Vendas: {total_predicted:.0f}")