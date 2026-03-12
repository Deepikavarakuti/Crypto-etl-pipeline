import psycopg2

def load_data(df):

    conn = psycopg2.connect(
        host="localhost",
        database="crypto_db",
        user="postgres",
        password="password"
    )

    cur = conn.cursor()

    for index, row in df.iterrows():
        cur.execute("""
            INSERT INTO crypto_prices (crypto_name, price_usd, timestamp)
            VALUES (%s, %s, %s)
        """, (row["crypto_name"], row["price_usd"], row["timestamp"]))

    conn.commit()
    cur.close()
    conn.close()