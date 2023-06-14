import matplotlib.pyplot as plt


plt.plot([128, 256, 512], [5.342374350002501, 21.431653893989278, 84.29271631600568], label='AES')
plt.plot([128, 256, 512], [11.86348790199554, 47.49458078801399, 187.07173354100087], label='3DES')
plt.plot([128, 256, 512], [0.4437664169963682, 1.6795199100015452, 6.708804947003955], label='Blowfish')

plt.xlabel('Tamanho da imagem (pixels)')
plt.ylabel('Tempo (segundos)')

plt.legend(loc="upper left")

plt.title('Tempo de execução')

plt.savefig(f'plots/execution-time-comparison.png')
plt.close()