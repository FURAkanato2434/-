"""
[课程内容]: Python爬虫实战：突破小红书反爬，采集评论数据信息 https://www.xiaohongshu.com/

[授课老师]: 青灯教育-自游   [上课时间]: 20:00 可以点歌 可以问问题

[环境使用]:
    Python 3.10
    Pycharm

[模块使用]:
    requests --> pip install requests
    b --> pip install DrissionPage
---------------------------------------------------------------------------------------------------
win + R 输入cmd 输入安装命令 pip install 模块名 (如果你觉得安装速度比较慢, 你可以切换国内镜像源)
先听一下歌 等一下后面进来的同学,20:00 正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信python10010
---------------------------------------------------------------------------------------------------

"""
# # 导入自动化模块
# from DrissionPage import ChromiumPage
# # 导入日期转换模块
# from datetime import datetime
# # 导入csv模块
# import csv
# # 创建文件对象
# f = open('data.csv', mode='w', encoding='utf-8', newline='')
# # 字典写入方法
# csv_writer = csv.DictWriter(f, fieldnames=[
#     '昵称',
#     '日期',
#     '点赞',
#     '回复',
#     '地区',
#     '评论',
# ])
# # 写入表头
# csv_writer.writeheader()
# # 打开浏览器 (实例化浏览器对象)
# dp = ChromiumPage()
# # 监听数据包
# dp.listen.start('comment/page')
# # 访问网站
# dp.get('https://www.xiaohongshu.com/explore/65a63bf3000000002a0154a3?xsec_token=AB0gj6buELXRvAtPz0WVVM10HzyDf19cADiknjDZrlo2M=&xsec_source=pc_search')
# # 构建循环翻页
# for page in range(1, 21):
#     print(f'正在采集第{page}页的数据内容')
#     # 等待数据包加载
#     r = dp.listen.wait()
#     # 获取响应数据 -> json字典数据
#     json_data = r.response.body
#     # 字典取值, 提取评论数据所在列表
#     comments = json_data['data']['comments']
#     # for循环遍历, 提取列表里面的元素
#     """
#     comments = ['1', '2', '3']
#     # 对于comments中的元素循环提取, 用index变量接收
#     for a in comments:
#         print(a)
#     """
#     for index in comments:
#         """在循环中提取具体每条评论信息内容"""
#         # 获取index字典中所有的键
#         key_list = [i for i in index.keys()]
#         # 判断是否存在地区数据
#         if 'ip_location' in key_list:
#             ip_location = index['ip_location']
#         else:
#             ip_location = '未知'
#         # 提取评论时间戳
#         t = str(index['create_time'])[:-3]
#         # 把时间戳转成日期
#         date = str(datetime.fromtimestamp(int(t)))
#         dit = {
#             '昵称': index['user_info']['nickname'],
#             '日期': date,
#             '点赞': index['like_count'],
#             '回复': index['sub_comment_count'],
#             '地区': ip_location,
#             '评论': index['content'],
#         }
#         # 写入数据
#         csv_writer.writerow(dit)
#         print(dit)
#     id_ = index['id']
#     # 定位标签
#     tab = dp.ele(f'#comment-{id_}')
#     # 下滑页面
#     dp.scroll.to_see(tab)


import pandas as pd
df = pd.read_csv('data.csv')
# x = df['地区'].value_counts().index.to_list()
# y = df['地区'].value_counts().to_list()
# from pyecharts import options as opts
# from pyecharts.charts import Pie
# from pyecharts.faker import Faker
#
# c = (
#     Pie()
#     .add(
#         "",
#         [
#             list(z)
#             for z in zip(
#                 x,
#                 y,
#             )
#         ],
#         center=["40%", "50%"],
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="评论用户地区分布情况"),
#         legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     .render("pie_scroll_legend.html")
# )
import jieba
import wordcloud

content = ''.join([str(i) for i in df['评论']])
string = ' '.join(jieba.lcut(content))
wc = wordcloud.WordCloud(
    height=700,
    width=1000,
    background_color='white',
    font_path='msyh.ttc',
)
wc.generate(string)
wc.to_file('wordcloud.png')