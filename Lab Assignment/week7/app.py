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

# with app.app_context():
#     db.create_all()
#     db.session.add(Course(course_code='CSE01', course_name="DBMS", course_description="Database Management System"))
#     db.session.add(Course(course_code='CSE02', course_name="PDSA", course_description="DSA"))
#     db.session.add(Course(course_code='CSE03', course_name="MAD1", course_description="Modern App Dev 1"))

#     db.session.commit()


# Flask work

@app.route("/")
def index():
    students = Student.query.all()
    return render_template("student_index.html", students=students)

@app.route("/student/<int:student_id>")
def info_student(student_id):
    student = Student.query.filter_by(student_id=student_id).first()
    enrollments = db.session.query(Course).join(Enrollments).filter(Enrollments.estudent_id == student_id).order_by(Course.course_id).all()

    if student:
        return render_template("info_student.html", student=student, enrollments=enrollments)
    else:
        return render_template("error.html", val='no-record')

@app.route("/student/create", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        roll_num = request.form.get("roll")
        fname = request.form.get("f_name")
        lname = request.form.get("l_name")

        student = Student.query.filter_by(roll_number=roll_num).first()
        if not student:
            db.session.add(Student(roll_number=roll_num, first_name=fname, last_name=lname))
            db.session.commit()
            return redirect(url_for("index"))
        else:
            return render_template("error.html", val='student_exist')
    
    return render_template("add_student.html")

@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def update_student(student_id):
    if request.method == "POST":
        fname = request.form.get("f_name")
        lname = request.form.get("l_name")
        course = request.form.get("course")

        student = Student.query.filter_by(student_id=student_id).first()
        if student:
            student.first_name = fname
            student.last_name = lname
        
        enrollment = Enrollments.query.filter_by(estudent_id=student_id, ecourse_id=course).first()
        if not enrollment and course:
            db.session.add(Enrollments(estudent_id=student_id, ecourse_id=course))
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

@app.route("/student/<int:student_id>/withdraw/<int:course_id>")
def withdraw_course(student_id, course_id):
    enrollment = Enrollments.query.filter_by(estudent_id=student_id, ecourse_id=course_id).first()
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/courses")
def course_index():
    courses = Course.query.all()
    return render_template("course_index.html", courses=courses)

@app.route("/course/<int:course_id>")
def info_course(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    enrollments = db.session.query(Student).join(Enrollments).filter(Enrollments.ecourse_id == course_id).order_by(Student.student_id).all()

    if course:
        return render_template("info_course.html", course=course, enrollments=enrollments)
    else:
        return render_template("error.html", val='no-record')
    

@app.route("/course/create", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        c_code = request.form.get("code")
        c_name = request.form.get("c_name")
        c_desc = request.form.get("desc")

        course = Course.query.filter_by(course_code=c_code).first()
        if not course:
            db.session.add(Course(course_code=c_code, course_name=c_name, course_description=c_desc))
            db.session.commit()
            return redirect(url_for("course_index"))
        else:
            return render_template("error.html", val='course_exist')
    
    return render_template("add_course.html")
        
@app.route("/course/<int:course_id>/update", methods=["GET", "POST"])
def update_course(course_id):
    if request.method == "POST":
        c_name = request.form.get("c_name")
        c_desc = request.form.get("desc")

        course = Course.query.filter_by(course_id=course_id).first()
        if course:
            course.course_name = c_name
            course.course_description = c_desc
        db.session.commit()
        ...
        return redirect(url_for("course_index"))

    course = Course.query.filter_by(course_id=course_id).first()
    return render_template("update_course.html", course=course)

@app.route("/course/<int:course_id>/delete")
def delete_course(course_id):
    enrollments = Enrollments.query.filter_by(ecourse_id=course_id).all()
    for enroll in enrollments:
        db.session.delete(enroll)

    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        db.session.delete(course)
        db.session.commit()
    
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()