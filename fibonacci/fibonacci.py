
import matplotlib.pylab as plt  # matplotlib 에서의 pylab 모듈을 plt 라는 이름으로 불러온다.


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


def sigma(res_list: list, k: int = 1) -> int:
    res = 0  # 결괏값을 0으로 초기화한다.
    for i in range(k-1, len(res_list)):  # i에 k부터 리스트의 길이만큼 대입하며 반복한다.
        res += res_list[i]  # 결괏값에 리스트의 i번째 값을 더한다.
    return res  # 반복문이 끝나면 결괏값을 돌려준다.


def graph(res_list: list):
    x = list(range(1, len(res_list)+1))  # x값을 지정한다.
    y = res_list  # y에 res_list 를 대입한다.
    # 그래프를 그려주는 모듈인 matplotlib 의 pylab 안에있는 plot 함수를 사용하여 x, y를 대입하여 그래프를 그린다.
    plt.plot(x, y)
    plt.show()  # 그래프를 출력한다.


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


main()
