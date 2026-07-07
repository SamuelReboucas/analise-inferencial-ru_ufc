# Aceitação de Preparações Vegetarianas versus Preparações à Base de Carne nos Restaurantes Universitários da UFC

**Disciplina:** Análise Inferencial | **Instituição:** Universidade Federal do Ceará — UFC  
**Período analisado:** Janeiro a Junho de 2026

---

## 1. Introdução

Os Restaurantes Universitários (RUs) da Universidade Federal do Ceará (UFC) são espaços que oferecem refeições subsidiadas à comunidade acadêmica. Distribuídos em diferentes campi, os cinco refeitórios estudados — Benfica, Porangabussu, Pici 1, Pici 2 e Labomar — ofertam refeições de almoço e jantar, entre outras modalidades.

A inclusão de preparações vegetarianas de qualidade tem sido uma demanda crescente nas unidades de alimentação e nutrição (UAN) institucionais. A avaliação da aceitabilidade sensorial constitui um instrumento para orientar o planejamento do cardápio, identificar oportunidades de melhoria e subsidiar decisões de gestão.

Este trabalho investiga, com base nos registros de avaliação sensorial do Sistema RU da UFC ao longo do primeiro semestre de 2026, se há diferença estatisticamente significativa entre a aceitação de preparações vegetarianas e preparações à base de carne.

---

## 2. Justificativa

Essa comparação é relevante porque as decisões sobre frequência e composição do cardápio vegetariano dependem de evidências sobre a aceitabilidade real junto aos usuários — e não apenas de critérios nutricionais ou de custo. Além disso, a avaliação sensorial padronizada contribui para a gestão quando analisada com métodos estatísticos adequados, o que ajuda a transformar os registros do sistema em informações úteis para a tomada de decisão sobre o cardápio.

Há também um contexto mais amplo: diante do interesse crescente por padrões alimentares com menor consumo de proteína animal, importa verificar se as opções vegetarianas ofertadas têm boa aceitação entre os usuários — ou se a eventual ampliação desse cardápio poderia encontrar resistência.

---

## 3. Objetivos

### 3.1 Objetivo Geral

Comparar estatisticamente a aceitação média de preparações vegetarianas e de preparações à base de carne servidas nos Restaurantes Universitários da UFC durante o primeiro semestre de 2026.

### 3.2 Objetivos Específicos

1. Descrever o perfil de distribuição das notas de aceitação por grupo, refeitório e tipo de refeição;
2. Estimar pontualmente a nota média e a proporção de aceitação satisfatória para cada grupo;
3. Construir intervalos de confiança de 95% para a diferença entre médias e entre proporções;
4. Aplicar teste t pareado para verificar diferença significativa entre médias por contexto;
5. Aplicar teste de duas proporções como análise complementar;
6. Discutir a magnitude prática das diferenças e suas implicações para a gestão dos RUs.

---

## 4. População e Amostra

### 4.1 População de Interesse

Todas as avaliações sensoriais de preparações de Almoço e Jantar realizadas nos cinco Restaurantes Universitários da UFC, incluindo preparações vegetarianas (VEG) e preparações à base de carne (PB e PV), conforme a classificação adotada na base de dados do sistema.

### 4.2 Amostra Utilizada

A amostra é formada por **3.330 avaliações** extraídas da aba "Av. Sensorial" do Sistema RU, cobrindo o período de **5 de janeiro a 26 de junho de 2026**.

A base bruta possuía 6.147 registros. Foram mantidas apenas avaliações de Almoço e Jantar, excluindo-se o Café da manhã. Em seguida, foram selecionadas apenas as preparações VEG, PB e PV. Além disso, foram identificados **66 registros com Nota = 0** e ausência simultânea de preenchimento nos critérios sensoriais de aparência, textura, sabor, odor e avaliação global. Como esses casos indicam provável ausência de avaliação efetiva, foram removidos da base analítica para evitar distorção das médias e dos testes inferenciais. A amostra final resultou em **1.114 avaliações vegetarianas** e **2.216 avaliações de carne**.

> *Nota: a base constitui uma amostra por conveniência, não resultante de amostragem probabilística estrita. As inferências se aplicam ao período e contexto analisados.*

---

## 5. Variáveis Analisadas

