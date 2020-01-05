# Flask提供一组模块，帮你构建服务器端Web应用，这是一个微Web框架（轻级量的）
# Django是框架之母，有特别强大的管理功能。


from flask import Flask,render_template,request,redirect,escape # 模块是'flask'，类名是'Flask'
# 也可以用import flask，但后面就要用flask.Flask来指示Flask类，可读性不好
from vsearch import search4letters

app = Flask(__name__) # 创建Flask对象的一个实例，并把它赋给'app'


# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')

def log_request(req: 'flask_request',res:str) -> None:
    with open('vesearch.log','a') as log:
         print(req.form,req.remote_addr,req.user_agent,res,file=log,sep='|')

@app.route('/search4',methods=['POST'])
def do_search() -> 'str':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase,letters))
    log_request(request,results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_result=results,)
    return str(search4letters('life,the universe,and everthing','eiru,!')) # str让集合变为字符串

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vesearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data','Remove_addr','User_agent','Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')

if __name__ == '__main__':
    app.run(debug=True) # debug=True打开调节模式
# _name_
# 1、 _name_值由python解释器维护，在代码的任何地方使用这个值时，它会设置为当前活动模块的名字。
# 2、 _name_必须作为一个参数值传递这个值
# 3、有两个下划线是一种命名约定，叫duner name