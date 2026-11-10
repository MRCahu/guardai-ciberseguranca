# Executar o GuardAI

## Laboratório determinístico
Requisito: Python 3 com sqlite3, sem pacotes adicionais.

```bash
git clone https://github.com/MRCahu/guardai-ciberseguranca.git
cd guardai-ciberseguranca
python3 -m lab.demo
python3 -m unittest discover -s tests -v
```

## Hermes
Instale e configure o Hermes conforme https://hermes-agent.nousresearch.com/docs (provedor e autenticação próprios). Nunca coloque chaves no repositório.

Abra o terminal **na raiz deste projeto** e execute `hermes`. Peça explicitamente: “Leia AGENTS.md, agent/persona.md, agent/knowledge/security-basics.md e skills/vulnerability-analysis/SKILL.md. Use esse roteiro neste laboratório próprio, offline e sintético: revise lab/app.py, proponha a correção, compare lab/app_secure.py e execute os testes locais.”

Se o harness não carregar arquivos automaticamente, abra-os ou forneça os caminhos. O agente não executa sozinho sem um harness/modelo configurado. Veja os cenários em scenarios.md.

## Outros harnesses
O projeto base também documenta Codex, Claude Code, OpenCode e Antigravity em README-base.md. Não há modelo treinado ou serviço hospedado neste repositório.

## Limites de evidência
Os logs em evidence/ registram execução Python real. A análise em evidence/analysis.md foi realizada pelo assistente nesta sessão. Não é transcrição do Hermes. A validação interativa no Hermes depende de instalação e credenciais; não é apresentada como realizada.
