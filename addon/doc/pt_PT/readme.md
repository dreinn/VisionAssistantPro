# Documentação do Vision Assistant Pro

O **Vision Assistant Pro** é um assistente de IA multimodal avançado para o NVDA. Utiliza motores de IA de classe mundial para fornecer leitura de ecrã inteligente, tradução, ditado por voz e análise de documentos.

_Este suplemento foi lançado para a comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Configuração e Definições

Aceda ao **Menu NVDA > Preferências > Definições > Vision Assistant Pro**.

### 1.1 Definições de Conexão

- **Fornecedor:** Selecione o seu serviço de IA preferido. Os fornecedores suportados incluem o **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** e **Personalizado** (servidores compatíveis com OpenAI como o Ollama, LM Studio, Jan.ai ou KoboldCPP).
- **Nota Importante:** Recomendamos vivamente a utilização do **Google Gemini** para obter o melhor desempenho e precisão (especialmente para análise de imagens e ficheiros).
- **Chave de API (API Key):** Obrigatória. Pode introduzir várias chaves (separadas por vírgulas ou quebras de linha) para rotação automática.
- **Procurar Modelos (Fetch Models):** Após introduzir a sua chave de API, prima este botão para descarregar a lista mais recente de modelos disponíveis do fornecedor.
- **Modelo de IA:** Selecione o modelo principal utilizado para chat geral e análise.

### 1.2 Encaminhamento Avançado de Modelos

*Disponível para todos os fornecedores, incluindo Gemini, OpenAI, Groq, Mistral e Personalizado._

> **⚠️ Aviso:** Estas definições destinam-se **apenas a utilizadores avançados**. Se não tiver a certeza do que um modelo específico faz, deixe esta opção **desmarcada**. Selecionar um modelo incompatível para uma tarefa (por exemplo, um modelo apenas de texto para Visão) causará erros e fará com que o suplemento pare de funcionar.

Marque **"Encaminhamento Avançado de Modelos (Específico por tarefa)"** para desbloquear o controlo detalhado. Isto permite-lhe selecionar modelos específicos da lista pendente para diferentes tarefas:

- **Modelo de OCR / Visão:** Escolha um modelo especializado para analisar imagens.
- **Conversão de Voz em Texto (STT):** Escolha um modelo específico para ditado.
- **Conversão de Texto em Voz (TTS):** Escolha um modelo para gerar áudio.
- **Modelo de Operador de IA:** Selecione um modelo específico para tarefas de operação autónoma do computador.
_Nota: Funcionalidades não suportadas (por exemplo, TTS para o Groq) serão ocultadas automaticamente._

### 1.3 Configuração Avançada de Endpoint (Fornecedor Personalizado)

*Disponível apenas quando "Personalizado" estiver selecionado._

> **⚠️ Aviso:** Esta secção permite a configuração manual da API e foi concebida para **utilizadores avançados** que executam servidores locais ou proxies. URLs ou nomes de modelos incorretos quebrarão a conectividade. Se não sabe exatamente o que são estes endpoints, mantenha esta opção **desmarcada**.

Marque **"Configuração Avançada de Endpoint"** para introduzir manualmente os detalhes do servidor. Ao contrário dos fornecedores nativos, aqui deve **escrever** as URLs e os Nomes de Modelos específicos:

- **URL da Lista de Modelos:** O endpoint para procurar os modelos disponíveis.
- **URL do Endpoint de OCR/STT/TTS:** URLs completas para serviços específicos (por exemplo, `http://localhost:11434/v1/audio/speech`).
- **Modelos Personalizados:** Escreva manualmente o nome do modelo (por exemplo, `llama3:8b`) para cada tarefa.

### 1.3.1 Configurar IA Local (Configuração Numa Única Ação)

To tornar a integração de IA local e completamente offline extremamente simples, um botão dedicado **"Configurar IA Local"** está disponível dentro das Definições do Fornecedor Personalizado.

Se estiver a executar um servidor de modelo de IA local no seu computador:

1. Selecione **Personalizado** como seu Fornecedor.
2. Prima o botão **Configurar IA Local**.
3. Escolha o seu motor de IA local na caixa de diálogo acessível:
   - **Ollama** (predefinição para `http://127.0.0.1:11434`)
   - **LM Studio** (predefinição para `http://127.0.0.1:1234`)
   - **Jan.ai** (predefinição para `http://127.0.0.1:1337`)
   - **KoboldCPP** (predefinição para `http://127.0.0.1:5001`)
4. O suplemento configurará instantaneamente a URL local correta, o tipo de API e procurará automaticamente os seus modelos offline ativos para preencher a caixa de seleção **Modelo de IA**.

_Nota sobre Rede e Proxies:_ Este motor de conexão local possui um mecanismo avançado de desvio de proxy. Mesmo que esteja a utilizar uma VPN ativa no sistema ou um proxy em modo TUN, os seus pedidos de IA locais ignorá-los-ão completamente, garantindo conexões offline estáveis sem erros do tipo 502 Bad Gateway.

### 1.4 Preferências Gerais

- **Motor de OCR:** Escolha entre **Chrome (Rápido)** para resultados rápidos ou **IA (Avançado)** para uma preservação superior da disposição (layout).
  - _Nota:_ Se selecionar "IA (Avançado)", mas o seu fornecedor estiver definido como OpenAI/Groq, o suplemento encaminhará inteligentemente a imagem para o modelo de visão do seu fornecedor ativo.
