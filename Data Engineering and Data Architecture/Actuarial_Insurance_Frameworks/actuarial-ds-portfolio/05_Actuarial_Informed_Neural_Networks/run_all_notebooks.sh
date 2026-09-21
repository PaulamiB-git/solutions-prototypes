#!/bin/zsh
# Run all 6 notebooks in sequence using papermill.
# Each notebook is executed in-place (outputs saved to the .ipynb file).
# If any notebook fails, the script stops.
#
# Usage: cd to this directory, then:
#   ./run_all_notebooks.sh
#
# Estimated time: ~90 min on M1 Pro
#   NB01: ~1 min, NB02: ~2 min, NB03: ~55 min (Optuna + ensemble training),
#   NB04: ~25 min (residuals + ensemble forecast + e0), NB05: ~5 min, NB06: ~3 min

set -e  # Stop on first error

cd "$(dirname "$0")/notebooks"

NOTEBOOKS=(
    "01_data_and_baseline.ipynb"
    "02_actuarial_benchmarking.ipynb"
    "03_training_ablation_lambda.ipynb"
    "04_stochastic_forecasting.ipynb"
    "05_xai_validation.ipynb"
    "06_stress_test_scr.ipynb"
)

echo "=========================================="
echo "  Running all 6 notebooks in sequence"
echo "=========================================="
echo ""

TOTAL_START=$(date +%s)

for nb in "${NOTEBOOKS[@]}"; do
    echo "--- $nb ---"
    NB_START=$(date +%s)

    python3 -m papermill "$nb" "$nb" --no-progress-bar --request-save-on-cell-execute 2>&1

    NB_END=$(date +%s)
    NB_ELAPSED=$(( NB_END - NB_START ))
    echo "  ✓ Completed in $(( NB_ELAPSED / 60 ))m $(( NB_ELAPSED % 60 ))s"
    echo ""
done

TOTAL_END=$(date +%s)
TOTAL_ELAPSED=$(( TOTAL_END - TOTAL_START ))

echo "=========================================="
echo "  All notebooks executed successfully!"
echo "  Total time: $(( TOTAL_ELAPSED / 60 ))m $(( TOTAL_ELAPSED % 60 ))s"
echo "=========================================="