| Variável | Tipo | Descrição |
|----------|------|-----------|
| Nota | Quantitativa contínua (0–10) | Nota global de aceitação sensorial |
| Grupo | Qualitativa nominal (2 cat.) | Vegetariana (VEG) ou Carne (PB + PV) |
| Refeição | Qualitativa nominal | Almoço ou Jantar |
| Refeitório | Qualitativa nominal (5 cat.) | Benfica, Porangabussu, Pici 1, Pici 2, Labomar |
| Aceitacao_satisfatoria | Binária (0/1) | 1 se Nota >= 7; 0 caso contrário |

---

## 6. Planejamento Amostral

Fórmula utilizada: n = z² · p(1-p) / E²

| Parâmetro | Valor | Justificativa |
|-----------|-------|---------------|
| Nível de confiança | 95% (z = 1,96) | Padrão para estudos descritivos |
| Margem de erro (E) | 0,05 (5 pp) | Precisão adequada para proporções |
| Proporção preliminar (p) | 0,5 | Caso conservador (maximiza n) |
| n mínimo calculado | 385 | — |
| n disponível | 3.330 | Supera o mínimo em 8,6x |

---

## 7. Metodologia

### 7.1 Fonte dos Dados

Os dados foram extraídos da aba "Av. Sensorial" da planilha *2026 Sistema RU.xlsx*. As avaliações disponíveis na base foram registradas por avaliadores identificados no sistema. As categorias PB e PV foram tratadas como preparações à base de carne, conforme a classificação adotada na base de dados.

### 7.2 Procedimento de Coleta de Dados

Os dados utilizados neste estudo são secundários e foram obtidos a partir da planilha do Sistema RU da UFC. A coleta original corresponde aos registros de avaliações sensoriais das preparações servidas nos Restaurantes Universitários. Para este trabalho, foi utilizada a aba "Av. Sensorial", considerando avaliações realizadas entre janeiro e junho de 2026. A análise foi restrita às refeições de almoço e jantar e às preparações classificadas como VEG, PB e PV, conforme os critérios definidos na metodologia. Não foi aplicado questionário primário; os dados são integralmente provenientes dos registros operacionais do sistema.

### 7.3 Tratamento dos Dados

A limpeza foi realizada em Python com `pandas` e `numpy`. As etapas foram: (1) filtrar refeições de Almoço e Jantar; (2) selecionar preparações VEG, PB e PV; (3) remover registros com nota ausente; (4) remover 66 registros com Nota = 0 e critérios sensoriais todos ausentes; (5) criar as variáveis `Grupo` e `Aceitacao_satisfatoria`.

### 7.4 Métodos Estatísticos

**Análise descritiva:** média, mediana, desvio padrão, quartis, mínimo e máximo por grupo; proporção de aceitação satisfatória.

**Análise principal — Teste t pareado:** a comparação pareada reduz a influência de diferenças operacionais entre dias, restaurantes e refeições, pois compara preparações dentro de um mesmo contexto de serviço. Para cada combinação de Data × Refeitório × Refeição, calculou-se a média vegetariana e a média de carne, obtendo-se a diferença d = Media_Veg − Media_Carne. O teste t pareado foi aplicado sobre as 689 diferenças resultantes.

**Análise secundária — Teste z de duas proporções:** comparação da proporção de avaliações com Nota >= 7 entre os grupos, como evidência complementar. A análise de proporções foi utilizada como evidência complementar. Como os registros possuem estrutura operacional e podem envolver repetições por data, RU, refeição ou avaliador, seus resultados devem ser interpretados com cautela e não substituem a análise pareada principal.

**Softwares:** Python 3.x com `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy` e `statsmodels`.

---

## 8. Resultados

### 8.1 Estatísticas Descritivas

**Tabela 1 — Estatísticas da Nota por Grupo**

| Grupo | N | Média | Mediana | DP | Mín. | Q1 | Q3 | Máx. |
|-------|---|-------|---------|-----|------|-----|-----|------|
| Vegetariana | 1.114 | 7,77 | 8,0 | 0,52 | 2,4 | 8,0 | 8,0 | 9,0 |
| Carne | 2.216 | 7,64 | 8,0 | 0,64 | 2,6 | 7,4 | 8,0 | 10,0 |

