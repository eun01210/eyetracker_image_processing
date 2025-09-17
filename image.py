import cv2 # 이미지 편집 모듈 사용
import glob # 다수의 파일 불러오는 모듈 사용

bimage = cv2.imread("bimage.png") # 배경 이미지 불러오기 (하얀 화면)
h, w = bimage.shape[:2] # 이미지 크기 저장

def sqcolor(image, m, n): # 해당 이미지의 색을 저장하는 함수
    xy = [] # 색 채널을 담을 배열
    for i in range(0, n): # 입력된 y좌표 만큼 반복
        xy.append([]) # 배열 생성 (x*y만큼의 2차원 배열을 만들기 위함)
        for j in range(0, m): # 입력된 x좌표 만큼 반복
            xy[i].append("X") # 해당 칸을 X로 설정 (공백)
    for y in range(0, n): # 입력된 y좌표 만큼 반복
        for x in range(0, m): # 입력된 x좌표 만큼 반복
            B = image.item(y, x, 0) # 해당 좌표의 Blue값 저장
            G = image.item(y, x, 1) # 해당 좌표의 Green값 저장
            R = image.item(y, x, 2) # 해당 좌표의 Red값 저장
            xy[y][x] = (R, G, B) # 배열에 해당 좌표의 R,G,B값 저장

    return xy # 배열 반환

bixy = sqcolor(bimage, w, h) # 배경의 xy좌표의 색 저장
images = glob.glob("images\A\*.png") # images\A폴더에 있는 모든 png파일 불러오기

var = [] # 이미지 변화 측정을 위한 배열 (스택)

for i in range(0, h): # 배경 이미지의 y좌표 만큼 반복
    var.append([]) # 배열 생성 (x*y만큼의 2차원 배열을 만들기 위함)
    for j in range(0, w): # 배경 이미지의 x좌표 만큼 반복
        var[i].append(0) # 해당 칸을 0으로 설정 (스택)

for i in images: # 이미지의 수 만큼 반복
    print(i) # 몇 번째 이미지를 처리 중인지 출력
    che = cv2.imread(i) # 해당 이미지 불러오기
    chexy = sqcolor(che, w, h) # 해당 이미지의 색 저장
    for y in range(0, len(bixy)): # 해당 이미지의 y좌표만큼 반복
        min = "X" # 최솟값을 X로 설정
        max = "X" # 최댓값을 X로 설정
        for x in range(0, len(bixy[y])): # 해당 이미지의 x좌표만큼 반복
            temp = 0 # 임시 변수 (색 변화가 큰지 확인하기 위함)
            for t in chexy[y][x]: temp += t # 해당 이미지의 색 담기
            temp2 = 0 # 임시 변수
            for t in bixy[y][x]: temp2 += t # 배경 이미지의 색 담기
            if 60 <= abs(temp-temp2) <= 120: # 이미지가 색 차이가 나는 경우
                if min == "X": # 최솟값이 정해지지 않은 경우
                    min = x # 최솟값을 해당 x좌표로 설정
                    max = x # 최댓값을 해당 x좌표로 설정
                else: # 최솟값이 정해진 경우
                    if x > max: max = x # 최댓값을 해당 x좌표로 설정
        if min != "X": # 최솟값이 존재하는 경우
            for j in range(min, max+1): var[y][j] += 1 # 최솟값부터 최댓값까지 스택을 추가


for i in range(0, len(var)-1): # 모든 스택 확인
    for j in range(0, len(var[i])-1): # 모든 스택 확인 
        if var[i][j] != 0: # 해당 픽셀의 스택이 0이 아닌 경우
            bimage.itemset((i, j, 1), 255-var[i][j]*3.5) # 해당 픽셀의 Red값을 스택*3.5 만큼 뺌
            bimage.itemset((i, j, 2), 255-var[i][j]*3.5) # 해당 픽셀의 Green값을 스택*3.5 만큼 뺌

