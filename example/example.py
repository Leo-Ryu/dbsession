from config import db_connection
import A


db_session = db_connection.get_session()
a_1 = db_session.query(A.find_by_id, 1)
print(a_1)

all_a = db_session.query(A.get_all)
print(all_a)
