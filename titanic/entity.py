class Entity:
    def __init__(self, context, fname, train, test, id, label):
        self._context = context     # _ 1개는 default 접근의미, __2개는 private 접근 의미(default는 같은 패키지 내에서도 접근 가능)
        self._fname = fname
        self._train = train
        self._test = test
        self._id = id
        self._label = label

    # get, set 만들기
    # context
    @property
    def context(self) -> str:           # 리턴하는 결과값이 str 타입이라는 의미
        return self._context

    @context
    def context(self, context):
        self._context = context

    # fname
    @property
    def context(self) -> str:         
        return self._fname

    @context
    def context(self, fname):
        self._fname = fname

    # train
    @property
    def context(self) -> str:         
        return self._train

    @context
    def context(self, train):
        self._train = train

    # test
    @property
    def context(self) -> str:         
        return self._test

    @context
    def context(self, test):
        self._test = test

    # id
    @property
    def context(self) -> str:         
        return self._id

    @context
    def context(self, id):
        self._id = id

    # label
    @property
    def context(self) -> str:         
        return self._label

    @context
    def context(self, label):
        self._label = label
        
        
