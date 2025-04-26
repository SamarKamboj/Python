from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///week7_database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    enrollments = db.relationship("Enrollments", back_populates="student")

class Course(db.Model):
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    course_code = db.Column(db.String, unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String, nullable=True)
    enrollments = db.relationship("Enrollments", back_populates="course")

class Enrollments(db.Model):
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)
    student = db.relationship("Student", back_populates="enrollments")
    course = db.relationship("Course", back_populates="enrollments")


# Flask work

@app.route("/")
def index():
    students = Student.query.all()
    return render_template("index.html", students=students)

@app.route("/student/<int:student_id>")
def info_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    enrollments = db.session.query(Course).join(Enrollments).filter(Enrollments.estudent_id == student_id).order_by(Course.course_id).all()

    if student:
        return render_template("info_student.html", student=student, enrollments=enrollments)
    else:
        return render_template("error.html")

@app.route("/student/create", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        roll_num = request.form.get("roll")
        fname = request.form.get("f_name")
        lname = request.form.get("l_name")
        courses = request.form.getlist("courses")

        student = Student.query.filter_by(roll_number=roll_num).first()
        if not student:
            db.session.add(Student(roll_number=roll_num, first_name=fname, last_name=lname))
            db.session.commit()

            student = Student.query.filter_by(roll_number=roll_num).first()
            for course_id in courses:
                db.session.add(Enrollments(estudent_id=student.student_id, ecourse_id=course_id))
            db.session.commit()
            return redirect(url_for("index"))
        else:
            return render_template("error.html")
    
    courses = Course.query.all()
    return render_template("add_student.html", courses=courses)

@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def update_student(student_id):
    if request.method == "POST":
        fname = request.form.get("f_name")
        lname = request.form.get("l_name")
        courses = list(map(int, request.form.getlist("courses")))

        student = Student.query.filter_by(student_id=student_id).first()
        if student:
            student.first_name = fname
            student.last_name = lname
        
        enrollments = [enrollment.ecourse_id for enrollment in Enrollments.query.filter_by(estudent_id=student_id).all()]
        # Courses which need to be removed from the database
        for course_id in (set(enrollments)-set(courses)):
            Enrollments.query.filter_by(estudent_id=student_id, ecourse_id=course_id).delete()
        # Courses which need to be added in the database
        for course_id in (set(courses)-set(enrollments)):
            db.session.add(Enrollments(estudent_id=student_id, ecourse_id=course_id))

        db.session.commit()

        return redirect(url_for("index"))
        ...

    student = Student.query.filter_by(student_id=student_id).first()
    courses = Course.query.all()
    enrollments = [enrollment.ecourse_id for enrollment in Enrollments.query.filter_by(estudent_id=student_id).all()]
    return render_template("update_student.html", student=student, courses=courses, enrollments=enrollments)

@app.route("/student/<int:student_id>/delete")
def delete_student(student_id):
    # First delete all courses related to that student then remove the student
    enrollments = Enrollments.query.filter_by(estudent_id=student_id).all()
    for enroll in enrollments:
        db.session.delete(enroll)

    student = Student.query.filter_by(student_id=student_id).first()
    if student:
        db.session.delete(student)
    db.session.commit()
    
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()