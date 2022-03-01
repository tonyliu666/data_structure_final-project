# data_structure_final-project
#### 以下是 final project的內容介紹
[Prog2.pdf](https://github.com/tonyliu666/data_structure_final-project/files/8161766/Prog2.pdf)

**開檔**

*在程式執行之初，使用sys.argv(import sys)來接受cmd輸入的引數，然後將檔案讀取之後，把字串內容整理成 2D array*
(code line 118~ 145)


**設定圖形邊界**
*在圖片匯入之後，需要先做預處理，將原圖pgm邊界先做空白的動作(預設值 255)，最後再把預處理後的圖片傳入edge detection函式之中*

**edge detection**
*做銳化的數值計算 
![image](https://user-images.githubusercontent.com/48583047/156176331-df25e2dc-ff4f-4efe-8104-c9638caf2e2a.png)
若計算出的數值比128(pixel value)來的大，則該pixel value就為0(黑色)否則就為白色

**輸出銳化後的檔案**

