- **Voz do TTS:** Selecione o seu estilo de voz preferido. Esta lista é atualizada dinamicamente com base no seu fornecedor ativo.
- **Criatividade (Temperatura):** Controla a aleatoriedade da IA. Valores mais baixos são melhores para traduções/OCR precisos.
- **URL do Proxy:** Configure se os serviços de IA estiverem restritos na sua região (suporta proxies locais como `127.0.0.1` ou URLs de ponte).

## 2. Camada de Comando e Atalhos

Para evitar conflitos de teclado, este suplemento utiliza uma **Camada de Comando**.

1. Prima **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (ouvirá um sinal sonoro).
2. Solte as teclas e, em seguida, prima uma das seguintes teclas individuais:

| Tecla         | Função                      | Descrição                                                                                                                            |
| ------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Shift + A** | **Operador de IA**          | **Operação Autónoma:** Diga à IA para realizar uma tarefa no seu ecrã. Premir novamente aborta instantaneamente as operações ativas. |
| **E**         | **Explorador de IU**        | **Clique Interativo:** Identifica e clica em elementos de interface em qualquer aplicação.                                           |
| **T**         | Tradutor Inteligente        | Traduz o texto sob o cursor do navegador ou a seleção.                                                                               |
| **Shift + T** | Tradutor da Área de Transf. | Traduz o conteúdo que está atualmente na área de transferência.                                                                      |
| **R**         | Refinador de Texto          | Resume, corrige a gramática, explica ou executa **Pedidos Personalizados**.                                                          |
| **V**         | Visão de Objeto             | Descreve o objeto atual do navegador.                                                                                                |
| **O**         | Visão em Ecrã Inteiro       | Analisa a disposição e o conteúdo de todo o ecrã.                                                                                    |
| **Shift + V** | Análise de Vídeo Online     | Analisa vídeos do **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**.                                                         |
| **D**         | Leitor de Documentos        | Leitor avançado para PDF e imagens com seleção de intervalo de páginas.                                                              |
| **F**         | **Ação de Ficheiro Intel.** | Reconhecimento contextual de ficheiros de imagem, PDF ou TIFF selecionados.                                                          |
| **A**         | Transcrição de Áudio        | Transcreve ficheiros MP3, WAV ou OGG em texto.                                                                                       |
| **C**         | Solucionador de CAPTCHA     | Captura e resolve CAPTCHAs (Suporta portais governamentais).                                                                         |
| **S**         | Ditado Inteligente          | Converte voz em texto. Prima para iniciar a gravação, e novamente para parar/escrever.                                               |
| **Control+L** | **Assistente ao Vivo**      | **Copiloto em tempo real (apenas Gemini):** Inicia ou encerra uma conversa ao vivo por voz e ecrã com o assistente de IA.            |
| **I**         | Relatório de Status         | Anuncia o progresso atual (por exemplo, "A escanear...", "Inativo").                                                                 |
| **L**         | **Rotular Objeto**          | **Rotulagem Semântica por IA:** Rotula permanentemente o elemento/ícone focado atual.                                                |
| **Shift + L** | **Gerir/Escanear Rótulos**  | Abre o Gestor de Rótulos (se houver rótulos) ou escaneia a app em busca de elementos sem nome.                                       |
| **U**         | Verificar Atualização       | Verifica manualmente o GitHub para encontrar a versão mais recente do suplemento.                                                    |
| **Espaço**    | Relembrar Último Result.    | Mostra a última resposta da IA numa caixa de diálogo de chat para revisão ou acompanhamento.                                         |
| **H**         | Ajuda de Comandos           | Exibe uma lista de todos os atalhos disponíveis.                                                                                     |

### 2.1 Atalhos do Leitor de Documentos (Dentro do Visualizador)

- **Ctrl + PageDown:** Move para a página seguinte.
- **Ctrl + PageUp:** Move para a página anterior.
- **Alt + A:** Abre uma caixa de diálogo de chat para fazer perguntas sobre o documento.
- **Alt + R:** Força um **Reescaneamento com IA** utilizando o seu fornecedor ativo.
- **Alt + G:** Gera e guarda um ficheiro de áudio de alta qualidade (WAV/MP3). _Oculto se o fornecedor não suportar TTS._
- **Alt + S / Ctrl + S:** Guarda o texto extraído como um ficheiro TXT ou HTML.

## 3. Operador de IA - Controlo Autónomo de Computador

O **Operador de IA** transforma o Vision Assistant Pro de um leitor passivo num assistente ativo que pode interagir com o computador em seu nome. Pode pedir-lhe para descrever o ecrã, responder a perguntas sobre o que está a ver ou até mesmo assumir o controlo — clicando em botões, arrastando itens, escrevendo textos e navegando pelas aplicações utilizando comandos em linguagem natural.

A maior vantagem? Funciona perfeitamente em softwares completamente inacessíveis. Se estiver bloqueado numa aplicação personalizada, numa área de trabalho remota ou num sítio Web onde o seu leitor de ecrã fica totalmente silencioso, o operador não se importa. Como "vê" o ecrã visualmente, consegue encontrar, ler e interagir com elementos que possuem zero rótulos de acessibilidade.

### Como Funciona

