from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError
from .extensions import db, login_manager

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager.login_view = 'login'

def init_routes(app):
    from .models import User, Vote, Candidate, VoteSelection

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('home'))
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = User.query.filter_by(username=username).first()

            if user and user.check_password(password):
                login_user(user)  # Logs in the user using Flask-Login
                return redirect(url_for('home'))
            else:
                flash('Login failed. Check your username and password.', 'error')

        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Registered successfully! You can now log in.', 'success')
                return redirect(url_for('login'))
            except IntegrityError:
                db.session.rollback()
                flash('Username or email already exists.', 'error')
        return render_template('register.html')

    from collections import Counter

    @app.route('/home')
    def home():
        candidates = Candidate.query.all()
        votes_data = VoteSelection.query.with_entities(VoteSelection.candidate_id).all() 

        vote_counter = Counter([v[0] for v in votes_data])

        names = [c.name for c in candidates]
        vote_counts = [vote_counter.get(c.id, 0) for c in candidates]

        return render_template('home.html', names=names, votes=vote_counts)



    @app.context_processor
    def inject_candidates():
        boys = Candidate.query.filter_by(gender='boy').order_by(Candidate.name).all()
        girls = Candidate.query.filter_by(gender='girl').order_by(Candidate.name).all()
        return dict(boys=boys, girls=girls)

    @app.route('/candidate/<int:candidate_id>')
    @login_required
    def candidate(candidate_id):
        candidate = Candidate.query.get_or_404(candidate_id)
        return render_template('candidate.html', candidate=candidate)


    @app.route('/vote')
    @login_required
    def votepage():
        boys  = Candidate.query.filter_by(gender='boy').all()
        girls = Candidate.query.filter_by(gender='girl').all()
        return render_template('vote.html', boys=boys, girls=girls)

    @app.route('/submit_vote', methods=['POST'])
    @login_required
    def submit_vote():
        if current_user.has_voted:
            flash("You have already voted.", "error")
            return redirect(url_for('votepage'))
        
        boys = Candidate.query.filter_by(gender='boy').all()
        girls = Candidate.query.filter_by(gender='girl').all()

        boy_votes = [request.form.get(f"boy{i}") for i in range(1, 4)]
        girl_votes = [request.form.get(f"girl{i}") for i in range(1, 4)]

        if "" in boy_votes or "" in girl_votes:
            flash("All selections must be filled.", "error")
            return redirect(url_for('votepage'))

        # Check for duplicate votes
        if len(set(boy_votes)) < 3 or len(set(girl_votes)) < 3:
            # GOOD: re-render with previous form state
            flash("You can't vote for the same person twice!", "error")
            return render_template("vote.html", boys=boys, girls=girls)


        # Save Vote object
        vote = Vote(user_id=current_user.id)
        db.session.add(vote)
        db.session.flush()  # Ensures vote.id is available before inserting selections

        # Store each boy vote
        for i in range(1, 4):
            candidate_id = int(request.form[f'boy{i}'])
            selection = VoteSelection(
                vote_id=vote.id,
                candidate_id=candidate_id,
                position=i,
                gender='boy'
            )
            db.session.add(selection)

        # Store each girl vote
        for i in range(1, 4):
            candidate_id = int(request.form[f'girl{i}'])
            selection = VoteSelection(
                vote_id=vote.id,
                candidate_id=candidate_id,
                position=i,
                gender='girl'
            )
            db.session.add(selection)

        current_user.has_voted = True
        db.session.commit()


        flash("Your vote has been submitted successfully.", "success")
        return redirect(url_for('home'))

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('Logged out successfully.')
        return redirect(url_for('login'))