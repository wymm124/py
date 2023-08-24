from flask import Flask, render_template

# 在此处可以自定义 template_folder 属性来自定义文件夹的名称，如果定义了，则会去对应文件夹中找 html 文件
app = Flask(__name__)


# 创建了网址 /show/info 和 函数index 的对应关系
# 以后用户访问浏览器中的 /show/info，网址自动执行 index函数
@app.route("/show/info")
def index():
    # return "中国移不动"
    # return "中<h1>国</h1><span style='color:red;'>移不动</span>"

    # flask 内部是会自动打开这个文件，并读取内容，将内容返回给用户
    # 默认去当前项目目录的 templates 文件夹中找
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)
