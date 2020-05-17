
import tkinter as tk
import random

class Taj(tk.Tk):

    la=['Absent-minded','Adaptable','Aggressive','Aloof','Altruistic','Angry','Approval-seeking','Assertive']
    lb=['bodacious', 'beautiful',' big-hearted', 'brave', 'believable', 'bubbly', 'brilliant', 'benevolent', 'broad-minded', 'brainy', 'bedazzling', 'blameless', 'beneficent', 'beguiling', 'beatific']
    lc=['Calm','Charismatic','Charming','Cheerful','Clever','Compassionate','Compliant','Confident','Conforming','Conscientious','Considerate','Contemplative','Courageous','Creative','Cruel','Curious']
    ld=['DABBLE', 'DAIMON', 'DAINTIFY', 'DAINTY' , 'DANCE', 'DANCER', 'DANDY', 'DANKE', 'DANKEN', 'DAPPER' , 'DAPPERLY', 'DARING', 'DARINGLY', 'DARLING' , 'DASHING', 'DASHINGLY' , 'DAUNTLESS' , 'DAUWTRAPPEN', 'DAWN', 'DAYEE', 'DAZZLE', 'DAZZLED', 'DAZZLING', 'DAZZLINGLY' , 'DEBONAIRLY' , 'DECENCY' , 'DECENT']
    le=['eager','earnest','easy-going','efficient','egotistical','elfin','emotional','energeticent','erprising','enthusiastic','evasive','even-tempered','exacting','excellent','excitable','experienced']
    lf=['fabulous','fastidious','ferocious','fervent','fiery','flabby','flaky','frank','friendly','funny']
    lg=['generous','gentle','gloomy','gluttonous','good','grave','great','groggy','grouchy','guarded']
    lh=['hateful','hearty','helpful','hesitant','hot-headed','hypercritical','hysterical','hyper active','honesty']
    li=['inconsiderate','inconsistent','indefatigable','independent','indiscreet','indolent','industrious','inexperienced','insensitive','inspiring','intelligent','interesting','intolerant','inventive','irascible','irritable','irritating']
    lj=['jocular','jovial','joyous','judgmental','Jubilant','Jubilation']
    lk=['Keen','Keep up','Kind'',Kind-hearted','Kindly','Kudos']
    ll=['lame','lazy','lean','leery','lethargic','level-headed','listless','lithe','lively','local','logical','long-winded','lovable','love-lorn','lovely']
    lm=['maternal','mature','mean','meddlesome','mercurial','methodical','meticulous','mild','miserable','modest','moronic','morose','motivated']
    ln=['naive','nasty','natural','naughty','negative','nervous','noisy','normal','nosynum']
    lo=['obliging','obnoxious','old-fashioned','one-sided','orderly','ostentatious','outgoing','outspoken']
    lp=['pleasant','plucky','polite','popular','positive','powerful','practical','prejudiced','pretty','proficient','proud','provocative','prudent','punctual','passionate']
    lq=['quarrelsome','querulous','quick','quick-tempered','quiet']
    lr=['realistic','reassuring','reclusive','reliable','reluctant','resentful','reserved','resigned','resourceful','respected','respectful','responsible','restless','revered','ridiculous']
    ls=['sophisticated','soulful','soulless','sour','spirited','spiteful','stable','staid','steady','stern','stoic','striking','strong','stupid','sturdy','subtle','sulky','sullen','supercilious','superficial','surly','suspicious','sweet']
    lt=['tactful','tactless','talented','testy','thinking','thoughtful','timid','tired','tolerant','touchy','tranquil']
    lu=['Unique','Understand','Utilize','Uplift','Uplifting','Unyielding','Usually','Unfold','Uppermost','Ultra','Unselfish','User friendly']
    lv=['venal','versatile','vigilant','volcanic','vibrant','vulnerable','Vivacious','Virtuous']
    lw=['warm','warm','hearted','wary','watchful','weak','well-behaved','well-developed','well-intentioned','well-respected','well-rounded','willing','wonderful']
    lx=['Xenodochial','xebec','xenia','xenic','xenon','xeric','xerus']
    ly=['Yea','Yeah','Yearn','Yes','Yippee','Young','Youth','Youthful']
    lz=['Zeal','Zealous','Zest']
    co=["red","blue","green",'yellow','pink','gray','orange']


    def __init__(self):
        tk.Tk.__init__(self)
        self.l=tk.Label(self,text="Abbreviation of Your Name",fg="blue",font=('helvetica', 20)).pack(side="top",padx=20,pady=10)
        self.l=tk.Label(self,text="Enter your name",fg="red",font=('helvetica')).pack()
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Enter", command=self.on_button) 
        self.entry.pack()
        self.button.pack()

    def on_button(self):
        a=self.entry.get()
        for i in a:
            dis={'a':random.choice(self.la),'b':random.choice(self.lb),'c':random.choice(self.lc),'d':random.choice(self.ld),'e':random.choice(self.le),'f':random.choice(self.lf),'g':random.choice(self.lg),'h':random.choice(self.lh),'i':random.choice(self.li),'j':random.choice(self.lj),'k':random.choice(self.lk),'l':random.choice(self.ll),'m':random.choice(self.lm),'n':random.choice(self.ln),'o':random.choice(self.lo),'p':random.choice(self.lp),'q':random.choice(self.lq),'r':random.choice(self.lr),'s':random.choice(self.ls),'t':random.choice(self.lt),'u':random.choice(self.lu),'v':random.choice(self.lv),'w':random.choice(self.lw),'x':random.choice(self.lx),'y':random.choice(self.ly),'z':random.choice(self.lz)}
            col=random.choice(self.co)
            up=i.upper()
            low=i.lower()
            tk.Label(self,text=up+"-"+dis[low].upper(),fg=col,bg="white",font=('helvetica', 15,"bold")).pack()

app =Taj()
app.geometry('1080x1080')
app.mainloop()