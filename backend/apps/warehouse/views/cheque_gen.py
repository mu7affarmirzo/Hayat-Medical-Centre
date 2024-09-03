from django.shortcuts import get_object_or_404
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from apps.warehouse.models import WarehouseChequeModel


def generate_cheque_pdf(cheque_id):
    # Fetch the cheque from the database
    cheque = WarehouseChequeModel.objects.get(id=cheque_id)
    items = cheque.cheque_items.all()
    # pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))

    # Create a Django HttpResponse object to serve the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="cheque_{cheque.cheque_number}.pdf"'

    # Set up the PDF canvas
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # Title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 30, f"Hayat Medical Centre")

    # Cheque details
    p.setFont("Helvetica", 12)
    p.drawString(100, height - 60, f"Номер чека: {cheque.cheque_number}")
    p.drawString(100, height - 80, f"Patient: {cheque.patient.full_name if cheque.patient else 'Unknown'}")
    p.drawString(100, height - 100, f"Date: {cheque.created_at.strftime('%d.%m.%Y %H:%M:%S')}")
    p.drawString(100, height - 120, f"Cashier: {cheque.created_by.username}")

    # Table header
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, height - 150, "№")
    p.drawString(80, height - 150, "Item Name")
    p.drawString(250, height - 150, "Quantity")
    p.drawString(350, height - 150, "Price")
    p.drawString(450, height - 150, "Total")

    # Table content
    p.setFont("Helvetica", 12)
    y_position = height - 170
    for index, item in enumerate(items, start=1):
        p.drawString(50, y_position, str(index))
        p.drawString(80, y_position, item.item.item.name)
        p.drawString(250, y_position, str(item.quantity))
        p.drawString(350, y_position, f"{item.price:,}")
        p.drawString(450, y_position, f"{item.overall_price:,}")
        y_position -= 20

    # Total price
    p.drawString(350, y_position - 20, "Overall Total:")
    p.setFont("Helvetica-Bold", 12)
    p.drawString(450, y_position - 20, f"{cheque.total_price:,}")

    # Footer
    p.setFont("Helvetica", 10)
    p.drawString(100, y_position - 60, f"State: {cheque.state}")

    # Finalize the PDF
    p.showPage()
    p.save()

    return response

