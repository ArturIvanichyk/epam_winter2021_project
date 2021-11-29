from department_app import app
from department_app.database import populate

if __name__ == '__main__':
    #populate.populate_database()
    app.run(debug=True)