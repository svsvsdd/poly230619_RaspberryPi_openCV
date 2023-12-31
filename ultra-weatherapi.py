import RPi.GPIO as GPIO
import requests
import datetime
import time

GPIO.setwarnings(False)

TRIG = 23
ECHO = 24


GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)


def getLastBaseTime(calBase):
    t = calBase.hour
    if t < 2:
        calBase = calBase - datetime.timedelta(days=1)
        calBase = calBase.replace(hour=23)
    else:
        calBase = calBase.replace(hour=t - (t + 1) % 3)
    return calBase
# 기상청 API 호출 함수
def call_weather_api():
    print("def api start")
    calBase = datetime.datetime.now()
    calBase = getLastBaseTime(calBase)

    datetime00 = calBase.strftime("%Y%m%d") + calBase.strftime("%H") + '00'
    datetime01 = (calBase + datetime.timedelta(hours=1)).strftime("%Y%m%d") + (calBase + datetime.timedelta(hours=1)).strftime("%H") + '00'
    datetime02 = (calBase + datetime.timedelta(hours=2)).strftime("%Y%m%d") + (calBase + datetime.timedelta(hours=2)).strftime("%H") + '00'
    datetime03 = (calBase + datetime.timedelta(hours=3)).strftime("%Y%m%d") + (calBase + datetime.timedelta(hours=3)).strftime("%H") + '00'

    datePart0 = datetime00[:8]  # "YYYYMMDD"
    timePart0 = datetime00[8:]  # "HH00"
    datePart1 = datetime01[:8]  # "YYYYMMDD"
    timePart1 = datetime01[8:]  # "HH00"
    datePart2 = datetime02[:8]  # "YYYYMMDD"
    timePart2 = datetime02[8:]  # "HH00"
    datePart3 = datetime03[:8]  # "YYYYMMDD"
    timePart3 = datetime03[8:]  # "HH00"



    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'  # URL
    queryParams = {
        'serviceKey': 'pfwPJqSsq35REx9xZhUJmvGHVuFCPWyLXHFabpDm0vvuJWJOKBauTxCFCektk6tHTTEwHUnoGB/9gek1IyD9ww==',
        'pageNo': '1',
        'numOfRows': '1000',
        'dataType': 'JSON',
        'base_date': datePart0,
        'base_time': timePart0,
        'nx': '62',
        'ny': '123'
    }

    response = requests.get(url, params=queryParams)

    if response.status_code == 200:
        data = response.json()
        items = data['response']['body']['items']['item']

        filteredItems = [
            item for item in items
            if (
                (item['fcstDate'] == datePart0 and item['fcstTime'] == timePart0) or
                (item['fcstDate'] == datePart1 and item['fcstTime'] == timePart1) or
                (item['fcstDate'] == datePart2 and item['fcstTime'] == timePart2) or
                (item['fcstDate'] == datePart3 and item['fcstTime'] == timePart3)
            ) and item['category'] == 'POP' and float(item['fcstValue']) >= 30
        ]

        for item in filteredItems:
            print(f"{item['fcstDate']} {item['fcstTime']} 강수확률: {item['fcstValue']}%")
            
    else:
        print(f"Request failed with status code {response.status_code}")
# 초음파 거리 측정 함수
def measure_distance():
    print("def dis start")

    try:
        while True:
            
            GPIO.output(TRIG,True)
            time.sleep(0.00001)        # 10uS의 펄스 발생을 위한 딜레이
            GPIO.output(TRIG, False)
            while GPIO.input(ECHO)==0:
                start = time.time()     # Echo핀 상승 시간값 저장
            while GPIO.input(ECHO)==1:
                stop = time.time()      # Echo핀 하강 시간값 저장
            check_time = stop - start
            distance = check_time * 34300 / 2
            print("Distance : %.1f cm" % distance)
            time.sleep(0.4)
            
            # 거리 값을 반환
            
            return distance
            
    except KeyboardInterrupt:
        print("거리 측정 완료 ")
        GPIO.cleanup()
        
    # 거리 측정 로직 추가
    # 예시: GPIO 제어하여 초음파 거리 센서로부터 거리 값을 측정

try:
    while True:
        # 거리 값을 측정
        distance = measure_distance()

        # 거리 값에 따라 동작을 수행
        if distance < 10:  # 일정 거리보다 가까워지면 동작 수행
            # 기상청 API 호출
            response = call_weather_api()
            

            # 응답 데이터 처리 및 메시지 앱으로 전송하는 로직 추가

        # 일정 간격으로 반복
        # 예시: time.sleep() 등을 사용하여 적절한 간격으로 반복 실행

except KeyboardInterrupt:
    # 프로그램 종료 시 GPIO 리소스 해제
    GPIO.cleanup()