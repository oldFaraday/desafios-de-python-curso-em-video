sal = float(input('Digite o salário atual do funcionário: R$'))
if sal < 1250:
    print('O novo sário é de: R${:.2f}'.format(sal+(sal/10)))
else:
    print('O novo sário é de: R${:.2f}'.format(sal+(sal/100*15)))