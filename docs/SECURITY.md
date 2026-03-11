# Security

This document describes the security posture of marketing-skills and how we verify that skills are safe for AI agents.

## Overview

Skills are **trusted context** injected into AI agents. Unlike code execution (which can be sandboxed), prompt injection in skills can leak sensitive data, hijack agent behavior, or bypass safety guardrails. We take this seriously.

## Audit Checklist

| Check | Status |
|-------|--------|
| Pure Markdown — no executable code | ✓ |
| No `ignore previous` / `ignore all` hijack instructions | ✓ |
| No hidden instructions in HTML comments | ✓ |
| No `javascript:` / `data:` link injection | ✓ |
| No env var / API key exfiltration instructions | ✓ |
| Scope limited to SEO, content, marketing workflows | ✓ |

## Content Safety

- **Format**: All skills are `.md` files — no scripts, binaries, or executable code.
- **Scope**: Instructions cover SEO, content strategy, page optimization, paid ads, and related marketing tasks. No system-level or data-exfiltration directives.
- **References**: Product and website examples are illustrative only; no affiliation implied. See [reference-rules §6](reference-rules.md#6-product-and-website-examples).

## Verification

To verify skills yourself:

1. **Keyword scan** — Search for suspicious patterns:
   ```bash
   rg -i "ignore (previous|all)|system:.*send|execute.*eval" skills/
   ```
   Legitimate matches (e.g., "API key" in IndexNow docs) should be reviewed manually.

2. **HTML comments** — Check for hidden instructions:
   ```bash
   rg "<!--.*-->" skills/
   ```

3. **Link injection** — Ensure no `javascript:` or `data:` URLs:
   ```bash
   rg "javascript:|data:" skills/
   ```

## Skill Supply Chain & Poisoning

Skills are trusted context; attackers may embed malicious content ("skill poisoning") — e.g. base64-encoded scripts in Setup code blocks, prompt injection, credential exfiltration. Skills inherit the agent's full permissions (shell, files, env vars). **Mitigation**: Review skills before install; treat skills with scripts like executable code. [skills.sh](https://skills.sh) runs basic audits but cannot guarantee safety. See [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) for prompt injection patterns.

## Related

- [OWASP LLM Top 10: Prompt Injection](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [GitHub Issue #1](https://github.com/kostja94/marketing-skills/issues/1) — Proposal for automated prompt injection detection in skill validation tooling

## Reporting

If you find a security concern, please open an [issue](https://github.com/kostja94/marketing-skills/issues) or contact zyjstc@gmail.com.
