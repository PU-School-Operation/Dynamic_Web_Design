from flask import (
    Flask,
    request,
    render_template,
)  # 匯入 Flask, request 與 render_template

app = Flask(__name__)


# 1. 首頁：提供導覽連結 (P88)
@app.route("/")
def home():
    homepage = "<h1>Flask 範例主選單</h1>"
    homepage += "<a href='/user/小明'>使用動態路由</a><br>"
    homepage += "<a href='/search?keyword=flask&limit=5'>GET 傳遞參數</a><br>"
    homepage += "<a href='/poster'>POST 表單傳值</a><br>"
    homepage += "<a href='/hello/Tom?score=75'>模板渲染（Template）</a><br>"
    return homepage


# 2. 動態路由範例 (P60)
@app.route("/user/<string:name>")
def user(name):
    return f"<H1>哈囉，{name}！歡迎來到 我的網頁～</H1>"


# 3. GET 傳遞參數範例 (P61~P63)
@app.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword")
    limit = request.args.get("limit")
    if not keyword:
        return "請輸入搜尋關鍵字，例如：/search?keyword=flask"
    return f"搜尋關鍵字：{keyword}<br>顯示筆數限制：{limit or '未指定'}"


# 4. POST 表單傳值範例 (P64~P69)
@app.route("/poster", methods=["GET", "POST"])
def poster():
    if request.method == "POST":
        username = request.values.get("username", "未輸入")
        password = request.values.get("password", "未輸入")
        return f"<h3>POST 接收到的使用者：{username}，密碼：{password}</h3>"
    else:
        return """
        <h2>Flask POST 傳送資料範例</h2>
        <form action="#" method="post">
            <p>姓名：<input type="text" name="username"></p>
            <p>密碼：<input type="password" name="password"></p>
            <p><button type="submit">送出</button></p>
        </form>
        """


# 5. 模板渲染 (Template) 範例 (P70~P87)
@app.route("/hello/<string:name>")
def hello(name):
    # 從 GET 參數取得 score，預設為 0，並轉為整數供模板 if 判斷
    score = request.args.get("score", default=0, type=int)
    items = ["動態路由", "GET 傳遞參數", "POST 表單傳值", "Jinja2 模板渲染"]
    return render_template("hello.html", name=name, score=score, items=items)


# 主程式進入點
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
