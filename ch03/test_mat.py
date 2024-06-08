import matplotlib.pyplot as plt

pnt_x = 5
pnt_y = 3

fig, axes = plt.subplots(1,1,
                        figsize=(5,5))
plt.plot(pnt_x,
         pnt_y, 
         marker = 'o')
plt.show()