Ambos os grupos apresentam mediana de 8,0 e notas médias elevadas (acima de 7,6), indicando boa aceitação geral. O grupo vegetariano exibe média ligeiramente superior (7,77 vs. 7,64) e menor dispersão (DP = 0,52 vs. 0,64).

**Tabela 2 — Média da Nota por Refeitório e Grupo**

| Refeitório | Vegetariana | Carne |
|------------|-------------|-------|
| Benfica | 7,80 | 7,63 |
| Labomar | 7,82 | 7,63 |
| Pici 1 | 7,82 | 7,70 |
| Pici 2 | 7,91 | 7,63 |
| Porangabussu | 7,45 | 7,56 |

Em quatro dos cinco refeitórios, as preparações vegetarianas receberam nota média superior. Em Porangabussu a relação se inverteu levemente, sugerindo que fatores locais podem modular a aceitação.

**Tabela 3 — Proporção de Aceitação Satisfatória (Nota >= 7)**

| Grupo | N | N satisfatório | Proporção |
|-------|---|----------------|-----------|
| Vegetariana | 1.114 | 1.017 | 91,29% |
| Carne | 2.216 | 1.876 | 84,66% |

A proporção de avaliações satisfatórias é 6,64 pontos percentuais maior no grupo vegetariano (91,29%) em comparação ao grupo carne (84,66%).

![Figura 1 — Distribuição da nota por grupo (boxplot).](graficos/graf1_boxplot.png)

**Figura 1 — Distribuição da nota por grupo (boxplot).**

![Figura 2 — Histograma e densidade da nota por grupo.](graficos/graf2_densidade.png)

**Figura 2 — Histograma e densidade da nota por grupo.**

![Figura 3 — Média da nota por grupo.](graficos/graf3_media_grupo.png)

**Figura 3 — Média da nota por grupo.**

![Figura 4 — Média da nota por refeitório e grupo.](graficos/graf4_media_ru.png)

**Figura 4 — Média da nota por refeitório e grupo.**

![Figura 5 — Proporção de avaliações satisfatórias por grupo.](graficos/graf5_proporcao_satisfatoria.png)

**Figura 5 — Proporção de avaliações satisfatórias (Nota ≥ 7) por grupo.**

---

### 8.3 Estimação Pontual

Os parâmetros populacionais de interesse são a nota média de aceitação e a proporção de avaliações satisfatórias para cada grupo. As estimativas pontuais obtidas a partir da amostra são apresentadas na tabela abaixo.

| Parâmetro | Estimativa |
|-----------|-----------|
| Nota média — Vegetariana | 7,7655 |
| Nota média — Carne | 7,6421 |
| Diferença média pareada (d̄) | +0,1164 |
| Proporção satisfatória — Vegetariana | 91,29% |
| Proporção satisfatória — Carne | 84,66% |
| Diferença entre proporções | +6,64 pp |

**Interpretação:** A nota média estimada para preparações vegetarianas (7,7655) é ligeiramente superior à nota média das preparações à base de carne (7,6421), com diferença pareada de +0,1164 ponto na escala de 0 a 10. Ambos os grupos se encontram em faixa de boa aceitação (médias acima de 7,6 e medianas iguais a 8,0). A proporção estimada de avaliações satisfatórias é de 91,29% para o grupo vegetariano e 84,66% para o grupo carne — diferença de 6,64 pontos percentuais favorável às preparações vegetarianas. Essas estimativas pontuais constituem a melhor aproximação disponível dos parâmetros populacionais, sujeitas à margem de erro descrita na seção seguinte.

---

### 8.4 Estimação Intervalar

#### 8.4.1 IC para a Diferença de Médias Pareadas

**Fórmula:**

IC = d̄ ± t_(α/2, n−1) × (s_d / √n)

Onde:
- d̄ = diferença média pareada (Media_Veg − Media_Carne por contexto)
- s_d = desvio padrão das diferenças
- n = número de pares contextuais
- t_(α/2, n−1) = valor crítico da distribuição t com n−1 graus de liberdade

**Cálculo:**

