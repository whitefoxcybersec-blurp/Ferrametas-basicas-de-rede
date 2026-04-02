🛠️ Python Network Toolkit (Black Hat Edition)

Este repositório contém uma coleção de ferramentas de rede desenvolvidas em Python, inspiradas nos conceitos de segurança ofensiva e administração de sistemas. O toolkit inclui desde clientes simples até proxies complexos para interceptação de tráfego.




📋 Conteúdo do Combo

Ferramenta
Descrição
Uso Principal
Client UDP
Cliente leve para envio de datagramas UDP.
Testes de conectividade e fuzzing.
Servidor TCP
Servidor multithread para conexões TCP.
Simulação de serviços e recebimento de dados.
NetCat Python
Implementação personalizada do clássico NetCat.
Shell reverso, upload de arquivos e execução remota.
Proxy TCP
Interceptador de tráfego bidirecional com Hexdump.
Análise de protocolos e modificação de pacotes (MITM).







🚀 Como Utilizar

1. Client UDP

Envia uma mensagem rápida para um alvo específico.

Bash


python udp_client.py <target_host> <target_port>



2. Servidor TCP

Inicia um servidor que aceita múltiplas conexões simultâneas.

Bash


python tcp_server.py



3. NetCat Python

Uma ferramenta versátil para controle remoto.

•
Ouvir por uma shell:

Bash


python netcat.py -t 192.168.1.10 -p 5555 -l -c





•
Executar um comando específico:

Bash


python netcat.py -t 192.168.1.10 -p 5555 -l -e="cat /etc/passwd"





4. Proxy TCP

Intercepta a comunicação entre um cliente e um servidor remoto.

Bash


python proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]



Exemplo: python proxy.py 127.0.0.1 9000 10.10.10.5 80 True




🔍 Funcionalidades Avançadas

•
Hexdump em Tempo Real: O Proxy TCP e o NetCat incluem visualização em hexadecimal para análise profunda de pacotes.

•
Multithreading: O Servidor TCP e o Proxy utilizam threads para lidar com múltiplas conexões sem travar.

•
Packet Manipulation: Hooks integrados (request_handler e response_handler) para modificar dados em trânsito.




🛡️ Aviso Legal (Disclaimer)

Este toolkit foi desenvolvido para fins educacionais e de testes de segurança autorizados. O uso destas ferramentas para atacar alvos sem permissão prévia é ilegal. O autor não se responsabiliza pelo uso indevido deste software.




👤 Autor

Desenvolvido por WhiteFox como parte de estudos avançados em Python e Segurança de Redes.

