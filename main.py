import cv2

def generate_single_marker(aruco_dict):
   marker_size = 0
   while True:
    marker_size = int(input("Enter the marker size: "))

    if marker_size < 7:
        print('Marker Size is Small')
        continue
    else:
        print(f'You entered {marker_size}')
        break
    
   marker_id = int(input("Enter the marker ID: "))

   marker_img = cv2.aruco.generateImageMarker(aruco_dict, marker_id,
    marker_size)

   cv2.imwrite("marker_{}.png".format(marker_id), marker_img)

   marker_img = cv2.imread("marker_{}.png".format(marker_id))

   cv2.imshow("Marker", marker_img)

   print("Dimensions:", marker_img.shape)

   cv2.waitKey(0)

def generate_bulk_markers(aruco_dict):
   marker_size = 0
   while True:
    marker_size = int(input("Enter the marker size: "))

    if marker_size < 7:
        print('Marker Size is Small')
        continue
    else:
        print(f'You entered {marker_size}')
        break
   num_markers = int(input("Enter the total number of markers to generate: "))
   marker_imgs = []

   for marker_id in range(num_markers):
       marker_img = cv2.aruco.generateImageMarker(aruco_dict, marker_id,
        marker_size)

       cv2.imwrite("marker_{}.png".format(marker_id), marker_img)
       marker_imgs.append(cv2.imread("marker_{}.png".format(marker_id)))

   for marker_img in marker_imgs:
       cv2.imshow("Marker", marker_img)
       print("Dimensions:", marker_img.shape)
       cv2.waitKey(0)

def main():
   aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)

   user_input = input("Press '1' -->> Single Marker or "
                       "'2' -->> Markers in Bulk: ")

   if user_input == "1":
       generate_single_marker(aruco_dict)
   elif user_input == "2":
       generate_bulk_markers(aruco_dict)
   else:
       print("Invalid input. Please try again.")

if __name__ == "__main__":
   main()