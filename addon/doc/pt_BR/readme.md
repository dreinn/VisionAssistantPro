# Documentação do Vision Assistant Pro

O **Vision Assistant Pro** é um assistente de IA multimodal avançado para o NVDA. Ele utiliza mecanismos de IA de classe mundial para fornecer leitura de tela inteligente, tradução, ditado por voz e análise de documentos.

_Este complemento foi lançado para a comunidade em homenagem ao Dia Internacional das Pessoas com Deficiência._

## 1. Configuração

Vá para o **Menu NVDA > Preferências > Configurações > Vision Assistant Pro**.

### 1.1 Configurações de Conexão

- **Provedor:** Selecione seu serviço de IA preferido. Os provedores suportados incluem **Google Gemini**, **OpenAI**, **Mistral**, **Groq**, **MiniMax** e **Personalizado** (servidores compatíveis com OpenAI como Ollama, LM Studio, Jan.ai ou KoboldCPP).
- **Nota Importante:** Recomendamos fortemente o uso do **Google Gemini** para obter o melhor desempenho e precisão (especialmente para análise de imagens e arquivos).
- **Chave de API (API Key):** Obrigatória. Você pode inserir várias chaves (separadas por vírgulas ou quebras de linha) para rotação automática.
- **Buscar Modelos (Fetch Models):** Após inserir sua chave de API, pressione este botão para baixar a lista mais recente de modelos disponíveis do provedor.
- **Modelo de IA:** Selecione o modelo principal usado para chat geral e análise.

### 1.2 Roteamento Avançado de Modelos

_Disponível para todos os provedores, incluindo Gemini, OpenAI, Groq, Mistral e Personalizado._

> **⚠️ Aviso:** Estas configurações são destinadas **apenas para usuários avançados**. Se você não tiver certeza do que um modelo específico faz, deixe esta opção **desmarcada**. Selecionar um modelo incompatível para uma tarefa (por exemplo, um modelo apenas de texto para Visão) causará erros e fará o complemento parar de funcionar.

Marque **"Roteamento Avançado de Modelos (Específico por tarefa)"** para liberar o controle detalhado. Isso permite que você selecione modelos específicos da lista suspensa para diferentes tarefas:

- **Modelo de OCR / Visão:** Escolha um modelo especializado para analisar imagens.
- **Conversão de Fala em Texto (STT):** Escolha um modelo específico para ditado.
- **Conversão de Texto em Fala (TTS):** Escolha um modelo para gerar áudio.
- **Modelo de Operador de IA:** Selecione um modelo específico para tarefas de operação autônoma do computador.
_Nota: Recursos não suportados (por exemplo, TTS para o Groq) serão ocultados automaticamente._

### 1.3 Configuração Avançada de Endpoint (Provedor Personalizado)

*Disponível apenas quando "Personalizado" estiver selecionado._

> **⚠️ Aviso:** Esta seção permite a configuração manual da API e foi projetada para **usuários avançados** que executam servidores locais ou proxies. URLs ou nomes de modelos incorretos quebrarão a conectividade. Se você não sabe exatamente o que são esses endpoints, mantenha esta opção **desmarcada**.

Marque **"Configuração Avançada de Endpoint"** para inserir manualmente os detalhes do servidor. Ao contrário dos provedores nativos, aqui você deve **digitar** as URLs e os Nomes de Modelos específicos:

- **URL da Lista de Modelos:** O endpoint para buscar os modelos disponíveis.
- **URL do Endpoint de OCR/STT/TTS:** URLs completas para serviços específicos (por exemplo, `http://localhost:11434/v1/audio/speech`).
- **Modelos Personalizados:** Digite manualmente o nome do modelo (por exemplo, `llama3:8b`) para cada tarefa.

### 1.3.1 Configurar IA Local (Configuração em Uma Ação)

Para tornar a integração de IA local e completamente offline extremamente simples, um botão dedicado **"Configurar IA Local"** está disponível dentro das Configurações do Provedor Personalizado.

Se você estiver executando um servidor de modelo de IA local no seu computador:

1. Selecione **Personalizado** como seu Provedor.
2. Pressione o botão **Configurar IA Local**.
3. Escolha seu mecanismo de IA local na caixa de diálogo acessível:
   - **Ollama** (padrão para `http://127.0.0.1:11434`)
   - **LM Studio** (padrão para `http://127.0.0.1:1234`)
   - **Jan.ai** (padrão para `http://127.0.0.1:1337`)
   - **KoboldCPP** (padrão para `http://127.0.0.1:5001`)
4. O complemento configurará instantaneamente a URL local correta, o tipo de API e buscará automaticamente seus modelos offline ativos para preencher a caixa de seleção **Modelo de IA**.

_Nota sobre Rede e Proxies:_ Este mecanismo de conexão local possui um sistema avançado de desvio de proxy. Mesmo que você esteja usando uma VPN ativa no sistema ou um proxy em modo TUN, suas requisições de IA locais os ignorarão completamente, garantindo conexões offline estáveis sem erros do tipo 502 Bad Gateway.

### 1.4 Preferências Gerais

- **Mecanismo de OCR:** Escolha entre **Chrome (Rápido)** para resultados rápidos ou **IA (Avançado)** para uma preservação superior do layout.
  - _Nota:_ Se você selecionar "IA (Avançado)", mas seu provedor estiver definido como OpenAI/Groq, o complemento roteará inteligentemente a imagem para o modelo de visão do seu provedor ativo.
