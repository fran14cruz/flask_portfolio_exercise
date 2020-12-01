from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>') # dynamic url
def html_page(page_name):
    return render_template(page_name)

# write to database.txt file
def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

# write to database.csv file
def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as csv_database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message]) # pass parameters as an interable

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # Now let's access the data we grabbed from the contact form
    if request.method == 'POST': # if the action is 'POST'
        try:
            data = request.form.to_dict() # get everything into a dictionary
            write_to_csv(data) # call write_to_csv() function here and pass the data
            return redirect('/thankyou.html') # redirect to this url
        except:
            return 'DATA NOT SAVED TO DATABASE.'
    else:
        return 'TRY AGAIN.'