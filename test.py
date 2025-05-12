# print("Hello","World")
# print("Hello","from","python",sep=">>")

# print("Hello", end=" ")
# print("From th")

# a=2
# b=4
# print(f"a is {a} and b is {b}")
# print("a is ", a)

# if True:
#     print("j")

# a = input("Enter the number")
# print(a)

# nums = [1,2,3,4]
# nums2 = [4,5,2,5]
# nums.extend(nums2)
# nums.remove(2)
# print(f"nums : {nums}")
# print(f"nums : {nums2}")

# nums.insert(1,0)
# nums.remove(2)
# nums.index(1)
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# idx = nums.index(2)
# print(idx)

# srtd = sorted(nums)
# print(srtd)


# set_num = {1,1,2,2}
# print(set_num)

# dict = {"name1":"abc", "age":34}
# print(dict)
# print(dict["age"])
# print(list(dict.keys()))
# print(list(dict.values()))
# print(list(dict.items()))

# def printNum():
#     print("1j;")
# printNum()

# str = "jsadj fkla"
# print(str.split(' '))
# str = str.split(" ")
# print(str)
# print(" ".join(str))
# print(str)

# nums = [1,2,4,5]

# for x in nums:
#     print(x,end=" ")

# f = open("text.txt",'w')
# f.write("sdgsda")
# f.close()

# class car:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
#     def showDet(self):
#         print(f"the car {self.name} of model {self.model}")
# car1 = car('ad','mod1')
# car1.showDet()


class car:
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model

    def showCarDet(self):
        print(f"The car {self.name} of model {self.model} with the color {self.color}")

bmw = car('BMW','Black','Series_1')
# bmw = car()
# bmw.name = 'BMW'
# bmw.color = 'Black'
# bmw.model = "Series_1"
bmw.showCarDet()

# f = open('')

print("new line")