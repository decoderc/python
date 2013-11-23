class Stack():
	def __init__(self):#başlangıç değeri istemiyorum;yani "n" yok.
		self.items=[]#items listenin elemanlarıdır.Boş bir liste oluşturduk.

	def isEmpty(self):
		return self.items==[]

	def push(self,item):#burdaki item eklenecek elemandır.
		self.items.append(item)

	def pop(self,n=None):
		if self.isEmpty():
			return None
		if n==None:
			return self.items.pop()
		else:
			return self.items.pop(n)

	def peek(self,n=None):#sadece elemanı döndürür.
		if self.isEmpty():
			return None
		if n==None:
			return self.items[len(self.items)-1]#pythonda listeler 0. indisten başlar;o yüzden len-1 aldık.
		else:
			return self.items[n]

	def size(self):
		return len(self.items
                           
        def dividedBy2(decnumber):
        remstack=Stack()

               while decnumber>0:
               rem=decnumber%2
        
               remstack.push(rem)
               decnumber=decnumber/2

        binstring=""
               while not remstack.isEmpty():
               binstring=binstring + str(remstack.pop())

               return binstring
