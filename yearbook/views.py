"""
Yearbook Views - PDF Generation
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from students.models import Student
from lecturers.models import Lecturer
from school_pages.models import SchoolPage
from core.models import SiteSettings
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO
import os


@staff_member_required
def generate_yearbook(request):
    if request.method == 'POST':
        buffer = generate_yearbook_pdf()
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="CPS_Legacy_Chronicle_2026.pdf"'
        messages.success(request, 'Yearbook generated successfully!')
        return response

    settings = SiteSettings.get_instance()
    student_count = Student.objects.filter(is_approved=True).count()
    lecturer_count = Lecturer.objects.filter(is_active=True).count()

    context = {
        'student_count': student_count,
        'lecturer_count': lecturer_count,
        'settings': settings,
    }
    return render(request, 'yearbook/generate.html', context)


def generate_yearbook_pdf():
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()
    navy = HexColor('#0A1F44')
    gold = HexColor('#D4AF37')
    white_color = HexColor('#FFFFFF')

    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=28,
        textColor=navy,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=20
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=gold,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=10
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=navy,
        fontName='Helvetica-Bold',
        spaceAfter=12,
        spaceBefore=12
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8
    )

    name_style = ParagraphStyle(
        'CustomName',
        parent=styles['Normal'],
        fontSize=11,
        textColor=navy,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER
    )

    matric_style = ParagraphStyle(
        'CustomMatric',
        parent=styles['Normal'],
        fontSize=9,
        textColor=gold,
        alignment=TA_CENTER
    )

    story = []

    # COVER PAGE
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("CPS LEGACY CHRONICLE", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("CLASS OF 2026", subtitle_style))
    story.append(Spacer(1, 0.2*inch))

    settings = SiteSettings.get_instance()
    story.append(Paragraph(f"{settings.department}", ParagraphStyle(
        'Dept', parent=styles['Normal'], fontSize=12, alignment=TA_CENTER,
        textColor=navy, fontName='Helvetica-Bold'
    )))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"{settings.university}", ParagraphStyle(
        'Univ', parent=styles['Normal'], fontSize=11, alignment=TA_CENTER,
        textColor=navy
    )))
    story.append(Spacer(1, 0.3*inch))

    # Gold line
    line_data = [['']]
    line_table = Table(line_data, colWidths=[6*inch])
    line_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), gold),
        ('LINEBELOW', (0, 0), (-1, -1), 3, gold),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 0.5*inch))

    # Group photo placeholder
    story.append(Paragraph("[ Group Photo Placeholder ]", ParagraphStyle(
        'Photo', parent=styles['Normal'], fontSize=10, alignment=TA_CENTER,
        textColor=colors.gray
    )))
    story.append(PageBreak())

    # SCHOOL PAGES
    school_pages = SchoolPage.objects.filter(is_active=True).order_by('order')
    for page in school_pages:
        story.append(Paragraph(page.get_page_type_display(), heading_style))
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(f"{page.title}", ParagraphStyle(
            'Title2', parent=styles['Normal'], fontSize=14, textColor=navy,
            fontName='Helvetica-Bold'
        )))
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(f"<b>{page.full_name}</b>", name_style))
        story.append(Spacer(1, 0.2*inch))

        if page.photo and os.path.exists(page.photo.path):
            img = Image(page.photo.path, width=2*inch, height=2.5*inch)
            img.hAlign = 'CENTER'
            story.append(img)
            story.append(Spacer(1, 0.2*inch))

        story.append(Paragraph(f"<b>Message:</b> {page.message}", body_style))
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(f"<b>About:</b> {page.description}", body_style))
        if page.office:
            story.append(Spacer(1, 0.05*inch))
            story.append(Paragraph(f"<i>Office: {page.office}</i>", ParagraphStyle(
                'Office', parent=styles['Normal'], fontSize=9, textColor=colors.gray
            )))
        story.append(PageBreak())

    # LECTURERS SECTION
    story.append(Paragraph("OUR LECTURERS", ParagraphStyle(
        'LecTitle', parent=heading_style, fontSize=22, alignment=TA_CENTER
    )))
    story.append(Spacer(1, 0.2*inch))

    # Senior Lecturers
    senior_lecturers = Lecturer.objects.filter(lecturer_type='senior', is_active=True)
    if senior_lecturers.exists():
        story.append(Paragraph("Senior Lecturers", heading_style))
        story.append(Spacer(1, 0.1*inch))

        lec_data = []
        row = []
        for i, lecturer in enumerate(senior_lecturers):
            cell_content = []
            if lecturer.photo and os.path.exists(lecturer.photo.path):
                img = Image(lecturer.photo.path, width=1.2*inch, height=1.5*inch)
                cell_content.append(img)
            else:
                cell_content.append(Paragraph("[No Photo]", matric_style))
            cell_content.append(Paragraph(f"{lecturer.title} {lecturer.full_name}", name_style))
            if lecturer.specialization:
                cell_content.append(Paragraph(lecturer.specialization, matric_style))
            row.append(cell_content)
            if (i + 1) % 3 == 0:
                lec_data.append(row)
                row = []
        if row:
            lec_data.append(row)

        if lec_data:
            lec_table = Table(lec_data, colWidths=[2.2*inch]*3)
            lec_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ]))
            story.append(lec_table)
        story.append(PageBreak())

    # Junior Lecturers
    junior_lecturers = Lecturer.objects.filter(lecturer_type='junior', is_active=True)
    if junior_lecturers.exists():
        story.append(Paragraph("Junior Lecturers", heading_style))
        story.append(Spacer(1, 0.1*inch))

        lec_data = []
        row = []
        for i, lecturer in enumerate(junior_lecturers):
            cell_content = []
            if lecturer.photo and os.path.exists(lecturer.photo.path):
                img = Image(lecturer.photo.path, width=1.2*inch, height=1.5*inch)
                cell_content.append(img)
            else:
                cell_content.append(Paragraph("[No Photo]", matric_style))
            cell_content.append(Paragraph(f"{lecturer.title} {lecturer.full_name}", name_style))
            if lecturer.specialization:
                cell_content.append(Paragraph(lecturer.specialization, matric_style))
            row.append(cell_content)
            if (i + 1) % 3 == 0:
                lec_data.append(row)
                row = []
        if row:
            lec_data.append(row)

        if lec_data:
            lec_table = Table(lec_data, colWidths=[2.2*inch]*3)
            lec_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('TOPPADDING', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ]))
            story.append(lec_table)
        story.append(PageBreak())

    # STUDENTS SECTION
    story.append(Paragraph("CLASS OF 2026", ParagraphStyle(
        'StuTitle', parent=heading_style, fontSize=22, alignment=TA_CENTER
    )))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Computer Science Students", subtitle_style))
    story.append(Spacer(1, 0.3*inch))

    students = Student.objects.filter(is_approved=True).order_by('full_name')
    student_data = []
    row = []
    for i, student in enumerate(students):
        cell_content = []
        if student.image and os.path.exists(student.image.path):
            img = Image(student.image.path, width=1.2*inch, height=1.5*inch)
            cell_content.append(img)
        else:
            cell_content.append(Paragraph(f"<b>{student.get_initials()}</b>", ParagraphStyle(
                'Init', parent=styles['Normal'], fontSize=24, alignment=TA_CENTER,
                textColor=navy
            )))
        cell_content.append(Paragraph(student.full_name, name_style))
        cell_content.append(Paragraph(student.matric_number, matric_style))
        if student.favourite_programming_language:
            cell_content.append(Paragraph(
                f"<i>{student.get_favourite_programming_language_display()}</i>",
                ParagraphStyle('Lang', parent=styles['Normal'], fontSize=8, alignment=TA_CENTER, textColor=colors.gray)
            ))
        row.append(cell_content)
        if (i + 1) % 3 == 0:
            student_data.append(row)
            row = []
    if row:
        student_data.append(row)

    if student_data:
        stu_table = Table(student_data, colWidths=[2.2*inch]*3)
        stu_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 15),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E0E0E0')),
        ]))
        story.append(stu_table)

    # FOOTER PAGE
    story.append(PageBreak())
    story.append(Spacer(1, 3*inch))
    story.append(Paragraph("CPS LEGACY CHRONICLE", title_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Class of 2026 - Computer Science Department", subtitle_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(
        "This yearbook is a tribute to the hard work, dedication, and friendship "
        "that defined our journey through the Computer Science program. "
        "May we continue to excel in all our future endeavors.",
        ParagraphStyle('Footer', parent=body_style, alignment=TA_CENTER, fontSize=11)
    ))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
