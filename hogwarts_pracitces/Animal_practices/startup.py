#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/24 20:15
# @Author  : yuwenli


from Animcal import Animal
from Cat import Cat

if __name__ == "__main__":
    # 父类
    Animal = Animal()
    Animal.bark()
    Animal.run()
    # 子类
    shotHairCat = Cat()
    print(shotHairCat.hair)
    shotHairCat.bark()
    shotHairCat.run()
    shotHairCat.catchMice()
