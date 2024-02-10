from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize a list to store textbook names and URL links
textbooks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If a new textbook is submitted, add it to the list
        if 'textbook_name' in request.form and 'url_link' in request.form:
            textbook_name = request.form['textbook_name']
            url_link = request.form['url_link']
            textbooks.append({'name': textbook_name, 'url': url_link})
        # If a textbook is requested to be removed, remove it from the list
        elif 'remove_url' in request.form:
            remove_url = request.form['remove_url']
            textbooks[:] = [textbook for textbook in textbooks if textbook['url'] != remove_url]
        return redirect(url_for('index'))
    else:
        return render_template('index.html', textbooks=textbooks)

if __name__ == '__main__':
    app.run(debug=True)

