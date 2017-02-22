from ImageSearch.ColorDescriptor import ColorDescriptor
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-d","--dataset",required=True,
                help="Path to the directory containing dataset")
ap.add_argument("-i","--index", required=True,
                help="Path to the directory where index would be stored")
args = vars(ap.parse_args())

cd = ColorDescriptor((12,8,3))

output = open(args[index],w)

for imagePath in glob.glob(args["dataset"]+"/*.png"):
     imageID = imagePath[imagePath.rfind("/")+1:]
     image = cv2.imread(imagePath)

     features = cd.describe(image)

     features = [str(f) for f in features]
     output.write("%s,%s\n" %(imageID, "," .join(features)))

output.close()
