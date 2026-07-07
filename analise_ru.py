"""
Análise Inferencial — Aceitação de Preparações Vegetarianas vs. Carne
Restaurantes Universitários da UFC — 2026

Coloque este script e o arquivo "2026 Sistema RU (2).xlsx" na mesma pasta e execute:
    python analise_ru.py
"""

import os
import pandas as pd
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
import warnings; warnings.filterwarnings('ignore')

# Caminhos
ARQUIVO_ENTRADA = "2026 Sistema RU (2).xlsx"
PASTA_SAIDA     = "resultados"
PASTA_GRAFICOS  = "graficos"

os.makedirs(PASTA_SAIDA,   exist_ok=True)
os.makedirs(PASTA_GRAFICOS, exist_ok=True)

sns.set_style("whitegrid")
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'axes.titlesize':13,'axes.titleweight':'bold','figure.dpi':150})
CORES = {'Vegetariana':'#2ecc71','Carne':'#e74c3c'}


# 1. Leitura da base bruta
print("="*60, "\n1. LEITURA\n" + "="*60)

df_raw = pd.read_excel(ARQUIVO_ENTRADA, sheet_name="Av. Sensorial")
print(f"Shape bruto: {df_raw.shape}")
print(f"Período: {df_raw['data'].min().date()} a {df_raw['data'].max().date()}")


# 2. Limpeza
print("\n" + "="*60 + "\n2. LIMPEZA\n" + "="*60)

df = df_raw[df_raw['Refeição'].isin(['Almoço','Jantar'])].copy()
df = df[df['Preparação'].isin(['PB','PV','VEG'])]
df = df[df['Nota'].notna()]

# Remover zeros inválidos: nota 0 com todos os critérios em branco
# provavelmente significa que o avaliador abriu o registro mas não preencheu de fato
# (testei manter esses casos — a diferença nos resultados é pequena,
# mas conceptualmente faz mais sentido excluir)
criterios = ['Aparência','Textura','Sabor','Odor','Global']
mask_inv  = (df['Nota'] == 0) & df[criterios].isna().all(axis=1)
n_zeros   = int(mask_inv.sum())
df        = df[~mask_inv].copy()

# Criar variáveis de análise
df['Grupo']                  = df['Preparação'].map({'VEG':'Vegetariana','PB':'Carne','PV':'Carne'})
df['Aceitacao_satisfatoria'] = (df['Nota'] >= 7).astype(int)
df['Data']                   = pd.to_datetime(df['data']).dt.date

print(f"Zeros inválidos removidos : {n_zeros}")
print(f"Base final                : {len(df)}")
print(f"  Vegetariana             : {(df['Grupo']=='Vegetariana').sum()}")
print(f"  Carne                   : {(df['Grupo']=='Carne').sum()}")

df.to_excel(os.path.join(PASTA_SAIDA, "base_tratada.xlsx"), index=False)

g_veg = df[df['Grupo']=='Vegetariana']
g_car = df[df['Grupo']=='Carne']


# 3. Planejamento amostral — verificar se n disponível é suficiente
z_, p_, E_ = 1.96, 0.5, 0.05
n_min = int(np.ceil((z_**2 * p_*(1-p_)) / E_**2))
print(f"\nn mínimo: {n_min} | disponível: {len(df)} ({len(df)/n_min:.1f}x)")


# 4. Tabelas descritivas
tab_desc = df.groupby('Grupo')['Nota'].agg(
    N='count', Media='mean', Mediana='median', DP='std',
    Min='min', Q1=lambda x: x.quantile(.25),
    Q3=lambda x: x.quantile(.75), Max='max'
).round(2).reset_index()

tab_ru   = df.groupby(['Refeitório','Grupo'])['Nota'].mean().round(2).unstack().reset_index()
tab_ref  = df.groupby(['Refeição','Grupo'])['Nota'].mean().round(2).unstack().reset_index()
tab_prop = df.groupby('Grupo').agg(
    N=('Nota','count'), N_sat=('Aceitacao_satisfatoria','sum')).reset_index()
tab_prop['Prop_pct'] = (tab_prop['N_sat']/tab_prop['N']*100).round(2)

with pd.ExcelWriter(os.path.join(PASTA_SAIDA,"resultados_tabelas.xlsx")) as w:
    tab_desc.to_excel(w, sheet_name='Descritivo',  index=False)
    tab_ru.to_excel(w,   sheet_name='Media_RU',    index=False)
    tab_ref.to_excel(w,  sheet_name='Media_Ref',   index=False)
    tab_prop.to_excel(w, sheet_name='Prop_Sat',    index=False)

