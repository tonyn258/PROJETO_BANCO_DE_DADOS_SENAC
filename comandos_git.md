# Guia Git - Projeto Banco de Dados SENAC

## 1. Enviar alterações para o GitHub

Verifique o status do repositório:

```bash
git status
```

Adicionar todas as alterações:

```bash
git add .
```

Criar um commit:

```bash
git commit -m "Atualização do projeto"
```

Enviar para o GitHub:

```bash
git push origin master
```

---

## 2. Baixar (clonar) o projeto em outro computador

Abra o terminal do VS Code e navegue até a pasta onde deseja salvar o projeto:

```bash
cd "C:\Users\tonyn\OneDrive - SENAC em Minas - EDU\Documentos"
```

Clone o repositório:

```bash
git clone https://github.com/tonyn258/PROJETO_BANCO_DE_DADOS_SENAC.git
```

Entre na pasta do projeto:

```bash
cd PROJETO_BANCO_DE_DADOS_SENAC
```

Abra o projeto no VS Code:

```bash
code .
```

---

## 3. Atualizar o projeto com as últimas alterações do GitHub

Dentro da pasta do projeto, execute:

```bash
git pull origin master
```

---

## 4. Verificar a branch atual

```bash
git branch
```

---

## 5. Ver histórico de commits

```bash
git log --oneline -5
```
