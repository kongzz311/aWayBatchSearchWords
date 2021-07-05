#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:39:46 2019

@author: kongzz
"""
import pandas as pd
import requests
import os


def init(url):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    s = requests.session()
    s.headers.update(ua)
    s.get(url)
    return s


def fetch_exp(s, wd, url):
    params = {
        'a': 'getWordMean',
        'c': 'search',
        'list': '1',
        'word': wd,

    }
    return s.get(url, params=params)


def main():
    #   使用说明：把表格另存为csv格式 保存好 复制文件的地址 替换下面    originalFilePath = ‘’的路径
    #   运行结束后 假如顺利的话 在csv同目录下 就会出现一个新的文件里面有运行结果
    #   因为我就是也给自己用的 没有考虑其他异常 假如不成功的话 再找我～
    originalFilePath = '/Users/kongzz/Documents/MacBook Pro/Study/考研/英语/词汇/Vocabulary Builder/demo2.csv'
    FileName = os.path.split(originalFilePath)[1]
    PathName = os.path.split(originalFilePath)[0]
    #    editedFilePath = originalFilePath.replace(FileName, '')
    wds = pd.read_csv(originalFilePath, header=None)
    for i in range(10):
        wds['new_colu' + str(i)] = ''
    url = "http://www.iciba.com/index.php"
    session = init(url)
    for index, row in wds.iterrows():
        wd = row[0]
        if str(wd) != 'nan':
            exp = fetch_exp(session, wd, url)
            print(exp)
            try:
                wds.iloc[index, 1] = '[' + str(exp.json()['baesInfo']['symbols'][0]['ph_en']) + ']'
                parts = exp.json()['baesInfo']['symbols'][0]['parts']
                I = 2
                for item in parts:
                    wds.iloc[index, I] = item['part']
                    wds.iloc[index, I + 1] = str(item['means'])
                    I = I + 2
            except KeyError:
                print('KeyError ' + wd)
            except:
                print('Something wrong')

    wds.to_csv(os.path.join(PathName, FileName.split('.')[-2] + 'Edited.csv'))


if __name__ == '__main__':
    main()