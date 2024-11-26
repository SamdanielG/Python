def traffic_light(action):
    switcher = {
    'red':'stop',
    'yellow':'slow down',
    'green':'go',
            }
    return switcher.get(action,"invalid action")
print(traffic_light('red'))
print(traffic_light('yellow'))
print(traffic_light('green'))
print(traffic_light('blue'))
    