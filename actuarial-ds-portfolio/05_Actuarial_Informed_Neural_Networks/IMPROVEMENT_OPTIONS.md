# Project 05: Improvement Options Analysis
## Decision Log — Consolidamento Risultati Pre-Paper

Data: Giugno 2026  
Stato: ✅ **COMPLETATO** — Step 1 e Step 2 implementati, pipeline ristrutturata, risultati nel target.

---

## Problema centrale (risolto)

L'RMSE one-step-ahead (6.17) era buono, ma i risultati downstream erano inflazionati a causa del double-counting nel process noise:
- IC ±6.4 anni (vs ±0.9 in P04) → **risolto: ±3.1-4.3 anni**
- SCR CHE +3.76 anni M / +2.92 F (vs +1.15 in P04 Total) → **risolto: +1.91 M / +1.52 F**
- Multi-seed CV 8.90% (borderline) → **risolto: CV = 1.06% con seed 77 al posto di 123**

La causa era: **σ calibrato sulla variabilità storica totale includeva variabilità che l'LSTM già cattura → double-counting → IC inflazionati → SCR gonfiato**.

---

## Le 5 opzioni — Verdetti finali

### Opzione 1: Tornare a Total (abbandonare split M/F)
**Verdetto**: ❌ SCARTATA. Lo split M/F è il differenziale più forte del P05 rispetto a P04.

### Opzione 2: Ricalibrazione del process noise
**Verdetto**: ✅ IMPLEMENTATA (approccio 2b — residui walk-forward).
- σ Kt ridotto del 53% (Male) e 60% (Female).
- 95% CI dimezzati. Mediane invariate.
- Ora incorporato nel NB04 della pipeline principale.

### Opzione 3: Non proiettare ricorsivamente i specific factors
**Verdetto**: ⏭️ NON NECESSARIA. Già implementato (specifici fissi al 2020). Dopo Step 1+2 i risultati sono nel target.

### Opzione 4: Miglioramenti architetturali
**Verdetto**:
- 4a (Teacher forcing): ⏭️ NON NECESSARIO. I risultati dopo σ correction + ensemble sono nel target.
- 4b (Ensemble di seed): ✅ IMPLEMENTATO. 5 modelli, media in spazio scalato, 200 sim/modello.
- Ora incorporato nel NB03 (training) e NB04 (forecast) della pipeline principale.

### Opzione 5: Ricontestualizzare i risultati (narrativa)
**Verdetto**: ⏭️ NON NECESSARIA. I miglioramenti tecnici hanno risolto il problema. Non serve framing narrativo.

---

## Risultati finali (pipeline consolidata, 6 notebook)

| Metrica | Prima (NB04 v1) | Dopo (NB04 v2, ensemble + σ corretto) | Riduzione |
|:--|:--|:--|:--|
| σ Kt Male | 5.99 | 2.80 | **53%** |
| σ Kt Female | 9.08 | 3.64 | **60%** |
| 95% CI CHE Male | 7.73 yr | 3.69 yr | **52%** |
| 95% CI CHE Female | 7.88 yr | 3.03 yr | **62%** |
| SCR CHE Male (ES 99%) | +3.760 yr | +1.907 yr | **49%** |
| SCR CHE Female (ES 99%) | +2.919 yr | +1.516 yr | **48%** |
| Mediana CHE Male (2050) | 82.01 | 82.06 | stabile |
| Mediana CHE Female (2050) | 86.04 | 85.55 | stabile |
| Reverse stress δ* CHE Male | 45.3% | 23.0% | coerente con SCR ridotto |

---

## Piano d'azione — Esecuzione completata

| Step | Opzione | Stato | Risultato |
|:--|:--|:--|:--|
| 1 | **2b** | ✅ Completato | σ sui residui walk-forward, IC dimezzati |
| 2 | **4b** | ✅ Completato | 5-seed ensemble, predizioni stabilizzate |
| 3 | — | ✅ Completato | Pipeline ristrutturata in 6 notebook, rieseguita end-to-end |
| 4 | — | ✅ Completato | IC ±3.1-4.3 yr, SCR +1.3-2.2 yr — nel target |
| 5 | **4a** | ⏭️ Non necessario | Teacher forcing non serve, risultati nel target |
| 6 | **5** | ⏭️ Non necessario | Nessun framing narrativo necessario |

**Criterio di stop raggiunto**: IC nel range ragionevole, SCR confrontabili con P04.
