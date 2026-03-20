# from flask import Flask, render_template, request, redirect, session
# from models import db, User, Mentor, Chat
# from ai import analyze_question, best_mentor

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# app.secret_key = "secret"

# db.init_app(app)

# with app.app_context():
#     db.create_all()

#     # Add mentors once
#     if Mentor.query.count() == 0:
#         db.session.add(Mentor(name="Aman", subject="python", stars=5))
#         db.session.add(Mentor(name="Riya", subject="math", stars=4))
#         db.session.add(Mentor(name="Kabir", subject="ai", stars=5))
#         db.session.commit()

# @app.route("/")
# def home():
#     return render_template("index.html")

# # SIGNUP
# @app.route("/signup", methods=["GET","POST"])
# def signup():
#     if request.method == "POST":
#         u = request.form["username"]
#         p = request.form["password"]

#         db.session.add(User(username=u, password=p))
#         db.session.commit()

#         return redirect("/login")
#     return render_template("signup.html")

# # LOGIN
# @app.route("/login", methods=["GET","POST"])
# def login():
#     if request.method == "POST":
#         u = request.form["username"]
#         p = request.form["password"]

#         user = User.query.filter_by(username=u, password=p).first()

#         if user:
#             session["user"] = u
#             return redirect("/dashboard")

#         return "Invalid login"
#     return render_template("login.html")

# # DASHBOARD
# @app.route("/dashboard", methods=["GET","POST"])
# def dashboard():
#     if "user" not in session:
#         return redirect("/login")

#     mentor = None
#     subject = None

#     if request.method == "POST":
#         q = request.form["question"]

#         subject = analyze_question(q)
#         mentors = Mentor.query.all()
#         mentor = best_mentor(subject, mentors)

#     return render_template("dashboard.html", mentor=mentor, subject=subject)

# # CHAT
# @app.route("/chat/<mentor>", methods=["GET","POST"])
# def chat(mentor):
#     if "user" not in session:
#         return redirect("/login")

#     if request.method == "POST":
#         msg = request.form["message"]

#         db.session.add(Chat(user=session["user"], mentor=mentor, message=msg))
#         db.session.commit()

#     messages = Chat.query.filter_by(mentor=mentor).all()

#     return render_template("chat.html", mentor=mentor, messages=messages)

# # LOGOUT
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/")

# if __name__ == "__main__":
#     app.run(debug=True, port=5002)