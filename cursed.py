from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC

PlaySound("portal-radio.wav", SND_FILENAME|SND_LOOP|SND_ASYNC)
while True:
    pass
