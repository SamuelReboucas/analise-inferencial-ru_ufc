Aceitação de Preparações Vegetarianas versus Preparações à Base de Carne
nos RUs da UFC — Disciplina: Análise Inferencial, 2026

OBJETIVO
--------
Comparar estatisticamente a aceitação de preparações vegetarianas
e preparações à base de carne nos Restaurantes Universitários da
UFC, com base nos registros do Sistema RU (janeiro–junho de 2026).

ARQUIVOS
--------
  2026 Sistema RU (2).xlsx  → base original do Sistema RU
  analise_ru.py             → script Python da análise
  relatorio_final.pdf       → documento principal para avaliação
  relatorio_final.md        → relatório em Markdown
  base_tratada.xlsx         → base após limpeza
  resultados_tabelas.xlsx   → tabelas descritivas (4 abas)
  pares_contextuais.xlsx    → pares usados no teste t
  graficos/                 → gráficos gerados pelo script

COMO RODAR
----------
Coloque o arquivo "2026 Sistema RU (2).xlsx" na mesma pasta do script.

  pip install pandas numpy matplotlib seaborn scipy statsmodels openpyxl
  python analise_ru.py

Os arquivos de resultado são gerados em resultados/ e graficos/.

PARÂMETROS ESTATÍSTICOS
------------------------
  Nível de confiança : 95%  (z = 1,96)
  Margem de erro     : 5 pp
  Alpha              : 0,05
  Análise principal  : teste t pareado (contexto: Data × Refeitório × Refeição)
  Análise secundária : teste z de duas proporções

RESULTADOS PRINCIPAIS
----------------------
  Base final: 3.330 registros (66 zeros sem preenchimento removidos)
  Vegetariana: 1.114  |  Carne: 2.216

  Nota média Vegetariana : 7,7655
  Nota média Carne       : 7,6421
  Diferença pareada      : +0,1164  |  IC 95%: [+0,0699; +0,1629]
  t = 4,9145  |  gl = 688  |  p-valor = 0,00000111

  Prop. satisfatória Veg  : 91,29%
  Prop. satisfatória Carne: 84,66%
  Diferença: +6,64 pp  |  IC 95%: [+4,40 pp; +8,87 pp]
  z = 5,3508  |  p < 0,001

  Obs: Porangabussu é o único refeitório onde carne supera levemente
  vegetariana — não está claro se é padrão ou flutuação do período.