- **Voz do TTS:** Selecione seu estilo de voz preferido. Esta lista é atualizada dinamicamente com base no seu provedor ativo.
- **Criatividade (Temperatura):** Controla a aleatoriedade da IA. Valores mais baixos são melhores para traduções/OCR precisos.
- **URL do Proxy:** Configure se os serviços de IA estiverem restritos na sua região (suporta proxies locais como `127.0.0.1` ou URLs de ponte).

## 2. Camada de Comando e Atalhos

Para evitar conflitos de teclado, este complemento usa uma **Camada de Comando**.

1. Pressione **NVDA + Shift + V** (Tecla Mestra) para ativar a camada (você ouvirá um bipe).
2. Solte as teclas e, em seguida, pressione uma das seguintes teclas individuais:

| Tecla         | Função                         | Descrição                                                                                                                                |
| ------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Shift + A** | **Operador de IA**             | **Operação Autônoma:** Diga à IA para realizar uma tarefa na sua tela. Pressionar novamente aborta instantaneamente as operações ativas. |
| **E**         | **Explorador de IU**           | **Clique Interativo:** Identifica e clica em elementos de interface em qualquer aplicativo.                                              |
| **T**         | Tradutor Inteligente           | Traduz o texto sob o cursor do navegador ou a seleção.                                                                                   |
| **Shift + T** | Tradutor de Área de Transf.    | Traduz o conteúdo que está atualmente na área de transferência.                                                                          |
| **R**         | Refinador de Texto             | Resume, corrige a gramática, explica ou executa **Comandos Personalizados**.                                                             |
| **V**         | Visão de Objeto                | Descreve o objeto atual do navegador.                                                                                                    |
| **O**         | Visão em Tela Cheia            | Analisa o layout e o conteúdo de toda a tela.                                                                                            |
| **Shift + V** | Análise de Vídeo Online        | Analisa vídeos do **YouTube**, **Instagram**, **TikTok** ou **Twitter (X)**.                                                             |
| **D**         | Leitor de Documentos           | Leitor avançado para PDF e imagens com seleção de intervalo de páginas.                                                                  |
| **F**         | **Ação de Arquivo Intel.**     | Reconhecimento contextual de arquivos de imagem, PDF ou TIFF selecionados.                                                               |
| **A**         | Transcrição de Áudio           | Transcreve arquivos MP3, WAV ou OGG em texto.                                                                                            |
| **C**         | Solucionador de CAPTCHA        | Captura e resolve CAPTCHAs (Suporta portais governamentais).                                                                             |
| **S**         | Ditado Inteligente             | Converte fala em texto. Pressione para iniciar a gravação, e novamente para parar/digitar.                                               |
| **Control+L** | **Assistente ao Vivo**         | **Copiloto em tempo real (apenas Gemini):** Inicia ou encerra uma conversa ao vivo por voz e tela com o assistente de IA.                |
| **I**         | Relatório de Status            | Anuncia o progresso atual (por exemplo, "Escaneando...", "Inativo").                                                                     |
| **L**         | **Rotular Objeto**             | **Rotulagem Semântica por IA:** Rotula permanentemente o elemento/ícone focado atual.                                                    |
| **Shift + L** | **Gerenciar/Escanear Rótulos** | Abre o Gerenciador de Rótulos (se houver rótulos) ou escaneia o app em busca de elementos sem nome.                                      |
| **U**         | Verificar Atualização          | Verifica manualmente o GitHub em busca da versão mais recente do complemento.                                                            |
| **Espaço**    | Relembrar Último Resultado     | Mostra a última resposta da IA em uma caixa de diálogo de chat para revisão ou acompanhamento.                                           |
| **H**         | Ajuda de Comandos              | Exibe uma lista de todos os atalhos disponíveis.                                                                                         |

### 2.1 Atalhos do Leitor de Documentos (Dentro do Visualizador)

- **Ctrl + PageDown:** Move para a próxima página.
- **Ctrl + PageUp:** Move para a página anterior.
- **Alt + A:** Abre uma caixa de diálogo de chat para fazer perguntas sobre o documento.
- **Alt + R:** Força um **Re-escaneamento com IA** usando seu provedor ativo.
- **Alt + G:** Gera e salva um arquivo de áudio de alta qualidade (WAV/MP3). _Oculto se o provedor não suportar TTS._
- **Alt + S / Ctrl + S:** Salva o texto extraído como um arquivo TXT ou HTML.

## 3. Operador de IA - Controle Autônomo de Computador

O **Operador de IA** transforma o Vision Assistant Pro de um leitor passivo em um assistente ativo que pode interagir com o computador em seu nome. Você pode pedir para ele descrever a tela, responder a perguntas sobre o que ele está vendo ou até mesmo assumir o controle — clicando em botões, arrastando itens, digitando textos e navegando pelos aplicativos usando comandos em linguagem natural.

A maior vantagem? Ele funciona perfeitamente em softwares completamente inacessíveis. Se você estiver travado em um aplicativo personalizado, em uma área de trabalho remota ou em um site onde o seu leitor de tela fica totalmente silencioso, o operador não se importa. Como ele "vê" a tela visualmente, ele consegue encontrar, ler e interagir com elementos que possuem zero rótulos de acessibilidade.

### Como Funciona

