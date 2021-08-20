from PIL import Image,ImageTk,ImageOps
import tkinter
from tkinter import filedialog

#画像サイズ
image_width = 480
image_height = 270

#アプリケーション実行
app = tkinter.Tk()
app.title(u"画像分割保存")
app.geometry("550x350")
app.resizable(width = False, height = False)

#開くイベント
def file_open():
    global image, path_address
    name = tkinter.filedialog.askopenfilename(title = "ファイル選択", initialdir="C:/", filetypes=[("Image File","*.png;*.jpg")])

    image = Image.open(name)
    path_address = image
    image = ImageOps.pad(image, (image_width, image_height))
    image = ImageTk.PhotoImage(image =  image)

    image_canvas.create_image(image_width / 2, image_height / 2, image = image)

#閉じるイベント
def file_close():
    image_canvas.delete("all")

#実行イベント
def execution_button_click():
    #トリミング前の値の定義,処理
    width = path_address.width / horizontal
    height = path_address.height / vertical
    vertical_count = 1
    picture_number = 1
    start_y = 0 - height
    end_y = 0
    while(vertical >= vertical_count):
        start_y += height
        end_y += height
        vertical_count += 1

        #値の初期化
        horizontal_count = 1
        start_x = 0
        end_x = width

        while(horizontal >= horizontal_count):
            crop_box = (start_x, start_y, end_x, end_y)
            img = path_address.crop(crop_box)
            img.save('OutputPicture/picture' + str(picture_number) + '.png')
            start_x += width
            end_x += width
            horizontal_count += 1
            picture_number += 1

#分割数設定処理イベント
def division_set():
    global division_set_window, vertical_entry, horizontal_entry
    division_set_window = tkinter.Toplevel()
    division_set_window.geometry("300x200")
    division_set_window.title(u"分割数指定")
    division_set_window.resizable(width = False, height = False)
    division_set_window.attributes("-topmost", True)

    #入力欄設定
    vertical_label = tkinter.Label(division_set_window, text="縦分割数")
    vertical_label.place(x=20, y=30)
    vertical_entry = tkinter.Entry(division_set_window, width=30)
    vertical_entry.insert(tkinter.END,u"")
    vertical_entry.pack()
    vertical_entry.place(x=80, y=30)

    horizontal_label = tkinter.Label(division_set_window, text="横分割数")
    horizontal_label.place(x=20, y=90)
    horizontal_entry = tkinter.Entry(division_set_window, width=30)
    horizontal_entry.insert(tkinter.END, u"")
    horizontal_entry.pack()
    horizontal_entry.place(x=80, y=90)

    ok_button = tkinter.Button(division_set_window, text="OK", command = ok_button_click)
    ok_button.place(x=130, y=150)

def ok_button_click():
    global vertical, horizontal
    str_vertical = vertical_entry.get()
    vertical = int(str_vertical)
    str_horizontal = horizontal_entry.get()
    horizontal = int(str_horizontal)
    division_set_window.destroy()


#メインウィンドウ処理実行ボタン
execution_button = tkinter.Button(app, text = "実行", command = execution_button_click)
execution_button.place(x = 470, y = 300)

#メニュー
menu = tkinter.Menu(app)

#ファイルの子メニュー
file = tkinter.Menu(menu, tearoff = 0)
file.add_command(label="開く", command = file_open)
file.add_command(label="閉じる", command = file_close)
file.add_separator()
file.add_command(label="終了", command = app.quit)

#設定の子メニュー
division = tkinter.Menu(menu, tearoff = 0)
division.add_command(label="分割数指定", command = division_set)

#親メニュー
menu.add_cascade(label="ファイル", menu=file)
menu.add_cascade(label="設定", menu=division)
app.config(menu=menu)

image_canvas = tkinter.Canvas(app, width = image_width, height = image_height)
image_canvas.pack()

app.mainloop()
