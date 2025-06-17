from myapp.init import create_app, db
from myapp.models import Candidate
app = create_app()
with app.app_context():
  Candidate.query.delete()
  db.session.commit()

  db.session.add_all([
      Candidate(name='Ryan', gender='boy', bio='Aspiring leader.', image_url='images/Ryan.png'),
      Candidate(name='Isaac.R', gender='boy', bio='Passionate about sport.', image_url='images/IsaacR.jpg'),
      Candidate(name='Milo', gender='boy', bio='Tech enthusiast.', image_url='images/Milo.jpg'),
      Candidate(name='Liam', gender='boy', bio='Creative thinker.', image_url='images/Liam.jpg'),
      Candidate(name='Angus', gender='boy', bio='Community helper.', image_url='images/Angus.png'),
      Candidate(name='Luke', gender='boy', bio='Future innovator.', image_url='images/Luke.png'),
      Candidate(name='Isaac.S', gender='boy', bio='Nature lover.', image_url='images/IsaacS.png'),
      Candidate(name='Brandan', gender='boy', bio='Sports enthusiast.', image_url='images/Brandan.png'),
      Candidate(name='Amber', gender='girl', bio='Focused on wellbeing.', image_url='images/Amber.png'),
      Candidate(name='Sophie', gender='girl', bio='Cultural ambassador.', image_url='images/Sophie.png'),
      Candidate(name='Elizabeth', gender='girl', bio='Environment advocate.', image_url='images/Elizabeth.jpg'),
      Candidate(name='Emma', gender='girl', bio='Community builder.', image_url='images/Emma.png'),
      Candidate(name='Khloe', gender='girl', bio='Future leader.', image_url='images/Khloe.png'),
      Candidate(name='Lisa', gender='girl', bio='Tech innovator.', image_url='images/Lisa.png'),
  ])
  db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)