| Componente | Valor |
|------------|-------|
| d̄ (diferença média pareada) | 0,1164 |
| s_d (desvio padrão das diferenças) | 0,6217 |
| n (número de pares) | 689 |
| Erro padrão: SE = s_d / √n = 0,6217 / √689 | 0,0237 |
| t_(0,025 ; 688) (valor crítico bilateral, 95%) | 1,9632 |
| Limite inferior: 0,1164 − 1,9632 × 0,0237 | **+0,0699** |
| Limite superior: 0,1164 + 1,9632 × 0,0237 | **+0,1629** |

**IC 95% para a diferença média pareada: [+0,0699 ; +0,1629]**

**Interpretação:** Com 95% de confiança, a diferença média entre a nota de preparações vegetarianas e de carne nos RUs da UFC, no período analisado, está entre +0,07 e +0,16 ponto. Como o intervalo não contém zero e é inteiramente positivo, há evidência de que preparações vegetarianas têm aceitação média superior.

---

#### 8.4.2 IC para a Diferença entre Proporções

**Fórmula:**

IC = (p̂_veg − p̂_carne) ± z_(α/2) × √[ p̂_veg(1−p̂_veg)/n_veg + p̂_carne(1−p̂_carne)/n_carne ]

**Cálculo:**

| Componente | Valor |
|------------|-------|
| p̂_veg (prop. satisfatória — Vegetariana) | 0,9129 |
| p̂_carne (prop. satisfatória — Carne) | 0,8466 |
| n_veg | 1.114 |
| n_carne | 2.216 |
| Variância parcial veg: 0,9129 × 0,0871 / 1.114 | 0,0000714 |
| Variância parcial carne: 0,8466 × 0,1534 / 2.216 | 0,0000586 |
| SE = √(0,0000714 + 0,0000586) | 0,01140 |
| z_(0,025) | 1,96 |
| Limite inferior: 0,0663 − 1,96 × 0,01140 | **+0,0440 (+4,40 pp)** |
| Limite superior: 0,0663 + 1,96 × 0,01140 | **+0,0887 (+8,87 pp)** |

**IC 95% para a diferença entre proporções: [+4,40 pp ; +8,87 pp]**

**Interpretação:** Com 95% de confiança, a proporção de avaliações satisfatórias das preparações vegetarianas supera a das preparações à base de carne entre 4,40 e 8,87 pontos percentuais. Essa diferença é mais expressiva na escala percentual do que na escala de notas: a cada 100 avaliações, as preparações vegetarianas produzem entre 4 e 9 avaliações satisfatórias a mais.

---

### 8.5 Análise Inferencial Principal — Teste t Pareado

**H0: media_d = 0  |  H1: media_d ≠ 0** (bilateral; α = 0,05)

| Parâmetro | Valor |
|-----------|-------|
| Número de pares contextuais | 689 |
| Diferença média (d̄) | +0,1164 |
| Desvio padrão das diferenças (s_d) | 0,6217 |
| Erro padrão (SE = s_d/√n) | 0,0237 |
| Estatística t = d̄ / SE | 4,9145 |
| Graus de liberdade | 688 |
| p-valor (bilateral) | 0,00000111 |
| IC 95% para d̄ | [+0,0699 ; +0,1629] |
| **Decisão** | **Rejeita H0** |

Os resultados indicam evidência estatística de diferença entre as médias de aceitação. No período e nos restaurantes analisados, as preparações vegetarianas apresentaram nota média ligeiramente superior. A magnitude da diferença foi pequena — cerca de 0,116 ponto na escala de notas — o que indica que a significância estatística não deve ser confundida com grande relevância prática.

![Figura 6 — Histograma e QQ-plot das diferenças pareadas (Veg − Carne).](graficos/graf6_diferencas_pareadas.png)

**Figura 6 — Histograma e QQ-plot das diferenças pareadas (Veg − Carne).**

### 8.6 Análise Secundária — Teste de Duas Proporções

**H0: p_veg = p_carne  |  H1: p_veg ≠ p_carne** (bilateral; α = 0,05)

| Parâmetro | Valor |
|-----------|-------|
| Proporção satisfatória — p_veg | 91,29% |
| Proporção satisfatória — p_carne | 84,66% |
| Diferença (p_veg − p_carne) | +6,64 pp |
| IC 95% para a diferença | [+4,40 pp ; +8,87 pp] |
| Estatística z | 5,3508 |
| p-valor | 0,00000009 |
| **Decisão** | **Rejeita H0** |

