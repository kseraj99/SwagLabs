#
# def test_sysdate(db_connection):
#     cursor = db_connection.cursor()
#     cursor.execute("SELECT * from empinfo")
#     result = cursor.fetchone()
#     assert result is not None
#     print(f"Current DB date: {result[0]}")
#     cursor.close()


def test_sysdate(db_connection):
    """Test that we can fetch sysdate from Oracle DB"""
    cursor = db_connection.cursor()
    cursor.execute("select * from empinfo")
    result = cursor.fetchone()

    assert result is not None, "No data returned from DB"
    print(f"These are the tables data: {result}")

    cursor.close()