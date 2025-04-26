from pyhtml import *
import sys
import csv
import matplotlib.pyplot as plt

if not sys.argv[1] in ('-c', '-s') or not sys.argv[2]:
    error_template = html(
        head(
            title("Something went wrong")
        ),
        body(
            h1("Wrong Inputs"),
            p("Something went wrong")
        )
    )
    with open("output.html", 'w') as file:
        file.write(error_template.render())
    sys.exit()
elif (sys.argv[1] == '-c' and sys.argv[2][0] != '2') or(sys.argv[1] == '-s' and sys.argv[2][0] != '1'):
    error_template = html(
        head(
            title("Something went wrong")
        ),
        body(
            h1("Wrong Inputs"),
            p("Something went wrong")
        )
    )
    with open("output.html", 'w') as file:
        file.write(error_template.render())
    sys.exit()

id_type, id_value = sys.argv[1], sys.argv[2]

table_data = []
course_marks = []
with open("data.csv") as csv_file:
    total_marks = 0
    for value in csv.DictReader(csv_file):
        if id_type == '-s' and id_value == value["Student id"].strip():
            total_marks += int(value[" Marks"].strip())
            table_data.append(tr(td(value["Student id"].strip()), td(value[" Course id"].strip()), td(value[" Marks"].strip())))
        elif id_type == '-c' and id_value == value[" Course id"].strip():
            course_marks.append(int(value[" Marks"].strip()))

if not table_data and not course_marks:
    error_template = html(
        head(
            title("Something went wrong")
        ),
        body(
            h1("Wrong Inputs"),
            p("Something went wrong")
        )
    )
    with open("output.html", 'w') as file:
        file.write(error_template.render())
    sys.exit()

avg_marks = round(sum(course_marks)/len(course_marks), 2) if course_marks else 0
mx_marks = max(course_marks) if course_marks else 0

with open("output.html", 'w') as file:
    if id_type == '-s':
        student = html(
            head(title("Student Data")),
            body(
                h1("Student Details"),
                table(border='1')(
                    tr(
                        th("Student ID"),
                        th("Course ID"),
                        th("Marks")
                    ),
                    table_data,
                    tr(
                        td(colspan=2, style="text-align: center;")("Total Marks"),
                        td(total_marks)
                    )
                )
            )
        )
        file.write(student.render())
    elif id_type == '-c':
        plt.hist(course_marks)
        plt.savefig("output.jpg")

        course = html(
            head(title("Course Data")),
            body(
                h1("Course Details"),
                table(border='1')(
                    tr(
                        th("Average Marks"),
                        th("Maximum Marks")
                    ),
                    tr(
                        td(avg_marks),
                        td(mx_marks)
                    )
                ),
                img(src="output.jpg")
            )
        )
        file.write(course.render())
