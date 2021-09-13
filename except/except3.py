'''
java
try {
  //예외 발생할 것 같은 코드
}catch(IndexOutOfRangeException){
  //예외 처리하는 코드
}catch{
  //예외 처리하는 코드

}finally{
  //무조건 실행되어야하는 코드
}

python

try:
  # 예외가 발생할 것 같은 코드
except IndexError as e:  # 특정 예외
  # 예외 처리하는 코드
except:
  # 예외 처리하는 코드
else:
  # 예외가 발생하지 않았을 때 실행하는 코드
finally:
  # 꼭 실행해야하는 코드

'''

