# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:31:15 2021

@author: Asus
"""

import APRRI as app
app.greet()
app.mode_choose()
app.start()
while True:
   input("Hit enter to resume the session")
   app.start()