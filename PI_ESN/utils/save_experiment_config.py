import json


def save_experiment_config(
    filepath,
    signal_config=None,
    vdp_params=None,
    data_split=None,
    esn_params=None,
    piesn_params=None,
):
    """
    Gera um arquivo .txt (ou .cfg) contendo todos os parâmetros do experimento.
    Se algum conjunto de parâmetros não for passado, a função ignora.
    """

    def format_block(title, data_dict):
        out = []
        out.append("# -----------------------------")
        out.append(f"# {title}")
        out.append("# -----------------------------")
        out.append(json.dumps(data_dict, indent=4))
        out.append("\n")
        return "\n".join(out)

    text = []
    text.append("# ==========================================================")
    text.append("# Experiment Configuration - Van der Pol + PI-ESN")
    text.append("# ==========================================================\n")

    if signal_config:
        text.append(format_block("Input Signal Configuration", signal_config))

    if vdp_params:
        text.append(format_block("Van der Pol Oscillator Parameters", vdp_params))

    if data_split:
        text.append(format_block("Data Splitting Parameters", data_split))

    if esn_params:
        text.append(format_block("Echo State Network (ESN) Parameters", esn_params))

    if piesn_params:
        text.append(
            format_block("Physics-Informed ESN (PI-ESN) Parameters", piesn_params)
        )

    # SALVAR O ARQUIVO
    with open(filepath, "w") as f:
        f.write("\n".join(text))

    print(f"Config file saved to: {filepath}")
