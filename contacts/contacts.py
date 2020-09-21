class Contact:
    def __init__(self, name, phone, email, addr):
        self.name = name    # self.name과 name은 서로 다른 존재인데, 할당함으로써 연결된다.
        self.phone = phone
        self.email = email
        self.addr = addr

    def print_info(self):
        print(f'이름 : {self.name}, 전화번호 : {self.phone}, 이메일 : {self.email}, 주소 : {self.addr}')
        # self.name과 name은 서로 다른 존재이므로 {self.name}과 {name}은 서로 다른 상태이다.

    @staticmethod
    def set_contact():
        name = input('이름')        
        phone = input('전화번호')
        email = input('이메일')
        addr = input('주소')
        contact = Contact(name, phone, email, addr)
        return contact

    @staticmethod
    def get_contact(clist):
        for i in clist:
            i.print_info()

    @staticmethod
    def del_contact(clist, name):
        for i, t in enumerate(clist):
            if t.name == name:
                del clist[i]
    
    @staticmethod
    def print_menu():
        print('1 연락처 입력')
        print('2 연락처 출력')
        print('3 연락처 삭제')
        print('4 종료')
        menu = input('메뉴 선택 : ')
        return menu

    @staticmethod
    def run():
        clist = []
        while 1:
            menu = Contact.print_menu()
            if menu == '1':
                t = Contact.set_contact()
                clist.append(t)

            elif menu == '2':
                Contact.get_contact(clist)
                
            elif menu == '3':
                name = input('삭제할 이름을 입력하세요 : ')
                Contact.del_contact(clist, name)

            elif menu == '4':
                break

if __name__ == '__main__':
    Contact.run()

            

    