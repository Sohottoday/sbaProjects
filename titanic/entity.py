from dataclasses import dataclass

# @dataclass 는 __init__, __repr__, __eq__
@dataclass          # https://sjquant.tistory.com/30
class Entity:

    context : str
    fname : str
    train : object
    test : object
    id : str
    label : str

    # def __init__(self, context, fname, train, test, id, label):
    #     self._context = context     # _ 1개는 default 접근의미, __2개는 private 접근 의미(default는 같은 패키지 내에서도 접근 가능)
    #     self._fname = fname
    #     self._train = train
    #     self._test = test
    #     self._id = id
    #     self._label = label


    # get, set 만들기
    # context
    @property
    def context(self) -> str:           # 리턴하는 결과값이 str 타입이라는 의미
        return self._context

    @context.setter
    def context(self, context):
        self._context = context

    # fname
    @property
    def fname(self) -> str:         
        return self._fname

    @fname.setter
    def fname(self, fname):
        self._fname = fname

    # train
    @property
    def train(self) -> str:         
        return self._train

    @train.setter
    def train(self, train):
        self._train = train

    # test
    @property
    def test(self) -> str:         
        return self._test

    @test.setter
    def test(self, test):
        self._test = test

    # id
    @property
    def id(self) -> str:         
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # label
    @property
    def label(self) -> str:         
        return self._label

    @label.setter
    def label(self, label):
        self._label = label
        
        
