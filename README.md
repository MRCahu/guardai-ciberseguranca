# GuardAI — Cibersegurança e análise de vulnerabilidades

Especialização defensiva do [DIO Agent](https://github.com/digitalinnovationone/dio-agent) para o desafio **GuardAI: Agente Inteligente para Cibersegurança e Análise de Vulnerabilidades** da DIO.

O agente esclarece o contexto antes de sugerir comandos, analisa evidências, avalia risco e orienta correções. A especialização ocorre por arquivos Markdown, sem treinamento de modelo.

## Por que esta especialização?
Transformar revisão de segurança em um processo explicável e repetível. A melhoria escolhida é um **formato padronizado de análise**, com matriz didática de impacto × probabilidade, evidências e risco residual. O laboratório fornece validação automatizada do vetor SQL Injection.

## Arquivos criados e alterados
| Caminho | Finalidade |
|---|---|
| [SKILL.md](skills/vulnerability-analysis/SKILL.md) | Roteiro defensivo e formato obrigatório |
| [README da skill](skills/vulnerability-analysis/README.md) | Uso e critérios de aceitação |
| [Conhecimento](agent/knowledge/security-basics.md) | Fundamentos, matriz e referências |
| [Persona](agent/persona.md) | Comportamento do GuardAI |
| [AGENTS.md](AGENTS.md) | Registro e acionamento da habilidade |
| [Laboratório vulnerável](lab/app.py) | Concatenação SQL intencional, somente em memória |
| [Correção](lab/app_secure.py) | Consulta parametrizada |
| [Testes](tests/test_sql_injection.py) | Login legítimo, bypass e entradas extremas |
| [Runbook](docs/runbook.md) | Instalação, Hermes e reprodução |
| [Cenários](docs/scenarios.md) | Contexto incompleto, laboratório e instruções não confiáveis |
| [Validação do agente](evidence/agent-validation.md) | Perguntas de contexto e revisão independente reais |
| [Análise](evidence/analysis.md) | Achado, correção e limites |
| [Testes executados](evidence/tests.txt) | Saída real da suíte |
| [Demonstração](evidence/demo.txt) | Comparação executada das versões |
| [README original](docs/README-base.md) | Proveniência e instruções da base |

## Reprodução rápida
Python 3, sem dependências externas e sem acesso à rede:

```bash
git clone https://github.com/MRCahu/guardai-ciberseguranca.git
cd guardai-ciberseguranca
python3 -m lab.demo
python3 -m unittest discover -s tests -v
```

O bypass sintético retorna `True` na versão vulnerável e `False` na parametrizada. Credenciais válidas continuam aceitas.

## Usar como agente no Hermes
Siga o [runbook](docs/runbook.md). Instale/configure o Hermes pela documentação oficial, execute `hermes` na raiz e peça a leitura dos arquivos da especialização. O prompt completo e os cenários estão documentados. Outros harnesses compatíveis também podem carregar os arquivos.

## Evidências e honestidade
Os logs Python são execuções reais; a análise documenta a revisão feita nesta sessão pelo assistente. Não há alegação de execução no Hermes, indisponível neste ambiente. Dois cenários foram validados por uma instância independente do assistente, com trechos reais em evidence/agent-validation.md; os demais são critérios de aceitação. Capturas do repositório complementam os logs, quando disponíveis.

## Escopo e limitações
Somente dados fictícios, SQLite em memória, sem servidor, scanner ou destino externo. O exemplo vulnerável é material didático. Senhas em texto existem apenas para isolar a falha e não servem para produção. A correção cobre o vetor testado; não certifica segurança integral. A matriz não equivale ao CVSS. CWE-89 descreve a fraqueza; ATT&CK T1190 só se aplica condicionalmente a exploração de aplicação exposta.

## Proveniência
Base: digitalinnovationone/dio-agent, commit `5f5e11d95583d0eabcd883b214ef0e51bfb8889c`. Arquivos educacionais originais preservados, com especialização em AGENTS.md e persona. Autor da adaptação: Mauro Cahú, com apoio de IA. Não se presume licença não declarada pelo projeto base.
