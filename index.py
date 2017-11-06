from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2

#construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "Path to the directory that contains the images")
ap.add_argument("-i","--index",required = True, help = "Path to store the indexed images")
args = vars(ap.parse_args())

cd = ColorDescriptor((8,12,3))

output = open(args["index"],"w")


for imagePath in glob.glob(args["dataset"]+ "/*.jpg"):
    imageID = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    features = cd.describe(image)

    features = [str(f) for f in features]
    output.write("%s %s \n" % (imageID, ",".join(features)))

output.close()
