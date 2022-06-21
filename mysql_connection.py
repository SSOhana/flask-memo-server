import mysql.connector

def get_connection() :
    connection = mysql.connector.connect(
        host = 'yh-db.caohoyy07jik.ap-northeast-2.rds.amazonaws.com',
        database = 'memo_db', 
        user = 'memo_user1',
        password = '2105hello' 
    )
    return connection   
