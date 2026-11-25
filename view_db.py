"""
Database Viewer Utility: Inspects and exports all tables and records in aegis_live.db
Generates database_view.html so you can view all tables and records in your browser.
"""

import sqlite3
import os
import json

def view_database(db_path: str = "aegis_live.db"):
    if not os.path.exists(db_path):
        print(f"Error: {db_path} does not exist!")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    tables = [r[0] for r in cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name").fetchall()]

    print("=" * 80)
    print(f" DATABASE CONTENT REPORT FOR: {os.path.abspath(db_path)}")
    print(f" Total Tables Found: {len(tables)}")
    print("=" * 80)

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Aegis Database Inspector</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; padding: 24px; }}
        h1 {{ color: #38bdf8; margin-bottom: 8px; }}
        .meta {{ color: #94a3b8; font-size: 14px; margin-bottom: 24px; }}
        .table-card {{ background: #1e293b; border-radius: 8px; padding: 16px; margin-bottom: 24px; border: 1px solid #334155; }}
        h2 {{ color: #a5b4fc; font-size: 18px; margin-top: 0; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 13px; }}
        th, td {{ padding: 8px 12px; text-align: left; border-bottom: 1px solid #334155; }}
        th {{ background: #0f172a; color: #38bdf8; font-weight: 600; }}
        tr:hover {{ background: rgba(255,255,255,0.03); }}
        .empty {{ color: #64748b; font-style: italic; }}
    </style>
</head>
<body>
    <h1>Aegis Live Database Inspector</h1>
    <div class="meta">Database File: <code>{os.path.abspath(db_path)}</code> | File Size: {os.path.getsize(db_path):,} bytes</div>
"""

    for table in tables:
        rows = cursor.execute(f"SELECT * FROM {table}").fetchall()
        print(f"\nTABLE: {table} ({len(rows)} records)")

        html_content += f"""
        <div class="table-card">
            <h2>Table: <code>{table}</code> ({len(rows)} rows)</h2>
        """

        if rows:
            columns = rows[0].keys()
            html_content += "<table><thead><tr>"
            for col in columns:
                html_content += f"<th>{col}</th>"
            html_content += "</tr></thead><tbody>"

            for r in rows:
                html_content += "<tr>"
                for col in columns:
                    val = r[col]
                    html_content += f"<td>{val if val is not None else '<span class=\"empty\">NULL</span>'}</td>"
                html_content += "</tr>"
            html_content += "</tbody></table>"

            # Print first 2 rows to terminal
            for r in rows[:3]:
                print("  ", dict(r))
            if len(rows) > 3:
                print(f"  ... and {len(rows)-3} more rows")
        else:
            html_content += "<p class='empty'>No rows yet in this table.</p>"
            print("  (Empty table)")

        html_content += "</div>"

    html_content += "</body></html>"

    with open("database_view.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("\n" + "=" * 80)
    print(" Exported visual HTML report: database_view.html")
    print(" Double click database_view.html in Windows Explorer to see all tables in your browser!")
    print("=" * 80)

if __name__ == "__main__":
    view_database()
