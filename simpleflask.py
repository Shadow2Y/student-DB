#from io import StringIO
import requests
import sys
import os
from flask import Flask,request,send_file,jsonify,json
from flask_cors import CORS
import flask_cors
import sqlite3 as sql

app = Flask(__name__)
CORS(app)

@app.route("/",methods=["GET"])
def home():
    if request.method == 'GET':
        return "TRY /view OR /add"


@app.route("/view",methods=["GET"])
def viewer():
    if request.method == 'GET':
        users = []
        conn = sql.connect('database.db')
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM students;")
        rows = cur.fetchall()

        for i in rows:
            user = {}
            user["stuname"] = i["NAME"]
            user["stureg"] = i["RegNo"]
            user["studob"] = i["DOB"]
            users.append(user)
        response = jsonify(users)        
        response.headers.add("Access-Control-Allow-Origin", "*")
        conn.close()
        return response

@app.route("/add",methods=["POST"])
def adder():
    if request.method == 'POST':
        stu = request.json
        conn = sql.connect('database.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO students (NAME, RegNo, DOB) VALUES (?, ?, ?)",(stu['name'],stu['reg'],stu['dob']))
        conn.commit()
        return "YES"
        

if __name__ == "__main__":
    app.run(debug=True) 