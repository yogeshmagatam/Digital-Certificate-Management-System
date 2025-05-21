from fpdf import FPDF

def generate_pdf(data, output_path):
    pdf = FPDF('L', 'mm', 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # Gold border
    pdf.set_draw_color(212, 175, 55)  # Gold color
    pdf.set_line_width(3)
    pdf.rect(10, 10, 277, 190)

    # Light watermark background
    pdf.set_text_color(230, 230, 230)
    pdf.set_font("Arial", 'B', 80)
    pdf.set_xy(0, 80)
    pdf.cell(297, 40, "CERTIFICATE", align='C', ln=1)
    pdf.set_xy(10, 10)  # Reset position

    # Title
    pdf.set_text_color(44, 62, 80)
    pdf.set_font("Times", 'B', 36)
    pdf.ln(20)
    pdf.cell(0, 20, "Certificate of Achievement", ln=True, align='C')

    # Subtitle
    pdf.set_font("Arial", '', 20)
    pdf.set_text_color(52, 73, 94)
    pdf.ln(5)
    pdf.cell(0, 15, "This is to certify that", ln=True, align='C')

    # Recipient Name (larger font)
    pdf.ln(5)
    pdf.set_font("Times", 'B', 40)  # Increased font size
    pdf.set_text_color(41, 128, 185)
    pdf.cell(0, 22, data.get("name", ""), ln=True, align='C')

    # Event Participation Line (larger font)
    pdf.set_font("Arial", '', 26)  # Increased font size
    pdf.set_text_color(44, 62, 80)
    pdf.ln(2)
    pdf.cell(0, 16, f"has successfully participated in", ln=True, align='C')

    # Event Name (larger font)
    pdf.set_font("Arial", 'B', 32)  # Increased font size
    pdf.set_text_color(39, 174, 96)
    event = data.get("event", "")
    pdf.cell(0, 18, event, ln=True, align='C')

    # Date and Email
    pdf.ln(10)
    pdf.set_font("Arial", '', 14)
    pdf.set_text_color(44, 62, 80)
    date = data.get("date", "")
    email = data.get("email", "")
    pdf.cell(0, 10, f"Date: {date}", ln=True, align='C')
    if email:
        pdf.cell(0, 10, f"Email: {email}", ln=True, align='C')

    # Signature line and issuer
    pdf.ln(25)
    pdf.set_font("Arial", '', 16)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(0, 6, "__________________________", ln=True, align='R')
    pdf.cell(0, 5, "Authorized Signature", ln=True, align='R')
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 5, "Organization Name", ln=True, align='R')

    pdf.output(output_path)
    return output_path