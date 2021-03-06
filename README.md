# 피보나치 수열 계산기
이 프로젝트는 학교 수학1 과목의 세특을 위해 제작되었습니다. (20916 이동훈)

## 소개
+ 이 프로젝트는 세특 제출용으로, 수학1 시간에 배운 **수열** 단원을 이용하여, 교과서 156p의 "창의융합 프로젝트" 의 "피보나치 수열" 부분을 이용하여 제작되었습니다.
+ 이 프로젝트는 VScode(코드 에디터) 를 이용하여 제작되었습니다.
+ 또한, 이 프로젝트는 **정보** 과목의 **문제해결과 프로그래밍** 단원을 이용하여 문제인식, 구성 등을 하였습니다.
+ **Python 3.8.10** 을 이용해 제작하였습니다.
+ 시간상 CLI 형식으로 제작하였습니다. (시간날때 GUI로 바꿀 예정입니다.)
+ black code style 를 사용하여, 설명이 긴 줄일경우 이상하게 잘릴수도 있습니다.
+ 만약 그림들이 흐리게 보이신다면, 그림을 클릭해주세요!!

## 코드(프로그램) 실행법
+ ~~이 프로그램은 exe파일로 패키징 되어 있음으로, 오른쪽 tag쪽에서 파일을 확인하실수 있습니다. (모듈과의 호환성으로 인한 오류로인해 사용 불가능합니다.)
+ 이 프로그램은 또한 이 리포 내의 fibonacci.py 파일을 python으로 실행할수도 있습니다.

-----

### 주제 선정 동기
수1 시간에 수열단원을 배우고, 교과서를 더 살펴보다가 156p 에 있는 "창의융합 프로젝트" 중의 "피보나치 수열" 이라는 내용을 발견했고, '음... 우리가 이 피보나치수열의 n번째 항을 구할때 n이 작다면 쉽게 구할수 있겠지만, n이 크다면 어떻게 구해야 할까?' 라는 생각이 들었고, 정보시간에 배웠던 "문제해결과 프로그래밍" 단원의 내용과, 최근에 배우고있는 "python" 이라는 프로그래밍 언어도 활용하여 피보나치 수열이 증가하는것을 그래프로 나타내고 싶어서 이 주제를 선정해서 탐구하게 되었다.

### 교과서와의 연관성
+ 수1 교과서 156p의 창의융합 프로젝트-피보나치 수열 부분을 활용하였습니다.
+ 정보 교과서의 문제해결과 프로그래밍 단원 활용을 활용하였습니다.

-----
## 탐구하기
이제 주제에 대해서 탐구해보자!!

### 문제분석
문제 : 피보나치 수열을 구하는 방법은 간단하게 아래의 식처럼 구할 수 있다.

