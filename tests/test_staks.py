import sqlite3

import pytest


def run_query(file):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    with open(file, "r", encoding="utf-8") as f:
        sql = f.read()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result

def test_total_orders():
    assert run_query("tasks/query_01.sql")[0][0] == 10

def test_total_spent():
    assert run_query("tasks/query_02.sql")[0][0] == pytest.approx(1847.46, 0.01)

def test_avg_price_by_category():
    result = dict(run_query("tasks/query_03.sql"))
    assert result["Electronics"] == pytest.approx(249.99, 0.01)
    assert result["Books"] == pytest.approx(12.05, 0.01)
    assert result["Clothing"] == pytest.approx(44.17, 0.01)

def test_total_quantity_per_customer():
    result = dict(run_query("tasks/query_04.sql"))
    assert result["Alice"] == 5
    assert result["Bob"] == 6
    assert result["Charlie"] == 7
    assert result["David"] == 3
    assert result["Eve"] == 1

def test_last_order_per_category():
    result = dict(run_query("tasks/query_05.sql"))
    assert result["Electronics"] == "2024-06-07"
    assert result["Books"] == "2024-06-06"
    assert result["Clothing"] == "2024-06-06"
