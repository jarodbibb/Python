class Underscore(object):
    def map(self, arg, f):
        results = []
        for index, item in enumerate(arg):
            if(isinstance(item, int)):
                results.append(f(arg[index]))
         
        return sorted(results)

    def find(self, arg, f):
        results = []
        for val in arg:
            if f(val):
               
                results.append(val)

        return results

    def reduce(self, arg, f):
        sum = 0 
        for val in arg: 
            sum = f(sum, val)
        return sum

    def filter(self, arg, f):
        results = []
        for val in arg:
            if f(val):
                results.append(val)

        return results

    def reject(self, arg, f):
        results = []
        for val in arg:
            if not f(val):
                results.append(val)
        return results



    # def filter(self, list, arg2 ):
    #     new_list = []
    #     for x in list:
    #         if x == arg2:
    #             new_list.append(x)

    #     return new_list


    # def reject(self):

_ = Underscore()

map1 = _.map([1, 2, 3], lambda num: num * 3)
print map1
# => [3, 6, 9]

map2 = _.map([1, 2, 3], lambda num: num + 3)
print map2
# => [3, 6, 9]

find1 = _.find([1, 2, 3, 4, 5, 6], lambda num: num % 2 == 0 )
print find1

find2 = _.find(["hello", "world", "hows", "are", "you"], lambda val: val == "how" )
print find2

sumReduce= _.reduce([1,2,4,5], lambda sum, num: sum + num)
print sumReduce

tryfilter = _.filter([1,2,3,4], lambda num: num % 2 == 0)
print tryfilter

simplereject = _.reject([1,2,3,4], lambda num: num % 2 == 0)
print simplereject

