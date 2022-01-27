from flask import Flask, request,redirect, render_template, Blueprint
from os import listdir,mkdir
from datetime import date
from markupsafe import escape

app = Flask(__name__)

ip_list = listdir("ip")

@app.route("/",methods = ["GET","POST"])
def main():
    today = date.today()
    today = today.strftime("%d-%m-%Y")
    if request.method == "POST":
        data = request.get_data(as_text=True)

        if request.remote_addr not in ip_list:
            mkdir(f"ip/{str(request.remote_addr)}")
            ip_list.append(str(request.remote_addr))

        with open(f"ip/{str(request.remote_addr)}/{today}.txt","a",encoding="utf-8") as f:
            f.write(data)

        return redirect("/")
    
    return render_template("base.html",ip_s = ip_list)


@app.route("/<ip_addr>")
def files(ip_addr):
    ip_addr = escape(ip_addr)
    files_list = ""
    try:
        files_list = listdir(f"ip/{ip_addr}")
    except:
        pass
    return render_template("file_list.html",files = files_list,ip = ip_addr)

@app.route("/<ip_addr>/<file>")
def content(ip_addr,file):
    ip_addr = escape(ip_addr)
    file = escape(file)
    file_content = ""
    with open(f"ip/{ip_addr}/{file}","r",encoding="utf-8") as f:
        file_content = f.read()

    return render_template("content.html",content = file_content)

if __name__ == '__main__':
    app.run(debug = True)