import matplotlib.pyplot as plt

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1) # make a blank plotting area
# fig, ax = plt.subplots()  # ax를 포함하고 있는 fig를 반환. 위의 두 line을 한번에 처리.
fig = plt.figure()
ax1 = fig.add_subplot(3, 3, 1)
ax5 = fig.add_subplot(3, 3, 5)
ax9 = fig.add_subplot(3, 3, 9)


plt.show()