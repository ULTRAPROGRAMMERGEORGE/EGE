print('x','y',"z","w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if x or y or z or w: # тут ты пишешь свою таблицу истиности с символами типа x -> y или другая хуйня
                    print(x,y,z,w)