# WAPerceptionChallenge
This is the completed perception coding challenge that was completed by Sandeep Sankar.
The coding challenge was provided by Wisconsin Autonomous.

## Resulting Image
This is the image that is outputted by my implementation, which draws lines on the red cones in the image.


answer.png
:-----------:
![](https://github.com/ssankar25/WAPerceptionChallenge/blob/main/answer.png)

## Methodology
The methodology for designing this program involved researching what algorithms in OpenCV are useful in boundary and edge detection, and then designing the program.
The design process of this program included first learning Python and its basic syntax, as my main experience was mostly in Java prior to this. Then, I learned the different operations involved in OpenCV, including HSV color mapping, binary masking, and linear regression, which were then used in the final implementation of the program. 

## Challenges
The main challenge I encountered when writing this program was using the contour array to draw a linear regression. I first tried using a loop to connect all the points in the contour, which did not work because the contour array included points on both the left and right cone boundaries, so those were incorrectly connected to one another. However, even after separating the two cone paths, the resulting image was still incorrect since the lines did not trail off the edge of the boundary, as they did in the sample answer.png image given by WA. As a result, I used the fitLine function in OpenCV to draw a linear regression over the cone boundaries, giving the correct image.

## Libraries Used
The libraries that I used were OpenCV and numpy. OpenCV was used to detect the cones in the image, while numpy was used to organize the array and draw the linear regression.
