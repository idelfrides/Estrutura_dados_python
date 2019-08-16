# ----------------------------------------
#           importing modules
# ----------------------------------------
import EstruturasDados as ds

# ----------------------------------
# THIS METHOD CONTAIN METHODS USED
# LIKE COMPLEMEN
# ----------------------------------


class HelperModule(object):

    def __init__(self):
        pass


    def app_info(self):
        print('''
        *********************************************
            THIS APPLICATION IMPLEMENTS A CRUD 
            OPERATIONS ON DATA STRUCTURES,
            LIKE: 
            ---- IMUTABLE ----------
                - TUPLE
                - STRING
            ---- MUTABLE -----------
                - LIST
                - DICTIONARY
                - FILE
                - SET     
                
        *********************************************  
        
        ''')

    def menu(self):
        print(' MENU \n\n 1 - Listas \n 2 - Dicionário \n 3 - Arquivos \n 4 - Conjuntos  \n 0 - Sair\n')
        yes_option = False
        option = None
        while yes_option is False:
            try:
                option = int(input('\n\n Enter an option:  '))
                if option in range(5):
                    yes_option = True
                else:
                    print('\n opcao: ', option)
                    print('\n WARNING: OPCAO INVALIDA!!!\n\n')
            except Exception as error:
                print('\n You entered a CARACTER or a STRING')
                print('\n WARNING: INVALID OPTION!!!')
                print('\n PYTHON SAID: {}'.format(error))
        return option

    def menu_atividade(self):
        print('\n MENU DE ATIVIDADES CRUD: \n'
              '\n 1 - CREATE '
              '\n 2 - READ '
              '\n 3 - UPDATE '
              '\n 4 - DELETE  '
              '\n 0 - Voltar pra MENU DE ESTRUTURA\n\n')
        yes_act = False
        option = None
        while yes_act is False:
            try:
                option = int(input('\n\n Enter an action to perform:  '))
                if option in range(5):
                    yes_act = True
                else:
                    print('\n You entered --> {} '.format(option))
                    print('AVISO: OPCAO INVALIDA!!!\n\n')
            except Exception as error:
                print('\n You entered a CARACTER or a STRING')
                print('\n WARNING: INVALID OPTION!!!')
                print('\n PYTHON SAID: {}'.format(error))
        return option


    def my_set(self, instance, value):
        dso = ds.EstruturasDados()
        if value == 1:
            dso.lista = instance
        elif value == 2:
            dso.dicio = instance
        elif value == 3:
            dso.arq = instance
        elif value == 4:
            dso.conj = instance
        else:
            pass


    def my_get(self, owner):
        dso = ds.EstruturasDados()
        if owner == 1:
            if dso.lista:
                return 1
            else:
                return 0
        elif owner == 2:
            if dso.dicio:
                return 1
            else:
                return 0
        elif owner == 3:
            print(dso.arq)
            if dso.arq > 0:
                return 1
            else:
                return 0
        elif owner == 4:
            if dso.conj:
                return 1
            else:
                return 0
        else:
            pass


    def verif_estrut_exist(self, est):
        if est == 1:
           return  self.my_get(1)  # LIST
        elif est == 2:      # dictionary exist
            return self.my_get(2)  # DICT
        elif est == 3:      # list exist
            return self.my_get(3)  # FILE
        elif est == 4:
            return self.my_get(4)  # SET
        else:
            pass


    def info_structure(self, est):
        info = """
        --------------------------------------
            VOCE ESCOLHEU TRABALHAR COM ...
        --------------------------------------        
        """
        struc_upper = est.upper()
        if est == 'lista':
            print('{} {}'.format(info, struc_upper))
        elif est == 'dicionario':
            print('{} {}'.format(info, struc_upper))
        elif est == 'arquivo':
            print('{}{}'.format(info, struc_upper))
        elif est == 'conjunto':
            print('{}{}'.format(info, struc_upper))
        else:
            pass
        

    def all_values_lista(self):
        dso = ds.EstruturasDados()
        lista = dso.lista
        preench = True
        ind = lista.__len__()
        valor = None
        while preench is True:
            print('\n Informe um numero, caractere ou palavra pra Lista[%d]' %(ind + 1))
            print('\n quit -> pra sair')
            help_value = input('\n Enter some: ')
            if help_value.isnumeric():
                valor = int(help_value)
                lista.append(valor)
                print(lista)
                ind = ind + 1
            elif help_value.isalpha() and (help_value != 'QUIT' and help_value != 'quit'):
                lista.append(help_value)
                print(lista)
                ind = ind + 1
            elif help_value == 'QUIT' or help_value == 'quit':
                preench = False
                self.my_set(lista, 1)
            elif help_value.isalnum():
                preench = True
            else:
                pass
        return


    def all_values_dict(self):
        dso = ds.EstruturasDados()
        dicio = dso.dicio
        preench = True
        ind = dicio.__len__()
        valor = None
        while preench is True:
            print('\n Informe um numero, caractere ou palavra pra Dicionario[%d]' %(ind + 1))
            print('\n quit -> pra sair')
            help_value = input('\n Enter some: ')

            if help_value.isnumeric():
                ind = + 1
                valor = int(help_value)
                dicio[(ind)] = valor
                print(dicio)
            elif help_value.isalpha() and (help_value != 'QUIT' and help_value != 'quit'):
                ind = ind + 1
                dicio[(ind)] = help_value
                print(dicio)
            elif help_value == 'QUIT' or help_value == 'quit':
                preench = False
                self.my_set(dicio, 2)
            elif help_value.isalnum():
                preench = True
            else:
                pass
        return


    def all_values_conj(self):
        dso = ds.EstruturasDados()
        conj = dso.conj
        preench = True
        ind = conj.__len__()
        valor = None
        while preench is True:
            ind = ind + 1
            print('\n Informe um numero, caractere ou palavra pra Conjunto[%d]' % (ind + 1))
            print('\n quit -> pra sair')
            help_value = input('\n Enter some: ')
            if help_value.isnumeric():
                valor = int(help_value)
                conj.add(valor)
                print(conj)
                ind = ind + 1
            elif help_value.isalpha() and (help_value != 'QUIT' and help_value != 'quit'):
                conj.add(help_value)
                print(conj)
                ind = ind + 1
            elif help_value == 'QUIT' or help_value == 'quit':
                preench = False
                self.my_set(conj, 1)
            elif help_value.isalnum():
                preench = True
            else:
                pass
        return
