
class hh:


    def sol(self,a):

        qq = self.sol
        self.b = []


        def sub_sol(a):
            if a == 0 :
                return
            self.b = [1,2]


            sub_sol(a-1)


        sub_sol(a)
        print self.b


if __name__=="__main__":
    h = hh()
    h.sol(15)