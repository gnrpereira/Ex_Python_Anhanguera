"""
Exercício 12:
   Faça um programa que auxilie uma empresária a calcular o custo do produto. Ela liga 
    para SP pelo celular e conversa com uma vendedora, durante a ligação elas conversam 
    por 18 minutos mas ao final ela encomenda 50 Blusas que serão vendidas em sua loja. 
    A vendedora informa que cada camisa custa R$ 18,50, mas esse valor não é fixo, hoje 
    custa esse valor, então solicita que o pagamento seja por PIX e informa que tem a taxa 
    de R$ 25,00 para que o motoqueiro leve a encomenda dela até a garagem onde o 
    ônibus se encontra. A empresária faz o PIX solicitado e envia o comprovante para a 
    vendedora. A empresária descobre que a ligação lhe custou R$ 2,50 para falar com a 
    vendedora da loja. A menina da loja comprova que o PIX chegou e manda o motoqueiro 
    entregar a encomenda no ônibus. Ao chegar no ônibus o motorista guarda a 
    encomenda no bagageiro e a noite viaja de SP para Valadares. A empresária recebe a 
    informação que o ônibus chegou e vai de carro durante 8 km até a garagem do ônibus 
    buscar a sua encomenda. O motorista informa que o fardo custa R$ 70,00, ela paga e 
    retorna para a loja, onde ela estava. Sabemos que o carro que ela dirige é um JAGUAR 
    e que ele consome 1Litro de Gasolina a cada 4 Km, e que o litro da gasolina é R$ 6,50. 
    
    Sendo assim:  
    a. Informe de quanto foi o PIX que ela fez para a vendedora.  
    
    b. informe qual foi o custo de cada blusa que ela comprou, incidindo todas as 
    despesas que ela teve desde o momento que conversou com a vendedora até o 
    momento que ela está com as blusas na loja. 
    
    c. Agora sabendo que ela quer ganhar o dobro, de quanto ela tem que vender cada 
    camisa ? 
    
    d. Lembrar que as informações podem ser diferentes a cada compra que a 
    empresária fizer. 
    
    e. Salve com o nome de 12-CustoLoja. 
"""

preco_blusa = 18.50 
quantidade_blusas = 50  
valor_pix = preco_blusa * quantidade_blusas  

taxa_entrega_motoqueiro = 25.00  
custo_ligacao = 2.50  
taxa_motorista = 70.00  

distancia_garagem = 8  
consumo_carro = 4  
preco_gasolina = 6.50  
custo_gasolina = (distancia_garagem * 2 / consumo_carro) * preco_gasolina  # Ida e volta


despesa_total = valor_pix + taxa_entrega_motoqueiro + custo_ligacao + taxa_motorista + custo_gasolina


custo_por_blusa = despesa_total / quantidade_blusas


preco_venda_blusa = custo_por_blusa * 2


print(f"O valor total do PIX feito para a vendedora foi: R$ {valor_pix:.2f}")
print(f"O custo total de cada blusa, considerando todas as despesas, foi: R$ {custo_por_blusa:.2f}")
print(f"Para ganhar o dobro, a empresária deve vender cada blusa por: R$ {preco_venda_blusa:.2f}")