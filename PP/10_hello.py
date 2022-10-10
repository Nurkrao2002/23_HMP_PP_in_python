from watch import Watch
w1=Watch("Fossil","Silver")           # w1,w2 is an object
w2=Watch("Fastrack","Black")
# print(w1.wname, w1.wcolor)
# print(w2.wname, w2.wname)
# print(w1.fp, w1.az)  # calling with the help of an object
# print(w2.fp, w2.az)
# print(Watch.fp, Watch.az)  # calling with the help of a classname
# print(Watch.wname, Watch.wcolor)  # will print an error , AttributeError
w1.purchase()
# w1.color()
# w2.purchase()
# w2.color()

# w1.az="Myntra"
# Watch.az="Amazo"
# print(w1.fp, w1.az)  # Flipkart Myntra
# print(w2.fp, w2.az)  # Flipkart Amazo

# print(w1.wname, w2.wcolor)
# print(w2.wname,w1.wcolor)

