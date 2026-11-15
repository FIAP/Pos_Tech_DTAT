import streamlit as st
import tiktoken
import html

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="TokenLab | Tokenização em LLMs",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Página */
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(76, 110, 245, 0.08), transparent 28%),
            radial-gradient(circle at 90% 10%, rgba(18, 184, 134, 0.06), transparent 25%),
            #f7f9fc;
    }

    /* Largura */
    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Header */
    .hero {
        background: linear-gradient(120deg, #172554 0%, #1e3a8a 48%, #334155 100%);
        padding: 34px 40px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.16);
    }

    .hero-title {
        font-size: 38px;
        font-weight: 750;
        margin-bottom: 5px;
        letter-spacing: -0.8px;
    }

    .hero-subtitle {
        font-size: 17px;
        opacity: 0.88;
        max-width: 900px;
        line-height: 1.6;
    }

    .hero-label {
        display: inline-block;
        background: rgba(255,255,255,0.13);
        border: 1px solid rgba(255,255,255,0.20);
        border-radius: 30px;
        padding: 6px 12px;
        font-size: 12px;
        margin-bottom: 15px;
        letter-spacing: 0.4px;
    }

    /* Caixa explicativa */
    .concept-box {
        background: white;
        border: 1px solid #e5eaf1;
        border-left: 5px solid #2563eb;
        padding: 20px 24px;
        border-radius: 12px;
        margin: 12px 0 25px 0;
        box-shadow: 0 3px 15px rgba(15,23,42,0.04);
        color: #1e293b;
        line-height: 1.65;
    }

    /* Cards */
    .metric-card {
        background: white;
        border: 1px solid #e5eaf1;
        border-radius: 15px;
        padding: 20px 22px;
        box-shadow: 0 4px 18px rgba(15,23,42,0.045);
        min-height: 105px;
    }

    .metric-label {
        color: #64748b;
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: .4px;
    }

    .metric-value {
        color: #0f172a;
        font-size: 31px;
        font-weight: 750;
        margin-top: 5px;
    }

    .metric-note {
        color: #64748b;
        font-size: 12px;
        margin-top: 3px;
    }

    /* Painel dos tokenizadores */
    .tokenizer-header {
        background: white;
        border: 1px solid #e5eaf1;
        border-radius: 14px;
        padding: 18px 21px;
        margin-bottom: 15px;
        box-shadow: 0 3px 14px rgba(15,23,42,0.04);
    }

    .tokenizer-title {
        font-size: 19px;
        font-weight: 700;
        color: #172554;
    }

    .tokenizer-description {
        color: #64748b;
        font-size: 13px;
        margin-top: 5px;
    }

    /* Tokens */
    .token-area {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        min-height: 150px;
        line-height: 2.7;
        box-shadow: 0 3px 14px rgba(15,23,42,0.04);
    }

    .token {
        display: inline-block;
        padding: 5px 9px;
        border-radius: 7px;
        margin: 3px 2px;
        font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
        font-size: 13px;
        border: 1px solid;
        cursor: default;
    }

    .token-0 {
        background: #eff6ff;
        color: #1e40af;
        border-color: #bfdbfe;
    }

    .token-1 {
        background: #ecfdf5;
        color: #065f46;
        border-color: #a7f3d0;
    }

    .token-2 {
        background: #fefce8;
        color: #854d0e;
        border-color: #fde68a;
    }

    .token-3 {
        background: #faf5ff;
        color: #6b21a8;
        border-color: #e9d5ff;
    }

    .token-4 {
        background: #fff1f2;
        color: #9f1239;
        border-color: #fecdd3;
    }

    /* Conclusão */
    .conclusion {
        background: #f0fdf4;
        border: 1px solid #bbf7d0;
        border-radius: 14px;
        padding: 20px 24px;
        color: #14532d;
        line-height: 1.6;
    }

    .warning-box {
        background: #fff7ed;
        border: 1px solid #fed7aa;
        border-radius: 14px;
        padding: 20px 24px;
        color: #7c2d12;
        line-height: 1.6;
    }

    .section-title {
        font-size: 23px;
        font-weight: 720;
        color: #0f172a;
        margin-top: 16px;
        margin-bottom: 5px;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 18px;
    }

    /* Rodapé */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# FUNÇÕES
# ============================================================

TOKENIZADORES = {
    "r50k_base — geração anterior": {
        "encoding": "r50k_base",
        "descricao": "Tokenizador associado à geração GPT-3 e modelos anteriores."
    },
    "cl100k_base — geração GPT-3.5 / GPT-4": {
        "encoding": "cl100k_base",
        "descricao": "Vocabulário ampliado utilizado por diferentes modelos da geração GPT-3.5/GPT-4."
    },
    "o200k_base — geração posterior": {
        "encoding": "o200k_base",
        "descricao": "Tokenizador mais recente, com vocabulário substancialmente ampliado."
    }
}


