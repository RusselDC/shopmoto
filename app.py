from data_layer.AbstractShopDao import AbstractShopDao
import bcrypt

runner = AbstractShopDao()

#password = 'Russeldc189'
#hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#print(bcrypt.checkpw("Russeldc189".encode('utf-8'), hashed))
#print(runner.write("""INSERT INTO users
#(user_id, user_name, user_email, user_contact_number, user_password)
#VALUES (%s, %s, %s, %s, %s) returning *;
#""",('ABC1234567','russel_dc','delacruzruss12@gmail.com',9215774058,bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()))))

