class Personage:
    def __init__(self,age,first_name,last_name):
        self.__age=age
        self.first_name=first_name
        self.last_name=last_name
    @classmethod
    def full_name(cls,age,name):
        first_name,last_name=name.split()
        return cls(age,first_name,last_name )

    @property
    def age(self):
        return f"j'ai {self.__age } ans"
    @age.setter
    def age(self,age):
        assert isinstance(age,int)
        self.__age=age

p1=Personage(25,"Yao","Bosco")
print(p1.age)
p1.age= 26
print(p1.age)
p1.full_name("Yao BOSCO",25)
print(p1.full_name() )
