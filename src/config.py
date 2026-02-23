from utils.base_dir import get_base_data_dir

DEBUG = True
SQLALCHEMY_DATABASE_URI = f'sqlite:///{get_base_data_dir() / "data/db/words_data.db"}'
SQLALCHEMY_TRACK_MODIFICATIONS = False