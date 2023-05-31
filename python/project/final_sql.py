from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os.path
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, "../secret.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg


HOSTNAME = get_secret("Mysql_Hostname")
PORT = get_secret("Mysql_Port")
USERNAME = get_secret("Mysql_Username")
PASSWORD = get_secret("Mysql_Password")
DBNAME = get_secret("Mysql_DBname")

DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DBNAME}"

Base = declarative_base()


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    data = Column(LargeBinary)


def db_conn():
    engine = create_engine(DB_URL)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


session = db_conn()

image_names = [
    "combined_figure",
    "combined_pie_chart",
    "final_2018graph",
    "final_2020graph",
    "final_2022graph",
    "final_2023graph",
    "pie_chart_2020",
    "pie_chart_2022",
]

for image_name in image_names:
    with open(f"{image_name}.png", "rb") as file:
        binary_data = file.read()
    image = Image(name=image_name, data=binary_data)
    session.add(image)

session.commit()



session.close()