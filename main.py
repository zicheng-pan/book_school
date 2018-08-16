from flask import Flask, render_template, request, session, redirect, make_response
import util.getFile as fileUtil
import os
app = Flask(__name__)
app.secret_key = "super secret key"
file_path = './历史小说'
user_dict = {}
@app.route('/')
def lxd_list():
    file_list = fileUtil.getFileBypath(file_path)
    session['user'] = None
    return render_template("book_list.html",file_list = file_list)

file_generator = None
@app.route('/testpage/<book_name>')
def getBook_detailss(book_name):
    book_name = book_name +'.txt'
    if not session.get('user'):
        file_generator = fileUtil.getFileContent(os.path.join(file_path, book_name))
        session['user']="user"
        user_dict['user'] = file_generator
    content = user_dict['user'].__next__()
    return render_template("book_content.html",content_text = content,title=book_name)

file_generator = None
@app.route('/book_content/<book_name>')
def getBook_details(book_name):
    print('request book:'+book_name)
    book_name = book_name +'.txt'
    if not session.get('user'):
        file_generator = fileUtil.getFileContent(os.path.join(file_path, book_name))
        session['user']="user"
        user_dict['user'] = file_generator
    content = user_dict['user'].__next__()
    return render_template("book_content_pan.html",content_text = content,title=book_name)

@app.route('/getredmoney/<time>')
def getMoney(time):
    print("time:"+str(time))
    #TODO count money
    #TODO insert into database
    # del data
    return render_template("getmoney.html",money=time)


# del data source
if __name__ == '__main__':
    app.secret_key = 'super secret key'

    app.run('0.0.0.0',8080,debug=True)