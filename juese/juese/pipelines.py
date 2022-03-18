# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class JuesePipeline(object):
    def __init__(self):
        result = open('juese.xls', 'w', encoding='gbk')
        result.write('角色\t等级\t生命值\t攻击力\t防御力\n')
    def process_item(self, item, spider):
        result = open('juese.xls','a',encoding='gbk')
        l = []
        l.append([item['name'],1,item['hp_1'],item['attack_1'],item['defend_1']])
        l.append([item['name'],20,item['hp_20'],item['attack_20'],item['defend_20']])
        l.append([item['name'],40,item['hp_40'],item['attack_40'],item['defend_40']])
        l.append([item['name'], 50, item['hp_50'], item['attack_50'], item['defend_50']])
        l.append([item['name'], 60, item['hp_60'], item['attack_60'], item['defend_60']])
        l.append([item['name'], 70, item['hp_70'], item['attack_70'], item['defend_70']])
        l.append([item['name'], 80, item['hp_80'], item['attack_80'], item['defend_80']])
        l.append([item['name'], 90, item['hp_90'], item['attack_90'], item['defend_90']])
        for i in range(8):
            for j in range(5):
                result.write(str(l[i][j]))
                result.write('\t')
            result.write('\n')
        return item
