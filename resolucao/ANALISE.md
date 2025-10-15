# SOLID
Antes, a classe ProcessadorDePedidos fazia tudo:

processava o pedido,
fazia o pagamento,
enviava a notificação.

Isso deixava o código bagunçado e difícil de mudar.
Por exemplo, se eu quisesse adicionar Pix ou SMS, eu teria que mexer diretamente na classe principal — e isso não é bom.

# responsabilidade unica

Agora cada coisa tem sua própria classe:

Pedido só representa o pedido.
Classes de pagamento só cuidam do pagamento.
Classes de notificação só cuidam da notificação.
ProcessadorDePedidos apenas coordena tudo.

Assim fica bem mais organizado.

# adicionamento de extensão
Se eu quiser adicionar um novo tipo de pagamento ou notificação,
eu só crio uma nova classe e pronto  não preciso alterar código que já existe.
Exemplo: criei PagamentoPix e NotificadorSMS sem mexer em nada da lógica principal.