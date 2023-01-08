from flask import Flask, render_template

app = Flask(__name__)
#in the function return render_template(‘index.html’)
@app.route("/")

def first_webpage():
    #Create a variable
    name = 'Hailey'
    # Pass the variable in the template
    return render_template('index.html', student_name = name)

if __name__  ==  '__main__':
    app.run(debug=True)


