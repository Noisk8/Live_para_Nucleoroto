d2 >> loop ("sizas_gonorrea", 1, dur=60, bpm=80, amp=1).solo()

er >> play ("|x4| ", amp=1.3)


b1 >> dbass(dur=PDur(3,8), sus=2, chop=0, shape=PWhite(0,1/2),amp=0, pan=PWhite(-1,1)).sometimes("offadd", 4) + var([0,2],4)

c1 >> play("@", dur=1/4, sample=P[:8].rotate([0,1,3]), rate=4, pan=-0.5, amp=0)

p2 >> pads([0,2,4,6], dur=4, spin=4, oct=4.3,amp=4, chop=[8,16], hpf=linvar([500,2000],16), hpr=0.2).every(8, "shuffle")



bm >> play ("[--]", amp=0, sample=6)


de >> play("<Vs><[--]><.{.+[ +]}O( [( u)O])>", lpf=var([0,1000],[28,4]))

br >> play (" |o2|", dur=2/2, amp=1)

ft >> play (" |=2|", amp=3, chop=0)



Scale.default="minor"; Clock.bpm=120; Root.default=var([0,3],32)

b1 >> dirt([0,0,0.5], dur=PDur(3,8), sus=1, amp=0, chop=2, drive=0.5, formant=1, oct=(6), room=0.2).spread()

var.switch = var([1,1],[32])
p3 >> glass(oct=6, rate=linvar([-2,2],16), shape=0.5, amp=3, amplify=var([0,var.switch],64), room=0.5)

p1 >> pasha(var([0,2,0.5],[3,1/2,1/2]), dur=PDur(3,8), amp=0, oct=6, sus=1, pan=PWhite(-1,1)).every(4, "dur.shuffle")



er >> play ("|x4| ", amp=1.2)

h1 >> play("G(:-)", rate=-1/2, pshift=var([0,3],[6,2])+(0.1,0), pan=(-1,1), room=1, amp=1.6)

d2 >> play("x-", sample=2).sometimes("stutter", 4, dur=3)

d3 >> play("  I ", sample=2, hpf=(0,2000), lpf=(300,0), hpr=0.5)

b1 >> dbass(var([0,6,5,2],[6,2]), dur=PDur(3,8,[0,2]), sus=2, chop=.5, rate=4, amp=1.3)

p2 >> blip([0,1,[[3,4],2]], dur=[4,3,1], amp=1.2, drive=PWhite(0.2,0.7), oct=4, lpf=2000, room=1/2, echo=0.75, echotime=6, sus=1).penta().spread()

k1 >> klank(oct=6, lpf=200, lpr=0.5)




var.chords = 2
Scale.default = 'yu'

q1 >> ambi(var.chords , amp=2, sus=4, oct=5, hpf=1222)

ut >> dirt(dur=PDur(8,8), amp=0, root=0)

d1 >> play("ksfs", crush=linvar([2, 8], 16),  bits=0.3, echo=0, room=0, echotime=[2,4], amp=1.3, lpf=0)


kr >> prophet(P[0,5,3,6,4,2,7,8,2,5,6] + [6,3,7,8,2,4,6,3,5,], amp=2, dur=1/4, oct=6, glide=0.08, pan= 1)

k2 >> prophet(P[0,5,3,6,4,2,7,8,2,5,6] + [6,3,7,8,2,4,6,3,5,], amp=0, dur=1/4, oct=5, pan=-1, formant=0)

er >> play ("|x4| ", amp=0)

po >> play ("[--]", amp=0)

jk >> play (" |o2|", amp=0, dur=2/2)

u3 >> play(' |~3|', amp=0)
