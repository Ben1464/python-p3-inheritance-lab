from user import User
class Student (User):

   
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.knowledge=[]

    def learn(self,n):
        pass
        return self.knowledge.append(n)





Ben =Student('Ben','Mwangi')
Ben.learn('Physics')
print(Ben.knowledge)