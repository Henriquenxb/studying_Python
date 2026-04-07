jedi = ['Yoda', 'Luke', 'Obi-Wan', 'Anakin']
print(f'A lista original contém: \n {jedi}\n')



#Inserção no fim da lista
jedi.append("Luminara")
print(f'Após a inserção a lista contém: \n {jedi}\n')


#Inserção no fim da lista com input
jedi.append(str(input('Digite o nome de outro Jedi: ')))
print(f'Após a inserção a lista contém: \n {jedi}\n')


#Inserção em posição
jedi.insert(1,"Palpatine")
#obs: ao usar o .insert(<índice/posição na lista>,<conteúdo que entrará na lista>) precisamos passar o parâmetro que identifica o índice de onde o valor será inserido
print(f'Após a inserção na posição indicada a lista contém: \n {jedi}')