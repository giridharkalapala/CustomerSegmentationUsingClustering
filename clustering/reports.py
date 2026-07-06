import pandas as pd
from django.http import HttpResponse
from reportlab.pdfgen import canvas


def export_csv(df):

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="customers.csv"'

    df.to_csv(response, index=False)

    return response


def export_excel(df):

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    response["Content-Disposition"] = 'attachment; filename="customers.xlsx"'

    with pd.ExcelWriter(response, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)

    return response


def export_pdf(df):

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="customers.pdf"'

    p = canvas.Canvas(response)

    y = 800

    p.setFont("Helvetica-Bold", 14)
    p.drawString(40, y, "Customer Segmentation Report")

    y -= 30

    p.setFont("Helvetica", 10)

    for _, row in df.iterrows():

        text = (
            f"ID:{row['CustomerID']}   "
            f"Gender:{row['Gender']}   "
            f"Age:{row['Age']}   "
            f"Income:{row['Annual_Income']}   "
            f"Spending:{row['Spending_Score']}   "
            f"Segment:{row['Segment']}"
        )

        p.drawString(40, y, text)

        y -= 18

        if y < 40:
            p.showPage()
            y = 800

    p.save()

    return response