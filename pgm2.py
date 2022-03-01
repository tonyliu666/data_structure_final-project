import sys
import math
import pdb


def remove_empty_lists(l):
    keep_going = True
    prev_l = l
    while keep_going:
        
        new_l = remover(prev_l)
        
        if new_l == prev_l:
            keep_going = False
       
        prev_l = new_l
    #return the result
    return new_l
def remover(l):
    
    newlist = []
    
    for i in l:
        
        
        if isinstance(i, list) and len(i) != 0:
            newlist.append(remover(i))
        
        if not isinstance(i, list):
            newlist.append(i)
    
    
    return newlist
def EdgeDetection(pixel):
	pixelconstant=128
	pixel=setboarder(pixel)
	
	for arr in pixel:
		for i in arr:
			if (i!=arr[0]|arr[-1]):
				if (i not in pixel[0][:])&(i not in pixel[-1][:]):
					indexY=arr.index(i)
					indexX=pixel.index(arr)
					try:
						rightindex=[indexX,indexY+1]
						upindex=[indexX-1,indexY]
						leftindex=[indexX,indexY-1]
						downindex=[indexX+1,indexY]
						uprightindex=[indexX-1,indexY+1]#右上角
						upleftindex=[indexX+1,indexY+1]
						downrightindex=[indexX+1,indexY+1]
						downleftindex=[indexX+1,indexY-1]
						a=pixel[indexX-1][indexY-1]
						b=pixel[indexX][indexY-1]
						c=pixel[indexX+1][indexY-1]
						d=pixel[indexX-1][indexY]
						f=pixel[indexX+1][indexY]
						g=pixel[indexX-1][indexY+1]
						h=pixel[indexX][indexY+1]
						i=pixel[indexX+1][indexY+1]
						x=(c+2*f+i)-(a+2*d+g)
						y=(g+2*h+i)-(a+2*b+c)
						if(math.sqrt(x*x+y*y)>=pixelconstant):
							i=0
							pixel[indexX][indexY]=i
						else:
							i=255
							pixel[indexX][indexY]=i
					except:
						pixel[indexX][indexY]=255
					

			

	return pixel 		

def writefile(width,height,maxval,pixel,path):
		lines=['P2\n','{0}{1}\n'.format(width,height),'{0}\n'.format(str(maxval))]
		for row in pixel:
			for val in row:
				lines.append("{0}\n".format(str(val)))
		with open(path,'w')as f:
			f.writelines(lines)			


def setboarder(pixel):#設定外圍的boarder為255
	pixel=list(pixel)
	i=len(pixel[0][:])
	a=0
	while a<i:
		pixel[0][a]=255
		a+=1
	

	for setting in pixel[1:-1][0:]:
		a=pixel.index(setting)
		setting[0]=255
		setting[-1]=255
		pixel[a]=setting
		
	h=len(pixel[-1][0:])
	b=0
	while b<h:
		pixel[-1][b]=255
		b+=1
	
	return(pixel)

#主程式開始地方
a=sys.argv[1]

	
with open(a) as pgm:#開檔
	count=0
	string=""
	empty2=[]
	BeforeFourLine=[]
	for word in pgm:#將字串內容合併成陣列
		empty3=[[]]
		emptyFourLine=[[]]
		count+=1
		empty=[]
			
			
		if count>=5:	
			
			word=word.replace("\n","")
			empty=word.split()
			results=list(map(int,empty))		
			empty2.append(results)
			empty2.append(empty3)
			
		else:
			stringlist=[]
			word=word.replace("\n","")
			stringlist=word.split()
			BeforeFourLine.append(stringlist)
			BeforeFourLine.append(emptyFourLine)
				
	while([[]] in BeforeFourLine):
		BeforeFourLine.remove([[]])#去空的二維陣列
				
	while([[]] in empty2):
		empty2.remove([[]])

	
#程式測試區塊
result=EdgeDetection(empty2)
writefile(512,512,255,result,"test_out.pgm")
	
					












