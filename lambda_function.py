import json
import boto3
import psycopg2
from reportlab.pdfgen import canvas

s3 = boto3.client('s3')
ses = boto3.client('ses', region_name='ap-south-1')

DB_HOST = "postgres.cvkcs4q28uf5.ap-south-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "rootomj3"

BUCKET_NAME = "ticketpdf-bucket"
SENDER_EMAIL = "omjkbp@gmail.com"


# ---------------- DB FETCH ----------------
def get_booking_details(booking_id):

    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT
            u.name,
            b.pnr,
            b.train_name,
            b.route,
            b.journey_date,
            b.class_key,
            b.seats,
            b.passengers,
            b.amount
        FROM bookings b
        LEFT JOIN users u ON b.user_id = u.id
        WHERE b.id = %s
    """, (booking_id,))

    row = cur.fetchone()

    cur.close()
    conn.close()

    return row


# ---------------- LAMBDA ----------------
def lambda_handler(event, context):

    print("Event:", event)

    message = json.loads(event['Records'][0]['Sns']['Message'])

    booking_id = message['booking_id']
    email = message['email']

    details = get_booking_details(booking_id)

    if not details:
        return {"statusCode": 404, "body": "Booking not found"}

    name = details[0]
    pnr = details[1]
    train_name = details[2]
    route = details[3]
    journey_date = details[4]
    class_key = details[5]
    seats = details[6]
    passengers = details[7]
    amount = details[8]

    # ---------------- PDF ----------------
    pdf_file = f"/tmp/{booking_id}.pdf"
    pdf = canvas.Canvas(pdf_file)

    pdf.drawString(100, 780, "RAILWAY E-TICKET")
    pdf.drawString(100, 740, f"PNR: {pnr}")
    pdf.drawString(100, 710, f"Passenger: {name}")
    pdf.drawString(100, 680, f"Train: {train_name}")
    pdf.drawString(100, 650, f"Route: {route}")
    pdf.drawString(100, 620, f"Date: {journey_date}")
    pdf.drawString(100, 590, f"Class: {class_key}")
    pdf.drawString(100, 560, f"Seats: {seats}")
    pdf.drawString(100, 530, f"Passengers: {passengers}")
    pdf.drawString(100, 500, f"Amount: Rs {amount}")

    pdf.save()

    # ---------------- S3 UPLOAD ----------------
    s3_key = f"tickets/{booking_id}.pdf"

    s3.upload_file(pdf_file, BUCKET_NAME, s3_key)

    pdf_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{s3_key}"

    # ---------------- EMAIL ----------------
    ses.send_email(
        Source=SENDER_EMAIL,
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': 'Railway Ticket Confirmed'},
            'Body': {
                'Text': {
                    'Data': f"Your ticket is ready:\n{pdf_url}"
                }
            }
        }
    )

    return {
        "statusCode": 200,
        "body": "Success"
    }