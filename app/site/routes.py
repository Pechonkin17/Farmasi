from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.site.models import Contact
from app.bot.telegram_bot import send_message
import asyncio

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    error_message = None

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']

        if name and phone:
            if Contact.phone_exists(phone):
                error_message = 'Користувач з таким номером телефону вже існує'
            else:
                new_contact = Contact(name=name, phone=phone)
                db.session.add(new_contact)
                db.session.commit()

                message = f"New contact added:\nName: {name}\nPhone: {phone}"
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    loop.run_until_complete(send_message(message))
                finally:
                    loop.close()

                return redirect(url_for('main.thank_you'))

    return render_template('index.html', error_message=error_message)

@main.route('/thank-you', methods=['GET', 'POST'])
def thank_you():
    if request.method == 'POST':
        return redirect("https://t.me/Farmasi_official_bot")

    return render_template('subscription.html')