from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import os


def display(decodedObjects):
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')



# Display barcode and QR code location  
##def display(im, decodedObjects):
##    # Loop over all decoded objects
##    for decodedObject in decodedObjects:
##        points = decodedObject.polygon
##
##        # If the points do not form a quad, find convex hull
##        if len(points) > 4:
##            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
##            hull = list(map(tuple, np.squeeze(hull)))
##        else:
##            hull = points;
##
##        # Number of points in the convex hull
##        n = len(hull)
##
##        # Draw the convext hull
##        for j in range(0, n):
##            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)
##
##    # Display results
##    cv2.imshow("Results", im)
##    cv2.waitKey(0)


# Main
def scan():
    # Reads image, decodes, and returns 'Type + Data' if barcode present, else empty array
    filepath = os.getcwd() + "/test_images/" + "capture.jpg"
    im = cv2.imread(filepath)
    decodedObjects = pyzbar.decode(im)
    if decodedObjects == []:  # no barcode detected
        return False
    else:                     # barcode detected, data of barcode returned
        for obj in decodedObjects:
            obj = str(obj.data).strip("b").strip("'")
            return (obj)
        
if __name__ == '__main__':
    print(scan())
     
    
##    print ("Press any key to stop program")
##    display(im, decodedObjects)