cv2.imwrite('finish.png', bimage) # 이미지 제작
'''
bimage = cv2.imread("bimage.png")
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
bixy = sqcolor(bimage, w, h)
images = glob.glob("images\B\*.png")

var = []

for i in range(0, h):
    var.append([])
    for j in range(0, w):
        var[i].append(0)

for i in images:
    print(i)
    che = cv2.imread(i)
    chexy = sqcolor(che, w, h)
    for y in range(0, len(bixy)):
        min = "X"
        max = "X"
        for x in range(0, len(bixy[y])):
            temp = 0
            for t in chexy[y][x]: temp += t
            temp2 = 0
            for t in bixy[y][x]: temp2 += t
            if 60 <= abs(temp-temp2) <= 120:
                if min == "X":
                    min = x
                    max = x
                else:
                    if x > max: max = x
        if min != "X":
            for j in range(min, max+1): var[y][j] += 1


for i in range(0, len(var)-1):
    for j in range(0, len(var[i])-1):
        if var[i][j] != 0:
            bimage.itemset((i, j, 2), 255-var[i][j]*2.45)
            bimage.itemset((i, j, 1), 255-var[i][j]*2.45)

cv2.imwrite('finish2.png', bimage)
bimage = cv2.imread("bimage.png")
#ㅡㅡㅡㅡㅡㅡㅡ
bixy = sqcolor(bimage, w, h)
images = glob.glob("images\C\*.png")

var = []

for i in range(0, h):
    var.append([])
    for j in range(0, w):
        var[i].append(0)

for i in images:
    print(i)
    che = cv2.imread(i)
    chexy = sqcolor(che, w, h)
    for y in range(0, len(bixy)):
        min = "X"
        max = "X"
        for x in range(0, len(bixy[y])):
            temp = 0
            for t in chexy[y][x]: temp += t
            temp2 = 0
            for t in bixy[y][x]: temp2 += t
            if 60 <= abs(temp-temp2) <= 120:
                if min == "X":
                    min = x
                    max = x
                else:
                    if x > max: max = x
        if min != "X":
            for j in range(min, max+1): var[y][j] += 1


for i in range(0, len(var)-1):
    for j in range(0, len(var[i])-1):
        if var[i][j] != 0:
            bimage.itemset((i, j, 2), 255-var[i][j]*2.5)
            bimage.itemset((i, j, 1), 255-var[i][j]*2.5)

cv2.imwrite('finish3.png', bimage)
bimage = cv2.imread("bimage.png")
#ㅡㅡㅡㅡㅡㅡㅡ
bixy = sqcolor(bimage, w, h)
images = glob.glob("images\D\*.png")

var = []

for i in range(0, h):
    var.append([])
    for j in range(0, w):
        var[i].append(0)

for i in images:
    print(i)
    che = cv2.imread(i)
    chexy = sqcolor(che, w, h)
    for y in range(0, len(bixy)):
        min = "X"
        max = "X"
        for x in range(0, len(bixy[y])):
            temp = 0
            for t in chexy[y][x]: temp += t
            temp2 = 0
            for t in bixy[y][x]: temp2 += t
            if 60 <= abs(temp-temp2) <= 120:
                if min == "X":
                    min = x
                    max = x
                else:
                    if x > max: max = x
        if min != "X":
            for j in range(min, max+1): var[y][j] += 1


for i in range(0, len(var)-1):
    for j in range(0, len(var[i])-1):
        if var[i][j] != 0:
            bimage.itemset((i, j, 2), 255-var[i][j]*4)
            bimage.itemset((i, j, 1), 255-var[i][j]*4)

cv2.imwrite('finish4.png', bimage)
bimage = cv2.imread("bimage.png")
#ㅡㅡㅡㅡㅡㅡㅡ
bixy = sqcolor(bimage, w, h)
images = glob.glob("images\E\*.png")

var = []

for i in range(0, h):
    var.append([])
    for j in range(0, w):
        var[i].append(0)

for i in images:
    print(i)
    che = cv2.imread(i)
    chexy = sqcolor(che, w, h)
    for y in range(0, len(bixy)):
        min = "X"
        max = "X"
        for x in range(0, len(bixy[y])):
            temp = 0
            for t in chexy[y][x]: temp += t
            temp2 = 0
            for t in bixy[y][x]: temp2 += t
            if 60 <= abs(temp-temp2) <= 120:
                if min == "X":
                    min = x
                    max = x
                else:
                    if x > max: max = x
        if min != "X":
            for j in range(min, max+1): var[y][j] += 1


for i in range(0, len(var)-1):
    for j in range(0, len(var[i])-1):
        if var[i][j] != 0:
            bimage.itemset((i, j, 2), 255-var[i][j]*3.5)
            bimage.itemset((i, j, 1), 255-var[i][j]*3.5)

cv2.imwrite('finish5.png', bimage)
#ㅡㅡㅡㅡㅡㅡㅡ'''