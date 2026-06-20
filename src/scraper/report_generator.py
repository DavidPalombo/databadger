from pathlib import Path

def generate_html_report(data, filename):
    pages_discovered = data["summary"]["pages_discovered"]
    links_found =  data["summary"]["links_found"]
    forms_found = data["summary"]["forms_found"]

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DataBadger Report</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
            }}

            th {{
                text-align: left;
            }}
        </style>
    </head>
    <body>

    <h1>DataBadger Scan Report</h1>

    <p><strong>Target:</strong> {data["target"]}</p>

    <p><strong>Pages Discovered:</strong> {pages_discovered}</p>
    <p><strong>Links Found:</strong> {links_found}</p>
    <p><strong>Forms Found:</strong> {forms_found}</p>

    <h2>Pages</h2>

    <table>
    <tr>
        <th>URL</th>
        <th>Status</th>
        <th>Links</th>
        <th>Forms</th>
    </tr>
    """

    for page in data["pages"]:
        html += f"""
        <tr>
            <td>{page["url"]}</td>
            <td>{page["status_code"]}</td>
            <td>{len(page["links"])}</td>
            <td>{len(page["forms"])}</td>
        </tr>
        """

    html += """
    </table>

    </body>
    </html>
    """

    Path(filename).write_text(html, encoding = "utf-8")

