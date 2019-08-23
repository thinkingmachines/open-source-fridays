import imageio
import imgaug as ia
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage

def display_results(image, boxes):
    bbs = []
    for box in boxes['output']['faces']:
        x, y, w, h = box['bounding_box']
        bbs.append(BoundingBox(x1=x, x2=x+w, y1=y, y2=y+h))
        
    image = imageio.imread(image)
    bbs = BoundingBoxesOnImage(bbs, shape=image.shape)
    ia.imshow(bbs.draw_on_image(image, size=2))