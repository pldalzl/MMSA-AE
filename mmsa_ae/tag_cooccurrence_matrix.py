import sys
import csv
import logging

from collections import defaultdict


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


def create_photos_list():
    with open(photos, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            photos_list.append(row)
    log.info('photos_list length = ' + str(len(photos_list)))


def create_photos_tags_list():
    with open(photos_tags, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            photos_tags_list.append(row)
    log.info('photos_tags_list length = ' + str(len(photos_tags_list)))


def create_tag_list():
    with open(tags_csv, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            tags_list.append(row[0])
    log.info('tags_list length = ' + str(len(tags_list)))


def create_tag_matrix():
    # create matrix with tags
    for tag_x in sorted(tags_list):
        for tag_y in sorted(tags_list):
            mlist.append((tag_x, tag_y))

    # generate blank matrix table
    for i in sorted(tags_list):
        for j in sorted(tags_list):
            matrix[(i),(j)]
    log.info(matrix)

def main(argv):
    # create_photos_list()
    create_photos_tags_list()
    create_tag_list()
    create_tag_matrix()

if __name__ == "__main__":
    main(sys.argv)