1. Prima **NVDA + Shift + V** e, em seguida, prima **Shift + A** (ou utilize o atalho direto) para abrir a caixa de diálogo do Operador de IA.
2. Escreva o que deseja fazer em linguagem simples (por exemplo, "Clique no botão Guardar", "O que diz a mensagem de erro?" ou "Renomeie o ficheiro para final.pdf").
3. A IA analisará o seu ecrã, identificará os elementos relevantes e executará a ação ou fornecerá a resposta. Se uma tarefa exigir vários passos, o operador continuará a trabalhar até que a mesma seja concluída.
4. Prima **Shift + A** novamente a qualquer momento para abortar instantaneamente uma operação em curso.

### Ações Suportadas

O operador compreende uma ampla variedade de comandos:

- **Descrever e Responder**: "Descreva a disposição do ecrã" ou "O que diz a mensagem de erro?"
- **Clicar**: "Clique no botão Guardar"
- **Clique com o Botão Direito**: "Clique com o botão direito no ficheiro"
- **Duplo Clique**: "Dê um duplo clique no documento"
- **Arrastar e Largar**: "Arraste o documento para a pasta Arquivo"
- **Escrever**: "Escreva 'Olá Mundo' na caixa de pesquisa"
- **Deslocar (Scroll)**: "Desloque para baixo três vezes"
- **Premir Teclas**: "Prima Enter", "Prima Tab", "Prima Escape"
- **Tarefas de Vários Passos**: "Abra o Explorador de Ficheiros, encontre o relatório e renomeie-o para final.pdf"

### Notas Importantes

- **⚠️ Aviso de Utilização da API**: Como o operador precisa de "ver" exatamente o que está a acontecer no ecrã, envia uma captura de ecrã em alta resolução a cada passo. O uso frequente consumirá a sua quota de API muito mais rápido do que as funcionalidades padrão baseadas em texto.
- **Aplicações em Modo Administrador**: Se o NVDA não estiver a ser executado com privilégios de Administrador, o operador poderá não conseguir interagir com janelas que exigem permissões elevadas. Isto é uma limitação de segurança do Windows, não um erro no suplemento.
- **Boas Práticas**: Para obter os melhores resultados, dê comandos claros e específicos. "Clique no botão azul Submeter na parte inferior do formulário" quase sempre funcionará melhor do que apenas "Clique no botão".

## 4. Pedidos Personalizados e Variáveis

Pode gerir os seus pedidos em **Definições > Pedidos > Gerir Pedidos...**.

### Variáveis Suportadas

- `[selection]`: Texto selecionado atualmente.
- `[clipboard]`: Conteúdo da área de transferência.
- `[screen_obj]`: Captura de ecrã do objeto do navegador.
- `[screen_fg_obj]`: Captura de ecrã da janela ativa em primeiro plano.
- `[screen_full]`: Captura de ecrã de ecrã inteiro.
- `[file_ocr]`: Selecionar ficheiro de imagem/PDF para extração de texto.
- `[file_read]`: Selecionar documento para leitura (TXT, Código, PDF).
- `[file_audio]`: Selecionar ficheiro de áudio para análise (MP3, WAV, OGG).

***
**Nota:** É necessária uma ligação de internet ativa para todas as funcionalidades de IA. Documentos de várias páginas são processados automaticamente.

## 5. Suporte e Comunidade

Mantenha-se atualizado com as últimas notícias, recursos e lançamentos:

- **Canal do Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **Problemas no GitHub (GitHub Issues):** Para relatórios de erros e pedidos de funcionalidades.

## 6. Apoiantes do Projeto

Um agradecimento sincero aos membros da nossa comunidade que apoiam o desenvolvimento contínuo e a manutenção deste projeto através das suas generosas contribuições financeiras:

- **@Alyabani94**
- **Ali Alamri**
- **Ilya**
- **Apoiante Anónimo** (`UQDd...CnMY`)
- **leonardo0216**
- **Sergei Fleytin**

_Se deseja apoiar o projeto financeiramente e ver o seu nome aqui, pode encontrar a opção **Doar** no menu Ferramentas do NVDA (submenu Vision Assistant) ou durante o processo de configuração após a instalação._

## Alterações para 7.0.0

