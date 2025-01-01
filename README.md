# E-commerce Data Pipeline

## Descrição
Este projeto simula um pipeline de dados para análise de vendas de um e-commerce. Ele abrange desde a geração de dados fictícios até o processamento e análise usando Apache Spark, PostgreSQL e Python.

## Funcionalidades
- Geração de dados fictícios de clientes, produtos e vendas.
- Processamento de dados usando Apache Spark.
- Armazenamento em banco de dados relacional.
- Análise de dados com SQL e Python.

## Tecnologias Utilizadas
- Python
- Apache Spark
- PostgreSQL
- Docker

## Estrutura do Projeto
```
ecommerce-data-pipeline/
├── data/                # Dados brutos simulados
├── scripts/             # Scripts Python
├── notebooks/           # Notebooks para visualização
├── airflow_dag/         # Pipeline Airflow (opcional)
├── Dockerfile           # Configuração de ambiente
├── requirements.txt     # Dependências
├── README.md            # Documentação
```

## Como Executar
1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Gere os dados simulados:**
   ```bash
   python scripts/data_generator.py
   ```

3. **Processe os dados com Spark:**
   ```bash
   python scripts/data_processing.py
   ```

4. **Configure o banco de dados:**
   - Execute o script SQL `scripts/db_setup.sql` para criar as tabelas.

5. **Carregue e analise os dados:**
   - Use `scripts/data_analysis.py` para realizar consultas e gerar insights.

## Resultados e Insights
- Produtos mais vendidos por categoria.
- Faturamento total por faixa etária dos clientes.
- Análise temporal de vendas.
