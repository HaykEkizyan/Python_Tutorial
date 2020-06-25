def catWalk(code):
    return " ".join(code.split())

print(catWalk("def      m   e  gaDifficu     ltFun        ction(x):"))                  # def m e gaDifficu ltFun ction(x):
print(catWalk("      for      i      in         ra   nge(x,   29):"))                   # for i in ra nge(x, 29):
print(catWalk("r e t u r n True"))                                                      # r e t u r n True
print(catWalk("  re    turn  x    +  y  *     z"))                                      # re turn x + y * z
print(catWalk("v er si on = s ett ings.VE RSION"))                                      # v er si on = s ett ings.VE RSION
print(catWalk("   o      bje        ct_      id = db.       Col      umn(db      .Intege       r, null        able        =Fal       se)   "))          # o bje ct_ id = db. Col umn(db .Intege r, null able =Fal se)