- **Retoma de Escaneamentos Inacabados**: Adicionado um recurso de retoma tanto para o Leitor de Documentos quanto para as Ações de Ficheiro Inteligentes. Se um escaneamento for interrompido, agora pode continuar de onde parou em vez de começar do zero.
- **Nova Variável `[screen_fg_obj]`**: Adicionada uma variável de pedido personalizado para capturar uma captura de ecrã apenas da janela ativa em primeiro plano, em vez de todo o ecrã.
- **Tentativas Inteligentes e Rotação de Chaves**: O suplemento agora repete silenciosamente a operação até 5 vezes na mesma chave ao encontrar sobrecargas temporárias no servidor (como "alta procura" ou respostas malformadas). Se as tentativas falharem, muda automaticamente para a próxima chave de API da sua lista.
- **Deteção de Cortina de Ecrã**: Adicionada uma verificação para evitar capturas de ecrã quando a Cortina de Ecrã estiver ativa (seja permanentemente ativada ou alternada temporariamente pelo atalho). O sistema emitirá um aviso e interromperá a ação, evitando que envie imagens pretas e desperdice tokens de API.
- **Ajustes no Leitor de Documentos**: A caixa de diálogo de intervalo do PDF agora pré-seleciona automaticamente o idioma de destino predefinido das definições do seu suplemento. Também foi aprimorado o gerenciamento de threads para garantir que as tarefas em segundo plano parem de forma limpa quando o leitor for fechado.
- **Integração Nativa de OCR do Mistral**: Integrada a API nativa de OCR de Documentos do Mistral. Documentos com várias páginas são reunidos, enviados e processados automaticamente em lotes utilizando o endpoint especializado `/v1/ocr` do Mistral, enquanto imagens de página única são processadas diretamente sem conversões desnecessárias para PDF.
- **Manipuladores Dinâmicos de URL Personalizada**: Modificar a URL de API Personalizada agora limpa instantaneamente a lista de modelos em cache e restaura a caixa de texto para introdução manual de modelos. Isto garante total compatibilidade com endpoints personalizados (como o Cloudflare AI Gateway) que não suportam o endpoint padrão de listagem `/v1/models`.
- **Reformulação do Motor de Entrada do Operador de IA**: O sistema subjacente de simulação de rato e teclado para o Operador de IA foi completamente reconstruído. A API herdada `mouse_event` foi substituída pela moderna API `SendInput` do Windows, trazendo uma compatibilidade significativamente maior com aplicações modernas, janelas protegidas por UAC e ecrãs de alta densidade de píxeis (high-DPI).
- **Correção nas Operações de Arrastar e Largar**: As ações de arrastar e largar no Operador de IA estão agora totalmente estáveis e confiáveis. O novo motor utiliza curvas naturais de suavização ("easing"), posicionamento preciso do cursor, temporização otimizada e uma técnica inteligente de "toque leve" para garantir que o Windows e as aplicações reconheçam e executem corretamente os gestos de arrastar e largar sem falhar a meio do caminho.
- **Suporte a Múltiplos Monitores**: O Operador de IA suporta agora totalmente configurações com múltiplos monitores. Os movimentos e cliques do rato funcionam corretamente em todos os monitores utilizando a flag `MOUSEEVENTF_VIRTUALDESK`, garantindo o posicionamento preciso independentemente de em qual monitor a aplicação de destino esteja.
- **Simulação de Teclado Aprimorada**: Injeção de teclas aprimorada para suportar totalmente as "Teclas Estendidas" (como as setas do teclado, Home, End, Page Up/Down, Insert, Delete e F1-F12). Isto garante que os comandos de navegação e atalhos enviados pelo Operador de IA funcionem perfeitamente em todas as aplicações.
- **Suporte a Imagens HEIC/HEIF**: Adicionado suporte nativo para formatos de fotos do iPhone. Agora pode selecionar diretamente ficheiros `.heic` e `.heif` para descrição por IA, OCR ou Leitura de Documentos sem necessidade de conversão prévia.

## Alterações para 6.5.0

- **Assistente ao Vivo**: Adicionado um recurso de assistente de voz e ecrã em tempo real, disponível exclusivamente para o fornecedor Google Gemini (isto inclui fornecedores personalizados compatíveis com o Gemini). Inclui personalização interativa de voz e profundidade de raciocínio diretamente na caixa de diálogo, com reconexão automática ao alterar as definições.
- **Fornecedor de IA MiniMax**: Integrado o MiniMax como um fornecedor de mesmo nível com suporte multimodal completo (chat, visão, OCR), TTS personalizado utilizando mais de 300 vozes dinâmicas e remoção automática de blocos de raciocínio (ex: `<think>...</think>`) dos resultados.
- **Tradução no Visualizador de Documentos**: Corrigida uma falha silenciosa de tradução para utilizadores do NVDA que não utilizam o idioma inglês, garantindo que o código de idioma padrão de 2 letras seja enviado ao Google Tradutor em vez do nome do idioma localizado.
- **Tentativa de Escaneamento em Lote de PDF**: Implementada uma lógica de repetição separada, altamente otimizada e silenciosa para o escaneamento em lote de documentos PDF, evitando uploads redundantes e janelas de erro perturbadoras durante as tentativas.
- **Status do Visualizador de Documentos**: Corrigido um bug onde o status geral do plugin (verificado através da tecla `I`) ficava travado em "Processamento em Lote Iniciado" durante escaneamentos de documentos longos.
- **Resolução de Travamento de Threads**: Corrigido um travamento grave de asserção de thread `IsMain() failed in wxTimerImpl` ao abrir documentos a partir de uma thread em segundo plano, transferindo a fila de chamadas da GUI para `wx.CallAfter`.

## Alterações para 6.1.2

- **Pré-verificação de Rótulos Duplicados**: Corrigido um problema na rotulagem individual onde a verificação de duplicados usava chaves de coordenadas antigas, fazendo com que o NVDA fizesse pedidos de IA duplicados para objetos já rotulados em vez de anunciar o rótulo existente.
- **Chat de Documentos para Fornecedores Não-Gemini**: Corrigida uma verificação estrita de chave de API no Chat de Documentos (`on_ask`) para garantir que os utilizadores do OpenAI, Groq ou de fornecedores personalizados locais (como o Ollama) possam conversar com documentos com sucesso sem serem bloqueados.
- **Tradução Rápida de OCR do Chrome**: Restaurada a API de tradução gratuita e sem necessidade de chave para o OCR do Chrome. A tradução do texto extraído agora ignora a IA do Gemini, economizando quotas de API e acelerando o processo de tradução.
- **Filtro Alfanumérico de CAPTCHA**: Corrigida a lógica de filtragem no solucionador de CAPTCHA para garantir que os caracteres não alfanuméricos sejam limpos adequadamente em todas as situações.
- **Atualização da Ajuda da Camada de Comando**: Corrigido o atalho de anúncio de status no menu de ajuda de `L` para `I`, e adicionados ambos os comandos de rotulagem (`L` e `Shift+L`) à lista.

