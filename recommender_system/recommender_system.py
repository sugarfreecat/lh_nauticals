import pandas as pd
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

CSV_DIR = Path(__file__).resolve().parent.parent / "1-lh_nautical_csv"
products_csv = CSV_DIR / "products.csv"
product_variants_csv = CSV_DIR / "product_variants.csv"
orders_csv = CSV_DIR / "orders.csv"
order_items_csv = CSV_DIR / "order_items.csv"

chosen_product = "Motor de Popa 1949"

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
    )[["customer_id", "product_variant_id"]]

    orders_items_variants = orders_items.merge(
        product_variants,
        left_on="product_variant_id",
        right_on="id"
    )[["customer_id", "product_id"]]

    unified_df = orders_items_variants.merge(
        products,
        left_on="product_id",
        right_on="id"
    )[["customer_id", "product_id", "name"]]

    return unified_df

def user_product_matrix(unified_df):
    matrix = pd.crosstab(
        unified_df["customer_id"],
        unified_df["product_id"]
    )

    matrix = (matrix > 0).astype(int)

    return matrix.T

def get_cosine_similarity(user_product_matrix):
    similarity = cosine_similarity(user_product_matrix)
    similarity_df = pd.DataFrame(
        similarity,
        index=user_product_matrix.index,
        columns=user_product_matrix.index
    )
    return similarity_df

def get_chosen_product_id(products, chosen_product):
    chosen_product_id = products[products["name"] == chosen_product]["id"].values[0]
    return chosen_product_id

def get_top_n_similar_products(similarity_df, chosen_product_id, n=5):
    similarity_chosen_product = similarity_df.loc[chosen_product_id]
    similarity_chosen_product = similarity_chosen_product.drop(chosen_product_id)
    top_n_similar_products = similarity_chosen_product.sort_values(ascending=False).head(n).rename("similarity")
    return top_n_similar_products

def get_final_result(df, products):
    result = df.reset_index()
    result = result.merge(
        products,
        left_on="product_id",
        right_on="id"
    )[["product_id", "name", "similarity"]]

    return result

if __name__ == "__main__":
    products, product_variants, orders, order_items = load_data()
    unified_df = merge_data(products, product_variants, orders, order_items)

    chosen_product_id = get_chosen_product_id(products, chosen_product)

    matrix = user_product_matrix(unified_df)
    similarity = get_cosine_similarity(matrix)

    top5 = get_top_n_similar_products(similarity, chosen_product_id, n=5)
    resultado = get_final_result(top5, products)

    print(f"Produtos mais similares ao produto escolhido ({chosen_product}):")
    print(resultado)