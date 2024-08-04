from flask import Flask, request, jsonify

# Create a dictionary to store students
students = {}

# Create documents for each student
student_data = [
    {"matric_number": "BHU/23/04/05/0023", "password": "1234567890"},
    {"matric_number": "BHU/23/04/05/0027", "password": "2345678901"},
    {"matric_number": "BHU/23/04/05/0010", "password": "3456789012"},
    {"matric_number": "BHU/23/04/05/0022", "password": "4567890123"},
    {"matric_number": "BHU/23/04/09/0072", "password": "5678901234"}
]

for student in student_data:
    students[student["matric_number"]] = student["password"]

print("Student data loaded successfully!")

# Define a function to verify student credentials
def verify_student(matric_number, password):
    if matric_number in students and students[matric_number] == password:
        return True
    else:
        return False

# Create a Flask app
app = Flask(__name__)

# Define a login route
@app.route("/login", methods=["POST"])
def login_student():
    data = request.get_json()
    matric_number = data["matric_number"]
    password = data["password"]

    if verify_student(matric_number, password):
        return jsonify({"message": "Student logged in successfully"})
    else:
        return jsonify({"message": "Invalid credentials"})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)