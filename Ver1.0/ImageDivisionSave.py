from PIL import Image

#Inputする画像の名前を拡張子付きで入力
picture_name = "Test1.png"
path = Image.open('InputPicture/' + picture_name)

#分割指定
vertical = 2    #縦分割数
horizontal = 4  #横分割数

width = path.width / horizontal
height = path.height / vertical

#トリミング前の値の定義,処理
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
        img = path.crop(crop_box)
        img.save('OutputPicture/picture' + str(picture_number) + '.png')
        start_x += width
        end_x += width
        horizontal_count += 1
        picture_number += 1