from flask import Flask, render_template, request, redirect, url_for
import sqlite3


MyMark = Flask(__name__)

conn = sqlite3.connect('students.db')
cursor = conn.cursor()


@MyMark.route('/')
def login_page():
    return render_template('login.html')

@MyMark.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Insert the data into the database
        db = get_db()
        cursor.execute("SELECT username,password FROM authentication WHERE username = ? AND password = ?", (username, password))
        student = cursor.fetchone()
        if student:
            return render_template('hello.html')

        db.commit()
        db.close()               
    
    return render_template('login.html')

if __name__ == '__main__':
    MyMark.run(debug=True)

# # Fetch student report card
# @MyMark.route('/get_report_card')
# def get_report_card():
#     try:
#         cursor.execute("SELECT * FROM student_marks WHERE student_no = '123456'")
#         student_info = cursor.fetchone()
#         cursor.execute("SELECT * FROM marks WHERE student_no = '123456'")
#         report_card = cursor.fetchall()
#         if student_info:
#             data = {
#                 'student_no': student_info[0],
#                 'school_name': student_info[1],
#                 'report_card': [{'subject': row[1], 'grade': row[2]} for row in report_card]
#             }
#             return jsonify(data)
#         else:
#             return jsonify({'message': 'Student not found'}), 404
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500

# Generate and download report card as PDF
# @MyMark.route('/download_report_card')    
# def download_report_card():
#     try:
#         # Generate PDF report card (dummy implementation)
#         # You would use a PDF generation library to create the report card dynamically
#         # For demonstration purposes, we'll just send a dummy PDF file
#         dummy_pdf_path = 'dummy_report_card.pdf'
#         if not os.path.exists(dummy_pdf_path):
#             with open(dummy_pdf_path, 'w') as f:
#                 f.write('Sample PDF content')
#         return send_file(dummy_pdf_path, as_attachment=True)
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500

# if __name__ == '__main__':
#     MyMark.run(debug=True)