print("\nDescritivo por grupo:"); print(tab_desc.to_string(index=False))
print("\nProporção satisfatória:"); print(tab_prop.to_string(index=False))


# 5. Gráficos
def salvar(nome):
    plt.savefig(os.path.join(PASTA_GRAFICOS, nome), dpi=150, bbox_inches='tight')
    plt.close(); print(f"  Salvo: {nome}")

# G1 – Boxplot
fig, ax = plt.subplots(figsize=(7,5))
bp = ax.boxplot([g_veg['Nota'],g_car['Nota']], labels=['Vegetariana','Carne'],
                patch_artist=True, widths=0.5,
                medianprops=dict(color='black',linewidth=2))
for patch,cor in zip(bp['boxes'],['#2ecc71','#e74c3c']):
    patch.set_facecolor(cor); patch.set_alpha(0.7)
ax.set_title('Distribuição da Nota por Grupo\n(Almoço e Jantar — RUs da UFC, 2026)')
ax.set_xlabel('Grupo'); ax.set_ylabel('Nota (0–10)'); ax.set_ylim(0,11)
plt.tight_layout(); salvar('graf1_boxplot.png')

# G2 – Densidade
fig, ax = plt.subplots(figsize=(8,5))
for grupo,cor in CORES.items():
    vals = df[df['Grupo']==grupo]['Nota']
    ax.hist(vals, bins=20, density=True, alpha=0.4, color=cor, label=grupo)
    vals.plot.kde(ax=ax, color=cor, linewidth=2)
ax.set_title('Distribuição da Nota por Grupo — Histograma e Densidade\n(Almoço e Jantar — RUs da UFC, 2026)')
ax.set_xlabel('Nota (0–10)'); ax.set_ylabel('Densidade')
ax.legend(title='Grupo'); plt.tight_layout(); salvar('graf2_densidade.png')

# G3 – Média por grupo
medias = df.groupby('Grupo')['Nota'].mean()
fig, ax = plt.subplots(figsize=(6,4.5))
bars = ax.bar(medias.index, medias.values,
              color=[CORES[g] for g in medias.index],
              edgecolor='black', linewidth=0.7, alpha=0.85, width=0.5)
for bar,val in zip(bars,medias.values):
    ax.text(bar.get_x()+bar.get_width()/2, val+0.05, f'{val:.2f}',
            ha='center', va='bottom', fontweight='bold')
ax.set_ylim(0,10); ax.set_xlabel('Grupo'); ax.set_ylabel('Média (0–10)')
ax.set_title('Média da Nota por Grupo\n(Almoço e Jantar — RUs da UFC, 2026)')
plt.tight_layout(); salvar('graf3_media_grupo.png')

# G4 – Média por RU
tab_ru_p = df.groupby(['Refeitório','Grupo'])['Nota'].mean().reset_index()
rus = sorted(df['Refeitório'].dropna().unique())
x   = np.arange(len(rus)); width = 0.35
fig, ax = plt.subplots(figsize=(9,5))
for i,(grupo,cor) in enumerate(CORES.items()):
    vals = [tab_ru_p.loc[(tab_ru_p['Refeitório']==ru)&(tab_ru_p['Grupo']==grupo),'Nota'].values for ru in rus]
    vals = [v[0] if len(v)>0 else np.nan for v in vals]
    bars = ax.bar(x+i*width-width/2, vals, width, label=grupo,
                  color=cor, alpha=0.8, edgecolor='black', linewidth=0.5)
    for bar,val in zip(bars,vals):
        if not np.isnan(val):
            ax.text(bar.get_x()+bar.get_width()/2, val+0.05, f'{val:.1f}',
                    ha='center', va='bottom', fontsize=8.5)
ax.set_xticks(x); ax.set_xticklabels(rus, rotation=15, ha='right')
ax.set_ylim(0,10.5); ax.set_xlabel('Refeitório'); ax.set_ylabel('Média (0–10)')
ax.set_title('Média da Nota por Refeitório e Grupo\n(Almoço e Jantar — RUs da UFC, 2026)')
ax.legend(title='Grupo'); plt.tight_layout(); salvar('graf4_media_ru.png')

# G5 – Proporção satisfatória
props = df.groupby('Grupo')['Aceitacao_satisfatoria'].mean()*100
fig, ax = plt.subplots(figsize=(6,4.5))
bars = ax.bar(props.index, props.values,
              color=[CORES[g] for g in props.index],
              edgecolor='black', linewidth=0.7, alpha=0.85, width=0.5)
for bar,val in zip(bars,props.values):
    ax.text(bar.get_x()+bar.get_width()/2, val+0.5, f'{val:.1f}%',
            ha='center', va='bottom', fontweight='bold')
