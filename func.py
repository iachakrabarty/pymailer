from parliament import Context, event
import mysql.connector
import json




@event
def main(context: Context):
    """
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """
    # print(f"Method: {context.request.method}")

    # The return value here will be applied as the data attribute
    # of a CloudEvent returned to the function invoker
    mydb = mysql.connector.connect(host="172.30.132.107", user="codecraftshop", password="codecraftshop", database="codecraftshopdb")
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO VISITOR_LOG (V_TIME) VALUES (curdate())")

    mycursor.execute("SELECT COUNT(1) FROM VISITOR_LOG")

    rowcount = mycursor.fetchone()[0]
    print (rowcount)

    # items = []
    
    # for x in mycursor:
    #     items.append(x)
    return { "vcount": rowcount }
    # return json.dumps(items)
    # return { "message": "Howdy!" }
