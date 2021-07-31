# from werkzeug.useragents import UserAgent
# from user_agents import parse

import datetime
from enum import unique
from flask import Flask, flash, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import string
import random
import ipaddress
from sqlalchemy.orm import backref

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'flaskTesAKsg' 

db = SQLAlchemy(app)

class Company(db.Model):
    id_com = db.Column(db.Integer, primary_key=True)
    name_com = db.Column(db.String(30))
    email_com = db.Column(db.String(80), unique=True)
    password_com = db.Column(db.String(80))
    domain_com = db.Column(db.String(20))
    ref_com = db.Column(db.String(20), unique=True)
    affiliaters = db.relationship('Affiliater', backref='product_owner')
    reports = db.relationship('Report', backref='report_owner')

    def __init__(self, name_com, email_com, password_com, domain_com, ref_com):
        self.name_com = name_com
        self.email_com = email_com
        self.password_com = password_com
        self.domain_com = domain_com
        self.ref_com = ref_com

class Affiliater(db.Model):
    id_aff = db.Column(db.Integer, primary_key=True)
    name_aff = db.Column(db.String(30))
    email_aff = db.Column(db.String(80))
    password_aff = db.Column(db.String(80))
    ref_aff = db.Column(db.String(20), unique=True)
    id_company = db.Column(db.Integer, db.ForeignKey('company.id_com'))
    reports = db.relationship('Report', backref='affiliate_owner')


    def __init__(self, name_aff, email_aff, password_aff, ref_aff, id_company):
        self.name_aff = name_aff
        self.email_aff = email_aff
        self.password_aff = password_aff
        self.ref_aff = ref_aff
        self.id_company = id_company
        # for arg in argv:
        #     (self, arg)

class Report(db.Model):
    id_report = db.Column(db.Integer, primary_key=True)
    date_report = db.Column(db.TIMESTAMP)
    ip_report = db.Column(db.String(15))
    user_agent = db.Column(db.String(255))
    click_report = db.Column(db.Integer, default=1)
    id_company = db.Column(db.Integer, db.ForeignKey('company.id_com'))
    id_aff = db.Column(db.Integer, db.ForeignKey('affiliater.id_aff'))


    def __init__(self, date_report, ip_report, user_agent, id_company, id_aff):
        self.date_report = date_report
        self.ip_report = ip_report
        self.user_agent = user_agent
        self.id_company = id_company
        self.id_aff = id_aff
        # for k, v in kwargs.items():
        #     setattr(self, k, v)



@app.before_first_request
def create_tables():
    db.create_all()


def product_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = Company.query.filter_by(ref_com=rand_letters).first()
        if not short_url:
            return rand_letters

def product_url_Aff():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = Affiliater.query.filter_by(ref_aff=rand_letters).first()
        if not short_url:
            return rand_letters


@app.route('/')
def index():
    
    return "dian"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        website = request.form['website']
        email = request.form['email']
        password = request.form['password']
        ref_company = product_url()

        user_company = Company(username, email, password, website, ref_company)
        db.session.add(user_company)
        db.session.commit()
        flash(f'Pendaftaran Anda telah berhasil')
        return redirect(url_for('login'))
    else:
        if "user" in session:
            return redirect(url_for('dashboardCom'))
        return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    email_com = request.form.get('email')
    password_com = request.form.get('password')
    user = Company.query.filter_by(email_com=email_com, password_com=password_com).first()
    
    if user:
        session["user"] = user.id_com
        return redirect(url_for('dashboardCom'))
    else:
        if "user" in session:
            return redirect(url_for('dashboardCom'))
        flash(f'Please check your login details and try again.')

    return render_template("login.html")



@app.route('/dashboard', methods=['GET', 'POST'])
def dashboardCom():

    if "user" in session:
        data_com = session["user"]
        Com = Company.query.filter_by(id_com=data_com).first()

        current_time = datetime.datetime.utcnow()
        this_day = current_time - datetime.timedelta(days = 1)
        one_week = current_time - datetime.timedelta(days = 7)
        one_month = current_time - datetime.timedelta(days = 30)

        number_user = db.session.query(Affiliater).filter(data_com == Affiliater.id_company).count()
        member_aff = db.session.query(Affiliater).filter(data_com == Affiliater.id_company).all()
        get_report = db.session.query(Report, Affiliater).join(Affiliater).filter(Affiliater.id_company == data_com).all()

        get_clickDay = db.session.query(Report).filter(data_com == Report.id_company, Report.date_report > this_day ).count()
        get_clickWeek = db.session.query(Report).filter(data_com == Report.id_company, Report.date_report > one_week ).count()
        get_clickMonth = db.session.query(Report).filter(data_com == Report.id_company, Report.date_report > one_month ).count()

        return render_template("dashboard.html", link_com=Com.ref_com, 
                                number_user = number_user, member_aff = member_aff, get_report = get_report, get_clickDay = get_clickDay, get_clickWeek = get_clickWeek, get_clickMonth = get_clickMonth)
    else: 
        return redirect(url_for("login"))

@app.route('/logout')
def logoutCom():
    session.pop("user", None)
    return redirect(url_for('login'))



