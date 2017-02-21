# print "Sean"

# name = "sean"
# print name
#
# forty_two = 40 + 2;
# print forty_two;

animals = [
        "wolf",
        "hawk",
        "hyena"
        ];
# print animals[-1]
animals.append("pangolin");
# print animals[-1];
# del animals[0];

animals.remove("hyena");
# print animals;

animals.insert(0,"emu")
# print animals

animals.pop();
# print animals

fools = "Michael, Paul, Mason, Casey, Connie, Sarah, AndEHHH"
fools_as_array = fools.split(", ");
# print fools_as_array;
# print sorted(fools_as_array)
fools_as_array.sort();
# print fools_as_array;
fools_as_array.reverse();
# print fools_as_array;

# print len(fools_as_array)

# print fools_as_array[2:3]

# for student in fools_as_array:
    # print student
    # pass
# for i in range(1,10):
    # print i

def say_hell(name):
    print "Please go to Hell, " + name;

say_hell("Drew");

name = "Sean";
age = 400;

my_array = [];
my_array.append(name);
my_array.append(age);
print my_array;

full_name = "Sean Bhupathi"
split_name = full_name.split(" ");
print split_name;

def sum_odd_numbers():
    sum = 0;
    for i in range(1,5000):
        if i % 2 == 1:
            sum += i;
    print sum;

sum_odd_numbers();
