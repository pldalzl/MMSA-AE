import sys
import csv
import math
import logging

import pandas as pd

from collections import defaultdict
from operator import itemgetter

logging.basicConfig(filename='ae_debug.log', level=logging.DEBUG)
log = logging.getLogger('log')

# path variables
photos = '../data/photos.csv'
tags_csv = '../data/tags.csv'
photos_tags = '../data/photos_tags.csv'

# data structures
photos_list = []
photos_tags_list = []
tags_list = []
mlist = []
matrix = defaultdict(int)

tags_dict = defaultdict(list)
photoid_dict = defaultdict(list)


def create_photos_list():
    with open(photos, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            photos_list.append(row)


def create_photos_tags_list():
    with open(photos_tags, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            photos_tags_list.append(row)

    list.sort(photos_tags_list)


def create_tag_list():
    with open(tags_csv, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            tags_list.append(row[0])

    list.sort(tags_list)


def create_tag_matrix():
    for tag_x in tags_list:
        for tag_y in tags_list:
            mlist.append((tag_x, tag_y))
    for i in tags_list:
        for j in tags_list:
            matrix[(i), (j)]


def calculate_cooccurrences():
    count = 0
    for photoid, tag in photos_tags_list:
        photoid_dict[photoid].append(tag)
    for outer_tag in tags_list:
        for inner_tag in tags_list:
            for pid in photoid_dict:
                if inner_tag == outer_tag:
                    break
                elif inner_tag in photoid_dict[pid] and outer_tag in photoid_dict[pid]:
                    count = matrix[(outer_tag), (inner_tag)]
                    count = count + 1
                    matrix[(outer_tag), (inner_tag)] = count
                else:
                    count = 0
    names = [t for t in matrix.iterkeys()]
    print names
    df = pd.DataFrame([item for sublist in map(lambda a: a.keys(), matrix.iterkeys()) for item in sublist], columns=tags_list)
    print df


def compute_top5():
    water_list = []
    people_list = []
    london_list = []
    query_tags_dict = {'water': water_list, 'people': people_list, 'london': london_list}

    for tag in query_tags_dict.keys():
        for key in matrix.keys():
            if key[0] == tag:
                query_tags_dict[tag].append([key, matrix.get(key)])

    water_list = sorted(water_list, key=itemgetter(1), reverse=True)[0:5]
    people_list = sorted(people_list, key=itemgetter(1), reverse=True)[0:5]
    london_list = sorted(london_list, key=itemgetter(1), reverse=True)[0:5]
    results_list = [water_list, people_list, london_list]
    log.info('Results of top 5 tags :')
    log.info(results_list)

def compute_IDF():
    for tag_pair in matrix.iterkeys():
        x = matrix[tag_pair]
        num_images = len(photos_list)
        num_tags_dict = {}
        for image, tag in photos_tags_list:
            num_tags_dict[image].append(tag)
        num_tags =[]
        idf = math.log()

def output_matrix_csv():
    # df = pd.DataFrame(matrix.values(), index=pd.MultiIndex.from_tuples(matrix.keys(), names=[tags_list]))
    # df = pd.DataFrame(matrix.items())
    # df.set_index(0, inplace=True)
    # print df
    # df.to_csv('../data/matrix.csv', sep='\t', encoding='utf-8')
    pass


def main(argv):
    result = []
    create_photos_list()
    create_photos_tags_list()
    create_tag_list()
    create_tag_matrix()
    calculate_cooccurrences()
    compute_top5()
    output_matrix_csv()
    # log.info(sorted(matrix.items(), key=lambda x: x[1], reverse=True))



if __name__ == "__main__":
    main(sys.argv)
