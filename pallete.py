# PASCAL Context
colours_context = [(0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128),
                   (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0), (192, 128, 0),
                   (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128), (0, 64, 0), (128, 64, 0),
                   (0, 192, 0), (128, 192, 0), (0, 64, 128), (128, 64, 128), (0, 192, 128), (128, 192, 128),
                   (64, 64, 0), (192, 64, 0), (64, 192, 0), (192, 192, 0), (64, 64, 128), (192, 64, 128),
                   (64, 192, 128), (192, 192, 128), (0, 0, 64), (128, 0, 64), (0, 128, 64), (128, 128, 64),
                   (0, 0, 192), (128, 0, 192), (0, 128, 192), (128, 128, 192), (64, 0, 64), (192, 0, 64),
                   (64, 128, 64), (192, 128, 64), (64, 0, 192), (192, 0, 192), (64, 128, 192), (192, 128, 192),
                   (0, 64, 64), (128, 64, 64), (0, 192, 64), (128, 192, 64), (0, 64, 192), (128, 64, 192),
                   (0, 192, 192), (128, 192, 192), (64, 64, 64), (192, 64, 64), (64, 192, 64), (192, 192, 64)]

# Cityscapes
colours_cityscapes = [(128, 64, 128), (244, 35, 231), (69, 69, 69)
                      # 0 = road, 1 = sidewalk, 2 = building
    , (102, 102, 156), (190, 153, 153), (153, 153, 153)
                      # 3 = wall, 4 = fence, 5 = pole
    , (250, 170, 29), (219, 219, 0), (106, 142, 35)
                      # 6 = traffic light, 7 = traffic sign, 8 = vegetation
    , (152, 250, 152), (69, 129, 180), (219, 19, 60)
                      # 9 = terrain, 10 = sky, 11 = person
    , (255, 0, 0), (0, 0, 142), (0, 0, 69)
                      # 12 = rider, 13 = car, 14 = truck
    , (0, 60, 100), (0, 79, 100), (0, 0, 230)
                      # 15 = bus, 16 = train, 17 = motocycle
    , (119, 10, 32)]
# 18 = bicycle

# colour map
colours_voc12 = [(0, 0, 0)
                 # 0=background
    , (128, 0, 0), (0, 128, 0), (128, 128, 0), (0, 0, 128), (128, 0, 128)
                 # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
    , (0, 128, 128), (128, 128, 128), (64, 0, 0), (192, 0, 0), (64, 128, 0)
                 # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
    , (192, 128, 0), (64, 0, 128), (192, 0, 128), (64, 128, 128), (192, 128, 128)
                 # 11=diningtable, 12=dog, 13=horse, 14=motorbike, 15=person
    , (0, 64, 0), (128, 64, 0), (0, 192, 0), (128, 192, 0), (0, 64, 128)]
# 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor

# ADE20k 150 categories
colours_ade = [[120, 120, 120], [180, 120, 120], [  6, 230, 230], [ 80,  50,  50], [  4, 200,   3], [120, 120,  80], [140, 140, 140], [204,   5, 255], [230, 230, 230], [  4, 250,   7], [224,   5, 255],
 [235, 255,   7], [150,   5,  61], [120, 120,  70], [  8, 255,  51], [255,   6,  82], [143, 255, 140], [204, 255,   4], [255,  51,   7], [204,  70,   3], [  0, 102, 200], [ 61, 230, 250],
 [255,   6,  51], [ 11, 102, 255], [255,   7,  71], [255,   9, 224], [  9,   7, 230], [220, 220, 220], [255,   9,  92], [112,   9, 255], [  8, 255, 214], [  7, 255, 224], [255, 184,   6],
 [ 10, 255,  71], [255,  41,  10], [  7, 255, 255], [224, 255,   8], [102,   8, 255], [255,  61,   6], [255, 194,   7], [255, 122,   8], [  0, 255,  20], [255,   8,  41], [255,   5, 153],
 [  6,  51, 255], [235,  12, 255], [160, 150,  20], [  0, 163, 255], [140, 140, 140], [250,  10,  15], [ 20, 255,   0], [ 31, 255,   0], [255,  31,   0], [255, 224,   0], [153, 255,   0],
 [  0,   0, 255], [255,  71,   0], [  0, 235, 255], [  0, 173, 255], [ 31,   0, 255], [ 11, 200, 200], [255,  82,   0], [  0, 255, 245], [  0,  61, 255], [  0, 255, 112], [  0, 255, 133],
 [255,   0,   0], [255, 163,   0], [255, 102,   0], [194, 255,   0], [  0, 143, 255], [ 51, 255,   0], [  0,  82, 255], [  0, 255,  41], [  0, 255, 173], [ 10,   0, 255], [173, 255,   0],
 [  0, 255, 153], [255,  92,   0], [255,   0, 255], [255,   0, 245], [255,   0, 102], [255, 173,   0], [255,   0,  20], [255, 184, 184], [  0,  31, 255], [  0, 255,  61], [  0,  71, 255],
 [255,   0, 204], [  0, 255, 194], [  0, 255,  82], [  0,  10, 255], [  0, 112, 255], [ 51,   0, 255], [  0, 194, 255], [  0, 122, 255], [  0, 255, 163], [255, 153,   0], [  0, 255,  10],
 [255, 112,   0], [143, 255,   0], [ 82,   0, 255], [163, 255,   0], [255, 235,   0], [  8, 184, 170], [133,   0, 255], [  0, 255,  92], [184,   0, 255], [255,   0,  31], [  0, 184, 255],
 [  0, 214, 255], [255,   0, 112], [ 92, 255,   0], [  0, 224, 255], [112, 224, 255], [ 70, 184, 160], [163,   0, 255], [153,   0, 255], [ 71, 255,   0], [255,   0, 163], [255, 204,   0],
 [255,   0, 143], [  0, 255, 235], [133, 255,   0], [255,   0, 235], [245,   0, 255], [255,   0, 122], [255, 245,   0], [ 10, 190, 212], [214, 255,   0], [  0, 204, 255], [ 20,   0, 255],
 [255, 255,   0], [  0, 153, 255], [  0,  41, 255], [  0, 255, 204], [ 41,   0, 255], [ 41, 255,   0], [173,   0, 255], [  0, 245, 255], [ 71,   0, 255], [122,   0, 255], [  0, 255, 184],
 [  0,  92, 255], [184, 255,   0], [  0, 133, 255], [255, 214,   0], [ 25, 194, 194], [102, 255,   0], [ 92,   0, 255]]


def gene_pascal_pallete(num_cls):
    n = num_cls
    pallete = [0] * (n * 3)
    for j in range(0, n):
        lab = j
        pallete[j * 3 + 0] = 0
        pallete[j * 3 + 1] = 0
        pallete[j * 3 + 2] = 0
        i = 0
        while lab:
            pallete[j * 3 + 0] |= (((lab >> 0) & 1) << (7 - i))
            pallete[j * 3 + 1] |= (((lab >> 1) & 1) << (7 - i))
            pallete[j * 3 + 2] |= (((lab >> 2) & 1) << (7 - i))
            i = i + 1
            lab >>= 3
    return pallete


if __name__ == '__main__':
    NUM_CLASS = 60  # 21 for VOC2012
    vocpallete = gene_pascal_pallete(NUM_CLASS)
    palletes = []
    for i in range(0, 180, 3):
        R = vocpallete[i]
        G = vocpallete[i + 1]
        B = vocpallete[i + 2]
        palletes_one = [R, G, B]
        palletes.append(tuple(palletes_one))
    print(palletes)
