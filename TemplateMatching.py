import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0;
    var_t = 0;
    location = [0, 0];
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------ 
    mean_t = temp.mean() #np.mean(temp)#[np.mean(temp,axis=0) np.mean(temp,axis=1)] 
    var_t= temp.var()
    max_corr = 0;
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0;
            var_s = 0;
            corr = 0;
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------ 
            roi= src[i:i+temp.shape[0],j:j+temp.shape[1]]
            mean_s= roi.mean()
            var_s= roi.var()
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            product = 0 
            for k in range (temp.shape[0]):
                for l in range (temp.shape[1]):
                    product = product + (roi[k,l] - mean_s) * (temp[k,l] - mean_t)    
            corr= (1/(temp.shape[0]*temp.shape[1]))* product /(var_s * var_t)
            #print(corr)
            if corr > max_corr:
                max_corr = corr;
                location = [i, j];
    return location

# load source and template images
source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
temp = cv2.imread('template_img.jpg',0) # read image in grayscale
location = TemplateMatching(source_img, temp, 20);
#location = [240,260]
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------ 
output = cv2.rectangle(match_img,(location[0],location[1]),(location[0]+temp.shape[1],location[1]+temp.shape[0]),(0,255,0),3)

# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------ 
cv2.imwrite('NCC_Out.jpg',output)

# Display the template image and the matching result
cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
cv2.imshow('TemplateImage', temp)
cv2.imshow('MyTemplateMatching', match_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
