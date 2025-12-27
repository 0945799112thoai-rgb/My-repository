import pymysql
# Dòng này cực kỳ quan trọng để vượt qua lỗi "mysqlclient 2.2.1 or newer is required"
pymysql.version_info = (2, 2, 7, "final", 0) 
pymysql.install_as_MySQLdb()