## Alterações para 6.1.1

- **Atendimento de Saída de Raciocínio do Gemma 4**: Corrigido um problema com os modelos Gemma 4 onde todo o processo de pensamento interno era exibido como a resposta final, ou onde desativar o pensamento resultava em respostas vazias. O suplemento agora isola e extrai corretamente apenas a resposta de texto limpa e final.
- **OCR em Lote a partir do Explorador de Ficheiros**: Agora pode selecionar várias fotos ou PDFs diretamente no Explorador de Ficheiros do Windows e extrair texto ou analisá-los em lote. O suplemento filtrará e processará automaticamente apenas os formatos de ficheiro suportados.

## Alterações para 6.1.0

- **Integração Universal de IA Local (Configurar IA Local)**: Adicionado um novo botão **"Configurar IA Local"** nas Definições do Fornecedor Personalizado. Os utilizadores agora podem configurar automaticamente motores de IA locais, incluindo o **Ollama**, **LM Studio**, **Jan.ai** e **KoboldCPP** instantaneamente.
- **Desvio Inteligente de Proxy Local**: Reconstruída a lógica de conexão com um mecanismo avançado de desvio de proxy. O suplemento é agora inteligente o suficiente para ignorar completamente os proxies do sistema Windows em conexões de loopback local, garantindo conexões estáveis com a IA local mesmo quando a sua VPN ou modo TUN estiver ativo.
- **Rotulagem por IA Ultra-Estável (v2)**: Substituídas as chaves de coordenadas absolutas do ecrã por um sistema híbrido avançado de **Assinatura do Objeto**. Os rótulos agora dependem de identificadores programáticos (UIA **AutomationId** ou Win32 **ControlID**) e coordenadas relativas à janela, tornando os seus rótulos personalizados completamente resistentes ao redimensionamento de janelas, movimentação, troca de monitor ou alteração na escala do ecrã.
- **Migração Automática de Rótulos Transparente**: A atualização é completamente transparente. O suplemento migrará automaticamente os seus rótulos legados baseados em coordenadas antigas para o novo formato de impressão digital estável em segundo plano no primeiro foco, com zero perda de dados.

## Alterações para 6.0

- **Apresentando a Rotulagem Semântica por IA**: Os utilizadores agora podem rotular permanentemente botões e ícones sem nome usando IA. Pressione **L** para rotular o objeto atual do navegador (suportando tanto o foco por Tab quanto a navegação de objetos) ou **Shift+L** para escanear e rotular toda a aplicação de uma vez.
- **Gerenciamento Inteligente de Rótulos**: Adicionada uma nova caixa de diálogo do Gestor de Rótulos totalmente acessível (via **Shift+L** se os rótulos existirem) para visualizar, renomear ou eliminar rótulos personalizados em lote.
- **Análise Direta de Ficheiros (Ignorar Caixa de Diálogo de Ficheiro)**: O suplemento é agora inteligente o suficiente para detectar se está focado num ficheiro PDF ou de imagem no Explorador de Ficheiros do Windows. Pressionar **F (Ação de Ficheiro Inteligente)** ou **D (Leitor de Documentos)** num ficheiro realçado irá processá-lo imediatamente, ignorando completamente a caixa de diálogo padrão "Abrir".

## Alterações para 5.6

- **Adicionado Mecanismo de OCR "Nenhum (Extrair Camada de Texto)"**: Os utilizadores agora podem extrair texto diretamente de PDFs pesquisáveis sem usar créditos de IA, melhorando significativamente a velocidade e a privacidade para documentos baseados em texto.
- **Precisão Refinada do Explorador de IU**: Aprimorado o comando do Explorador de IU para identificar melhor os tipos de elementos (como Itens de Lista) e relatar estados com precisão, tais como "(Marcado)", "(Selecionado)" ou "(Expandido)", ignorando componentes do sistema Windows como a Barra de Tarefas e o Relógio.
- **Lembrete de Configuração de Instalação**: Adicionada uma notificação após a instalação para guiar os utilizadores ao menu de definições para configurar as suas chaves de API e preferências.

## Alterações para 5.5.2

- **Correção de Problema de Escrita no Operador de IA:** Resolvido um erro em que a letra 'v' era escrita em vez de colar o texto em determinados sistemas. Esta correção aborda conflitos de temporização que ocorriam durante alta carga do sistema.
- **Estabilidade Aprimorada:** Adicionado um tratamento robusto de erros para operações de área de transferência para evitar travamentos do suplemento quando a área de transferência do sistema estiver temporariamente bloqueada por outros aplicativos.
- **Otimização de Temporização:** Ajustados os atrasos internos para eventos de teclado para garantir maior confiabilidade em diferentes velocidades de sistema e melhor compatibilidade com Gestores de Área de Transferência de terceiros.

## Alterações para 5.5 (A Atualização de Automação)

