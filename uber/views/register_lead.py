from flask import Blueprint, render_template, jsonify, request
from uber.forms.call_registration import LeadForm
from uber.models.lead import Lead

home = Blueprint('home', __name__)


@home.route('/')
def home_page():
    form = LeadForm()
    return render_template('index.html', form=form)


@home.route('/save-lead-data', methods=['POST'])
def save_lead_data():
    form = LeadForm()
    for key, value in request.form.items():
        getattr(form, key).data = value
    if form.validate_on_submit():
        Lead.create({k: v for k, v in form.data.items() if k not in ('csrf_token', 'submit')})
        return jsonify({'lead_created': True})

    return render_template('form_update.html', form=form)

