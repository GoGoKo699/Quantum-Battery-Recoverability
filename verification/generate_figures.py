"""Generate the committed finite-input sweeps and SVG directly from Python."""
import json
import math
import os
from pathlib import Path
import tempfile

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "qbr-mpl"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from channel_models import native_case


def main():
    root = Path(__file__).resolve().parent
    results, figures = root / "results", root / "figures"
    results.mkdir(exist_ok=True)
    figures.mkdir(exist_ok=True)
    rows = []
    for exponent in [1.0, 4 / 3, 1.5]:
        for n in [32, 128, 512, 2048, 8192]:
            N = math.ceil(4 * n ** exponent)
            r = native_case(n, N, kappa=0.2, g=1.0)
            r.update(regime="fixed_g", energy_exponent=exponent, energy_coefficient=4)
            rows.append(r)
    for exponent, coefficient in [(2.0, 8), (2.5, 2)]:
        for n in [4, 8, 16, 32]:
            N = math.ceil(coefficient * n ** exponent)
            r = native_case(n, N, kappa=0.05, g=1 / math.sqrt(N), calibrated=True)
            r.update(regime="fixed_Omega", energy_exponent=exponent,
                     energy_coefficient=coefficient)
            rows.append(r)
    for r in rows:
        assert abs(r["output_trace"] - 1) < 3e-9
        assert r["min_output_eigenvalue"] > -3e-9
        assert r["reference_input_trace_error"] <= r["proved_diamond_upper"] + 3e-9
    (results / "native_gate_sweeps.json").write_text(json.dumps(rows, indent=2) + "\n")

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "svg.hashsalt": "quantum-battery-recoverability-v1",
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(10.7, 4.2), constrained_layout=True)
    colors = ["#B64C38", "#B18B25", "#216C91"]
    for p, color, marker, label in zip(
            [1.0, 4 / 3, 1.5], colors, ["s", "o", "^"],
            [r"$N=4n$", r"$N\simeq4n^{4/3}$", r"$N\simeq4n^{3/2}$"]):
        data = [r for r in rows if r["regime"] == "fixed_g" and r["energy_exponent"] == p]
        axes[0].loglog([r["n"] for r in data],
                       [r["reference_input_entanglement_infidelity"] for r in data],
                       color=color, marker=marker, label=label, linewidth=1.6, markersize=5)
    axes[0].set_title(r"Fixed bare coupling: $\kappa/g=0.2$")
    for p, color, marker, label in zip(
            [2.0, 2.5], ["#B18B25", "#216C91"], ["o", "^"],
            [r"$N=8n^2$", r"$N\simeq2n^{5/2}$"]):
        data = [r for r in rows if r["regime"] == "fixed_Omega" and r["energy_exponent"] == p]
        axes[1].loglog([r["n"] for r in data],
                       [r["reference_input_entanglement_infidelity"] for r in data],
                       color=color, marker=marker, label=label, linewidth=1.6, markersize=5)
    axes[1].set_title(r"Fixed enhanced rate: $\kappa/\Omega=0.05$")
    for ax in axes:
        ax.set_xlabel("Register qubits n")
        ax.set_ylabel("Reference-input entanglement infidelity")
        ax.grid(True, which="major", alpha=0.2)
        ax.legend(frameon=False, loc="best")
    fig.savefig(figures / "native_gate_scaling.svg", metadata={"Date": None},
                facecolor="white")
    # The PNG is only a local visual-review intermediate; SVG is the repository artifact.
    fig.savefig(Path(tempfile.gettempdir()) / "qbr_native_gate_scaling.png", dpi=170,
                facecolor="white")
    plt.close(fig)
    print(f"Generated {len(rows)} finite native-gate cases and figures/native_gate_scaling.svg")
    print("Plotted quantities concern one reference-entangled input, not an optimized channel norm.")


if __name__ == "__main__":
    main()