- **Operador de IA (Controle Autónomo - Shift+A):** Esta é a joia da coroa da v5.5. O Vision Assistant Pro evoluiu de um assistente passivo para se tornar o seu **Operador de IA** pessoal. Ele não apenas descreve o ecrã — ele assume o comando.
  - _Como funciona:_ Agora pode dar instruções verbais para operar o seu PC. Por exemplo, numa aplicação completamente inacessível onde o seu leitor de ecrã permanece em silêncio, pode pressionar **Shift+A** e escrever: _"Clique no botão Definições"_ ou _"Encontre o campo de pesquisa, escreva 'Últimas Notícias' e pressione enter."_ A IA identifica visualmente os elementos, move o rato e executa a tarefa por si.
  - _Nota de Desempenho:_ Este recurso é otimizado para o **Gemini 3.0 Flash (Preview)**, entregando respostas incrivelmente rápidas e inteligentes que podem lidar até mesmo com as disposições de interface de utilizador mais complexas.
  - **⚠️ Aviso de Utilização da API:** Como o Operador de IA precisa de "ver" exatamente o que está a acontecer para ser preciso, ele envia uma captura de ecrã em alta resolução a cada passo. Por favor, note que o uso frequente consumirá a sua quota de API muito mais rápido do que as tarefas padrão baseadas em texto.
- **Explorador de Interface de Utilizador Visual (E):** Cansado de navegar por "botões sem rótulo"? Pressione **E** para ativar o Explorador de IU. A IA escaneará a janela inteira e gerará uma lista de cada elemento clicável que ela vê — incluindo ícones, gráficos e menus. Basta escolher um item da lista e o Operador de IA clicará nele por si. É como ter uma "camada acessível" por cima de qualquer aplicação.
- **Ação de Ficheiro Inteligente Sensível ao Contexto (F):** A tecla "F" foi completamente reformulada. Ela não pressupõe mais que deseja apenas o OCR. Quando seleciona uma única imagem, ela agora pergunta inteligentemente qual é a sua intenção: pode escolher uma **Descrição Visual Detalhada** para entender a cena ou uma **Extração de Texto Estruturada (OCR)** para leitura. O menu adapta-se dinamicamente com base no tipo de ficheiro e no seu motor de IA ativo.
- **Otimização do Núcleo:** Realizámos uma limpeza profunda na lógica interna do suplemento, removendo funções legadas não utilizadas e códigos redundantes. Isto resulta numa experiência mais enxuta, rápida e confiável para todos os utilizadores.

## Alterações para 5.0

- **Arquitetura Multi-Fornecedor**: Adicionado suporte completo para o **OpenAI**, **Groq** e **Mistral** junto ao Google Gemini. Os utilizadores agora podem escolher o seu backend de IA preferido.
- **Encaminhamento Avançado de Modelos**: Utilizadores de fornecedores nativos (Gemini, OpenAI, etc.) agora podem selecionar modelos específicos de uma lista suspensa para diferentes tarefas (OCR, STT, TTS).
- **Configuração Avançada de Endpoint**: Utilizadores de fornecedores personalizados podem introduzir manualmente URLs e nomes de modelos específicos para controlo granular sobre servidores locais ou de terceiros.
- **Visibilidade Inteligente de Recursos**: O menu de definições e a interface do Leitor de Documentos agora ocultam automaticamente recursos não suportados (como TTS) com base no fornecedor selecionado.
- **Busca Dinâmica de Modelos**: O suplemento agora procura a lista de modelos disponíveis diretamente da API do fornecedor, garantindo compatibilidade com novos modelos assim que forem lançados.
- **OCR e Tradução Híbridos**: Otimizadas lógicas para usar o Google Tradutor para maior velocidade ao usar o OCR do Chrome, e tradução baseada em IA ao usar os motores Gemini/Groq/OpenAI.
- **"Re-escanear com IA" Universal**: O recurso de re-escanear do Leitor de Documentos não está mais limitado ao Gemini. Ele agora utiliza qualquer fornecedor de IA que esteja ativo no momento para reprocessar as páginas.

## Alterações para 4.6

- **Reabertura Interativa de Resultados:** Adicionada a tecla **Espaço** à camada de comando, permitindo que os utilizadores reabram instantaneamente a última resposta da IA numa janela de chat para perguntas de acompanhamento, mesmo quando o modo "Saída Direta" estiver ativo.
- **Hub da Comunidade no Telegram:** Adicionado um link para o "Canal Oficial do Telegram" no menu Ferramentas do NVDA, fornecendo uma maneira rápida de se manter atualizado com as últimas notícias, recursos e lançamentos.
- **Estabilidade de Resposta Aprimorada:** Otimizada a lógica central para os recursos de Tradução, OCR e Visão para garantir um desempenho mais confiável e uma experiência mais suave ao usar a saída de fala direta.
- **Orientação de Interface Aprimorada:** Atualizadas as descrições de definições e documentação para explicar melhor o novo sistema de reabertura e como ele funciona junto com as definições de saída direta.

## Alterações para 4.5

