import matplotlib.pyplot as plt

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1) # make a blank plotting area
# fig, ax = plt.subplots()  # ax를 포함하고 있는 fig를 반환. 위의 두 line을 한번에 처리.
fig,ax = plt.subplot_mosaic([["left0","right0"],["left1","rigth0"]])

plt.show()