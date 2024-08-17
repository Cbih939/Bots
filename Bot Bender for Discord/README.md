# Discord Bot Documentation

**Desenvolvedor:** Cbih936

---

## Visão Geral

Este bot foi desenvolvido para ser utilizado em servidores do Discord, permitindo a automação de tarefas específicas, como o envio de mensagens privadas para os membros, exceto aqueles com cargos administrativos.

## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:** 
  - `discord.py`: Utilizada para interação com a API do Discord.
  - `logging`: Para monitoramento e registro de atividades do bot.

## Configuração

1. **Token de Acesso**
   - Substitua `'YOUR_TOKEN_KEY_HERE'` pelo token do seu bot. O token é obtido na [Developer Portal do Discord](https://discord.com/developers/applications).

2. **Intents**
   - Os intents configuram as permissões que o bot terá, como visualizar membros e acessar o conteúdo das mensagens. É essencial ativar essas permissões tanto no código quanto na configuração do bot na Developer Portal.

3. **Prefixo de Comando**
   - O bot está configurado para usar `!` como prefixo dos comandos. Isso significa que todos os comandos deverão ser precedidos por `!`.

## Funcionalidades

- **Conexão do Bot**
  - Quando o bot se conecta ao Discord, uma mensagem é registrada no log, confirmando que ele está ativo.

- **Comando: `!send_message`**
  - **Descrição:** Envia uma mensagem privada para todos os usuários no servidor, exceto aqueles que possuem cargos administrativos.
  - **Uso:** `!send_message [mensagem]`
  - **Parâmetros:**
    - `mensagem`: A mensagem que será enviada a todos os membros (exceto administradores).
  - **Restrições:**
    - O comando só pode ser executado dentro de um servidor.
    - Usuários com cargos como "admin", "moderador", "administrator", ou "mod" serão ignorados.

## Exemplo de Uso

Para enviar uma mensagem de boas-vindas a todos os membros (exceto administradores):

```bash
!send_message Bem-vindos ao servidor! Estamos felizes em tê-los aqui.
