def solution(arr):
   left = 0
   right = len(arr)-1

   # TOOD: @@@ 빈칸 채우기
   while left < right:  # len(arr)/2
       # arr[left]과 arr[right]의 값을 서로 바꿈
       arr[left], arr[right] = arr[right], arr[left]

       # temp = arr[left]
       # arr[left] = arr[right]
       # arr[right] = temp

       left += 1
       right -= 1

   return arr

#The following is code to output testcase.
arr = [1, 4, 2, 3]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret, " .")
