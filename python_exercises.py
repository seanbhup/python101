string = "sean";
# print string.upper();

# print string.title();

# print string[::-1];


# word = raw_input("enter a message: ")
# leetmsg = word
# leetwords = "aeioutsu"
#
# for letter in word:
#     if letter in leetwords:
#         leetmsg = leetmsg.replace('a', "4")
#         leetmsg = leetmsg.replace('e', "3")
#         leetmsg = leetmsg.replace('i', str(1))
#         leetmsg = leetmsg.replace('o', str(0))
#         leetmsg = leetmsg.replace('t', str(7))
#         leetmsg = leetmsg.replace('s', '$')
#         leetmsg = leetmsg.replace('u', 'U')
# print "Translated Message: ", leetmsg;

# word = raw_input("(WARNING DONT DO MORE THAN ONE TIME) Enter a message: ")
# leetmsg = word
# leetwords = "aaeeiioouu"
#
# for letter in word:
#     if letter in leetwords:
#         leetmsg = leetmsg.replace('a', "aaa")
#         leetmsg = leetmsg.replace('ee', "eee")
#         leetmsg = leetmsg.replace('ii', "iii")
#         leetmsg = leetmsg.replace('oo', "ooo")
#         leetmsg = leetmsg.replace('uu', 'uuu')
# print "Translated Message: ", leetmsg;

# list = [-1,0,1,2,3,4,5];
# # print sum(list);
# # print max(list);
# # print min(list);
# def stuff(list):
#     new_list = [];
#     for number in list:
#         # if number % 2 == 0:
#         #     print number;
#         number_times_two = number * 2;
#         new_list.append(number_times_two);
#         print new_list;
#
# stuff(list);

#
# list1 = [1,2,3];
# list2 = [4,5,6];
# def mult_vec(list, list2):
#     new_num_list = []
#     for number1 in list1:
#         for number2 in list2:
#             new_num = number1 * number2
#             new_num_list.append(new_num);
#             print new_num_list;
#
# mult_vec(list1,list2);

# a = [1,2,3,4]
# b = [2,3,4,5]
# ab = [];
# for i in range(0, len(a)):
#      ab.append(a[i]*b[i])
#
# print ab;

# one = [ [2, -2],[6, 3] ]
# two = [ [1, 6], [1, 8] ]
# three = [];
# for i in range(0, len(one)):
#     for j in range(0, len(one[0])):
#         three.append(one[j][i]+two[j][i]);
#
# print three;
#
# one = [ [2, -2],
#         [6, 3] ]
# two = [ [1, 6],
#         [1, 8] ]
#
# three = [3, 7,
#         4, 11]

# def sum_odd_numbers():
#     sum = 0;
#     for i in range(1,5000):
#         if i % 2 == 1:
#             sum += i;
#     print sum;
#
# sum_odd_numbers();

# for i in range(1,11):
#     if i % 2 == 1:
#         print i


#
# def stuff(number):
#     for i in range(1,number+1):
#         print "*"
# stuff(10)

# size = 5
# for i in range(size):
#     print ('*' * size)

# def square(number):
#     for i in range(1, number + 1):
#         print line(number)
#     return ""
#
# def line(number):
#     num_range = number+1
#     for i in range(1, num_range):
#         if i in [0, num_range-1]
#         print "X",
#     return ""
#
# square(10);

# height = 10;
# width = 5;
# for i in range(height):
#     for j in range(width):
#         if (i in [0, width-1]) or (j in [0, height-1]):
#             print ("*");
#

h = int(input('Type in a number for height and width for the square: ')) - 2;
top = ((h+2) * '*');
bottom = top;
print (top)
for i in range (0, h): print ('*' + (' ' * (h)) + '*')
print (bottom)