---

## 9. Verificação das Condições de Aplicação

**Independência:** o pareamento por contexto reduz confundimento, mas pode haver correlação residual associada a avaliadores repetidos.

**Tamanho amostral:** 689 pares e 3.330 observações — amplamente suficiente.

**Normalidade:** Shapiro-Wilk resultou em W = 0,9204, p < 0,001. Isso indica afastamento formal da normalidade, mas com 689 pares o Teorema Central do Limite favorece a aproximação normal da média das diferenças, tornando o teste t pareado razoavelmente robusto neste contexto. O QQ-plot das diferenças confirma que os desvios se concentram nas caudas, não no corpo central da distribuição.

**Proporções:** os produtos n*p e n*(1-p) são superiores a 10 em ambos os grupos.

**Limitações:** amostragem por conveniência; avaliadores identificados no sistema (não usuários diretos); variação de cardápio ao longo do período; desequilíbrio amostral tratado pela agregação contextual.

---

## 10. Discussão

Os resultados indicam que as preparações vegetarianas apresentaram aceitação estatisticamente superior no período analisado. A diferença de 0,116 ponto na nota média é pequena em magnitude, e ambos os grupos estão numa faixa de boa aceitação (médias acima de 7,6, medianas de 8,0).

A diferença de 6,64 pp na proporção de avaliações satisfatórias tem maior relevância gerencial: a cada 100 avaliações, as preparações vegetarianas geram entre 4 e 9 avaliações satisfatórias a mais do que as de carne.

A análise por refeitório indica que a vantagem vegetariana não é uniforme — em Porangabussu a relação se inverte levemente. Estudos futuros poderiam investigar diferenças por tipo de cardápio, controlar o efeito do avaliador, aplicar modelos mistos, coletar avaliações diretamente dos usuários e ampliar o período de análise.

---

## 11. Conclusão

No período e nos Restaurantes Universitários analisados, as preparações vegetarianas apresentaram aceitação média ligeiramente superior às preparações à base de carne. A diferença foi estatisticamente significativa (t = 4,9145; gl = 688; p = 0,00000111; IC 95%: [+0,0699; +0,1629]), mas de pequena magnitude prática (0,116 ponto em escala de 0 a 10).

Como análise secundária, verificou-se que a proporção de avaliações satisfatórias (Nota >= 7) é significativamente maior para preparações vegetarianas (91,29% vs. 84,66%; z = 5,3508; p < 0,001; IC 95%: [+4,40 pp; +8,87 pp]).

Os resultados sugerem que as preparações vegetarianas não apresentaram rejeição maior em relação às preparações à base de carne, podendo ser consideradas bem aceitas no contexto avaliado. Por se tratar de amostra por conveniência, a generalização dos resultados deve ser feita com cautela.

Ressalva-se ainda que os avaliadores registrados no sistema não são necessariamente os estudantes e demais usuários que frequentam regularmente os RUs — o que levanta a questão de se a aceitação medida aqui reflete a percepção desse público mais amplo.

---

## 12. Referências

MONTGOMERY, D. C.; RUNGER, G. C. **Estatística Aplicada e Probabilidade para Engenheiros**. 6. ed. Rio de Janeiro: LTC, 2016.

BUSSAB, W. O.; MORETTIN, P. A. **Estatística Básica**. 10. ed. São Paulo: Saraiva, 2023.

BRASIL. Ministério da Educação. **Programa Nacional de Assistência Estudantil (PNAES)**. Portaria Normativa n.º 39, de 12 de dezembro de 2007.

DUTCOSKY, S. D. **Análise Sensorial de Alimentos**. 4. ed. Curitiba: Champagnat, 2013.

ABREU, E. S.; SPINELLI, M. G. N.; PINTO, A. M. S. **Gestão de Unidades de Alimentação e Nutrição: um modo de fazer**. São Paulo: Metha, 2016.

PROENÇA, R. P. C. et al. **Qualidade nutricional e sensorial na produção de refeições**. Florianópolis: UFSC, 2005.

---

*Análise realizada em Python 3.x com pandas, numpy, matplotlib, seaborn, scipy e statsmodels.*
