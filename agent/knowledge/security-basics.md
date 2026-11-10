# Fundamentos de segurança

- Vulnerabilidade: fraqueza que pode ser explorada.
- Ameaça: evento ou agente capaz de causar dano.
- Risco: combinação contextual de probabilidade e impacto.
- Confidencialidade: impedir acesso não autorizado.
- Integridade: impedir alteração indevida.
- Disponibilidade: manter acesso ao serviço e aos dados quando necessário.

## Matriz didática de risco
Impacto: 1 = limitado a dados sintéticos e ambiente isolado; 2 = dano limitado e recuperável em serviço real; 3 = dados sensíveis, acesso indevido relevante ou interrupção crítica.
Probabilidade: 1 = isolamento e precondições restritas; 2 = acesso limitado ou precondições plausíveis; 3 = entrada acessível ao adversário e exploração simples/reproduzível.
Produto: 1–2 baixa; 3–4 média; 6 alta; 9 crítica. Não é CVSS. Ausência de contexto exige classificação provisória, sem números arbitrários. Diferencie gravidade intrínseca da fraqueza do risco no ambiente analisado.

## Boas práticas
Consultas parametrizadas separam instruções SQL dos valores. Validação de entrada ajuda, mas não substitui parametrização. Use menor privilégio, atualização, backups testados, logs sem segredos e autenticação adequada. Senhas reais exigem hash apropriado; o laboratório usa valores sintéticos em texto apenas para isolar SQL Injection.

## Taxonomias e fontes oficiais
- CWE-89 (SQL Injection): https://cwe.mitre.org/data/definitions/89.html
- ATT&CK T1190 (Exploit Public-Facing Application): https://attack.mitre.org/techniques/T1190/
- SQLite Python e placeholders: https://docs.python.org/3/library/sqlite3.html
- OWASP SQL Injection Prevention: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

A técnica T1190 depende de aplicação exposta; um teste local de SQL Injection, sozinho, não demonstra essa técnica em uma intrusão.
