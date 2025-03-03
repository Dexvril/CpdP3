from django.db import connection

def query(sql, params=None):
    with connection.cursor() as cursor:
        cursor.execute(sql, params)

        # Jika query adalah SELECT, ambil hasilnya
        if sql.strip().lower().startswith("select"):
            return dictfetchall(cursor)
        else:
            return None  # Untuk DELETE/INSERT/UPDATE, kembalikan None

def dictfetchall(cursor):
    """Mengambil semua hasil query dalam bentuk dictionary."""
    columns = [col[0] for col in cursor.description] if cursor.description else []
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
