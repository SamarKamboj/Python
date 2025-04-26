def get_data():
    import csv

    data = []
    with open('data.csv') as csv_file:
        for row in csv.DictReader(csv_file):
            temp = dict()
            temp['StudentID'] = row['Student id'].strip()
            temp['CourseID'] = row[' Course id'].strip()
            temp['Marks'] = row[' Marks'].strip()
            data.append(temp)
    return data

from flask import Flask, render_template, request
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id, id_value = request.form.get("ID"), request.form.get("id_value")
        if id == 'student_id':
            data = list(filter(lambda x: x['StudentID'] == id_value, get_data()))
            if not data:
                return render_template("error.html")
            total_marks = sum([int(i['Marks']) for i in data])
            return render_template("student_details.html", data=data, total_marks=total_marks)
        elif id == 'course_id':
            data = list(filter(lambda x: x['CourseID'] == id_value, get_data()))
            if not data:
                return render_template("error.html")
            
            # generate bar graph
            plt.hist([int(row['Marks']) for row in data])
            plt.savefig("static/output.jpg")

            avg_marks, max_marks = sum([int(row['Marks']) for row in data])/len(data), max([int(row['Marks']) for row in data])
            return render_template("course_details.html", avg_marks=avg_marks, max_marks=max_marks)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)