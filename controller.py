from nicolascalclib import soma, subs, mult, divs, powX, raiz

class Request():
    num1: float
    num2: float
    op: str

    def __init__(self, num1: float, op: str, num2: float):
        self.num1 = num1
        self.op = op
        self.num2 = num2
    
    def control(self):
        match(self.op):
            case("soma"):  
                return Response(soma(self.num1, self.num2))
            case("subs"):
                return Response(subs(self.num1, self.num2))
            case("mult"):
                return Response(mult(self.num1, self.num2))
            case("divs"):
                ans: float
                msg: str = "Divisão por Zero"

                try:
                    ans = divs(self.num1, self.num2)
                except ValueError as ve:
                    return Response(msg)
                
                return Response(ans)
            case("powX"):
                return Response(powX(self.num1, self.num2))
            case("raiz"):
                ans: float
                msg: str = "Expoente Zero"

                try:
                    ans = raiz(self.num1, self.num2)
                except ValueError as ve:
                    return Response(msg)
                
                return Response(ans)
        
        return Response("Operação não implementada")

class Response():
    num: float
    err: str

    def __init__(self, num: float):
        self.num = num
        self.err = ""
    
    def __init__(self, err: str):
        self.num = 0
        self.err = err