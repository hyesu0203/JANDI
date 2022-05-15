'''
[78] 짝수 합 구하기
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

입력
정수 1개가 입력된다. (0 ~ 100)
5

출력
1부터 입력된 수까지 짝수의 합을 출력한다.
6
'''
sum = 0
num = int(input())
for i in range(0, num+1, 2):
    sum = sum+i
print(sum)

'''
[79] 원하는 문자가 입력될 때까지 반복 출력하기
'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

입력
문자들이 1개씩 계속해서 입력된다.
x b k d l q g a c

출력
'q'가 입력될 때까지 입력된 문자를 줄을 바꿔 한 줄씩 출력한다.
x
b
k
d
l
q
'''
# for 풀이
word = input().split()
for i in word:
    if i == 'q':
        break
    print(i)

# while 풀이
i = 0
word = input().split()
while word[i] != 'q':
    print(word[i])
    i = i+1

'''
[80] 언제까지 더해야 할까?
1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지 계속 더하는 프로그램을 작성해보자.
즉, 1부터 n까지 정수를 계속 더한다고 할 때, 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.

입력
정수 1개가 입력된다.
55

출력
1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가, 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력한다.
10
'''
# for 풀이
num = int(input())
sum = 0
for i in range(1, num+1):
    sum = sum+i
    if sum >= num:
        break
print(i)

# while 풀이
num = int(input())
sum = 0
i = 0
while sum < num:
    i = i+1
    sum = sum+i
print(i)

'''
[81] 주사위를 2개 던지면?
1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때 나올 수 있는 모든 경우를 출력해보자.

입력
주사위 2개의 면의 개수 n, m이 공백을 두고 입력된다.
단, n, m은 10이하의 자연수
2 3

출력
나올 수 있는 주사위의 숫자를 한 세트씩 줄을 바꿔 모두 출력한다.
첫 번째 수는 n, 두 번째 수는 m으로 고정해 출력하도록 한다.
1 1
1 2
1 3
2 1
2 2
2 3
'''
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)

'''
[82] 16진수 구구단
16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운 영일(01)이는 16진수끼리 곱하는 16진수 구구단에 대해서 궁금해졌다.
A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)

입력
16진수로 한 자리 수가 입력된다.
단, A ~ F 까지만 입력된다.
B

출력
입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다.
계산 결과도 16진수로 출력해야 한다.
B*1=B
B*2=16
B*3=21
B*4=2C
B*5=37
B*6=42
B*7=4D
B*8=58
B*9=63
B*A=6E
B*B=79
B*C=84
B*D=8F
B*E=9A
B*F=A5
'''
dan = input()
for i in range(1, 16):
    gop = hex(i)[2:].upper()
    dap = hex(int(dan, 16)*i)[2:].upper()  # 문자를 정수로 바꾸는 메서드
    print('{}*{}={}'.format(dan, gop, dap))

'''
[83] 3 6 9 게임의 왕이 되자
3 6 9 게임을 하던 영일이는 3 6 9 게임에서 잦은 실수로 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 마스터 프로그램을 작성해 보자.

입력
10 보다 작은 정수 1개가 입력된다. (1 ~ 9)
9

출력
1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데, 3 또는 6 또는 9인 경우 그 수 대신 영문 대문자 X 를 출력한다.
1 2 X 4 5 X 7 8 X
'''
# 3의 배수일 때 X처리하는게 정답
num = int(input())
for i in range(1, num+1):
    if i % 3 == 0:
        print('X')
    else:
        print(i)

'''
[84] 빛 섞어 색 만들기
빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 빛의 색을 만들어 내려고 한다.
빨강(r), 초록(g), 파랑(b) 각각의 빛의 개수가 주어질 때,
(빛의 강약에 따라 0 ~ n-1 까지 n가지의 빛 색깔을 만들 수 있다.)
주어진 rgb 빛들을 다르게 섞어 만들 수 있는 모든 경우의 조합(r g b)과 총 가짓 수를 계산해보자.

입력
빨녹파(r, g, b) 각 빛의 강약에 따른 가짓수(0 ~ 128))가 공백을 사이에 두고 입력된다. 예를 들어, 3 3 3 은 각 색깔 빛에 대해서 그 강약에 따라 0~2까지 3가지의 색이 있음을 의미한다.
2 2 2

출력
만들 수 있는 rgb 색의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로 줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력한다.
0 0 0
0 0 1
0 1 0
0 1 1
1 0 0
1 0 1
1 1 0
1 1 1
8
'''
r, g, b = map(int, input().split())
count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count += 1
print(count)

'''
[85] 소리 파일 저장용량 계산하기
1초 동안 마이크로 소리강약을 체크하는 수를 h (헤르쯔, Hz 는 1초에 몇 번? 체크하는가를 의미한다.)
한 번 체크한 결과를 저장하는 비트 b (2비트를 사용하면 0 또는 1 두 가지, 16비트를 사용하면 65536가지..)
좌우 등 소리를 저장할 트랙 개수인 채널 c (모노는 1개, 스테레오는 2개의 트랙으로 저장함을 의미한다.)
녹음할 시간 s가 주어질 때, 필요한 저장 용량을 계산하는 프로그램을 작성해보자.

입력
h, b, c, s 가 공백을 두고 입력된다.
h는 48,000이하, b는 32이하(단, 8의배수), c는 5이하, s는 6,000이하의 자연수이다.
44100 16 2 10

출력
필요한 저장 공간을 MB 단위로 바꾸어 출력한다.
단, 소수점 둘째 자리에서 반올림해 첫째 자리까지 출력하고 MB를 공백을 두고 출력한다.
1.7 MB
'''
h, b, c, s = map(int, input().split())
save = h*b*c*s / (8 * 1024 * 1024)
print(round(save, 1), 'MB')


