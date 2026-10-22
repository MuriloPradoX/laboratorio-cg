import numpy as np
import streamlit as st


def ampliar(imagem, fator=20):
    return np.repeat(np.repeat(imagem, fator, axis=0), fator, axis=1)


# Cores (RGB) conferidas com um seletor de cores
VERMELHO = (186, 12, 47)
BRANCO = (255, 255, 255)
AZUL = (0, 32, 91)

st.title("Bandeira da Noruega")

bandeira = np.zeros((16, 22, 3), dtype=np.uint8)
bandeira[:] = VERMELHO          # fundo
bandeira[:, 6:10] = BRANCO      # faixa vertical branca
bandeira[6:10, :] = BRANCO      # faixa horizontal branca
bandeira[:, 7:9] = AZUL         # faixa vertical azul (cobre o branco)
bandeira[7:9, :] = AZUL         # faixa horizontal azul (cobre o branco)
st.image(ampliar(bandeira))