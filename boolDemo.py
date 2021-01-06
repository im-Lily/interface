# python bool 타입 특징
# bool
# True(T), False(F)
# not, and, or -> 논리연산자
# &, |, ~ -> 비교연산자

# False로 간주
# "" , [], (), {}, 숫자(0 이외의 숫자는 True), None

# 2진수로 표현 -> 0101 & 0000 -> 0000 -> 0
xValue = 5
yValue = 0
print(xValue & yValue)
print(bool(xValue & yValue))
# 2진수로 표현 -> 0101 & 0000 -> 0101 -> 5
print(xValue | yValue)
print(bool(xValue | yValue))

trueValue = True
falseValue = False

print(int(trueValue))
print(int(falseValue))

print(trueValue & falseValue)
print(trueValue | falseValue)

print('and - ', trueValue and falseValue)
print('or - ', trueValue or falseValue)
print('not - ', not trueValue)

