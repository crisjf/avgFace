from imutils import face_utils
import os,argparse
import imutils
import dlib
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--dir", required=True,help="path images")
args = vars(ap.parse_args())

predictor_path = 'predictors/shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

path = os.path.join('images',args['dir'])

imageFiles = [f for f in os.listdir(path) if f.split('.')[-1].lower() == 'jpg']

if not os.path.exists(os.path.join(path,'points')):
	os.makedirs(os.path.join(path,'points'))

for ifile in imageFiles:
	print ifile
	pointsFile = os.path.join(path,'points',ifile+'.txt')
	out = open(pointsFile,mode='w')

	image = cv2.imread(os.path.join(path,ifile))
	image = imutils.resize(image, width=600)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	 
	# detect faces in the grayscale image
	rects = detector(gray, 1)

	# loop over the face detections
	for (i, rect) in enumerate(rects):
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
		for (x, y) in shape:
			out.write(str(x)+' '+str(y)+'\n')
	out.close()