1. Pressione **NVDA + Shift + V** e, em seguida, pressione **Shift + A** (oi use o atalho direto) para abrir a caixa de diálogo do Operador de IA.
2. Digite o que você deseja fazer em linguagem simples (por exemplo, "Clique no botão Salvar", "O que diz a mensagem de erro?" ou "Renomeie o arquivo para final.pdf").
3. A IA analisará sua tela, identificará os elementos relevantes e executará a ação ou fornecerá a resposta. Se uma tarefa exigir várias etapas, o operador continuará trabalhando até que ela seja concluída.
4. Pressione **Shift + A** novamente a qualquer momento para abortar instantaneamente uma operação em andamento.

### Ações Suportadas

O operador compreende uma ampla variedade de comandos:

- **Descrever e Responder**: "Descreva o layout da tela" ou "O que diz a mensagem de erro?"
- **Clicar**: "Clique no botão Salvar"
- **Clique com o Botão Direito**: "Clique com o botão direito no arquivo"
- **Clique Duplo**: "Clique duas vezes no documento"
- **Arrastar e Soltar**: "Arraste o documento para a pasta Arquivo"
- **Digitar**: "Digite 'Olá Mundo' na caixa de pesquisa"
- **Rolar**: "Role para baixo três vezes"
- **Pressionar Teclas**: "Pressione Enter", "Pressione Tab", "Pressione Escape"
- **Tarefas de Várias Etapas**: "Abra o Explorador de Arquivos, encontre o relatório e renomeie-o para final.pdf"

### Notas Importantes

- **⚠️ Aviso de Uso da API**: Como o operador precisa "ver" exatamente o que está acontecendo na tela, ele envia uma captura de tela em alta resolução a cada etapa. O uso frequente consumirá sua cota de API muito mais rápido do que os recursos padrão baseados em texto.
- **Aplicativos em Modo Administrador**: Se o NVDA não estiver sendo executado com privilégios de Administrador, o operador poderá não conseguir interagir com janelas que exigem permissões elevadas. Esta é uma limitação de segurança do Windows, não um bug no complemento.
- **Boas Práticas**: Para obter os melhores resultados, dê comandos claros e específicos. "Clique no botão azul Enviar na parte inferior do formulário" quase sempre funcionará melhor do que apenas "Clique no botão".

## 4. Comandos Personalizados e Variáveis

Você pode gerenciar seus comandos em **Configurações > Comandos > Gerenciar Comandos...**.

### Variáveis Suportadas

- `[selection]`: Texto selecionado atualmente.
- `[clipboard]`: Conteúdo da área de transferência.
- `[screen_obj]`: Captura de tela do objeto do navegador.
- `[screen_fg_obj]`: Captura de tela da janela ativa em primeiro plano.
- `[screen_full]`: Captura de tela da tela cheia.
- `[file_ocr]`: Selecionar arquivo de imagem/PDF para extração de texto.
- `[file_read]`: Selecionar documento para leitura (TXT, Código, PDF).
- `[file_audio]`: Selecionar arquivo de áudio para análise (MP3, WAV, OGG).

***
**Nota:** Uma conexão de internet ativa é necessária para todos os recursos de IA. Documentos de várias páginas são processados automaticamente.

## 5. Suporte e Comunidade

Fique atualizado com as últimas notícias, recursos e lançamentos:

