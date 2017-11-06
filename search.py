from colordescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--index",required=True, help ="Path where indexed images are stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

cd = ColorDescriptor((8,12,3))

query = cv2.imread(args["query"])
features = cd.describe(query)

searcher = Searcher(args["index"])
results = searcher.search(features)

cv2.imshow("Query",query)

for (score,resultID) in results:
    result = cv2.imread(args["result_path"] +"/" + resultID.split(' ',1)[0])
 #   cv2.namedWindow("Result", 0)
#    cv2.resizeWindow("Result",800,800)
    cv2.imshow("Result",result)
    cv2.waitKey(0)

    