'''
[86] 그림 파일 저장용량 계산하기
이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b 가 주어질 때, 
압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.

입력
w, h, b 가 공백을 두고 입력된다. 단, w, h는 모두 정수이고 1~1024 이다. b는 40이하의 4의 배수이다.
1024 768 24

출력
필요한 저장 공간을 MB 단위로 바꾸어 출력한다. 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력한 뒤 MB를 출력한다.
2.25 MB
'''
w, h, b = map(int, input().split())
save = w*h*b/(8*1024*1024)
print(round(save, 2), 'MB')


'''
[87] 여기까지! 이제 그만~
1, 2, 3 ... 을 순서대로 계속 더해나갈 때, 그 합이 입력한 정수보다 작을 동안만 계속 더하는 프로그램을 작성해보자.
즉, 1부터 n까지 정수를 계속 더한다고 할 때, 어디까지 더해야 입력한 수보다 같거나 커지는지 알아보고자 하는 문제이다.
하지만, 이번에는 그 때의 합을 출력해야 한다.
예를 들어 57을 입력하면 1+2+3+...+8+9+10=55에 다시 11을 더해 66이 될 때, 그 값 66이 출력되어야 한다.

입력
언제까지 합을 계산할 지, 정수 1개를 입력받는다.
단, 입력되는 자연수는 100,000,000이하이다.
57

출력
1, 2, 3, 4, 5 ... 순서대로 계속 더해가다가, 그 합이 입력된 정수보다 커지거나 같아지는 경우, 그때까지의 합을 출력한다.
66
'''
num = int(input())
sum = 0
for i in range(1, num+1):
    sum = sum+i
    if sum >= num:
        break
print(sum)

'''
[88] 3의 배수는 통과?
1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자.
예를 들면, 1 2 4 5 7 8 10 11 13 14 ... 와 같이 출력하는 것이다.

입력
정수 1개를 입력받는다.
(1 ~ 100)
10

출력
1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가시켜 출력하되 3의 배수는 출력하지 않는다.
1 2 4 5 7 8 10
'''
num = int(input())
for i in range(1, num+1):
    if i % 3 == 0:
        continue
    print(i)

'''
[89] 수 나열하기1
어떤 규칙에 따라 수를 순서대로 나열한 것을 수열(series)이라고 한다.
예를 들어 1 4 7 10 13 16 19 22 25 ... 은 1부터 시작해 이전에 만든 수에 3을 더해 다음 수를 만든 수열이다.
이러한 것을 수학에서는 앞뒤 수들의 차이가 같다고 하여 등차(차이가 같다의 한문 말) 수열이라고 한다.
수열을 알게 된 영일이는 갑자기 궁금해졌다.
"그럼.... 123번째 나오는 수는 뭘까?"

영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.
시작 값(a), 등차(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자.

입력
시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)가 공백을 두고 입력된다.(모두 0 ~ 100)
1 3 5

출력
n번째 수를 출력한다.
13
'''
a, d, n = map(int, input().split())
list = []

for i in range(n):
    a = a+d
    list.append(a)
print(list[-2])

'''
[90] 수 나열하기2
어떤 규칙에 따라 수를 순서대로 나열한 것을 수열이라고 한다.
예를 들어 2 6 18 54 162 486 ... 은 2부터 시작해 이전에 만든 수에 3을 곱해 다음 수를 만든 수열이다.
이러한 것을 수학에서는 앞뒤 수들의 비율이 같다고 하여 등비(비율이 같다의 한문 말) 수열이라고 한다.
등비 수열을 알게된 영일이는 갑자기 궁금해졌다.
"그럼.... 13번째 나오는 수는 뭘까?"

영일이는 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.
시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)가 입력될 때 n번째 수를 출력하는 프로그램을 만들어보자.

입력
시작 값(a), 등비의 값(r), 몇 번째 인지를 나타내는 정수(n)가 공백을 두고 입력된다.(모두 0 ~ 10)
2 3 7

출력
n번째 수를 출력한다.
1458
'''
a, r, n = map(int, input().split())
list = []

for i in range(n):
    a = a*r
    list.append(a)
print(list[-2])

'''
[91] 수 나열하기3
어떤 규칙에 따라 수를 순서대로 나열한 것을 수열이라고 한다.
예를 들어 1 -1 3 -5 11 -21 43 ... 은 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.
이런 이상한 수열을 알게 된 영일이는 또 궁금해졌다.
"그럼.... 13번째 나오는 수는 뭘까?"

영일이는 물론 수학을 아주 잘하지만 이런 문제는 본 적이 거의 없었다...
그래서 프로그램을 만들어 더 큰 수도 자동으로 계산하고 싶어졌다.
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)가 입력될 때, n번째 수를 출력하는 프로그램을 만들어보자.

입력
시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n)가 공백을 두고 입력된다.
(a, m, d는 -50 ~ +50, n은 10이하의 자연수)
1 -2 1 8

출력
n번째 수를 출력한다.
-85
'''
a, m, d, n = map(int, input().split())
list = []

for i in range(n):
    a = a*(m)+d
    list.append(a)
print(list[-2])

'''
[92] 함께 문제 푸는 날
같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가 매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?
예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다 한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

입력
같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는, 방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)
3 7 9

출력
3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.
63
'''
a, b, c = map(int, input().split())
day = 1
while day % a != 0 or day % b != 0 or day % c != 0:
    day += 1
print(day)
# a,b,c로 나눴을 때 모두 나머지가 없을 경우 (=최고공배수)
# 반복문을 나오도록 조건문을 작성함
