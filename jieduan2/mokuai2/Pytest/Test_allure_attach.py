# 在测试报告中添加 text ，html ，png,MP4

import allure


def test_attach_text():
    # 添加文本信息
    allure.attach("添加文本信息", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    # 添加网页信息
    allure.attach("<body>这是html body</body>，“html测试快", attachment_type=allure.attachment_type.HTML)


def test_attach_png():
    # 添加图片
    allure.attach.file(r"E:\笔记\1计算机基础\1内容.png", name='添加图片', attachment_type=allure.attachment_type.PNG)


def test_attach_MP4():
    allure.attach.file(r"C:\Users\ZhouXiongWang\Desktop\新建文件夹\燃烧吧！废柴 01.mp4", name='添加视频',
                       attachment_type=allure.attachment_type.MP4)
