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

tags_dict = defaultdict(list)  # create dict based upon tag word from photos tag table
photoid_dict = defaultdict(list)  # create dict based upon photo id from photos tag table


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
    log.info('unsorted tags_list = ' + str(tags_list) + '\n')
    list.sort(tags_list)
    log.info('sorted tags_list = ' + str(tags_list))


def create_tag_matrix():
    for tag_x in tags_list:
        for tag_y in tags_list:
            mlist.append((tag_x, tag_y))
    for i in tags_list:
        for j in tags_list:
            matrix[(i), (j)]
    log.info(len(matrix))


def calculate_cooccurrences():
    count = 0
    for photoid, tag in sorted(photos_tags_list):
        tags_dict[tag].append(photoid)
    print tags_dict

    for photoid, tag in sorted(photos_tags_list):
        photoid_dict[photoid].append(tag)
    print photoid_dict

    for i in tags_list:
        for j in tags_list:
            for pid in photoid_dict:
                if j == i:
                    break
                elif j in photoid_dict[pid] and i in photoid_dict[pid]:
                    count = matrix[(i), (j)]
                    count = count+1
                    matrix[(i), (j)] = count
                else:
                    count = 0

    print sorted(matrix)
    foo = matrix[('sky', 'clouds')]
    print foo

def main(argv):
    # create_photos_list()
    create_photos_tags_list()
    create_tag_list()
    create_tag_matrix()
    calculate_cooccurrences()


if __name__ == "__main__":
    main(sys.argv)
