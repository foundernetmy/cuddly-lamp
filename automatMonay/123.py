import os
import sys
import csv
from email import encoders
from email.mime.base import MIMEBase

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QFileDialog, QListWidget


class EmailSender(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 800, 800)
        self.setWindowTitle('Email Sender')

        self.sender_label = QLabel('Sender email:', self)
        self.sender_label.move(50, 50)
        self.sender_label.setStyleSheet('font-size: 10px; font-weight: bold;padding-top: 10px;')

        self.sender_input = QLineEdit(self)
        self.sender_input.move(150, 50)
        self.sender_input.resize(200, 30)
        self.sender_input.setStyleSheet('font-size: 10px;padding-top: 10px;')

        self.recipient_label = QLabel('Recipient email:', self)
        self.recipient_label.move(50, 100)
        self.recipient_label.setStyleSheet('font-size: 10px; font-weight: bold;padding-top: 10px;')

        self.recipient_input = QLineEdit(self)
        self.recipient_input.move(150, 100)
        self.recipient_input.resize(200, 30)
        self.recipient_input.setStyleSheet('font-size: 10px;padding-top: 10px;')

        self.subject_label = QLabel('Email subject:', self)
        self.subject_label.move(50, 150)
        self.subject_label.setStyleSheet('font-size: 10px; font-weight: bold;padding-top: 10px;')

        self.subject_input = QLineEdit(self)
        self.subject_input.move(150, 150)
        self.subject_input.resize(200, 30)
        self.subject_input.setStyleSheet('font-size: 10px;padding-top: 10px;')

        self.message_label = QLabel('Email message:', self)
        self.message_label.move(50, 200)
        self.message_label.setStyleSheet('font-size: 10px; font-weight: bold;padding-top: 10px;')

        self.message_input = QTextEdit(self)
        self.message_input.move(150, 200)
        self.message_input.resize(500, 200)
        self.message_input.setStyleSheet('font-size: 10px;padding-top: 10px;')

        self.choose_file_button = QPushButton('Choose Recipients File', self)
        self.choose_file_button.move(50, 420)
        self.choose_file_button.resize(200, 40)
        self.choose_file_button.setStyleSheet('font-size: 10px; background-color: #007ACC; color: white;padding-top: 10px;')
        self.choose_file_button.clicked.connect(self.choose_file)
        self.send_button = QPushButton('Send Email', self)
        self.send_button.move(270, 420)
        self.send_button.resize(200, 40)
        self.send_button.setStyleSheet('font-size: 10px; background-color: #007ACC; color: white;padding-top: 10px;')
        self.send_button.clicked.connect(self.send_email)
        self.attach_file_button = QPushButton('Attach File', self)
        self.attach_file_button.move(50, 360)
        self.attach_file_button.resize(100, 40)
        self.attach_file_button.setStyleSheet('font-size: 10px; background-color: #007ACC; color: white;padding: 10px;')
        self.attach_file_button.clicked.connect(self.attach_file)
        self.attachment_label = QLabel('Attachments:', self)
        self.attachment_label.move(50, 470)
        self.attachment_label.setStyleSheet('font-size: 10px; font-weight: bold; padding-top: 10px;')

        self.attachment_list = QListWidget(self)
        self.attachment_list.move(50, 500)
        self.attachment_list.resize(500, 100)
        self.attachment_list.setStyleSheet('font-size: 10px;padding-top: 10px;')




        self.show()

    def choose_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open Recipients File', '', 'CSV files (*.csv)')
        if filename:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                recipients = []
                for row in reader:
                    recipients.append(row[0])
                self.recipient_input.setText(', '.join(recipients))


    def send_email(self):
        sender = self.sender_input.text()
        recipients = self.recipient_input.text().split(',')
        subject = self.subject_input.text()
        message = self.message_input.toPlainText()

        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.application import MIMEApplication

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = ", ".join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Add attachment if selected
        if hasattr(self, 'attachment_file'):
            with open(self.attachment_file, "rb") as f:
                attach = MIMEApplication(f.read(), _subtype='pdf')
                attach.add_header('Content-Disposition', 'attachment', filename=self.attachment_file.split("/")[-1])
                msg.attach(attach)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, 'password')
        text = msg.as_string()
        server.sendmail(sender, recipients, text)
        server.quit()

    def attach_file(self):
        self.attachment_file, _ = QFileDialog.getOpenFileName(self, 'Attach File', '', '')
        if self.attachment_file:
            self.attachment_label.setText(self.attachment_file.split("/")[-1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmailSender()
    sys.exit(app.exec_())