- **Gestor de Pedidos Avançado:** Introduzida uma caixa de diálogo de gestão dedicada nas definições para personalizar os pedidos padrão do sistema e gerenciar pedidos definidos pelo utilizador com suporte completo para adicionar, editar, reordenar e visualizar.
- **Suporte Abrangente a Proxy:** Resolvidos problemas de conectividade de rede garantindo que as configurações de proxy configuradas pelo utilizador sejam estritamente aplicadas a todas as requisições de API, incluindo tradução, OCR e geração de fala.
- **Migração Automatizada de Dados:** Integrado um sistema de migração inteligente para atualizar automaticamente as configurações de pedidos legados para um formato JSON v2 robusto na primeira execução, sem perda de dados.
- **Compatibilidade Atualizada (2025.1):** Definida a versão mínima exigida do NVDA para 2025.1 devido a dependências de biblioteca em recursos avançados como o Leitor de Documentos para garantir um desempenho estável.
- **Interface de Definições Otimizada:** Simplificada a interface de definições ao reorganizar o gerenciamento de pedidos numa caixa de diálogo separada, proporcionando uma experiência de utilizador mais limpa e acessível.
- **Guia de Variáveis de Pedido:** Adicionado um guia integrado nas caixas de diálogo de pedidos para ajudar os utilizadores a identificar e usar facilmente variáveis dinâmicas como [selection], [clipboard] e [screen_obj].

## Alterações para 4.0.3

- **Maior Resiliência de Rede:** Adicionado um mecanismo de repetição automática para lidar melhor com conexões de internet instáveis e erros temporários de servidor, garantindo respostas de IA mais confiáveis.
- **Caixa de Diálogo Visual de Tradução:** Introduzida uma janela dedicada para resultados de tradução. Os utilizadores agora podem navegar e ler traduções longas facilmente linha por linha, de forma semelhante aos resultados de OCR.
- **Visualização Formatada Agregada:** O recurso "Visualizar Formatado" no Leitor de Documentos agora exibe todas as páginas processadas numa única janela organizada com cabeçalhos de página claros.
- **Fluxo de Trabalho de OCR Otimizado:** Pula automaticamente a seleção de intervalo de páginas para documentos de página única, tornando o processo de reconhecimento mais rápido e contínuo.
- **Estabilidade de API Aprimorada:** Alterado para um método de autenticação baseado em cabeçalho mais robusto, resolvendo potenciais erros de "Todas as chaves de API falharam" causados por conflitos de rotação de chaves.
- **Correções de Bugs:** Resolvidos vários travamentos potenciais, incluindo um problema durante o encerramento do suplemento e um erro de foco na caixa de diálogo de chat.

## Alterações para 4.0.1

- **Leitor de Documentos Avançado:** Um novo e poderoso visualizador para PDF e imagens com seleção de intervalo de páginas, processamento em segundo plano e navegação contínua através de `Ctrl+PageUp/Down`.
- **Novo Submenu de Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" sob o menu Ferramentas do NVDA para acesso mais rápido aos recursos principais, definições e documentação.
- **Customização Flexível:** Agora pode escolher o seu mecanismo de OCR preferido e a voz do TTS diretamente do painel de definições.
- **Suporte a Múltiplas Chaves de API:** Adicionado suporte para múltiplas chaves de API do Gemini. Pode inserir uma chave por linha ou separá-las com vírgulas nas definições.
- **Mecanismo de OCR Alternativo:** Introduzido um novo mecanismo de OCR para garantir o reconhecimento confiável de texto mesmo ao atingir os limites de cota da API do Gemini.
- **Rotação Inteligente de Chaves de API:** Alterna automaticamente para a chave de API funcional mais rápida e a memoriza para contornar os limites de cota.
- **Documento para MP3/WAV:** Capacidade integrada para gerar e salvar arquivos de áudio de alta qualidade nos formatos MP3 (128kbps) e WAV diretamente dentro do leitor.
- **Suporte a Stories do Instagram:** Adicionada a capacidade de descrever e analisar Stories do Instagram usando suas URLs.
- **Suporte ao TikTok:** Introduzido suporte para vídeos do TikTok, permitindo descrição visual completa e transcrição de áudio dos clipes.
- **Caixa de Diálogo de Atualização Redesenhada:** Apresenta uma nova interface acessível com uma caixa de texto rolável para ler claramente as alterações da versão antes de instalar.
- **Status e UX Unificados:** Padronizadas as caixas de diálogo de ficheiros em todo o suplemento e aprimorado o comando 'L' para relatar o progresso em tempo real.

## Alterações para 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) dentro da Camada de Comando para fornecer uma lista de fácil acesso de todos os atalhos e suas funções.
- **Análise de Vídeo Online:** Expandido o suporte para incluir vídeos do **Twitter (X)**. Também foi aprimorada a detecção de URL e a estabilidade para uma experiência mais confiável.
- **Contribuição ao Projeto:** Adicionada uma caixa de diálogo opcional de doação para utilizadores que desejam apoiar as futuras atualizações e o crescimento contínuo do projeto.

## Alterações para 3.5.0

- **Camada de Comando:** Introduzido um sistema de Camada de Comando (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestra. Por exemplo, em vez de pressionar `NVDA+Control+Shift+T` para tradução, agora você pressiona `NVDA+Shift+V` seguido por `T`.
- **Análise de Vídeo Online:** Adicionado um novo recurso para analisar vídeos do YouTube e do Instagram diretamente fornecendo uma URL.

## Alterações para 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para ignorar a caixa de diálogo de chat e ouvir as respostas da IA diretamente via fala para uma experiência mais rápida e integrada.
- **Integração com a Área de Transferência:** Adicionada uma nova configuração para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações para 3.0

- **Novos Idiomas:** Adicionadas traduções em **Persa** e **Vietnamita**.
- **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) para ajudar os utilizadores a distinguir entre modelos gratuitos e com limite de taxa (pagos). Adicionado suporte para o **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade do Ditado:** Estabilidade do Ditado Inteligente significativamente aprimorada. Adicionada uma verificação de segurança para ignorar clipes de áudio com menos de 1 segundo, evitando alucinações da IA e erros vazios.
- **Manipulação de Ficheiros:** Corrigido um problema onde o upload de ficheiros com nomes que não estivessem em inglês falhava.
- **Otimização de Pedidos:** Lógica de Tradução aprimorada e resultados de Visão estruturados.

