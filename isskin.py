import cv2
import numpy as np
hs,ss,vs=np.load("[h,s,v]histskin.npy")  #(s for skin)
sums=np.sum(hs)  # (total pixels)
hn,sn,vn=np.load("[h,s,v]histnonskin.npy")  #(n nonskin)
sumn=np.sum(hn)  # (total pixels)
'''msp=float(max(hs)+max(ss)+max(vs))/(3*sums)
mnsp=float(min(hn)+min(sn)+min(vn))/(3*sumn)
print(msp)
print(mnsp)
print(msp/mnsp)'''
ps,pns,r=1,1,1 #probablities & ratio
img=cv2.imread("image.jpg",1)
img=cv2.resize(img, None, fx=0.9, fy=0.9)
cv2.imshow("orig",img)
imgc=img.copy()
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
new=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
new[:,:]=255
for x in range(img.shape[0]):
	for y in range(img.shape[1]):
		ps=float(hs[img[x,y][0]]+ss[img[x,y][1]]+vs[img[x,y][2]])/(3*sums)
		pns=float(hn[img[x,y][0]]+sn[img[x,y][1]]+vn[img[x,y][2]])/(3*sumn)
		r=ps/pns
		print(r)
		if(r<=3):# if r>3 then skin
			#new[x,y]=255-int((float(255)/16)*r)
			imgc[x,y]=255
	cv2.imshow("new",imgc)
	cv2.waitKey(1)
cv2.waitKey(0)
print(new,"Done!")
