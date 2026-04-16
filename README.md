# 📦 Sistema de Gestão de Inventário (Python)

Um sistema robusto via linha de comando para controle de produtos, sessões e validades, focado na organização modular e facilidade de manutenção.

## ✨ Funcionalidades
* **Gerenciamento de Produtos**: Cadastro (com geração automática de código), listagem, pesquisa e atualização.
* **Categorização**: Atribuição de produtos a sessões específicas (Ex: Limpeza, Alimentos).
* **Controle de Qualidade**: Registro de datas de validade e sistema de checagem automática para descarte de produtos vencidos.
* **Fluxo de Venda**: Integração com módulo de vendas para controle de saída de estoque.
* **Interface Modular**: Organização em múltiplos arquivos (.py) para garantir a separação de responsabilidades.

## 🏗️ Arquitetura do Sistema
O projeto é dividido nos seguintes módulos:
- `produtos.py`: Núcleo do sistema, gerencia o dicionário principal e o CRUD básico.
- `sessão.py`: Gerencia a atribuição de categorias aos produtos.
- `validacao.py`: Lógica para geração de validades e verificação de integridade dos produtos.
- `main.py`: Ponto de entrada da aplicação com menu interativo.

## 🛠️ Tecnologias
* **Python 3.x**
* **Módulo `random`**: Utilizado para geração de códigos e datas de teste.

## 🚀 Como testar
1. Certifique-se de ter o Python instalado.
2. Baixe os arquivos do repositório em uma única pasta.
3. Execute o arquivo principal:
   ```bash
   python main.py