## Alterações para 2.9

- **Adicionadas traduções em Francês e Turco.**
- **Visualização Formatada:** Adicionado um botão "Visualizar Formatado" nas caixas de diálogo de chat para visualizar a conversa com a estilização adequada (Cabeçalhos, Negrito, Código) numa janela de navegação padrão.
- **Configuração de Markdown:** Adicionada uma nova opção "Limpar Markdown no Chat" nas Definições. Desmarcar isso permite que os utilizadores vejam a sintaxe bruta do Markdown (por exemplo, `**`, `#`) na janela de chat.
- **Gerenciamento de Diálogos:** Corrigido um problema onde as janelas de "Refinar Texto" ou de chat abriam várias vezes ou falhavam em focar corretamente.
- **Melhorias de UX:** Padronizados os títulos das caixas de diálogo de ficheiro para "Abrir" e removidos anúncios de fala redundantes (por exemplo, "Abrindo menu...") para uma experiência mais suave.

## Alterações para 2.8

- Adicionada tradução em Italiano.
- **Relatório de Status:** Adicionado um novo comando (NVDA+Control+Shift+I) para anunciar o status atual do suplemento (por exemplo, "Enviando...", "Analisando...").
- **Exportação em HTML:** O botão "Salvar Conteúdo" nas caixas de diálogo de resultado agora salva a saída como um arquivo HTML formatado, preservando estilos como cabeçalhos e texto em negrito.
- **UI de Definições:** Layout do painel de Definições aprimorado com agrupamento acessível.
- **Novos Modelos:** Adicionado suporte para gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado Nepalês aos idiomas suportados.
- **Lógica do Menu Refinar:** Corrigido um bug crítico onde os comandos de "Refinar Texto" falhavam se o idioma da interface do NVDA não fosse o inglês.
- **Ditado:** Detecção de silêncio aprimorada para evitar saídas de texto incorretas quando nenhuma fala for inserida.
- **Configurações de Atualização:** "Verificar atualizações na inicialização" agora vem desativado por padrão para cumprir as políticas da Add-on Store.
- Limpeza de código.

## Alterações para 2.7

- Migrada a estrutura do projeto para o Modelo de Suplemento oficial da NV Access para melhor conformidade com as normas.
- Implementada lógica de repetição automática para erros HTTP 429 (Limite de Taxa) para garantir confiabilidade durante alto tráfego.
- Pedidos de tradução otimizados para maior precisão e melhor manuseio da lógica de "Troca Inteligente" (Smart Swap).
- Atualizada a tradução em Russo.

## Alterações para 2.6

- Adicionado suporte à tradução em Russo (Agradecimentos ao nvda-ru).
- Mensagens de erro atualizadas para fornecer feedback mais descritivo sobre a conectividade.
- Alterado o idioma de destino padrão para o Inglês.

## Alterações para 2.5

- Adicionado Comando de OCR de Ficheiro Nativo (NVDA+Control+Shift+F).
- Adicionado botão "Salvar Chat" às caixas de diálogo de resultado.
- Implementado suporte completo a localização (i18n).
- Migrado o feedback de áudio para o módulo de tons nativos do NVDA.
- Alterado para a API de Ficheiros do Gemini para melhor manipulação de ficheiros PDF e de áudio.
- Corrigido travamento ao traduzir textos contendo chaves.

## Alterações para 2.1.1

- Corrigido um problema onde a variável [file_ocr] não estava funcionando corretamente dentro de Pedidos Personalizados.

## Alterações para 2.1

- Padronizados todos os atalhos para usar NVDA+Control+Shift para eliminar conflitos com o layout de Laptop do NVDA e teclas de atalho do sistema.

## Alterações para 2.0

- Implementado sistema de Atualização Automática embutido.
- Adicionado Cache de Tradução Inteligente para recuperação instantânea de textos traduzidos anteriormente.
- Adicionada Memória de Conversa para refinar contextualmente os resultados em caixas de diálogo de chat.
- Adicionado comando Dedicado de Tradução da Área de Transferência (NVDA+Control+Shift+Y).
- Pedidos de IA otimizados para forçar estritamente a saída no idioma de destino.
- Corrigido travamento causado por caracteres especiais no texto de entrada.

## Alterações para 1.5

- Adicionado suporte para mais de 20 novos idiomas.
- Implementada Caixa de Diálogo Interativa de Refinamento para perguntas de acompanhamento.
- Adicionado recurso de Ditado Inteligente Nativo.
- Adicionada a categoria "Vision Assistant" à caixa de diálogo de Gestos de Entrada do NVDA.
- Corrigidos travamentos por COMError em aplicativos específicos como Firefox e Word.
- Adicionado mecanismo de repetição automática para erros de servidor.

## Alterações para 1.0

- Lançamento inicial.
