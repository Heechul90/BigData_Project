setwd('D:/Heechul/BigData_Project')
getwd()



### 데이터 셋을 이용하여 전력량을 예측하는 다중회귀 모델만들기

## 컬럼명



data <- read.csv('Data/dataset2(watt).csv',
                 header = T)
head(data)
str(data)
data <- data[, c(2 : 10)]
View(data)




## 산점도 그려보기
pairs(data)


## 1. 모든 변수로 fit1 모델 만들기
(fit1 <- lm(watt~., data = data))

summary(fit1)


## 2. Stepwise regression(backward)
step(fit1, direction = "backward")

## low_tem, dew_point, solar_quantity, ground_tem의 변수들이
## 영향력이 없는 변수로 판단되어 제거되었다.


## 3. Stepwise regression(forward)
fit2 <- lm(watt ~ 1, data = data)
step(fit2, direction = "forward", scope = ~avg_tem + low_tem + hig_tem + dew_point + spot_pressure + sea_pressure + solar_quantity + ground_tem)

## hig_tem을 제외하고 모든변수가 제외되었다.


## 4. Stepwise regression(both)
step(fit1, direction = "both")

## low_tem, dew_point, solar_quantity, ground_tem의 변수들이
## 영향력이 없는 변수로 판단되어 제거되었다.

## 세가지 방법중 backward와 both가 결과가 같아 
## low_tem, dew_point, solar_quantity, ground_tem 변수를 제거하고 fit2모델 설정


(fit2 <- lm(watt ~ avg_tem + hig_tem + spot_pressure + sea_pressure, data = data))
summary(fit2)



#  5. All possible regression
library(leaps)
subsets1 <- regsubsets(watt~., data = data, method = 'seqrep', nbest = 8) 
plot(subsets1)

## hig_tem변수만 있는 모델을 추천함


subsets2 <- regsubsets(watt~., data = data, method = 'exhaustive', nbest = 8)
plot(subsets2)

## sea_pressure만 있는 모델을 추천함















