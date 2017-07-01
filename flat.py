import numpy as np
import cv2
import time
from cStringIO import StringIO
import math

def main():
    im=cv2.imread('img1.png')
    mat=cv2.imread('mat.jpg')
    
    print im.shape
    # print datetime.now().strftime('%Y_%m_%d')
    # h=im.shape[0]
    # w=im.shape[1]
    # print cv2.__version__
    # print im[0:5,0:5]
    # x=np.zeros(5,5)
    # print x
    # cv2.circle(im,(w/2,h/2), 5, (0,0,255), -1)
    # cv2.circle(im,(w/2,0), 5, (0,0,255), -1)
    # cv2.line(im,(w/2,0),(w/2,h/2),(0,0,255),2)
    # cv2.circle(im,(w/2,h/2), h/2, (0,0,255), 2)
    # cv2.circle(im,(w/2,h/2), h/4, (255,0,255), 2)
    # cv2.circle(im,(w/2,h/2), 100, (0,255,0), 2)
    
    print im[0][0]
    new = np.zeros((3840,3840,3), np.uint8)
    pad=(3840-2160)/2
    new[pad:3840-pad,:]=im
    h=new.shape[0]
    w=new.shape[1]
    # cv2.circle(new,(w/2,w/2), w/2, (0,0,255), 2)
    mat = np.zeros((h,int(3.14159265359*w/2),3), np.uint8)
    print int(3.14159265359*w/2)
    

    # #############################
    # Circumference points method
    #
    # points=[]
    # for i in range(0,1):
    #     print i
    #     points=[]
    #     t = np.zeros((3840,3840),np.uint8)
    #     cv2.circle(t,(1920,1920),(1920-i) , 255, 1)
    #     points = np.transpose(np.where(t==255))
    #     print len(points)
    #     k=int(3.14159265359*w/2)-(len(points))
    #     print int(3.14159265359*w/2), '  ', len(points), '  ', k  
    #     s=0
    #     for p in points:
    #         # print p
    #         if p[0]<=1920:
    #             # print p, '  ', new[p[0]][p[1]]
    #             mat[i][s+k] = new[p[0]][p[1]]
    #             s=s+1
    #
    #
    ###################################################3
    

    ####################################################
    ####################################################
    ### remapping method
    # 
    #
    # for i in range(0,1):
    #     print i
    #     points=[]
    #     t = np.zeros((3840,3840),np.uint8)
    #     cv2.circle(t,(1920,1920),(1920-i) , 255, 1)
    #     points = np.transpose(np.where(t==255))
    #     print len(points)
        # k=int(3.14159265359*w/2)-(len(points))
        # print int(3.14159265359*w/2), '  ', len(points), '  ', k  
        # cv2.remap(src, map1, map2, interpolation[, dst[, borderMode[, borderValue]]]) 
        # cv2.remap(src, map1, map2, interpolation[, dst[, borderMode[, borderValue]]]) 

    #
    # 
    # 
    # 
    #     
    ###################################################
    ####################################################
    
    ####################################################
    ###polar method
    # #
    # v1.0
    # 
    # for r in range((w/2),1,-1):
    #     i=0
    #     for thetar in range(int(r*1.57079632679),-1,-1):
    #         mat[w/2-r][i]=new[int((h/2)+r*math.sin(90-thetar/r))][int((w/2)+r*math.cos(90-thetar/r))]
    #         i+=1
    #
    #
    #
    #v2.0
    # 
    print 'shape ', mat.shape
    print ' w ',w
    for r in range(int(w/2),1,-1):
        i=0
        # print 'r ', r
        
        for thetar in range(int(r*1.57079632679),-1,-1):
            # print 'theta ',thetar, ' i ', (r+int(w/2)), ' j ', (int(3.14159265359*w/2)-r+i)
            print ' i ', (w-(int(w/2)-r)-1),' j ',(int(3.14159265359*w/4)+i-1),  ' val ' ,new[int((h/2)+r*math.sin(90-thetar/r))][int((w/2)+r*math.cos(90-thetar/r))]
            mat[w-(int(w/2)-r)-1][int(3.14159265359*w/4)+i-1]=new[int((h/2)+r*math.sin(90-thetar/r))][int((w/2)+r*math.cos(90-thetar/r))]
            i+=1
    
    #
    #
    ####################################################
    ####################################################

    # t=np.array(h,dtype=np.float32)
    # print t
    # for i in range(0,h/2):
    #     t[i]=im[i][w/2]
    # for i in range((h/2)-1,-1,-1):
    #     t[(h/2)+(h/2)-i]=im[i][(w/2)+1]
    # pts1 = np.float32([[w/2,h/2],[w/2,0],[28,387],[389,390]])
    # pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    # new = np.copy(im)
    # new.fill(0)
    # cv2.imwrite('mat.jpg',new)
    # t = im[0:(h/2),(w/2):(w/2)+4]
    # # print t
    # fo = open("foo.txt", "wb")
    # fo.write(str(t));
    # fo.close();
    cv2.namedWindow('image',cv2.WINDOW_NORMAL );
    cv2.resizeWindow('image', 600,600)
    name='out/flat/mat_'+time.strftime('%Y%m%d_%H%M')+'.jpg'
    # cv2.imwrite(name,mat)
    cv2.imshow('image',mat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
