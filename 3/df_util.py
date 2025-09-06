from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def get_product_category_pairs(products_df: DataFrame, categories_df: DataFrame, product_category_df: DataFrame) -> DataFrame:
    result = (
        products_df.alias("p")
        .join(product_category_df.alias("pc"), col("p.product_id") == col("pc.product_id"), "left")
        .join(categories_df.alias("c"), col("pc.category_id") == col("c.category_id"), "left")
        .select(col("p.product_name").alias("product_name"), col("c.category_name").alias("category_name"))
    )
    return result