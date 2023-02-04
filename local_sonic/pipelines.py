# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import openpyxl
from itemadapter import ItemAdapter
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment


class LocalSonicPipeline:
    # def process_item(self, item, spider):
    #     return item

    # excel的pipeline
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        # 单元格里面的字居中
        # align = Alignment(horizontal='center', vertical='center')
        # # openpyxl的下标从1开始
        # for i in range(1, 300):
        #     for j in range(1, 300):
        #         self.ws.cell(i, j).alignment = align

        # 打开后下面的表的名
        self.ws.title = 'glassbong'
        self.ws.column_dimensions['A'].width = 19
        self.ws.column_dimensions['B'].width = 115.0
        self.ws.column_dimensions['B'].width = 90.0
        for i in range(2, 300):
            self.ws.row_dimensions[i].height = 114
        self.ws.append(('图片', "详情", '链接'))

    # def open_spider(self, spider):
    #     self.ws = open('glassbong.xlsx', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        pos = item.get('pos', '')
        img_ = item.get('img', '')
        title = item.get('title', '')
        href = item.get('href', '')

        img = Image(img_)
        img.width = 150
        img.height = 150
        print('+++++++++')
        img_pos = 'A' + str(pos+2)
        print(img_pos)
        self.ws.add_image(img, img_pos)
        self.ws.append((" ", title, href))
        # self.ws.append((imgPath, title, href))
        return item

    def close_spider(self, spider):
        self.wb.save('glassbong.xlsx')

        # json 的pipeline
    # def open_spider(self,spider):
    #         self.fp = open('movie1.json','w',encoding='utf-8')
    #
    #
    # def process_item(self, item, spider):
    #
    #     self.fp.write(str(item))
    #     return item
    #
    #
    # def close_spider(self,spider):
    #     self.fp.close()
