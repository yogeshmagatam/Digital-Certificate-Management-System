from fpdf import FPDF

def generate_pdf(data, output_path, qr_blob, template_type=1):
    pdf = FPDF('L', 'mm', 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    if template_type == 1:
        # Template 1: Gold border, watermark, blue/green highlights
        pdf.set_draw_color(212, 175, 55)
        pdf.set_line_width(3)
        pdf.rect(10, 10, 277, 190)
        pdf.set_text_color(230, 230, 230)
        pdf.set_font("Arial", 'B', 80)
        pdf.set_xy(0, 80)
        pdf.cell(297, 40, "CERTIFICATE", align='C', ln=1)
        pdf.set_xy(10, 10)
        pdf.set_text_color(44, 62, 80)
        pdf.set_font("Times", 'B', 36)
        pdf.ln(20)
        pdf.cell(0, 20, "Certificate of Achievement", ln=True, align='C')
        pdf.set_font("Arial", '', 20)
        pdf.set_text_color(52, 73, 94)
        pdf.ln(5)
        pdf.cell(0, 15, "This is to certify that", ln=True, align='C')
        pdf.ln(5)
        pdf.set_font("Times", 'B', 40)
        pdf.set_text_color(41, 128, 185)
        pdf.cell(0, 22, data.get("name", ""), ln=True, align='C')
        pdf.set_font("Arial", '', 26)
        pdf.set_text_color(44, 62, 80)
        pdf.ln(2)
        pdf.cell(0, 16, f"has successfully participated in", ln=True, align='C')
        pdf.set_font("Arial", 'B', 32)
        pdf.set_text_color(39, 174, 96)
        event = data.get("event", "")
        pdf.cell(0, 18, event, ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", '', 14)
        pdf.set_text_color(44, 62, 80)
        date = data.get("date", "")
        email = data.get("email", "")
        pdf.cell(0, 10, f"Date: {date}", ln=True, align='C')
        if email:
            pdf.cell(0, 10, f"Email: {email}", ln=True, align='C')
       # Signature block moved above gold margin
        pdf.set_y(170)  # move above bottom gold margin
        pdf.set_font("Arial", '', 16)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 6, "__________________________", ln=True, align='R')

        pdf.set_font("Arial", '', 14)
        pdf.cell(0, 6, "Authorized Signature", ln=True, align='R')

        pdf.set_font("Arial", 'I', 12)
        pdf.cell(0, 6, "Organization Name", ln=True, align='R')

    elif template_type == 2:
        # Template 2: Blue border, no watermark, different layout/colors
        pdf.set_draw_color(41, 128, 185)
        pdf.set_line_width(4)
        pdf.rect(15, 15, 267, 180)
        pdf.set_text_color(44, 62, 80)
        pdf.set_font("Helvetica", 'B', 38)
        pdf.ln(25)
        pdf.cell(0, 22, "Certificate of Excellence", ln=True, align='C')
        pdf.set_font("Helvetica", '', 18)
        pdf.set_text_color(52, 73, 94)
        pdf.ln(8)
        pdf.cell(0, 12, "Presented to", ln=True, align='C')
        pdf.ln(4)
        pdf.set_font("Helvetica", 'B', 36)
        pdf.set_text_color(39, 174, 96)
        pdf.cell(0, 20, data.get("name", ""), ln=True, align='C')
        pdf.set_font("Helvetica", '', 22)
        pdf.set_text_color(41, 128, 185)
        pdf.ln(4)
        pdf.cell(0, 14, f"For outstanding participation in", ln=True, align='C')
        pdf.set_font("Helvetica", 'B', 28)
        pdf.set_text_color(44, 62, 80)
        event = data.get("event", "")
        pdf.cell(0, 16, event, ln=True, align='C')
        pdf.ln(8)
        pdf.set_font("Helvetica", '', 14)
        pdf.set_text_color(44, 62, 80)
        date = data.get("date", "")
        email = data.get("email", "")
        pdf.cell(0, 10, f"Date: {date}", ln=True, align='C')
        if email:
            pdf.cell(0, 10, f"Email: {email}", ln=True, align='C')
        pdf.ln(18)
        pdf.set_font("Helvetica", '', 15)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 6, "__________________________", ln=True, align='R')
        pdf.cell(0, 5, "Director", ln=True, align='R')
        pdf.set_font("Helvetica", 'I', 12)
        pdf.cell(0, 5, "Your Organization", ln=True, align='R')
    else:
        raise ValueError("Unknown template_type")

    # Add QR code if provided
    print(f"Adding QR code to PDF: bytes")
    if qr_blob:
        print("QR code blob provided")
        qr_blob.seek(0)
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp.write(qr_blob.read())
            tmp.flush()
            try:
                # Place QR differently for each template
                if template_type == 1:
                    pdf.image(tmp.name, x=15, y=150, w=40, h=40)
                elif template_type == 2:
                    pdf.image(tmp.name, x=230, y=30, w=35, h=35)
            except Exception as e:
                print("QR image error:", e)
    pdf.output(output_path)
    return output_path