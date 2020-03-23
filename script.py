import webiopi
import time

# デバッグ出力を有効に
webiopi.setDebug()

# GPIOライブラリの取得
GPIO = webiopi.GPIO

inr1=12
inr2=18
inr3=19
inr4=13
inl1=27
inl2=22
inl3=24
inl4=23


# WebIOPiの起動時に呼ばれる関数
def setup():
    webiopi.debug("Script with macros - Setup")
    # GPIOのセットアップ
    GPIO.setFunction(inr1, GPIO.PWM)
    GPIO.setFunction(inr2, GPIO.PWM)
    GPIO.setFunction(inr3, GPIO.OUT)
    GPIO.setFunction(inr4, GPIO.OUT)
    GPIO.setFunction(inl1, GPIO.PWM)
    GPIO.setFunction(inl2, GPIO.PWM)
    GPIO.setFunction(inl3, GPIO.OUT)
    GPIO.setFunction(inl4, GPIO.OUT)
    # 初期のデューティー比を0%に（静止状態）
    GPIO.pwmWrite(in1, 0)
    GPIO.pwmWrite(in2, 0)
    GPIO.digitalWrite(in3, GPIO.LOW)
    GPIO.digitalWrite(in4, GPIO.LOW)
    GPIO.pwmWrite(in1, 0)
    GPIO.pwmWrite(in2, 0)
    GPIO.digitalWrite(in3, GPIO.LOW)
    GPIO.digitalWrite(in4, GPIO.LOW)

# WebIOPiにより繰り返される関数
def loop():
    webiopi.sleep(5)

# WebIOPi終了時に呼ばれる関数
def destroy():
    webiopi.debug("Script with macros - Destroy")
    # GPIO関数のリセット（入力にセットすることで行う）
    GPIO.setFunction(inr1, GPIO.IN)
    GPIO.setFunction(inr2, GPIO.IN)
    GPIO.setFunction(inr3, GPIO.IN)
    GPIO.setFunction(inr4, GPIO.IN)
    GPIO.setFunction(inl1, GPIO.IN)
    GPIO.setFunction(inl2, GPIO.IN)
    GPIO.setFunction(inl3, GPIO.IN)
    GPIO.setFunction(inl4, GPIO.IN)

# 4つのPWMにデューティー比をまとめてセットするためのマクロ
# commandIDは、iOSのSafariでPOSTがキャッシュされることへの対策
@webiopi.macro
def pwm4Write(duty1, duty2, duty3, duty4, commandID):
    GPIO.pwmWrite(inr1, float(duty1))
    GPIO.pwmWrite(inr2, float(duty2))
    GPIO.pwmWrite(inl1, float(duty3))
    GPIO.pwmWrite(inl2, float(duty4))