- **Canal do Telegram:** [t.me/VisionAssistantPro](https://t.me/VisionAssistantPro)
- **Problemas no GitHub (GitHub Issues):** For bug reports and feature requests.

## 6. Apoiadores do Projeto

Um agradecimento sincero aos membros da nossa comunidade que apoiam o desenvolvimento contínuo e a manutenção deste projeto através de suas generosas contribuições financeiras:

- **@Alyabani94**
- **Ali Alamri**
- **Ilya**
- **Apoiador Anônimo** (`UQDd...CnMY`)
- **leonardo0216**
- **Sergei Fleytin**

_Se você deseja apoiar o projeto financeiramente e ver seu nome aqui, você pode encontrar a opção **Doar** no menu Ferramentas do NVDA (submenu Vision Assistant) ou durante o processo de configuração após a instalação._

## Alterações para 7.0.0

- **Retomada de Verificações Inacabadas**: Adicionado um recurso de retomada tanto para o Leitor de Documentos quanto para as Ações de Arquivo Inteligentes. Se um escaneamento for interrompido, agora você pode continuar de onde ele parou em vez de começar do zero.
- **Nova Variável `[screen_fg_obj]`**: Adicionada uma variável de comando personalizado para capturar uma captura de tela apenas da janela ativa em primeiro plano, em vez de toda a tela.
- **Tentativas Inteligentes e Rotação de Chaves**: O complemento agora repete silenciosamente a operação até 5 vezes na mesma chave ao encontrar sobrecargas temporárias no servidor (como "alta demanda" ou respostas malformadas). Se as tentativas falharem, ele muda automaticamente para a próxima chave de API da sua lista.
- **Detecção de Cortina de Tela**: Adicionada uma verificação para evitar capturas de tela quando a Cortina de Tela estiver ativa (seja permanentemente ativada ou alternada temporariamente pelo atalho). O sistema emitirá um aviso e interromperá a ação, evitando que você envie imagens pretas e desperdice tokens de API.
- **Ajustes no Leitor de Documentos**: A caixa de diálogo de intervalo do PDF agora pré-seleciona automaticamente o idioma de destino padrão das configurações do seu complemento. Também foi aprimorado o gerenciamento de threads para garantir que as tarefas em segundo plano parem de forma limpa quando o leitor for fechado.
- **Integração Nativa de OCR do Mistral**: Integrada a API nativa de OCR de Documentos do Mistral. Documentos com várias páginas são mesclados, enviados e processados automaticamente em lotes usando o endpoint especializado `/v1/ocr` do Mistral, enquanto imagens de página única são processadas diretamente sem conversões desnecessárias para PDF.
- **Manipuladores Dinâmicos de URL Personalizada**: Modificar a URL de API Personalizada agora limpa instantaneamente a lista de modelos em cache e restaura a caixa de texto para inserção manual de modelos. Isso garante total compatibilidade com endpoints personalizados (como o Cloudflare AI Gateway) que não suportam o endpoint padrão de listagem `/v1/models`.
- **Reformulação do Motor de Entrada do Operador de IA**: O sistema subjacente de simulação de mouse e teclado para o Operador de IA foi completamente reconstruído. A API herdada `mouse_event` foi substituída pela moderna API `SendInput` do Windows, trazendo uma compatibilidade significativamente maior com aplicativos modernos, janelas protegidas por UAC e telas de alta densidade de pixels (high-DPI).
- **Correção nas Operações de Arrastar e Soltar**: As ações de arrastar e soltar no Operador de IA agora estão totalmente estáveis e confiáveis. O novo motor utiliza curvas naturais de suavização ("easing"), posicionamento preciso do cursor, temporização otimizada e uma técnica inteligente de "toque leve" para garantir que o Windows e os aplicativos reconheçam e executem corretamente os gestos de arrastar e soltar sem falhar no meio do caminho.
- **Suporte a Múltiplos Monitores**: O Operador de IA agora suporta totalmente configurações com múltiplos monitores. Os movimentos e cliques do mouse funcionam corretamente em todos os monitores usando a flag `MOUSEEVENTF_VIRTUALDESK`, garantindo o posicionamento preciso independentemente de em qual monitor o aplicativo de destino esteja.
- **Simulação de Teclado Aprimorada**: Injeção de teclas aprimorada para suportar totalmente as "Teclas Estendidas" (como as setas do teclado, Home, End, Page Up/Down, Insert, Delete e F1-F12). Isso garante que os comandos de navegação e atalhos enviados pelo Operador de IA funcionem perfeitamente em todos os aplicativos.
- **Suporte a Imagens HEIC/HEIF**: Adicionado suporte nativo para formatos de fotos do iPhone. Agora você pode selecionar diretamente arquivos `.heic` e `.heif` para descrição por IA, OCR ou Leitura de Documentos sem necessidade de conversão prévia.

## Alterações para 6.5.0

- **Assistente ao Vivo**: Adicionado um recurso de assistente de voz e tela em tempo real, disponível exclusivamente para o provedor Google Gemini (isso inclui provedores personalizados compatíveis com o Gemini). Inclui personalização interativa de voz e profundidade de raciocínio diretamente na caixa de diálogo, com reconexão automática ao alterar as configurações.
- **Provedor de IA MiniMax**: Integrado o MiniMax como um provedor de mesmo nível com suporte multimodal completo (chat, visão, OCR), TTS personalizado usando mais de 300 vozes dinâmicas e remoção automática de blocos de raciocínio (ex: `<think>...</think>`) dos resultados.
- **Tradução no Visualizador de Documentos**: Corrigida uma falha silenciosa de tradução para usuários do NVDA que não utilizam o idioma inglês, garantindo que o código de idioma padrão de 2 letras seja enviado ao Google Tradutor em vez do nome do idioma localizado.
- **Tentativa de Escaneamento em Lote de PDF**: Implementada uma lógica de repetição separada, altamente otimizada e silenciosa para o escaneamento em lote de documentos PDF, evitando uploads redundantes e janelas de erro perturbadoras durante as tentativas.
- **Status do Visualizador de Documentos**: Corrigido um bug onde o status geral do plugin (verificado através da tecla `I`) ficava travado em "Processamento em Lote Iniciado" durante escaneamentos de documentos longos.
- **Resolução de Travamento de Threads**: Corrigido um travamento grave de asserção de thread `IsMain() failed in wxTimerImpl` ao abrir documentos a partir de uma thread em segundo plano, transferindo a fila de chamadas da GUI para `wx.CallAfter`.

## Alterações para 6.1.2

- **Pré-verificação de Rótulos Duplicados**: Corrigido um problema na rotulagem individual onde a verificação de duplicatas usava chaves de coordenadas antigas, fazendo com que o NVDA fizesse requisições de IA duplicadas para objetos já rotulados em vez de anunciar o rótulo existente.
- **Chat de Documentos para Provedores Não-Gemini**: Corrigida uma verificação estrita de chave de API no Chat de Documentos (`on_ask`) para garantir que os usuários do OpenAI, Groq ou de provedores personalizados locais (como o Ollama) possam conversar com documentos com sucesso sem serem bloqueados.
- **Tradução Rápida de OCR do Chrome**: Restaurada a API de tradução gratuita e sem necessidade de chave para o OCR do Chrome. A tradução do texto extraído agora ignora a IA do Gemini, economizando cotas de API e acelerando o processo de tradução.
- **Filtro Alfanumérico de CAPTCHA**: Corrigida a lógica de filtragem no solucionador de CAPTCHA para garantir que os caracteres não alfanuméricos sejam limpos adequadamente em todas as situações.
- **Atualização da Ajuda da Camada de Comando**: Corrigido o atalho de anúncio de status no menu de ajuda de `L` para `I`, e adicionados ambos os comandos de rotulagem (`L` e `Shift+L`) à lista.

## Alterações para 6.1.1

- **Correção de Saída de Raciocínio do Gemma 4**: Corrigido um problema com os modelos Gemma 4 onde todo o processo de pensamento interno era exibido como a resposta final, ou onde desativar o pensamento resultava em respostas vazias. O complemento agora isola e extrai corretamente apenas a resposta de texto limpa e final.
- **OCR em Lote a partir do Explorador de Arquivos**: Agora você pode selecionar várias fotos ou PDFs diretamente no Explorador de Arquivos do Windows e extrair texto ou analisá-los em lote. O complemento filtrará e processará automaticamente apenas os formatos de arquivo suportados.

## Alterações para 6.1.0

- **Integração Universal de IA Local (Configurar IA Local)**: Adicionado um novo botão **"Configurar IA Local"** nas Configurações do Provedor Personalizado. Os usuários agora podem configurar automaticamente motores de IA locais, incluindo **Ollama**, **LM Studio**, **Jan.ai** e **KoboldCPP** instantaneamente.
- **Desvio Inteligente de Proxy Local**: Reconstruída a lógica de conexão com um mecanismo avançado de desvio de proxy. O complemento agora é inteligente o suficiente para ignorar completamente os proxies do sistema Windows em conexões de loopback local, garantindo conexões estáveis com a IA local mesmo quando sua VPN ou modo TUN estiver ativo.
- **Rotulagem por IA Ultra-Estável (v2)**: Substituídas as chaves de coordenadas absolutas da tela por um sistema híbrido avançado de **Assinatura do Objeto**. Os rótulos agora dependem de identificadores programáticos (UIA **AutomationId** ou Win32 **ControlID**) e coordenadas relativas à janela, tornando seus rótulos personalizados completamente resistentes ao redimensionamento de janelas, movimentação, troca de monitor ou alteração na escala da tela.
- **Migração Automática de Rótulos Transparente**: A atualização é completamente transparente. O complemento migrará automaticamente seus rótulos legados baseados em coordenadas antigas para o novo formato de impressão digital estável em segundo plano no primeiro foco, com zero perda de dados.

## Alterações para 6.0

- **Apresentando a Rotulagem Semântica por IA**: Os usuários agora podem rotular permanentemente botões e ícones sem nome usando IA. Pressione **L** para rotular o objeto atual do navegador (suportando tanto o foco por Tab quanto a navegação de objetos) ou **Shift+L** para escanear e rotular todo o aplicativo de uma vez.
- **Gerenciamento Inteligente de Rótulos**: Adicionada uma nova caixa de diálogo do Gerenciador de Rótulos totalmente acessível (via **Shift+L** se os rótulos existirem) para visualizar, renomear ou excluir rótulos personalizados em lote.
- **Análise Direta de Arquivos (Ignorar Caixa de Diálogo de Arquivo)**: O complemento agora é inteligente o suficiente para detectar se você está focado em um arquivo PDF ou de imagem no Explorador de Arquivos do Windows. Pressionar **F (Ação de Arquivo Inteligente)** ou **D (Leitor de Documentos)** em um arquivo realçado irá processá-lo imediatamente, ignorando completamente a caixa de diálogo padrão "Abrir".

## Alterações para 5.6

- **Adicionado Mecanismo de OCR "Nenhum (Extrair Camada de Texto)"**: Os usuários agora podem extrair texto diretamente de PDFs pesquisáveis sem usar créditos de IA, melhorando significativamente a velocidade e a privacidade para documentos baseados em texto.
- **Precisão Refinada do Explorador de IU**: Aprimorado o comando do Explorador de IU para identificar melhor os tipos de elementos (como Itens de Lista) e relatar estados com precisão, tais como "(Marcado)", "(Selecionado)" ou "(Expandido)", ignorando componentes do sistema Windows como a Barra de Tarefas e o Relógio.
- **Lembrete de Configuração de Instalação**: Adicionada uma notificação após a instalação para guiar os usuários ao menu de configurações para configurar suas chaves de API e preferências.

## Alterações para 5.5.2

- **Correção de Problema de Digitação no Operador de IA:** Resolvido um bug onde a letra 'v' era digitada em vez de colar o texto em determinados sistemas. Esta correção aborda conflitos de temporização que ocorriam durante alta carga do sistema.
- **Estabilidade Aprimorada:** Adicionado um tratamento robusto de erros para operações de área de transferência para evitar travamentos do complemento quando a área de transferência do sistema estiver temporariamente bloqueada por outros aplicativos.
- **Otimização de Temporização:** Ajustados os atrasos internos para eventos de teclado para garantir maior confiabilidade em diferentes velocidades de sistema e melhor compatibilidade com Gerenciadores de Área de Transfêrencia de terceiros.

## Alterações para 5.5 (A Atualização de Automação)

- **Operador de IA (Controle Autônomo - Shift+A):** Esta é a joia da coroa da v5.5. O Vision Assistant Pro evoluiu de um assistente passivo para se tornar o seu **Operador de IA** pessoal. Ele não apenas descreve a tela — ele assume o comando.
  - _Como funciona:_ Agora você pode dar instruções verbais para operar seu PC. Por exemplo, em um aplicativo completamente inacessível onde seu leitor de tela permanece em silêncio, você pode pressionar **Shift+A** e digitar: _"Clique no botão Configurações"_ ou _"Encontre o campo de pesquisa, digite 'Últimas Notícias' e pressione enter."_ A IA identifica visualmente os elementos, move o mouse e executa a tarefa para você.
  - _Nota de Desempenho:_ Este recurso é otimizado para o **Gemini 3.0 Flash (Preview)**, entregando respostas incrivelmente rápidas e inteligentes que podem lidar até mesmo com os layouts de interface de usuário mais complexos.
  - **⚠️ Aviso de Uso da API:** Como o Operador de IA precisa "ver" exatamente o que está acontecendo para ser preciso, ele envia uma captura de tela em alta resolução a cada etapa. Por favor, note que o uso frequente consumirá sua cota de API muito mais rápido do que as tarefas padrão baseadas em texto.
- **Explorador de Interface de Usuário Visual (E):** Cansado de navegar por "botões sem rótulo"? Pressione **E** para ativar o Explorador de IU. A IA escaneará a janela inteira e gerará uma lista de cada elemento clicável que ela vê — incluindo ícones, gráficos e menus. Basta escolher um item da lista e o Operador de IA clicará nele para você. É como ter uma "camada acessível" por cima de qualquer aplicativo.
- **Ação de Arquivo Inteligente Sensível ao Contexto (F):** A tecla "F" foi completamente reformulada. Ela não pressupõe mais que você deseja apenas o OCR. Quando você seleciona uma única imagem, ela agora pergunta inteligentemente qual é a sua intenção: você pode escolher uma **Descrição Visual Detalhada** para entender a cena ou uma **Extração de Texto Estruturada (OCR)** para leitura. O menu se adapta dinamicamente com base no tipo de arquivo e no seu motor de IA ativo.
- **Otimização do Núcleo:** Realizamos uma limpeza profunda na lógica interna do complemento, removendo funções legadas não utilizadas e códigos redundantes. Isso resulta em uma experiência mais enxuta, rápida e confiável para todos os usuários.

## Alterações para 5.0

- **Arquitetura Multi-Provedor**: Adicionado suporte completo para **OpenAI**, **Groq** e **Mistral** junto ao Google Gemini. Os usuários agora podem escolher seu backend de IA preferido.
- **Roteamento Avançado de Modelos**: Usuários de provedores nativos (Gemini, OpenAI, etc.) agora podem selecionar modelos específicos de uma lista suspensa para diferentes tarefas (OCR, STT, TTS).
- **Configuração Avançada de Endpoint**: Usuários de provedores personalizados podem inserir manualmente URLs e nomes de modelos específicos para controle granular sobre servidores locais ou de terceiros.
- **Visibilidade Inteligente de Recursos**: O menu de configurações e a interface do Leitor de Documentos agora ocultam automaticamente recursos não suportados (como TTS) com base no provedor selecionado.
- **Busca Dinâmica de Modelos**: O complemento agora busca a lista de modelos disponíveis diretamente da API do provedor, garantindo compatibilidade com novos modelos assim que forem lançados.
- **OCR e Tradução Híbridos**: Otimizada lógicas para usar o Google Tradutor para maior velocidade ao usar o OCR do Chrome, e tradução baseada em IA ao usar os motores Gemini/Groq/OpenAI.
- **"Re-escanear com IA" Universal**: O recurso de re-escanear do Leitor de Documentos não está mais limitado ao Gemini. Ele agora utiliza qualquer provedor de IA que esteja ativo no momento para reprocessar as páginas.

## Alterações para 4.6

- **Reabertura Interativa de Resultados:** Adicionada a tecla **Espaço** à camada de comando, permitindo que os usuários reabram instantaneamente a última resposta da IA em uma janela de chat para perguntas de acompanhamento, mesmo quando o modo "Saída Direta" estiver ativo.

- **Hub da Comunidade no Telegram:** Adicionado um link para o "Canal Oficial do Telegram" no menu Ferramentas do NVDA, fornecendo uma maneira rápida de se manter atualizado com as últimas notícias, recursos e lançamentos.
- **Estabilidade de Resposta Aprimorada:** Otimizada a lógica central para os recursos de Tradução, OCR e Visão para garantir um desempenho mais confiável e uma experiência mais suave ao usar a saída de fala direta.
- **Orientação de Interface Aprimorada:** Atualizadas as descrições de configurações e documentação para explicar melhor o novo sistema de reabertura e como ele funciona junto com as configurações de saída direta.

## Alterações para 4.5

- **Gerenciador de Comandos Avançado:** Introduzida uma caixa de diálogo de gerenciamento dedicada nas configurações para personalizar os comandos padrão do sistema e gerenciar comandos definidos pelo usuário com suporte completo para adicionar, editar, reordenar e visualizar.

- **Suporte Abrangente a Proxy:** Resolvidos problemas de conectividade de rede garantindo que as configurações de proxy configuradas pelo usuário sejam estritamente aplicadas a todas as requisições de API, incluindo tradução, OCR e geração de fala.
- **Migração Automatizada de Dados:** Integrado um sistema de migração inteligente para atualizar automaticamente as configurações de comandos legados para um formato JSON v2 robusto na primeira execução, sem perda de dados.
- **Compatibilidade Atualizada (2025.1):** Definida a versão mínima exigida do NVDA para 2025.1 devido a dependências de biblioteca em recursos avançados como o Leitor de Documentos para garantir um desempenho estável.
- **Interface de Configurações Otimizada:** Simplificada a interface de configurações ao reorganizar o gerenciamento de comandos em uma caixa de diálogo separada, proporcionando uma experiência de usuário mais limpa e acessível.
- **Guia de Variáveis de Comando:** Adicionado um guia integrado nas caixas de diálogo de comandos para ajudar os usuários a identificar e usar facilmente variáveis dinâmicas como [selection], [clipboard] e [screen_obj].

## Alterações para 4.0.3

- **Maior Resiliência de Rede:** Adicionado um mecanismo de repetição automática para lidar melhor com conexões de internet instáveis e erros temporários de servidor, garantindo respostas de IA mais confiáveis.

- **Caixa de Diálogo Visual de Tradução:** Introduzida uma janela dedicada para resultados de tradução. Os usuários agora podem navegar e ler traduções longas facilmente linha por linha, de forma semelhante aos resultados de OCR.
- **Visualização Formatada Agregada:** O recurso "Visualizar Formatado" no Leitor de Documentos agora exibe todas as páginas processadas em uma única janela organizada com cabeçalhos de página claros.
- **Fluxo de Trabalho de OCR Otimizado:** Pula automaticamente a seleção de intervalo de páginas para documentos de página única, tornando o processo de reconhecimento mais rápido e contínuo.
- **Estabilidade de API Aprimorada:** Alterado para um método de autenticação baseado em cabeçalho mais robusto, resolvendo potenciais erros de "Todas as chaves de API falharam" causados por conflitos de rotação de chaves.
- **Correções de Bugs:** Resolvidos vários travamentos potenciais, incluindo um problema durante o encerramento do complemento e um erro de foco na caixa de diálogo de chat.

## Alterações para 4.0.1

- **Leitor de Documentos Avançado:** Um novo e poderoso visualizador para PDF e imagens com seleção de intervalo de páginas, processamento em segundo plano e navegação contínua através de `Ctrl+PageUp/Down`.

- **Novo Submenu de Ferramentas:** Adicionado um submenu dedicado "Vision Assistant" sob o menu Ferramentas do NVDA para acesso mais rápido aos recursos principais, configurações e documentação.
- **Customização Flexível:** Agora você pode escolher seu mecanismo de OCR preferido e a voz do TTS diretamente do painel de configurações.
- **Suporte a Múltiplas Chaves de API:** Adicionado suporte para múltiplas chaves de API do Gemini. Você pode inserir uma chave por linha ou separá-las com vírgulas nas configurações.
- **Mecanismo de OCR Alternativo:** Introduzido um novo mecanismo de OCR para garantir o reconhecimento confiável de texto mesmo ao atingir os limites de cota da API do Gemini.
- **Rotação Inteligente de Chaves de API:** Alterna automaticamente para a chave de API funcional mais rápida e a memoriza para contornar os limites de cota.
- **Documento para MP3/WAV:** Capacidade integrada para gerar e salvar arquivos de áudio de alta qualidade nos formatos MP3 (128kbps) e WAV diretamente dentro do leitor.
- **Suporte a Stories do Instagram:** Adicionada a capacidade de descrever e analisar Stories do Instagram usando suas URLs.
- **Suporte ao TikTok:** Introduzido suporte para vídeos do TikTok, permitindo descrição visual completa e transcrição de áudio dos clipes.
- **Caixa de Diálogo de Atualização Redesenhada:** Apresenta uma nova interface acessível com uma caixa de texto rolável para ler claramente as alterações da versão antes de instalar.
- **Status e UX Unificados:** Padronizadas as caixas de diálogo de arquivos em todo o complemento e aprimorado o comando 'L' para relatar o progresso em tempo real.

## Alterações para 3.6.0

- **Sistema de Ajuda:** Adicionado um comando de ajuda (`H`) dentro da Camada de Comando para fornecer uma lista de fácil acesso de todos os atalhos e suas funções.

- **Análise de Vídeo Online:** Expandido o suporte para incluir vídeos do **Twitter (X)**. Também foi aprimorada a detecção de URL e a estabilidade para uma experiência mais confiável.
- **Contribuição ao Projeto:** Adicionada uma caixa de diálogo opcional de doação para usuários que desejam apoiar as futuras atualizações e o crescimento contínuo do projeto.

## Alterações para 3.5.0

- **Camada de Comando:** Introduzido um sistema de Camada de Comando (padrão: `NVDA+Shift+V`) para agrupar atalhos sob uma única tecla mestra. Por exemplo, em vez de pressionar `NVDA+Control+Shift+T` para tradução, agora você pressiona `NVDA+Shift+V` seguido por `T`.

- **Análise de Vídeo Online:** Adicionado um novo recurso para analisar vídeos do YouTube e do Instagram diretamente fornecendo uma URL.

## Alterações para 3.1.0

- **Modo de Saída Direta:** Adicionada uma opção para ignorar a caixa de diálogo de chat e ouvir as respostas da IA diretamente via fala para uma experiência mais rápida e integrada.

- **Integração com a Área de Transferência:** Adicionada uma nova configuração para copiar automaticamente as respostas da IA para a área de transferência.

## Alterações para 3.0

- **Novos Idiomas:** Adicionadas traduções em **Persa** e **Vietnamita**.
- **Modelos de IA Expandidos:** Reorganizada a lista de seleção de modelos com prefixos claros (`[Free]`, `[Pro]`, `[Auto]`) para ajudar os usuários a distinguir entre modelos gratuitos e com limite de taxa (pagos). Adicionado suporte para o **Gemini 3.0 Pro** e **Gemini 2.0 Flash Lite**.
- **Estabilidade do Ditado:** Estabilidade do Ditado Inteligente significativamente aprimorada. Adicionada uma verificação de segurança para ignorar clipes de áudio com menos de 1 segundo, evitando alucinações da IA e erros vazios.
- **Manipulação de Arquivos:** Corrigido um problema onde o upload de arquivos com nomes que não estivessem em inglês falhava.
- **Otimização de Prompts:** Lógica de Tradução aprimorada e resultados de Visão estruturados.

## Alterações para 2.9

- **Adicionadas traduções em Francês e Turco.**
- **Visualização Formatada:** Adicionado um botão "Visualizar Formatado" nas caixas de diálogo de chat para visualizar a conversa com a estilização adequada (Cabeçalhos, Negrito, Código) em uma janela de navegação padrão.
- **Configuração de Markdown:** Adicionada uma nova opção "Limpar Markdown no Chat" nas Configurações. Desmarcar isso permite que os usuários vejam a sintaxe bruta do Markdown (por exemplo, `**`, `#`) na janela de chat.
- **Gerenciamento de Diálogos:** Corrigido um problema onde as janelas de "Refinar Texto" ou de chat abriam várias vezes ou falhavam em focar corretamente.
- **Melhorias de UX:** Padronizados os títulos das caixas de diálogo de arquivo para "Abrir" e removidos anúncios de fala redundantes (por exemplo, "Abrindo menu...") para uma experiência mais suave.

## Alterações para 2.8

- Adicionada tradução em Italiano.

- **Relatório de Status:** Adicionado um novo comando (NVDA+Control+Shift+I) para anunciar o status atual do complemento (por exemplo, "Enviando...", "Analisando...").
- **Exportação em HTML:** O botão "Salvar Conteúdo" nas caixas de diálogo de resultado agora salva a saída como um arquivo HTML formatado, preservando estilos como cabeçalhos e texto em negrito.
- **UI de Configurações:** Layout do painel de Configurações aprimorado com agrupamento acessível.
- **Novos Modelos:** Adicionado suporte para gemini-flash-latest e gemini-flash-lite-latest.
- **Idiomas:** Adicionado Nepalês aos idiomas suportados.
- **Lógica do Menu Refinar:** Corrigido um bug crítico onde os comandos de "Refinar Texto" falhavam se o idioma da interface do NVDA não fosse o inglês.
- **Ditado:** Detecção de silêncio aprimorada para evitar saídas de texto incorretas quando nenhuma fala for inserida.
- **Configurações de Atualização:** "Verificar atualizações na inicialização" agora vem desativado por padrão para cumprir as políticas da Add-on Store.
- Limpeza de código.

## Alterações para 2.7

- Migrada a estrutura do projeto para o Modelo de Complemento oficial da NV Access para melhor conformidade com as normas.

- Implementada lógica de repetição automática para erros HTTP 429 (Limite de Taxa) para garantir confiabilidade durante alto tráfego.
- Prompts de tradução otimizados para maior precisão e melhor manuseio da lógica de "Troca Inteligente" (Smart Swap).
- Atualizada a tradução em Russo.

## Alterações para 2.6

- Adicionado suporte à tradução em Russo (Agradecimentos ao nvda-ru).

- Mensagens de erro atualizadas para fornecer feedback mais descritivo sobre a conectividade.
- Alterado o idioma de destino padrão para o Inglês.

## Alterações para 2.5

- Adicionado Comando de OCR de Arquivo Nativo (NVDA+Control+Shift+F).

- Adicionado botão "Salvar Chat" às caixas de diálogo de resultado.
- Implementado suporte completo a localização (i18n).
- Migrado o feedback de áudio para o módulo de tons nativos do NVDA.
- Alterado para a API de Arquivos do Gemini para melhor manipulação de arquivos PDF e de áudio.
- Corrigido travamento ao traduzir textos contendo chaves.

## Alterações para 2.1.1

- Corrigido um problema onde a variável [file_ocr] não estava funcionando corretamente dentro de Comandos Personalizados.

## Alterações para 2.1

- Padronizados todos os atalhos para usar NVDA+Control+Shift para eliminar conflitos com o layout de Laptop do NVDA e teclas de atalho do sistema.

## Alterações para 2.0

- Implementado sistema de Atualização Automática embutido.

- Adicionado Cache de Tradução Inteligente para recuperação instantânea de textos traduzidos anteriormente.
- Adicionada Memória de Conversa para refinar contextualmente os resultados em caixas de diálogo de chat.
- Adicionado comando Dedicado de Tradução da Área de Transferência (NVDA+Control+Shift+Y).
- Prompts de IA otimizados para forçar estritamente a saída no idioma de destino.
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