![image](https://user-images.githubusercontent.com/77449586/125951803-cb48217f-4e32-44d9-8672-5a013ed4e80f.png)

(0번째 항을 굳이 정의한 이유는, 피보나치 수열의 n번째 항을 구할땐 {n-1번째 항} + {n번째 항} 으로 구해야하는데, 1번째 항을 구할땐 그 이전의 항을 구할수 없기 때문이다.

하지만 저런 방식으로 구하기위해선 피보나치 수열의 9번째 항을 구하든, 10000번째항을 구하든 무조건 1번째 항부터 계산해서 더해나가야 하고, 수가 커질수록 매우 오랜시간이 걸리는 문제가 있다.

#### 현재상태, 목표상태, 조건, 필요한정보 찾기
현재상태 : 피보나치 수열의 n번째 항을 구할때, n의 값이 크다면 구하는데 시간이 오래 걸린다.

목표상태 : 피보나치 수열의 n번째 항을 구할때, n의 값이 크더라도 빠르게 구할수 있어야한다.

조건 : 실행 속도가 빨라야한다.

필요한 정보 : 피보나치 수열의 n번째 항을 구하는 방법, n의 값

#### 문제의 분해
+ 피보나치 수열을 구하는 방법은?
+ 같은 동작을 하더라도, 그것을 구현할수 있는 방법은 여러개인데, 그중 가장 효율적인 방법은?
+ 사용자에게 결괏값을 어떻게 전달할것인가?

### 문제의 구조화
아래는 프로그램이 돌아가는 과정을 간단하게 구조화해서, 정보시간에 배운 순서도로 표현한것이다.
![image](https://user-images.githubusercontent.com/77449586/125955834-871ea179-9fcc-4b21-bc08-ae1562be0c8c.png)

### 알고리즘
알고리즘의 다섯가지 조건은 아래와 같다.
+ 입력값이 0개 이상일것
+ 출력값이 1개 이상일것
+ 수행이 가능할것
+ 명령이 명확할것
+ 유한할것

위의 조건에 맞추어 알고리즘을 짜보도록 할 것이다.

#### 알고리즘 설계
먼저 **의사코드** 를 통해 구성하고나서, **순서도** 를 통하여 알고리즘을 설계할 것이다.

이 프로그램은 다음과 같은 순서로 작동될것이다.

1. 어떤 기능을 사용할것인지 고른다. (n번째 항만 구하기, n번째 항을 구하고 그래프도 그리기, k번째 항부터 n번째 항까지의 합 구하기, k번째 항부터 n번째 항까지의 합 과 그래프 구하기)
2. 기능에 따른 값 입력받기 (n번째 항을 구할경우 n만, k번째 항부터 n번째 항까지의 합을 구할경우 k 와 n)
3. 계산하기
4. 기능에 따른 결괏값 출력하기

이제 순서도를 그리기전에, 피보나치 수열의 값을 구하기 위한 가장 효율적인 방법을 생각해보자!

프로그래밍은 매우 자유로워서, 어떤 방법으로든 자신이 원하는 것을 구현해낼수 있다.

나는 가장 간단한 방법인 2가지 방법으로 구현해 볼 것이다!

첫번째 방법은 **반복문** 을 이용한 방법이다.

아래는 반복문을 이용하여 피보나치수열의 n번째 항을 구하는 코드이다.
```python
def fibo(n: int) -> int: # fibo 라는 이름의 정수형인 매개변수 n을 받는 함수를 정의한다.
    before_res = 0 # 이전값을 정의한다.
    res = 1 # 계산값을 정의한다.
    if n == 0: # 만약 n이 0일때
        return 0 # 0을 돌려준다
    for i in range(1, n): # i 에 1 부터 1-n 까지를 대입하며, 반복한다.
        res_copy = res # 결괏값의 복사본을 만든다.
        res = res + before_res # 이전 결괏값과 현재 결괏값을 더해 새로운 결괏값을 구한다.
        before_res = res_copy # 이전 결괏값엔 현재 결괏값을 넣어준다.

    return res # 결괏값을 돌려준다.
```

음... 일단 코드는 만들었는데, 어떤 방법으로 이 코드가 효율적인지를 알수있을까?

나는 일단 **코드의 실행시간** 을 기준으로 삼고 해보겠다.

python에서 정의한 함수를 사용하는 방법은 아래와 같다.
```python
fibo(3) # 위에서 만든 함수의 n에 3을 대입한다.
```

다음은 코드의 실행시간을 구하는 방법이다.

코드의 실행시간을 구하려면 {코드를 실행하고 난 시간} - {코드를 실행하기 전의 시간} 으로 구성하면 될것이다. 이것을 구현한것은 아래와 같다.

```python
import time # 시간관련 기능을 사용하게 해주는 모듈을 불러온다.
start = time.time() # 시작시간을 정의한다.
fibo(1000) # 함수를 실행한다.
take_time = time.time() - start # 현재시간에서 시작시간을 뺀다.
print(take_time) # 소요시간을 출력한다.
```

위의 코드를 이용하여 구한 실행소요시간은 `0.0009984970092773438초` 였다.
하지만 수가 너무작아서 비교하기에 어려움이 있어, n에 1000 대신 100000 을 넣어서 다시 하였고, 소요시간은 `0.12199640274047852초 (0.12초)` 였다.

이제 두번째 방법으로 구해보자.

두번째 방법은 재귀함수를 사용하는것이다.

재귀함수란, 자신이 자신을 호출하는 함수를 말하는데, 이것의 단점은 구하려는 값이 커지면 커질수록 복잡도가 증가하는 것이다.

재귀함수를 이용한 방법은 만약 n이 10 이라면, n-1인 9와 n-2인 8을 n에 대입하여 자기자신을 호출하고, 결국 n이 1 또는 0이 되게 된다면 1과 0을 반환하는 것이다.

이 코드의 실행과정을 그림으로 그려보면 다음과 같다.
![image](https://user-images.githubusercontent.com/77449586/125963160-2488a064-4126-4a71-855f-21c5d6b6ae80.png)

(각 값들은 아래의 두개 값을 합한것과 같다.)

코드는 아래와 같다.
```python
def fibo2(n: int) -> int: # fibo2 라는 이름의 정수형인 매개변수 n을 받는 함수를 정의한다.
    if n == 0: # 만약 n이 0일때
        return 0 # 0을 반환한다.
    elif n == 1 or n == 2: # 만약 n이 1일때
        return 1 # 1을 반환한다.
    else: # 위의 조건들이 성립하지 않는다면
        return fibo2(n - 1) + fibo2(n - 2) # 위의 그림처럼 아래의 수를 구하는 코드를 호출한다.
```

하지만 이 코드로 피보나치 수열의 100000번째 값을 구해보려고 시도하면 다음과 같은 오류가 발생한다. `RecursionError: maximum recursion depth exceeded in comparison`

저 에러는 너무 많은 재귀함수를 호출하려는것을 파이썬 인터프리터가 인지하고, 막는 것이다.

그렇다면 이 방법으로는 피보나치 수열의 값을 구할수 없는것일까? 

이런 상황에서 사용할수 있는 내장모듈의 함수가 있는데, 그것은 바로 functools 의 lru_cache 이다.

이 함수(데코레이터) 는 재귀함수에 사용하는 함수인데, 주로 하는 역할으로는 한번 호출된 함수의 결괏값을 저장한다.

이 함수를 적용한 코드로 다시 실행해 봤더니.. 앗!! 같은 오류가 난다.

이 함수를 적용함으로써 코드의 반복횟수는 995회에서 496회로 줄긴 했지만, 그럼에도 너무 많은 호출로인해 파이썬 인터프리터가 차단한것이다.

그럼으로, 이 방법은 적절하지 않다는것을 알수있다.

그래서 우리는 첫번째 방법을 사용해 볼것이다!!

위의 내용을 토대로 구체화 하여 순서도를 그려보자!!

아래의 사진은 순서도 모양의 의미이다
![image](https://user-images.githubusercontent.com/77449586/125957184-c496ba11-c547-4330-9df7-b725c9f85b01.png)

아래의 사진은 순서도로 구성한것이다.

![수1](https://user-images.githubusercontent.com/77449586/125966167-c2802399-52b5-446c-bc26-efa744a326dc.png)

이제 전체 코드를 짜보도록 하자.

피보나치수열의 n번째 항을 구하는 방법으로는 위에서 고른 코드를 이용할것이다.
```pyhon
def fibo(n: int) -> int:  # fibo 라는 이름의 정수형인 매개변수 n을 받는 함수를 정의한다.
    before_res = 0  # 이전값을 정의한다.
    res = 1  # 계산값을 정의한다.
    if n == 0:  # 만약 n이 0일때
        return 0  # 0을 돌려준다
    for i in range(1, n):  # i 에 1 부터 1-n 까지를 대입하며, 반복한다.
        res_copy = res  # 결괏값의 복사본을 만든다.
        res = res + before_res  # 이전 결괏값과 현재 결괏값을 더해 새로운 결괏값을 구한다.
        before_res = res_copy  # 이전 결괏값엔 현재 결괏값을 넣어준다.

    return res  # 결괏값을 돌려준다.
```

다음은 이 피보나치수열의 값들을 리스트로 돌려주는 코드이다.
```python
def fibo_list(n: int) -> list:
    before_res = 0  # 이전값을 정의한다.
    res = 1  # 계산값을 정의한다.
    res_list = []  # 리스트 형식으로 반환하기위해, 리스트를 정의한다.
    res_list.append(1)  # 첫번째 값을 넣어준다.
    if n == 0:  # 만약 n이 0일때
        return 0  # 0을 돌려준다
    for i in range(1, n):  # i 에 1 부터 1-n 까지를 대입하며, 반복한다.
        res_copy = res  # 결괏값의 복사본을 만든다.
        res = res + before_res  # 이전 결괏값과 현재 결괏값을 더해 새로운 결괏값을 구한다.
        before_res = res_copy  # 이전 결괏값엔 현재 결괏값을 넣어준다.
        res_list.append(res)  # 리스트의 마지막에 새로운 결괏값을 넣어준다.

    return res_list  # 결괏값을 돌려준다.
```

다음은 리스트의 값들을 합치는 함수이다. (시그마와 비슷한 역할이다.)
```python
def sigma(res_list: list, k: int = 1):
    res = 0  # 결괏값을 0으로 초기화한다.
    for i in range(k-1, len(res_list)):  # i에 k부터 리스트의 길이만큼 대입하며 반복한다.
        res += res_list[i]  # 결괏값에 리스트의 i번째 값을 더한다.
    return res  # 반복문이 끝나면 결괏값을 돌려준다.
```

다음은 리스트를 이용해 그래프를 그리는 코드이다.
```python
import matplotlib.pylab as plt  # matplotlib 에서의 pylab 모듈을 plt 라는 이름으로 불러온다. (그래프를 그려주는 패키지이다.)
def graph(res_list: list):
    x = list(range(1, len(res_list)+1))  # x값을 지정한다.
    y = res_list  # y에 res_list 를 대입한다.
    # 그래프를 그려주는 모듈인 matplotlib 의 pylab 안에있는 plot 함수를 사용하여 x, y를 대입하여 그래프를 그린다.
    plt.plot(x, y)
    plt.show()  # 그래프를 출력한다.
```

다음은 이 코드들을 작동하게 해주는 메인 함수 코드이다.
```python
def main():
    cal_type = int(input("""
어느 기능을 사용하시겠습니까?
    1. 피보나치 수열의 n번째항 만 구하기
    2. 피보나치 수열의 n번째항 과, 그래프 구하기
    3. 피보나치 수열의 k번째에서 n번째까지의 합 구하기
    4. 피보나치 수열의 k번째에서 n번째까지의 합과 그래프 구하기
>>
    """))  # input 함수는 사용자가 콘솔에 친 내용을 받아오며, 괄호안의 내용을 출력하는 함수이다.
    if cal_type == 1:  # 만약 cal_type 가 1이라면
        n = int(input("n을 입력해주세요 : "))  # 값을 입력받는다.
        res = fibo(n)  # 결괏값을 구한다.
        print(f"결괏값 : {res}")  # 결괏값을 출력한다.
    elif cal_type == 2:  # 만약 cal_type 가 2라면
        n = int(input("n을 입력해주세요 : "))  # 값을 입력받는다.
        res = fibo(n)  # 결괏값을 구한다.
        res_list = fibo_list(n)  # 그래프를 그리기위한 리스트를 구한다.
        graph(res_list)  # 그래프를 그린다.
        print(f"결괏값 : {res}")  # 결괏값을 출력한다.
    elif cal_type == 3:  # 만약 cal_type 가 3이라면
        n = int(input("n을 입력해주세요 : "))  # 값을 입력받는다.
        k = int(input("k를 입력해주세요 : "))  # 값을 입력받는다.
        res_list = fibo_list(n)  # 결괏값 리스트를 구한다.
        res = sigma(res_list, k)  # k항부터 n항까지의 합을 구한다.
        print(f"결괏값 : {res}")  # 결괏값을 출력한다.
    elif cal_type == 4:  # 만약 cal_type 가 4라면
        n = int(input("n을 입력해주세요 : "))  # 값을 입력받는다.
        k = int(input("k를 입력해주세요 : "))  # 값을 입력받는다.
        res_list = fibo_list(n)  # 결괏값 리스트를 구한다.
        res = sigma(res_list, k)  # k항부터 n항까지의 합을 구한다.
        graph(res_list)  # 그래프를 그린다.
        print(f"결괏값 : {res}")  # 결괏값을 출력한다.
    isrestart = input("다시 계산하시겠습니까? (y/n) : ")  # 값을 입력받는다.
    if isrestart == 'y':  # 만약 isrestart가 y라면
        main()  # 자신을 다시 실행시킨다.
    elif isrestart == 'n':  # 만약 isrestart가 n이라면
        print("수고하셨습니다.")  # 괄호안의 내용을 출력한다.
    else:  # 위의 조건들이 성립하지 않는다면
        print("옳지않은 입력입니다. 프로그램을 종료합니다.")  # 괄호안의 내용을 출력한다.
```

이제 코드를 모두 구성했다. 한번 테스트해보자! (만약 그림들이 흐리게 보이신다면, 그림을 클릭해주세요!!)
![usingexample2](https://user-images.githubusercontent.com/77449586/125972340-416edf3a-7dce-4357-b603-1f56470a67cc.gif)


#### exe 파일로 만들기
이 프로그램을 python이 설치되어있지 않은곳에서 실행해야 할 때도 있을것이다. 그럴때를 위해서 exe파일로 만들어보자. (이 프로젝트에서는 pyinstaller을 사용할것이다.)

먼저 아래의 명령어를 사용하여 pyinstaller 를 설치해보자

![image](https://user-images.githubusercontent.com/77449586/125972117-1493df5c-9d07-4362-93bb-49b5c2f4a904.png)

위의 명령어를 실행하면, 파이썬의 패키지 관리자인 pip가 알아서 필요한 파일들을 설치해줄것이다.

그 다음 명령어를 실행하면, pyinstaller 가 알아서 exe파일로 변환시켜준다.

## 느낀점
예전에 교과서에서 피보나치수열 이라는 내용을 발견했을때부터, 이 내용에 대해 깊이 탐구해보고, 이것을 이용하여 프로그램을 만들어보는 프로젝트를 한번 해보고싶었다.

이 활동을 하며 이 주제에 대해 깊이 탐구해보고, 추가적인 정보에 대하여 더 탐색을 해보며 모르는 내용을 알아보면서 프로그램을 만들어보니 매우 흥미로웠고, 정보시간에 배웠던 문제분석과 프로그래밍 단원을 수1의 피보나치 수열의 n번째 항을 구하는 프로그램을 만드는 과정에 활용해보니 더 뜻깊고, 흥미로웠던 활동이였던것 같다.

순서도를 그리는 것과, 가장 좋은 알고리즘을 생각하는 과정, 만들다가 버그가 생겨서 버그를 고치는 과정이 조금 힘들었지만 계속 고민하고, 노력하여 이 프로그램을 완성했을때는 정말 뿌듯했다.

이 내용을 이용해 친구를 가르쳐 주고 있다.

**선생님 긴글 읽느라 수고하셨습니다!!**
