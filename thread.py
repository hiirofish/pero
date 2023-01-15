from ogawa import og_main
from higashi import hi_main
from okada import ok_main
from yoshikawa import yo_main

from multiprocessing import Manager, Process
from time import sleep

def get_value(d):
  print("start get_gazevalue")
  while True:
    print("og_arg:",d["og_arg"])
    print("ok_arg:",d["ok_arg"])
    print("hi_arg:",d["hi_arg"])
    print("yo_arg:",d["yo_arg"])

    sleep(3)


if __name__ == "__main__":
    with Manager() as manager:
        d=manager.dict()
        d["og_arg"]=1
        d["ok_arg"]=2
        d["hi_arg"]=3
        d["yo_arg"]=4

        p1=Process(target=og_main,args=(d,))
        p2=Process(target=hi_main,args=(d,))
        p3=Process(target=ok_main,args=(d,))
        p4=Process(target=yo_main,args=(d,))
#        p5=Process(target=get_value,args=(d,))

        p1.start()
        p2.start()
        p3.start()
        p4.start()
#        p5.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()
#        p5.join()
