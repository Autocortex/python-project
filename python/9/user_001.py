from user import User 
from admin_privileges import Admin 
from admin_privileges import Privileges



user_001 = Admin('OlekSandr', 'Ivanov', 29, 'Korolj')
user_001.describe_user()
user_001.greet_user()
user_001.info_login_attempts()
user_001.increment_login_attempts()
user_001.info_login_attempts()
user_001.reset_login_attempts()
user_001.info_login_attempts()
user_001.privileges.show_privileges()