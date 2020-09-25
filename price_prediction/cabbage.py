import sys
sys.path.insert(0, '/Users/user/SbaProjects')

#import sys
#import os
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.file_handler import FileReader

import pandas as pd
import numpy as np
import tensorflow as tf
from dataclasses import dataclass

@dataclass
class Cabbage:

    # year,avgTemp,minTemp,maxTemp,rainFall,avgPrice
    year : int = 0
    avgTemp : float = 0.0
    minTemp : float = 0.0
    maxTemp : float = 0.0
    rainFall : float = 0.0
    avgPrice : int = 0

    def __init__(self):
        self.fileReader = FileReader()
        self.context = '/Users/user/SbaProjects/price_prediction/data/'


    def new_model(self, payload) -> object:
        this = self.fileReader
        this.context = self.context
        this.fname = payload
        return pd.read_csv(this.context + this.fname, sep=',')


    def create_tf(self, payload):
        xy = np.array(payload, dtype=np.float32)
        x_data = xy[:, 1:-1]        # feature
        y_data = xy[:, [-1]]        # price
        X = tf.compat.v1.placeholder(tf.float32, shape=[None, 4])
        Y = tf.compat.v1.placeholder(tf.float32, shape=[None, 1])
        W = tf.Variable(tf.random.normal([4, 1]), name='weight')
        b = tf.Variable(tf.random.normal([1]), name='bias')
        hyposthesis = tf.matmul(X, W) + b
        cost = tf.reduce_mean(tf.square(hyposthesis - Y))
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=0.000005)
        train = optimizer.minimize(cost)
        sess = tf.compat.v1.Session()
        sess.run(tf.compat.v1.global_variables_initializer())
        for step in range(100000):
            cost_, hypo_, _ = sess.run([cost, hyposthesis, train], feed_dict={X:x_data, Y:y_data})
            if step % 500 == 0:
                print(f'# {step} 손실비용 : {cost_}')
                print(f'- 배추가격 : {hypo_[0]}')

        saver = tf.train.Saver()
        saver.save(sess, self.context+'saved_model.ckpt')
        print('저장 완료')


    def service(self):
        X = tf.compat.v1.placeholder(tf.float32, shape=[None, 4])
        # year,avgTemp,minTemp,maxTemp,rainFall,avgPrice 에서 avgTemp, minTemp, maxTemp, rainFall을 입력받겠다는 의미
        # year는 모델에서 필요없는 값 -> 상관관계 X
        # avgPrice 는 얻고자 하는 답. 종속 변수
        # avgTemp, minTemp, maxTemp, rainFall는 종속변수를 결정하는 독립변수
        # 그리고 avgPrice를 결정하는 요소로 사용되는 파라미터
        # 통계와 확률의 범위로 용어 정의가 중요하다.
        # y = ax + b, 선형관계 linear
        # X는 대문자르 사용하고 확률변수라고 한다.
        # 비교, 웹프로그래밍(Java, C) 소문자 x 이렇게 하는데 이것은 한 타임에 하나의 value고 값은 외부에서 주어지는 하나의 값이므로 그냥 변수
        # 지금의 X는 값이 제한적이지만 집합상태로 많은 값이 있는 상태. 이럴 때 확률--변수
        W = tf.Variable(tf.random.normal([4, 1]), name='weight')
        b = tf.Variable(tf.random.normal([1]), name='bias')
        # 텐서에서 변수는 웹에서의 변수와 다르다
        # 이 변수를 결정하는 것은 외부값이 아니라 텐서가 내부에서 사용하는 변수
        # 기존 웹에서 사용하는 변수는 placeholder
        # variable이 텐서가 내부에서 변경하면서 작업하는 것
        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(tf.compat.v1.global_variables_initializer())
            saver.restore(sess, self.context + 'saved_model.ckpt')
            data = [[self.avgTemp, self.minTemp, self.maxTemp, self.rainFall], ]
            arr = np.array(data, dtype=np.float32)
            dict = sess.run(tf.matmul(X, W)+b, {X:arr[0:4]})
            # 위 코드는 Y = WX + b를 코드로 표현한 것, matmul은 상호 곱(matricx 형태이므로)
            print(dict[0])
        return int(dict[0])




if __name__ == "__main__":
    cabbage = Cabbage()
    # dframe = m.new_model('price_data.csv')
    # print(dframe.head())
    # m.create_tf(dframe)
    # m.avgPrice = 1
    print(cabbage.test())





    