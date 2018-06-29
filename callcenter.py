class Call(object):
    def __init__(self, id, name, num, time, reason):
        self.id = id
        self.name = name 
        self.num  = num 
        self.time = time 
        self.reason = reason
    
    def display(self):
        print "id: ", self.id, "name: ", self.name, "number: ", self.num, "time: ", self.time

class Center(object):
    def __init__(self, caller):
        self.calls = [caller]
        self.length = len(self.calls)
    def add(self, call_obj):
        self.calls.append(call_obj)
        return self
    def remove(self):
        self.calls.pop(0)
        return self 
    def printing(self):
        for x in self.calls:
            print x.name 
            print x.num
        return ","
    def hang_up(self, loser):
        for x in self.calls:
            if x.num == loser.num:
                self.calls.remove(loser)
        return self

    def info(self):
        print "name: ", self.printing()
    def organize(self):
        newlist = sorted(self.calls, key= lambda x: x.time, reverse = True)
        return newlist



            
      
        return self

new_call = Call("8", "Jarod", "4086913359", 4, "mad")
call2 = Call("9", "tom", "3838383", 3, "happy")
call2.display()

queue = Center(new_call)
queue.add(call2)
queue.organize()

print "testing< ", queue.organize()[0].name


