import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import shutil

if os.path.exists("./yolo-genshin/data/txt/"):  # 如果文件存在
    shutil.rmtree("./yolo-genshin/data/txt/")
    os.makedirs('./yolo-genshin/data/txt/')
else:
    os.makedirs('./yolo-genshin/data/txt/')



sets = ['train', 'test', 'val']

classes = ["character","hili","slime","caster","bighili","bosshili","samurai","robber"]


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('./yolo-genshin/data/xml/%s.xml' % (image_id))
    out_file = open('./yolo-genshin/data/txt/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()
print(wd)
for image_set in sets:
    os.remove("./yolo-genshin/data/"+image_set+".txt")
    if not os.path.exists('./yolo-genshin/data/txt/'):
        os.makedirs('./yolo-genshin/data/txt/')
    image_ids = open('./yolo-genshin/data/ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('./yolo-genshin/data/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        list_file.write('./yolo-genshin/data/Images/%s.png\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()