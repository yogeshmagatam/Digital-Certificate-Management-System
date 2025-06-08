from fpdf import FPDF
import os

def generate_pdf(data, output_path, qr_blob, template_type=1):
    pdf = FPDF('L', 'mm', 'A4')
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)

    # Define absolute path to the logo
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    logo_path = os.path.join(base_dir, "static", "images", "hmits_logo.png")

    print(f"Attempting to load logo from: {logo_path}")
    print(f"Logo file exists: {os.path.exists(logo_path)}")

    if template_type == 1:
        # Template 1: Classic Gold and Black
        # Single gold border
        pdf.set_draw_color(212, 175, 55)  # Gold
        pdf.set_line_width(3)
        pdf.rect(10, 10, 277, 190)
        
        # Add logo (Top Left)
        if os.path.exists(logo_path):
            pdf.image(logo_path, x=15, y=18, w=30) # Adjusted x, y, w
            
        # Institution Name
        pdf.set_text_color(44, 62, 80)
        pdf.set_font("Times", 'B', 20)
        pdf.ln(10)
        pdf.cell(0, 15, "HOLY MARY INSTITUTE OF TECHNOLOGY AND SCIENCE", ln=True, align='C')
        
        # Main content
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
        
        # Signature block
        pdf.set_y(170)
        pdf.set_font("Arial", '', 16)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(0, 6, "__________________________", ln=True, align='R')
        pdf.set_font("Arial", '', 14)
        pdf.cell(0, 6, "Authorized Signature", ln=True, align='R')
        pdf.set_font("Arial", 'I', 12)
        pdf.cell(0, 6, "Organization Name", ln=True, align='R')

    elif template_type == 2:
        # Template 2: Modern Minimalist Design
        # Background
        pdf.set_fill_color(245, 245, 245)  # Light gray background
        pdf.rect(0, 0, 297, 210, 'F')
        
        # Decorative top bar
        pdf.set_fill_color(41, 128, 185)  # Blue
        pdf.rect(0, 0, 297, 40, 'F')
        
        # Add logo (Top Left in blue bar)
        if os.path.exists(logo_path):
            pdf.image(logo_path, x=15, y=5, w=30) # Adjusted x, y, w

        # Institution Name
        pdf.set_text_color(255, 255, 255)  # White
        pdf.set_font("Helvetica", 'B', 20)
        pdf.ln(5)
        pdf.cell(0, 15, "HOLY MARY INSTITUTE OF TECHNOLOGY AND SCIENCE", ln=True, align='C')
        
        # Certificate title
        pdf.set_text_color(0, 0, 0)  # Black color
        pdf.set_font("Helvetica", 'B', 32)
        pdf.ln(5)
        pdf.cell(0, 20, "Certificate of Excellence", ln=True, align='C')
        
        # Main content area with subtle border
        pdf.set_draw_color(200, 200, 200)  # Light gray
        pdf.set_line_width(0.5)
        pdf.rect(20, 50, 257, 150)
        
        # Name section
        pdf.set_text_color(41, 128, 185)  # Blue
        pdf.set_font("Helvetica", 'B', 36)
        pdf.ln(20)
        pdf.cell(0, 25, data.get("name", ""), ln=True, align='C')
        
        # Achievement text
        pdf.set_text_color(80, 80, 80)  # Dark gray
        pdf.set_font("Helvetica", '', 18)
        pdf.ln(5)
        pdf.cell(0, 12, "has demonstrated exceptional dedication and", ln=True, align='C')
        pdf.cell(0, 12, "outstanding performance in", ln=True, align='C')
        
        # Event name
        pdf.set_font("Helvetica", 'B', 24)
        pdf.set_text_color(39, 174, 96)  # Green
        event = data.get("event", "")
        pdf.cell(0, 20, event, ln=True, align='C')
        
        # Date and email
        pdf.set_font("Helvetica", '', 14)
        pdf.set_text_color(100, 100, 100)  # Medium gray
        date = data.get("date", "")
        email = data.get("email", "")
        pdf.ln(10)
        pdf.cell(0, 8, f"Date: {date}", ln=True, align='C')
        if email:
            pdf.cell(0, 8, f"Email: {email}", ln=True, align='C')
        
        # Signature section with modern style
        pdf.set_y(250)  # Lower down to bottom of page; adjust as needed
        pdf.set_x(160)  # Move to the right side inside the box (not too close to edge)

        pdf.set_text_color(80, 80, 80)  # Dark gray
        pdf.set_font("Helvetica", '', 14)
        pdf.cell(40, 6, "_____________________", ln=True, align='R')  # Adjusted length
        pdf.set_font("Helvetica", 'B', 12)
        pdf.cell(40, 6, "Director", ln=True, align='R')
        pdf.set_font("Helvetica", 'I', 10)
        pdf.cell(40, 6, "Your Organization", ln=True, align='R')

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
                    pdf.image(tmp.name, x=20, y=160, w=35, h=35)
            except Exception as e:
                print("QR image error:", e)
    pdf.output(output_path)
    return output_path