def analisar_texto(texto, encoding_name):

    encoding = tiktoken.get_encoding(encoding_name)

    ids = encoding.encode(texto)

    tokens = []

    for indice, token_id in enumerate(ids):

        token_bytes = encoding.decode_single_token_bytes(token_id)

        fragmento = token_bytes.decode(
            "utf-8",
            errors="replace"
        )

        tokens.append(
            {
                "numero": indice + 1,
                "id": token_id,
                "texto": fragmento
            }
        )

    return tokens


def gerar_visualizacao_tokens(tokens):

    elementos = []

    for indice, token in enumerate(tokens):

        texto_token = token["texto"]

        # Torna espaços visíveis
        texto_visual = (
            texto_token
            .replace(" ", "␠")
            .replace("\\n", "↵")
            .replace("\\t", "⇥")
        )

        texto_visual = html.escape(texto_visual)

        classe = indice % 5

        tooltip = (
            f"Token #{token['numero']} | "
            f"ID: {token['id']} | "
            f"Texto: {repr(token['texto'])}"
        )

        tooltip = html.escape(tooltip)

        elementos.append(
            f"""
            <span
                class="token token-{classe}"
                title="{tooltip}">
                {texto_visual}
            </span>
            """
        )

    return "".join(elementos)


def card_metrica(titulo, valor, nota=""):

    return f"""
    <div class="metric-card">
        <div class="metric-label">{titulo}</div>
        <div class="metric-value">{valor}</div>
        <div class="metric-note">{nota}</div>
    </div>
    """


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## ◈ TokenLab")

    st.caption("Visualizador educacional de tokenização")

    st.divider()

    st.markdown("### Conceitos")

    st.markdown(
        """
        **Texto**  
        Informação escrita pelo usuário.

        **Tokenizador**  
        Converte o texto em unidades chamadas tokens.

        **Token**  
        Unidade que será processada pelo modelo.

        **Janela de contexto**  
        Limite de tokens que o modelo consegue considerar em uma interação.
        """
    )

    st.divider()

    st.markdown("### Fluxo básico")

    st.code(
        """Texto
  ↓
Tokenizador
  ↓
Tokens
  ↓
Modelo LLM
  ↓
Resposta""",
        language=None
    )

    st.divider()

    st.caption(
        "Esta aplicação demonstra tokenização. "
        "Ela não mede inteligência, precisão ou qualidade de um modelo."
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-label">DEMONSTRAÇÃO EDUCACIONAL • LARGE LANGUAGE MODELS</div>
        <div class="hero-title">TokenLab</div>
        <div class="hero-subtitle">
            Visualize como diferentes gerações de tokenizadores transformam
            linguagem humana em unidades que podem ser processadas por um
            modelo de inteligência artificial.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# INTRODUÇÃO
# ============================================================

st.markdown(
    """
    <div class="concept-box">
        <b>Como funciona?</b><br>
        Antes de uma frase chegar ao LLM, ela passa por um
        <b>tokenizador</b>. O tokenizador transforma o texto em pequenas
        unidades chamadas <b>tokens</b>. Diferentes gerações de
        tokenizadores podem representar exatamente a mesma informação
        utilizando quantidades diferentes de tokens.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# TEXTO
# ============================================================

st.markdown(
    '<div class="section-title">1. Texto de entrada</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Digite qualquer palavra, frase ou parágrafo para observar a tokenização em tempo real.'
    '</div>',
    unsafe_allow_html=True
)

texto = st.text_area(
    "Texto para análise",
    value=(
        "A inteligência artificial está transformando mundialmente "
        "a maneira como pessoas e organizações trabalham."
    ),
    height=140,
    label_visibility="collapsed"
)

# ============================================================
# ESCOLHA DOS TOKENIZADORES
# ============================================================

st.markdown(
    '<div class="section-title">2. Escolha os tokenizadores</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Compare duas gerações diferentes utilizando exatamente o mesmo texto.'
    '</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    escolha_1 = st.selectbox(
        "Tokenizador A",
        list(TOKENIZADORES.keys()),
        index=0
    )

with col2:

    escolha_2 = st.selectbox(
        "Tokenizador B",
        list(TOKENIZADORES.keys()),
        index=1
    )


# ============================================================
# PROCESSAMENTO
# ============================================================

if texto.strip():

    dados_1 = TOKENIZADORES[escolha_1]
    dados_2 = TOKENIZADORES[escolha_2]

    tokens_1 = analisar_texto(
        texto,
        dados_1["encoding"]
    )

    tokens_2 = analisar_texto(
        texto,
        dados_2["encoding"]
    )

    caracteres = len(texto)

    palavras = len(texto.split())

    qtd_1 = len(tokens_1)
    qtd_2 = len(tokens_2)

    diferenca = abs(qtd_1 - qtd_2)

    # ========================================================
    # MÉTRICAS
    # ========================================================

    st.markdown(
        '<div class="section-title">3. Resultado da análise</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(
            card_metrica(
                "Caracteres",
                caracteres,
                "Quantidade total de caracteres"
            ),
            unsafe_allow_html=True
        )

    with m2:
        st.markdown(
            card_metrica(
                "Palavras",
                palavras,
                "Separação convencional por espaços"
            ),
            unsafe_allow_html=True
        )

    with m3:
        st.markdown(
            card_metrica(
                "Tokens A",
                qtd_1,
                dados_1["encoding"]
            ),
            unsafe_allow_html=True
        )

    with m4:
        st.markdown(
            card_metrica(
                "Tokens B",
                qtd_2,
                dados_2["encoding"]
            ),
            unsafe_allow_html=True
        )

    st.write("")

    # ========================================================
    # COMPARAÇÃO VISUAL
    # ========================================================

    esquerda, direita = st.columns(2)

    with esquerda:

        st.markdown(
            f"""
            <div class="tokenizer-header">
                <div class="tokenizer-title">
                    A · {dados_1["encoding"]}
                </div>
                <div class="tokenizer-description">
                    {dados_1["descricao"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="token-area">
                {gerar_visualizacao_tokens(tokens_1)}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            f"{qtd_1} tokens para representar este texto."
        )

    with direita:

        st.markdown(
            f"""
            <div class="tokenizer-header">
                <div class="tokenizer-title">
                    B · {dados_2["encoding"]}
                </div>
                <div class="tokenizer-description">
                    {dados_2["descricao"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="token-area">
                {gerar_visualizacao_tokens(tokens_2)}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            f"{qtd_2} tokens para representar este texto."
        )

    # ========================================================
    # INTERPRETAÇÃO
    # ========================================================

    st.markdown(
        '<div class="section-title">4. Interpretação</div>',
        unsafe_allow_html=True
    )

    if qtd_1 < qtd_2:

        percentual = ((qtd_2 - qtd_1) / qtd_2) * 100

        st.markdown(
            f"""
            <div class="conclusion">
                Para este texto específico, <b>{dados_1["encoding"]}</b>
                utilizou <b>{diferenca} token(s) a menos</b> que
                <b>{dados_2["encoding"]}</b>, uma diferença aproximada
                de <b>{percentual:.1f}%</b>.
            </div>
            """,
            unsafe_allow_html=True
        )

    elif qtd_2 < qtd_1:

        percentual = ((qtd_1 - qtd_2) / qtd_1) * 100

        st.markdown(
            f"""
            <div class="conclusion">
                Para este texto específico, <b>{dados_2["encoding"]}</b>
                utilizou <b>{diferenca} token(s) a menos</b> que
                <b>{dados_1["encoding"]}</b>, uma diferença aproximada
                de <b>{percentual:.1f}%</b>.
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.info(
            "Neste exemplo, os dois tokenizadores produziram "
            "a mesma quantidade total de tokens."
        )

    # ========================================================
    # DETALHES TÉCNICOS
    # ========================================================

    st.write("")

    with st.expander(
        "Ver detalhes técnicos dos tokens"
    ):

        tab1, tab2 = st.tabs(
            [
                dados_1["encoding"],
                dados_2["encoding"]
            ]
        )

        with tab1:

            tabela_1 = [
                {
                    "#": t["numero"],
                    "Token ID": t["id"],
                    "Fragmento": repr(t["texto"])
                }
                for t in tokens_1
            ]

            st.dataframe(
                tabela_1,
                use_container_width=True,
                hide_index=True
            )

        with tab2:

            tabela_2 = [
                {
                    "#": t["numero"],
                    "Token ID": t["id"],
                    "Fragmento": repr(t["texto"])
                }
                for t in tokens_2
            ]

            st.dataframe(
                tabela_2,
                use_container_width=True,
                hide_index=True
            )

   

    

else:

    st.warning(
        "Digite algum texto para iniciar a análise."
    )


# ============================================================
# RODAPÉ
# ============================================================

st.markdown(
    """
    <div class="footer">
        TokenLab • Demonstração educacional sobre tokenização em Large Language Models<br>
        Desenvolvido em Python utilizando Streamlit e tiktoken
    </div>
    """,
    unsafe_allow_html=True
)