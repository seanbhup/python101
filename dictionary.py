# dictionary is JS object
# put key-value pairs(properties) in quotes

bunch = {
    "name": "Rob",
    "age": 129
};

zombie = {
    "speed": 10,
    "power": 6,
    "hunger": 12,
    "name": "Zombie"
};
# brackets instead of thing.prop for key value pairs
# print zombie["speed"];

zombie["weapon"] = "fist";
zombie["startX"] = 200;
zombie["startY"] = 150;

# print zombie;

if zombie["speed"] < 5:
    zombie["position"] = zombie["startX"] + 2;
elif zombie["speed"] < 10:
    zombie["position"] = zombie["startX"] + 4;
else:
    zombie["position"] = zombie["startX"] + 6;

zombie["pointless"] = "/n";
# print zombie;
del zombie["pointless"];
# print zombie;


skill = "redux"
stuff = {
    "html": 10,
    "css": 10,
    "javascript": 10,
    "python": 10,
    "jquery": 10,
    "bootstrap": 10,
    "nodejs": 10,
    "mysql": 10,
    "react": 10,
    skill : 10
};

# print stuff

# for loops in dictionaries start with key(placeholder), value
# for key,value in stuff.items():
    # print value;
    # print key;

# if zombie.has_key("mother_name"):
#     print zombie["mother_name"];
#
# for key in zombie:
#     print zombie[key];

zombies = [];
zombies.append({
    "speed": 10,
    "power": 6,
    "hunger": 12,
    "name": "Eel man"
});

zombies.append({
    "speed": 5,
    "power": 16,
    "hunger": 211,
    "name": "Agnes"
});

# print zombies[0]["name"];

# for zombie in zombies:
    # print zombie["name"];

zombies[0]["victims"] = ["fred weasley", "hermione granger"];

# print zombies[0];

# print zombies[0]["victims"][0];

zombie[0]["night_power_up"] = {
    "power": 23,
    "hunger": 20,
    "weapon": "human arm"
};