# Untuk Afffiliater
# Anda bisa ubah kode login, registri, logout, dan laporan
@app.route('/<ref_com>/', methods=['GET', 'POST'])
def refCom(ref_com):

    Com = Company.query.filter_by(ref_com=ref_com).first()
    if not Com:
        return "halaman tidak tersedia"

    if "userAff" in session:
        aku = session["userAff"]
        if aku == Com.id_com:
            return redirect(url_for('dashboardCom', ref_com=Com.ref_com))
        else:
            session.pop("userAff", None)
            return redirect(url_for('loginAff', ref_com=Com.ref_com))
    else:
        return redirect(url_for('registerAff', ref_com=Com.ref_com))


@app.route('/<ref_com>/register', methods=['GET', 'POST'])
def registerAff(ref_com):

    Com = Company.query.filter_by(ref_com=ref_com).first()
    if not Com:
        return "halaman tidak tersedia"

    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        ref_affiliater = product_url_Aff()

        user_affiliater = Affiliater(username, email, password, ref_affiliater, Com.id_com)
        db.session.add(user_affiliater)
        db.session.commit()
        flash(f'Pendaftaran Anda telah berhasil')
        return redirect(url_for('loginAff', ref_com=Com.ref_com))
    else:
        if "userAff" in session:
            return redirect(url_for('dashboardAff', ref_com=Com.ref_com))
        return render_template("register_affiliater.html", ref_com=Com)

@app.route('/<ref_com>/login', methods=['GET', 'POST'])
def loginAff(ref_com):
    Com = Company.query.filter_by(ref_com=ref_com).first()
    if not Com:
        return "halaman tidak tersedia"
    
    email_aff = request.form.get('email')
    password_aff = request.form.get('password')
    user_aff = Affiliater.query.filter_by(email_aff=email_aff, password_aff=password_aff).first()
    # user_aff = Company.query.join(Affiliater).filter(Affiliater.email_aff == email_aff, Affiliater.password_aff == password_aff).first()

    if user_aff:
        session["userAff"] = user_aff.id_aff
        return redirect(url_for('dashboardAff', ref_com=Com.ref_com))
    else:
        if "userAff" in session:
            return redirect(url_for('dashboardAff', ref_com=Com.ref_com))
        flash(f'Please check your login details and try again.')

    return render_template("login_affiliater.html")


@app.route('/<ref_com>/dashboard')
def dashboardAff(ref_com):
    Com = Company.query.filter_by(ref_com=ref_com).first()
    

    if not Com:
        return "halaman tidak tersedia"

    if "userAff" in session:
        aku = session["userAff"]
        Aff = Affiliater.query.filter_by(id_aff = aku).first()
        current_time = datetime.datetime.utcnow()
        this_day = current_time - datetime.timedelta(days = 1)
        one_week = current_time - datetime.timedelta(days = 7)
        one_month = current_time - datetime.timedelta(days = 30)


        if Aff.id_company == Com.id_com:
            get_report = db.session.query(Report).filter(aku == Report.id_aff).all()

            get_clickDay = db.session.query(Report).filter(aku == Report.id_aff, Report.date_report > this_day ).count()
            get_clickWeek = db.session.query(Report).filter(aku == Report.id_aff, Report.date_report > one_week ).count()
            get_clickMonth = db.session.query(Report).filter(aku == Report.id_aff, Report.date_report > one_month ).count()
            revenue = get_clickMonth * 500

            return render_template("dashboard_affiliater.html", link_com = Com.ref_com, link_ref = Aff.ref_aff, get_clickDay = get_clickDay, get_clickWeek = get_clickWeek, get_clickMonth = get_clickMonth, revenue = revenue, get_report = get_report)
        else:
            session.pop("userAff", None)
            return redirect(url_for('loginAff', ref_com=Com.ref_com))
    else:
        return redirect(url_for('loginAff', ref_com=Com.ref_com))

@app.route('/<ref_com>/<ref_aff>/', methods=['GET', 'POST'])
def redirectAff(ref_com, ref_aff):

    Com = Company.query.filter_by(ref_com=ref_com).first()
    Aff = Affiliater.query.filter_by(ref_aff=ref_aff).first()

    if not Com or not Aff:
        return "halaman tidak tersedia"
    # if not Aff:
    #     return "halaman tidak tersedia"

    if Com.id_com == Aff.id_company:
        if request.method == "GET":
            date_report = datetime.datetime.utcnow()
            ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
            user_agent = request.headers.get('User-Agent')

            report = Report(date_report, ip, user_agent, Com.id_com, Aff.id_aff)
            db.session.add(report)
            db.session.commit()
            return redirect(Com.domain_com)
    else: 
        return "Halaman tidak ada"

@app.route('/<ref_com>/logout', methods=['GET', 'POST'])
def logoutAff(ref_com):

    Com = Company.query.filter_by(ref_com=ref_com).first()
    
    if session.pop("userAff", None):
        return redirect(url_for('loginAff', ref_com=Com.ref_com))



if __name__ == '__main__':
    app.run(debug=True)