from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from utils import Base64

mail = Mail()
db = SQLAlchemy()

base64 = Base64()

