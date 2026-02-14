<!--
Sync Impact Report:
- Version change: Initial -> 1.0.0
- List of modified principles:
    - [PRINCIPLE_1_NAME] -> 最適化ロジックとUIの完全分離
    - [PRINCIPLE_2_NAME] -> 徹底した透明性と可視化
    - [PRINCIPLE_3_NAME] -> 堅牢なエラーハンドリングと親切なUI
    - [PRINCIPLE_4_NAME] -> モダンなコード品質基準
    - [PRINCIPLE_5_NAME] -> インタラクティブなユーザー体験
- Added sections: 技術スタックと制約, 開発ワークフローと検証
- Removed sections: N/A
- Templates requiring updates:
    - .specify/templates/plan-template.md (✅ updated)
    - .specify/templates/spec-template.md (✅ updated)
    - .specify/templates/tasks-template.md (✅ updated)
- Follow-up TODOs: None
-->

# LP_app Optimization Project Constitution

## Core Principles

### 最適化ロジックとUIの完全分離
最適化ロジック（Pyomoエンジン）とUI（Streamlit表示）を完全に分離する。エンジンはUIなしで独立して動作可能かつテスト可能でなければならない。

### 徹底した透明性と可視化
最適化の定式化（目的関数と制約式）を `st.latex` を用いてUI上に明示し、結果だけでなく「制約の余力（Slack）」や「ボトルネック」を可視化する。ユーザーが「なぜこの結果になったか」を直感的に理解できるようにする。

### 堅牢なエラーハンドリングと親切なUI
ソルバーが解を見つけられなかった（Infeasible）場合、単にエラーを表示するのではなく、ユーザーが次に取るべき行動（制約の緩和など）を示唆する親切なUIを提供する。

### モダンなコード品質基準
`Ruff` を使用して静的解析とコード整形を自動化し、PEP8 に準拠した一貫性のあるコードを維持する。型ヒントを積極的に使用して開発の堅牢性を確保する。

### インタラクティブなユーザー体験
Plotly や Altair を活用し、グラフを動的に操作可能にする。ユーザーがパラメータを変更した際の感度（Sensitivity）を直感的に感じられるようにツールチップやフィルターを活用して設計する。

## 技術スタックと制約
- **言語**: Python
- **最適化ライブラリ**: Pyomo
- **ソルバー**: CBC (デフォルト)
- **UIフレームワーク**: Streamlit
- **可視化**: Plotly, Altair
- **Linter/Formatter**: Ruff

## 開発ワークフローと検証
全てのコード変更は `Ruff` のチェックを通過しなければならず、最適化エンジンに対する単体テスト（Unit Test）が推奨される。`/speckit.plan` および `/speckit.tasks` は、これらの原則を遵守していることを確認するステップを含む必要がある。

## Governance
この憲法はプロジェクトの基本指針であり、全ての開発活動（`/speckit.implement`）はこの指針に従う必要がある。重要な指針の追加や変更はバージョンの繰り上げを行い、履歴を管理する。

**Version**: 1.0.0 | **Ratified**: 2026-02-14 | **Last Amended**: 2026-02-14
