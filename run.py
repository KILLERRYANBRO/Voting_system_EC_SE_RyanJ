from myapp.init import create_app, db
from myapp.models import Candidate
app = create_app()
#with app.app_context():
#  Candidate.query.delete()
#  db.session.commit()

#  db.session.add_all([
#      Candidate(name='Ryan', gender='boy', bio='Aspiring leader.'),
#      Candidate(name='Isaac', gender='boy', bio='Passionate about sport.'),
#      Candidate(name='Milo', gender='boy', bio='Tech enthusiast.'),
#      Candidate(name='Amber', gender='girl', bio='Focused on wellbeing.'),
#      Candidate(name='Sophie', gender='girl', bio='Cultural ambassador.'),
#      Candidate(name='Liz', gender='girl', bio='Environment advocate.')
#  ])
#  db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