ax.axhline(50, color='gray', linestyle='--', linewidth=1, label='50%')
ax.set_ylim(0,105); ax.set_xlabel('Grupo'); ax.set_ylabel('Proporção (%)')
ax.set_title('Avaliações Satisfatórias (Nota >= 7) por Grupo\n(Almoço e Jantar — RUs da UFC, 2026)')
ax.legend(); plt.tight_layout(); salvar('graf5_proporcao_satisfatoria.png')


# 6. Teste t pareado (análise principal)
df_ctx = df.groupby(['Data','Refeitório','Refeição','Grupo'])['Nota'].mean().reset_index()
df_piv = (df_ctx.pivot_table(index=['Data','Refeitório','Refeição'],
                              columns='Grupo', values='Nota')
          .dropna().reset_index())
df_piv.columns.name = None
df_piv = df_piv.rename(columns={'Carne':'Media_Carne','Vegetariana':'Media_Veg'})
df_piv['Diferenca'] = df_piv['Media_Veg'] - df_piv['Media_Carne']

n_pares = len(df_piv)
d_bar   = df_piv['Diferenca'].mean()
s_d     = df_piv['Diferenca'].std(ddof=1)
se      = s_d / np.sqrt(n_pares)
t_stat  = d_bar / se
gl      = n_pares - 1
p_valor = 2 * stats.t.sf(abs(t_stat), df=gl)
t_crit  = stats.t.ppf(0.975, df=gl)
ic_low  = d_bar - t_crit * se
ic_high = d_bar + t_crit * se

print(f"\n=== TESTE T PAREADO ===")
print(f"Pares: {n_pares} | d_bar={d_bar:.4f} | s_d={s_d:.4f}")
print(f"t={t_stat:.4f}, gl={gl}, p={p_valor:.8f}")
print(f"IC 95%: [{ic_low:.4f}; {ic_high:.4f}]")

# G6 – Diferenças
fig, axes = plt.subplots(1,2, figsize=(11,4.5))
axes[0].hist(df_piv['Diferenca'], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
axes[0].axvline(0, color='red', linestyle='--', linewidth=1.5, label='d=0')
axes[0].axvline(d_bar, color='orange', linestyle='-', linewidth=2, label=f'Media={d_bar:.3f}')
axes[0].set_title('Histograma das Diferencas Pareadas\n(Veg - Carne)')
axes[0].set_xlabel('Diferenca de Nota'); axes[0].set_ylabel('Frequencia')
axes[0].legend()
stats.probplot(df_piv['Diferenca'], plot=axes[1])
axes[1].set_title('QQ-Plot das Diferencas Pareadas')
axes[1].get_lines()[0].set(color='steelblue', markersize=4)
axes[1].get_lines()[1].set(color='red', linewidth=1.5)
plt.tight_layout(); salvar('graf6_diferencas_pareadas.png')

df_piv.to_excel(os.path.join(PASTA_SAIDA,"pares_contextuais.xlsx"), index=False)


# 7. Teste de proporções (análise secundária)
n_veg = len(g_veg); x_veg = g_veg['Aceitacao_satisfatoria'].sum()
n_car = len(g_car); x_car = g_car['Aceitacao_satisfatoria'].sum()
p_veg_hat = x_veg/n_veg; p_car_hat = x_car/n_car
dif_prop  = p_veg_hat - p_car_hat
se_dif    = np.sqrt(p_veg_hat*(1-p_veg_hat)/n_veg + p_car_hat*(1-p_car_hat)/n_car)
ic_dif_l  = dif_prop - 1.96*se_dif
ic_dif_h  = dif_prop + 1.96*se_dif
z_stat, p_prop = proportions_ztest([x_veg,x_car],[n_veg,n_car], alternative='two-sided')

print(f"\n=== PROPORÇÕES ===")
print(f"p_veg={p_veg_hat*100:.2f}%, p_car={p_car_hat*100:.2f}%")
print(f"Dif={dif_prop*100:.2f} pp, IC 95%: [{ic_dif_l*100:.2f}; {ic_dif_h*100:.2f}] pp")
print(f"z={z_stat:.4f}, p={p_prop:.8f}")


# 8. Verificação de normalidade das diferenças
sw_stat, sw_p = stats.shapiro(df_piv['Diferenca'])
print(f"\nShapiro-Wilk: W={sw_stat:.4f}, p={sw_p:.6f}")
print(f"n pares={n_pares} — TCL favorece robustez do teste t")

print("\nAnalise concluida.")
print(f"  Arquivos em ./{PASTA_SAIDA}/  e  ./{PASTA_GRAFICOS}/")
